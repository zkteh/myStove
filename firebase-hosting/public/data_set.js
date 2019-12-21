//this code is modified base on this tutorial
https://protoout.studio/posts/firebase-realtime-database-node-js

var admin = require("firebase-admin");

const sensor = require('ds18b20-raspi');
const timestamp = require('time-stamp');

// 1. サービスアカウント鍵を生成しserviceAccountKey.jsonでリネームしてフォルダ直下に配置
var serviceAccount = require("./serviceAccountKey.json");

admin.initializeApp({
	credential: admin.credential.cert(serviceAccount),
	// 2. Realtime DatabaseのページでdatabaseURLを確認して反映
  // databaseURL: "https://<databaseURL>.firebaseio.com"
	databaseURL: "https://mystove-24023.firebaseio.com/"
});

var db = admin.database();
var ref = db.ref("protoout/studio");
var usersRef = ref.child("sensorList");

//declar var for sensor reading 
var tempC = sensor.readSimpleC();

setInterval(function() {
	tempC = sensor.readSimpleC();

	usersRef.push({
		"temperature": tempC,
		"timestamp": timestamp('YYYY-MM-DD HH:mm:ss')
	});    
}, 3000);


ref.on("value", function(snapshot) {
	console.log("value Changed!!!");
	console.log(snapshot.val());
}, 
function(errorObject) {
	console.log("failed: " + errorObject.code);
} );

