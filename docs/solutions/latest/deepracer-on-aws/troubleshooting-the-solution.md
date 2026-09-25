---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/troubleshooting-the-solution.html
---

# Troubleshooting the solution
<a name="troubleshooting-the-solution"></a>

## Issues with logging in or creating an account
<a name="issues-with-logging-in-or-creating-an-account"></a>

1.  *When logging in with correct credentials, I get an error saying that I’ve provided an incorrect username or password*

   This can be caused by session data and webpage caching in the browser interfering with the normal login behavior. Try opening the console using a private browsing tab and logging in again. If you continue to experience issues, please contact your admin.

1.  *When logging in with correct credentials, I’am getting a 403 error*

   This issue can occur when CloudFront or the WAF (Web Application Firewall) is selective about which client requests it allows through and may block legitimate requests that do not meet its access criteria. To resolve this, try turning off your VPN and logging in again.

1.  *When I invite a user to DeepRacer on AWS as an admin, the user does not receive an invitation email*

   This can occur when your deployment is configured to use Amazon Cognito as the delivery method for authentication emails. Amazon Cognito has a limit of 50 emails per day per account, which includes invitation emails and password reset emails. A cloud admin can check whether this limit is being exceeded by accessing the CloudWatch Management Console > Metrics > All metrics > "DeepRacerOnAWS/Email" under Custom namespaces. If the value shown is greater than or equal to 50, then email volume has exceeded the daily limit for Cognito.

   If more throughput is needed, a cloud admin may consider switching to Amazon SES as the delivery method for authentication emails. This carries certain [Prerequisites](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/prerequisites.html) such as setting up a verified sender email and requesting production access for your account, but will remove the daily limit for sending authentication emails. Once the prerequisites are satisfied, a cloud admin can make this change (via AWS Launch Wizard, Amazon CloudFormation, or AWS CDK commands) by updating the application and selecting SES instead of Cognito for the delivery method, and providing a verified email address.

## Issues with creating a model
<a name="issues-with-creating-a-model"></a>

1.  *When I reach the end of the wizard, I get an error that I’ve exceeded a usage limit*

   This can be caused by your profile either nearing or reaching a usage limit (either compute usage or model storage) that has been set by your admin. The usage limit that is causing this may either be a deployment-wide usage limit (to control usage across the entire deployment), or an individual usage limit (to control usage for individual users). Contact your admin for further guidance. To prevent this, keep an eye on the usage metric that’s on both the home page as well as your profile page.

   For admins, find the corresponding user in the Users table and see whether their usage is nearing or has met one or more limits. If not, check whether either of the global limits are approaching their thresholds. If no limits have been set, contact your cloud admin for additional support.

1.  *I’m getting an error that my reward function is invalid*

   Reward functions are written in Python and must be valid in order to be trained. This likely means that your reward function code has a syntax error. Use the Validate button to help pinpoint the error in your code.

## Issues with viewing the model list
<a name="issues-with-viewing-the-model-list"></a>

1.  *When trying to view the model list, I’am getting a 403 error*

   This issue can occur when CloudFront or the WAF (Web Application Firewall) is selective about which client requests it allows through and may block legitimate requests that do not meet its access criteria. To resolve this, try turning off your VPN and viewing the model list again.

## Issues with training or evaluating a model
<a name="issues-with-training-or-evaluating-a-model"></a>

