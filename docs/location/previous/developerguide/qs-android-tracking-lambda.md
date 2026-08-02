---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/qs-android-tracking-lambda.html
---

# Tutorial: Use AWS Lambda with MQTT
<a name="qs-android-tracking-lambda"></a>

In order to create a connection between AWS IoT and Amazon Location, you need a Lambda function to process messages forwarded by EventBridge CloudWatch events. This function will extract any positional data, format it for Amazon Location, and submit it through the Amazon Location Tracker API.

The following procedure shows you how to create this function through the Lambda console:

1. Open the [console](https://console.aws.amazon.com/lambda/).

1. From the left navigation, choose **Functions**.

1. Then choose **Create Function**, and make sure that the **Author from scratch** option is selected.

1.  provide a **Function name**, and for the **Runtime** option, choose Node.js 16.x.

1. Choose **Create function**.

1. Open the **Code tab** to access the editor.

1. Overwrite the placeholder code in the `index.js` file with the following:

   ```
               const AWS = require('aws-sdk')
               const iot = new AWS.Iot();
               exports.handler =  function(event) {
                 console.log("event===>>>", JSON.stringify(event));
                 var param = {
                   endpointType: "iot:Data-ATS"
                 };
                 iot.describeEndpoint(param, function(err, data) {
                   if (err) {
                     console.log("error===>>>", err, err.stack); // an error occurred
                   } else {
                     var endp = data['endpointAddress'];
                     const iotdata = new AWS.IotData({endpoint: endp});
                     const trackerEvent = event["detail"]["EventType"];
                     const src = event["source"];
                     const time = event["time"];
                     const gfId = event["detail"]["GeofenceId"];
                     const resources = event["resources"][0];
                     const splitResources = resources.split(".");
                     const geofenceCollection = splitResources[splitResources.length - 1];
                     const coordinates = event["detail"]["Position"];
                     const deviceId = event["detail"]["DeviceId"];
                     console.log("deviceId===>>>", deviceId);
                     const msg =  {
                         "trackerEventType" : trackerEvent,
                         "source" : src,
                         "eventTime" : time,
                         "geofenceId" : gfId,
                         "coordinates": coordinates,
                         "geofenceCollection": geofenceCollection
                       };
                     const params = {
                       topic: `${deviceId}/tracker`,
                       payload: JSON.stringify(msg),
                       qos: 0
                     };
                     iotdata.publish(params, function(err, data) {
                         if (err) {
                           console.log("error===>>>", err, err.stack); // an error occurred
                         } else {
                           console.log("Ladmbda triggered===>>>", trackerEvent);  // successful response
                         }
                     });
                   }
                 });
               }
   ```

1. Press the **Deploy** to save the updated function.

1. Next open the **Configuration** tab.

1. In the **Triggers** section, press the **Add Trigger** button.

1. Select **EventBridge (CloudWatch Events)** in Source field.

1. Select the **Existing Rules** option.

1. Enter the rule name, for example `AmazonLocationMonitor-GEOFENCECOLLECTION_NAME`.

1. Press the **Add** button.

1.  This will also attach **Resource-based policy statements** in the permissions tab

Now you will set up the MQTT Test Client using AWS IoT, use the following procedure:

1. Open the [https://console.aws.amazon.com/iot/](https://console.aws.amazon.com/iot/).

1.  In the left navigation pane, select the **MQTT test client**.

1.  You'll see a section titled **MQTT test client** where you can configure your MQTT connection.

1.  After configuring the necessary settings, click on the **Connect** button to establish a connection to the MQTT broker using the provided parameters.

1.  Record endpoint, as it is used later in the tutoiral.

   Once connected to the test client, you can subscribe to MQTT topics or publish messages to topics using the respective input fields provided in the MQTT test client interface. Next you will create an AWS IoT policy.

1.  On the left side menu, under **Manage** expand **Security** option and click on **Policies**.

1.  Click on **Create Policy** button.

1.  Enter a policy name.

1.  On **Policy Document** select **JSON** tab.

1. Copy paste the policy shown below, but make sure to update all elements with your `{{REGION}}` and `{{ACCOUNT_ID}}`:

   ```
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Action": [
           "iot:Connect",
           "iot:Publish",
           "iot:Subscribe",
           "iot:Receive"
         ],
         "Resource": [
           "arn:aws:iot:{{REGION}}:{{ACCOUNT_ID}}:client/${cognito-identity.amazonaws.com:sub}",
           "arn:aws:iot:{{REGION}}:{{ACCOUNT_ID}}:topic/${cognito-identity.amazonaws.com:sub}",
           "arn:aws:iot:{{REGION}}:{{ACCOUNT_ID}}:topicfilter/${cognito-identity.amazonaws.com:sub}/*",
           "arn:aws:iot:{{REGION}}:{{ACCOUNT_ID}}:topic/${cognito-identity.amazonaws.com:sub}/tracker"
         ],
         "Effect": "Allow"
       }
     ]
   }
   ```

1. Select the **Create** button to finish.

After completing the previous procedure, you will now update the permissions for the guest role as follows:

1. Navigate to Amazon Cognito and open your identity pool. Then, proceed to user access and select the guest role.

1. Click on permission policies to enable editing.

   ```
   {
       'Version': '2012-10-17		 	 	 ',
       'Statement': [
           {
               'Action': [
                   'geo:GetMap*',
                   'geo:BatchUpdateDevicePosition',
                   'geo:BatchEvaluateGeofences',
                   'iot:Subscribe',
                   'iot:Publish',
                   'iot:Connect',
                   'iot:Receive',
                   'iot:AttachPrincipalPolicy',
                   'iot:AttachPolicy',
                   'iot:DetachPrincipalPolicy',
                   'iot:DetachPolicy'
               ],
               'Resource': [
                   'arn:aws:geo:us-east-1:{{{USER_ID}}}:map/{{{MAP_NAME}}}',
                   'arn:aws:geo:us-east-1:{{{USER_ID}}}:tracker/{{{TRACKER_NAME}}}',
                   'arn:aws:geo:us-east-1:{{{USER_ID}}}:geofence-collection/{{{GEOFENCE_COLLECTION_NAME}}}',
                   'arn:aws:iot:us-east-1:{{{USER_ID}}}:client/${cognito-identity.amazonaws.com:sub}',
                   'arn:aws:iot:us-east-1:{{{USER_ID}}}:topic/${cognito-identity.amazonaws.com:sub}',
                   'arn:aws:iot:us-east-1:{{{USER_ID}}}:topicfilter/${cognito-identity.amazonaws.com:sub}/*',
                   'arn:aws:iot:us-east-1:{{{USER_ID}}}:topic/${cognito-identity.amazonaws.com:sub}/tracker'
               ],
               'Effect': 'Allow'
           },
           {
               'Condition': {
                   'StringEquals': {
                       'cognito-identity.amazonaws.com:sub': '${cognito-identity.amazonaws.com:sub}'
                   }
               },
               'Action': [
                   'iot:AttachPolicy',
                   'iot:DetachPolicy',
                   'iot:AttachPrincipalPolicy',
                   'iot:DetachPrincipalPolicy'
               ],
               'Resource': [
                   '*'
               ],
               'Effect': 'Allow'
           }
       ]
   }
   ```

1. With the above policy changes, all necessary AWS resources are now configured appropriately for the application.
