

    let preview = document.getElementById("preview");
    let startButton = document.getElementById("startButton");
    let stopButton = document.getElementById("stopButton");
    let switchCameraButton = document.getElementById("switchCameraButton");
    let submitChallengeForm = document.getElementById("submitChallengeForm");
    let fileInputElement = document.getElementById("fileInputElement");


    loadRecordingStream(switchCameraButton.dataset.facing);

    switchCameraButton.addEventListener("click", function() {
        if(switchCameraButton.dataset.facing == "environment") {
            switchCameraButton.dataset.facing = "user";
        } else {
            switchCameraButton.dataset.facing = "environment";
        }
        
        loadRecordingStream(switchCameraButton.dataset.facing);
    },false);

    function loadRecordingStream(cameraFacing){
        log("LoadStream: "+cameraFacing);
        navigator.mediaDevices.getUserMedia({video: {facingMode:cameraFacing}, audio:true}).then(stream => {
            preview.src = null;
            preview.srcObject = stream;
            preview.captureStream = preview.captureStream || preview.mozCaptureStream;
            return new Promise(resolve => preview.onplaying = resolve);
        });
        logPreview();
        log("Stream Loaded!");
    }

    function log(msg){
        console.log("LOGMSG: "+msg);
    }

    function logPreview(){
        console.log("- - - - - PREVIEW-srcObject: "+preview.srcObject);
        console.log("- - - - - PREVIEW-src: "+preview.src);
        console.log("- - - - - PREVIEW-captureStream: "+preview.captureStream);
    }
    
    function startRecording(stream){
        log("Start Recording of stream: "+stream+"...")
        logPreview();
        Toggle_playstop();
        let recorder = new MediaRecorder(stream);
        let data = [];

        recorder.ondataavailable = event => data.push(event.data);
        recorder.start();
        log("Record State: "+recorder.state);

        let stopped = new Promise((resolve, reject) => {
            recorder.onstop = resolve;
            recorder.onerror = event => reject(event.name);
        });
        return Promise.all([stopped]).then(() => data);
    }

    function stop(stream) {
        log("Stop Recording");
        stream.getTracks().forEach(track => track.stop());
        logPreview();
    }

    startButton.addEventListener("click", function() {
        if(preview.srcObject == null) {
            log("Reconnect VideoPlayer to Camera Stream");
            loadRecordingStream(switchCameraButton.dataset.facing);
        }
        startRecording(preview.captureStream())
        .then (recordedChunks => {
            log("Preview CaptureStream has ended. Gathering Recorded Chunks...");
            let recordedBlob = new Blob(recordedChunks, {type:"video/webm"});
            preview.srcObject = null;
            preview.src = URL.createObjectURL(recordedBlob);

            log("- - Recorded "+recordedBlob.size + " bytes of " + recordedBlob.type + " media.");

            file = new File([recordedBlob],BuildRecordingFileName(".webm"),{type:"video/webm",lastModified:new Date().getTime()});
            container = new DataTransfer();
            container.items.add(file);
            fileInputElement.files = container.files;
            log("Recording Chunks have been compiled. Successfully Added Recording to fileInputElement");
        })
        .catch(log);
    },false);

    stopButton.addEventListener("click", function() {
        Toggle_playstop();
        stop(preview.srcObject);
    },false);

    function Toggle_playstop(){
        if(startButton.classList.contains("active")){
            startButton.className = startButton.className.replace(" active", "");
            stopButton.className += " active";
        } else {
            startButton.className += " active";
            stopButton.className = stopButton.className.replace(" active", "");
        }
    }
    
    function addLeadingZeros(n) {
        if (n <= 9) {
            return "0" + n;
            }
            return n
        }

    function BuildRecordingFileName(fileExtension){
        var currentDate = new Date();
        //var currDate = currentDate.getFullYear()+"-"+currentDate.getMonth()+"-"+currentDate.getDay()+"-"+currentDate.getHours()+"-"+currentDate.getMinutes()+"-"+currentDate.getSeconds();
        var year = currentDate.getFullYear();
        var month = addLeadingZeros(currentDate.getMonth() + 1);      // "+ 1" becouse the 1st month is 0
        var day = addLeadingZeros(currentDate.getDate());
        var hour = addLeadingZeros(currentDate.getHours());
        var minutes = addLeadingZeros(currentDate.getMinutes());
        var seconds = addLeadingZeros(currentDate.getSeconds())

        var currDate = year+"-"+month+"-"+day+"-"+hour+"-"+ minutes+"-"+ seconds;

        const urlParams = new URLSearchParams(window.location.search);
        var fileName= "S"+urlParams.get('student')+"_C"+urlParams.get('curriculum')+"_CH"+urlParams.get('challenge')+"_D"+currDate;
        return fileName+fileExtension;
    }