1.  *When I create a model and submit it for training, the model stays in a Queued state for an extended period of time*

   This can be caused by the underlying AWS account reaching its service quota limit for Amazon SageMaker AI training jobs. This can cause training jobs to be delayed, especially if your deployment often experiences high traffic volumes or burst traffic. *For cloud admins:* Try requesting a service limit increase through the [Service Quotas console](https://console.aws.amazon.com/servicequotas/) by selecting Amazon SageMaker and requesting an increase for the *ml.c7i.4xlarge for training job usage* quota.

1.  *When I create a model and submit it for training, the model enters an Error state*

   This means that an error occurred while attempting to train your model, contact your admin for further assistance.

   For cloud admins, try examining the `/aws/lambda/DeepRacerTraining` log group that is associated with your deployment in the Amazon CloudWatch Logs console.

1.  *How do I download the logs from my training or evaluation job?*
   + For **training jobs**, you can download the logs by clicking the **Download logs** button at the top of the **Training** section on the model detail page.
   + For **evaluation jobs**, you can download the logs by clicking the **Download logs** button at the top of the **Evaluation details** section on the model detail page, after selecting a model from the **Evaluations selector** and clicking **Load evaluation**.

## Issues with participating in a race
<a name="issues-with-participating-in-a-race"></a>

1.  *After my model finishes a race, I don’t see it appear in the leaderboard*

   This means that your model has not met the qualification requirements for the race. Keep training and evaluating your model as mentioned in the guide to improve performance.

## Issues with live races
<a name="issues-with-live-races"></a>

1.  *A model evaluation is showing a **Failed** status in the queue. What should I do?*

   Click **Reset** on the failed queue item. The system will take approximately 30 seconds to clean up the previous evaluation environment, after which the item returns to **Pending** status. You can then click **Launch** (or re-enable Autolaunch) to retry the evaluation.

   If the same model fails again after a reset, click **Remove** to remove it from the queue and proceed with the remaining submissions. For repeated or unexpected failures, examine the `/aws/lambda/DeepRacerTraining` and `/aws/lambda/DeepRacerLiveRacing` log groups in Amazon CloudWatch Logs. See [Using CloudWatch Logs to diagnose issues](#using-cloudwatch-logs-to-diagnose-issues).

1.  *The live race video stream is not loading or is stuck buffering*

   The video stream is delivered via Amazon Kinesis Video Streams as an HLS stream. Try the following steps:
   + Refresh the page to re-establish the stream connection.
   + Verify that the participant’s browser supports HLS playback (modern Chromium-based browsers and Safari are recommended).
   + If the stream does not recover, the facilitator can click **Reset** on the currently in-progress queue item to restart the evaluation, which will re-establish the stream.

     For cloud admins, check the `/aws/lambda/DeepRacerLiveRacing` log group for errors related to Kinesis Video Streams.

1.  *The leaderboard is not updating in real-time*

   Real-time leaderboard updates are delivered over a WebSocket connection via AWS IoT Core. If the leaderboard stops updating:
   + Refresh the page — the interface will automatically re-fetch the latest race state on reconnect.
   + If the issue persists for multiple participants, a cloud admin should check whether IoT Core is experiencing connectivity issues in the deployed region.

1.  *The **Launch** button is disabled and I cannot start the next evaluation*

   The **Launch** button is disabled when: an evaluation is already in progress, the race has been completed (winner declared), or the current time is before the scheduled live event time. If the button is enabled but launching fails with an error, verify that the "Submissions Open" toggle is off and that there are pending items in the queue. If the race was not intentionally completed, contact your cloud admin to check the `/aws/lambda/DeepRacerLiveRacing` log group for unexpected state transitions.

## Issues with physical racing events
<a name="issues-with-physical-racing-events"></a>

1.  *The **Timekeep** link on a track is unavailable and I cannot open the timekeeping page*

   Timekeeping is only available while the event is **In progress**. Open the event and check its status. An admin advances the event by choosing **Publish event**, then **Start racing**. See [Event lifecycle](event-lifecycle.md).

1.  *I cannot add a track to an event*

   The **Add track** button is unavailable for any of three reasons: the event is no longer in **Draft** or **Open** status, the event already has the maximum of 10 tracks, or no **Track layout** has been chosen in the event’s race configuration. Only admins can add tracks.

1.  *I cannot remove a track from an event*

   Tracks can only be removed while the event is in **Draft** status, and an event must keep at least one track. If you need to change the tracks on an event that has already been published, and the event has not yet started, the alternative is to create a replacement event with the correct tracks.

1.  *Creating a run for a racer is rejected*

   The racer has used all of the runs allowed by the event’s **Maximum runs per racer** setting. Confirm the racer’s existing runs on the **Runs** tab of the event details page. An admin can raise the limit by editing the event, subject to what the event’s current status allows.

1.  *Recording a lap fails, or a lap does not appear in the table*

   Laps can only be recorded while the run is **In progress**. If the run is paused, choose **Resume** before recording.

   If the request timed out, the timekeeping page marks the lap as pending and offers **Retry record lap**. Retrying is safe: the solution assigns lap numbers sequentially and rejects a duplicate, so a lap that was actually recorded the first time will not be recorded twice. Retry until the lap table matches what happened on track.

1.  *The countdown and the current lap timer are blank after I reloaded the page*

   Neither the countdown nor the lap stopwatch is saved, so they cannot be restored after a reload. This is expected. The run itself and every lap already recorded are unaffected. Use the run controls to end the run and then submit or discard it.

1.  *I cannot submit a run*

   A run cannot be submitted unless it has at least one valid lap, because there would be no time to score. Check the **Recorded laps** table for laps marked invalid. Either mark a lap valid, record a valid lap, or discard the run.

1.  *The combined leaderboard is missing*

   A combined leaderboard is created automatically once an event has two or more tracks, and the event must have a **Combined scoring strategy** set. An event with a single track has only that track’s leaderboard.

1.  *The combined leaderboard does not match the individual track leaderboards*

   The combined leaderboard is derived from the individual track results, so it updates a moment after them. If the difference persists, a recalculation has failed. A cloud admin can check the `CombinedLeaderboardRecomputeFailed` metric in the `DeepRacerIndy` namespace and examine the broadcast handler’s logs. See [Race management metrics](monitoring.md#race-management-metrics). Individual track leaderboards are unaffected and remain authoritative.

1.  *I deleted an event but some of its data appears to remain*

   Removing a deleted event’s records happens in the background, and for a large event it can take a short while. If records remain after that, the removal failed, and the `EventDeleteDLQAlarm` alarm is in the ALARM state. A cloud admin should examine the event deletion worker’s logs, then redrive the event deletion dead letter queue to retry. See [Alarms](monitoring.md#alarms).

1.  *A racer says they cannot see an event’s tracks*

   Racers can view events, runs, and recorded laps, but the track list is available only to admins and race facilitators. Racers see results through the event’s leaderboards. For the complete breakdown, see [Permissions matrix](types-of-users.md#permissions-matrix).

## Issues with importing or exporting a model
<a name="issues-with-importing-or-exporting-a-model"></a>

1.  *I’m having trouble opening a model that I’ve exported and downloaded to my Windows computer*

   If you are using a Windows computer, you’ll need to download and install a file extractor such as 7-Zip in order to extract the model once it has finished downloading to your computer.

## Issues with admin model downloads
<a name="issues-with-admin-model-downloads"></a>

1.  *I can’t see the Model Management page in the sidebar*

   The Model Management page is only visible to users with the Admin or Race Facilitator role. Ask your instance administrator to update your role if you need access to this feature.

1.  *I’m getting an "Access Denied" error when trying to download a model*

   Verify that your account has the Admin or Race Facilitator role. If your role was recently changed, log out and log back in for the change to take effect.

1.  *My download requests are being rejected with a rate limit error*

   The admin model management endpoints are protected by a rate limit of 100 requests per 5 minutes per user. If you are downloading many models at once, wait a few minutes before retrying.

## Issues with model optimization and car deployment
<a name="issues-with-model-optimization-and-car-deployment"></a>

1.  *I can’t push a model to a car, or the **Upload model to car** button is unavailable*

   A model must be optimized before you can deploy it to a car. On the **Model Management** > **Models** page, select the model and choose **Optimize for car**. After its status shows optimized, select the model again and choose **Upload model to car** to push it. For more information, see [Model management](model-management.md).

1.  *Pushing a model to a car fails because the car is offline or not manageable*

   The car must be activated in Device Management and online before you can push a model to it. AWS Systems Manager (SSM) delivers the push, so the car must be powered on and connected. Power on the car, connect it, and confirm it shows as online. Then retry the push.

   If the push still fails, check the deployment’s status on the **Upload Status** page, then review the relevant Amazon CloudWatch log group for details. The push-to-car workflow runs three AWS Lambda functions: `PushSendCommand`, `PushPollCommand`, and `PushUpdateStatus`. Their full names follow the deployment’s `DeepRacerIndy-Push*Fn` pattern, and their log group names are generated at deployment. To view a function’s logs, open the AWS Lambda console, select the relevant push function, then choose **Monitor** and **View CloudWatch logs**.

1.  *I see "Failed to start upload for" or "Car models were cleared but all uploads failed"*

   One or more models could not be dispatched to the car. The `DeployModel` API rejected the request before any transfer began. Common causes include the car going offline between selection and push, or the car type not being configured. Another cause is a deployment already in progress for the same model and car. If the car’s existing models were cleared before the push, the car currently has no models loaded. It will need new models pushed before it can race. Fix the underlying issue, then retry the push.

   The `DeployModel` function’s full name follows the deployment’s `DeepRacerIndyApi-DeployModelFunction` pattern, and its log group name is generated at deployment. To view its logs, open the AWS Lambda console, select the deploy model function, then choose **Monitor** and **View CloudWatch logs**.

1.  *A physical model import fails*

   The cause depends on the message that is shown:
   + A malware or scan message means the upload was rejected. These messages include *Malware detected in uploaded file*, *Model could not be scanned — re-upload a valid .tar.gz*, or a scan-timeout message. Re-upload a clean, valid `.tar.gz` file.
   + A generic message that includes a Request ID means the archive could not be converted. This message is *Model conversion failed — the uploaded model format may be incompatible*. Verify that the file is a valid AWS DeepRacer physical model archive that contains `model.pb` and `model_metadata.json`. If the problem continues, contact AWS Support and quote the Request ID.

1.  *Physical model imports fail because the malware scan service is unavailable*

   First, confirm that the Amazon GuardDuty Malware Protection plan is deployed and that its IAM role is configured correctly. This addresses the *Scan service unavailable* error.

   If the scan service is unavailable in your AWS Region, or is temporarily down, you can let imports proceed without a scan. Open the AWS Lambda console and select the model optimizer function. Its name is your deployment’s namespace followed by `-DeepRacerIndy-ModelOptimizerFn`, for example `default-DeepRacerIndy-ModelOptimizerFn`. Choose **Configuration**, then **Environment variables**, and set `ENABLE_GUARDDUTY_MALWARE_SCAN` to `false`. Imports then proceed without waiting for a malware scan.
**Warning**
Setting this variable to `false` bypasses malware scanning for imported physical models. Use it only as a temporary measure when the scan service is unavailable, and only if you trust the source of the models. Set it back to `true` when the scan service is restored. Updating the solution stack resets this variable to its deployed default.

1.  *A model optimization shows a **Failed** status*

   This is non-blocking. The model stays usable for virtual racing. To retry, select the model on the **Models** page and choose **Optimize for car** again.

1.  *I get the message "A deployment is already in progress for this model and car"*

   A push for the same model and car is already running. Wait for the current push to finish before you start another one for the same model and car.

1.  *I can’t submit a physical model to a community race*

   This is expected. Physical models are for car deployment only and cannot be entered into community races.

## Using CloudWatch Logs to diagnose issues
<a name="using-cloudwatch-logs-to-diagnose-issues"></a>

DeepRacer on AWS provisions a series of log groups to which AWS Lambda functions and other services configured by the solution emit logs. This section contains an inventory of those log groups and what they can be used for.

 **/aws/lambda/DeepRacerApis**

This log group contains the log output from all API handlers throughout the application. It is a useful first-stop for root-causing any form of failed request in the application.

 **/aws/lambda/DeepRacerEcrImages**

This log group contains the log output from all functions that are responsible for downloading and hosting the images that power the solution’s simulation capabilities. It can be useful for root-causing persistent errors that are returned from failed training or evaluation jobs.

 **/aws/lambda/DeepRacerIndy-RewardFunctionValidationFn**

This log group contains the log output from the reward function validator. This log group can be helpful in identifying why validation on a given reward function, or multiple reward functions, may have failed.

 **/aws/lambda/DeepRacerScheduled**

This log group contains the log output from all functions that are responsible for managing scheduled operations, such as resetting usage metrics at the turn of every month. It can be useful for diagnosing issues with usage metrics.

 **/aws/lambda/DeepRacerSystemEvents**

This log group contains the log output from all functions that are responsible for managing resource utilization, specifically model storage; as well as other cloud admin functions such as updating the CORS policy, updating web assets during a stack update, and other related functions.

 **/aws/lambda/DeepRacerUserIdentity**

This log group contains the log output from all functions that handle user authentication and management. The information in this log group can be useful for root-causing issues with inviting a user, initial account creation, user group assignment, and related processes.

 **/aws/lambda/DeepRacerWorkflow**

This log group contains the log output from the functions that handle model import workflows (dispatching, validating, and completing import operations). It can be useful for diagnosing issues with importing models.

 **/aws/lambda/DeepRacerTraining**

This log group contains the log output from the functions that are responsible for dispatching, initializing, monitoring, and finalizing training and evaluation jobs. It can be useful for diagnosing any errors that are thrown while a model is being trained or evaluated, or during a community race submission evaluation.

 **/aws/lambda/DeepRacerLiveRacing**

This log group contains the log output from all functions that support live race orchestration, including queue management, autolaunch, stream handling, and event state transitions. It is the primary log group for diagnosing issues with live races.

The functions that support physical racing events write to log groups whose names are generated when the solution is deployed, so they are not listed above. To reach them, open the **AWS Lambda** console and select the function you need, then choose **Monitor** → **View CloudWatch logs**. The function names are predictable:
+  `DeepRacerIndyApi-CreateLapFunction`, `DeepRacerIndyApi-UpdateLapFunction`, and `DeepRacerIndyApi-SetLapValidityFunction` handle lap recording, lap time corrections, and lap validity. `DeepRacerIndyApi-UpdateLapFunction` is where the `LAP_EDIT_AUDIT` entries are written.
+  `DeepRacerIndyApi-CreateRunFunction` and `DeepRacerIndyApi-TransitionRunStatusFunction` handle run creation and the run lifecycle, including scoring a submitted run.
+  `DeepRacerIndyApi-CreateEventFunction`, `DeepRacerIndyApi-EditEventFunction`, `DeepRacerIndyApi-TransitionEventStatusFunction`, `DeepRacerIndyApi-AddTrackToEventFunction`, and `DeepRacerIndyApi-RemoveTrackFromEventFunction` handle event and track configuration.
+  `DeepRacerEventManagement-DeleteWorkerFn` removes a deleted event’s records in the background. This is the log group to examine when `EventDeleteDLQAlarm` fires.

Substitute the operation name for any other Race Management function, following the same `DeepRacerIndyApi-{Operation}Function` pattern.

**Note**
Log output from these functions is retained for 90 days, apart from the event deletion worker, whose output is retained for 10 years.

## Using CloudWatch Logs Insights queries to diagnose issues
<a name="using-cloudwatch-logs-insights-queries-to-diagnose-issues"></a>

DeepRacer on AWS comes with a set of pre-configured sample queries that can be used either as-is or to create a custom query for logs in CloudWatch log groups. To access these:

1. Go to **Logs Insights** in Amazon CloudWatch, and select the log group(s) you would like to query.

1. Click **Saved and sample queries**, which will display a sidebar on the right-hand side of the screen with **DeepRacerOnAWS Sample Queries**, which can be expanded. Clicking one of the options will populate the sample log query in the query body.

1. When ready, click **Run query**.

 **Example:** The following CloudWatch Logs Insights query filters logs for error messages or exceptions, then displays the 200 most recent matching entries with their timestamps sorted newest first. This can help you get started with visualizing, analyzing, and localizing recent errors emitted by the system.

```
filter @message like /(?i)(Exception|error)/| fields @timestamp, @message | sort @timestamp desc | limit 200
```

## Using point-in-time recovery to restore data from a backup
<a name="using-point-in-time-recovery-to-restore-data-from-a-backup"></a>

DeepRacer on AWS uses an Amazon DynamoDB table that is configured with point-in-time recovery and continuous backups enabled by default. In the event that data in the table is accidentally deleted, lost, or otherwise corrupted, you can use the service’s backup recovery features to restore normal operation. See [Restoring a DynamoDB table from a backup](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Restore.Tutorial.html) for directions on how to restore your table to a certain point using the console or AWS CLI.
