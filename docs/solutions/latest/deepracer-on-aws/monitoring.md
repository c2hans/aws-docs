---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/monitoring.html
---

# Monitoring
<a name="monitoring"></a>

## Dashboard
<a name="dashboard"></a>

DeepRacer on AWS automatically provisions an Amazon CloudWatch dashboard which surfaces important graphs, metrics, and alarms that are relevant to operating the solution and can help with identifying potential issues. This dashboard can be accessed through the AWS Management Console by going to the **Amazon CloudWatch** console and clicking **Dashboards** in the left sidebar.

![DeepRacer on AWS dashboard top](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_dashboard_top.png)

The upper-half of this dashboard shows system alarm states (see [Alarms](#alarms)), followed by:
+  **Training instance usage** metrics, indicating the number of training jobs that are currently in use. This graph is helpful for identifying usage patterns for training and evaluation jobs, and can visually indicate cases such as when your current service quota is being reached.
+  **Training job outcomes**, indicating the number of training and evaluation jobs that have completed and/or failed.
+  **Queue metrics**, indicating the number of training and evaluation jobs that have been waiting in the queue over time.

![DeepRacer on AWS dashboard bottom](https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_dashboard_bottom.png)

The bottom-half of this dashboard shows additional graphs related to:
+  **API performance**, indicating the number of requests and latency, as well as the number of 4XX and 5XX errors over time.
+  **Database performance**, indicating the number of read and write capacity units being consumed, and the number of user and system errors over time.

## Alarms
<a name="alarms"></a>

DeepRacer on AWS automatically provisions CloudWatch alarms to monitor critical system components. These alarms help detect issues early and maintain the health of the deployment.

The deployment includes 20 CloudWatch alarms organized into eight monitoring categories:
+  **API import workflow monitoring** - 6 alarms that monitor model import processes
+  **User authentication monitoring** - 2 alarms that monitor user signup functions
+  **Asset processing monitoring** - 1 alarm that monitors asset packaging workflows
+  **Live race event monitoring** - 4 alarms that monitor live race broadcasting and IoT connectivity
+  **Live race workflow monitoring** - 2 alarms that monitor live race evaluation orchestration
+  **Race management monitoring** - 2 alarms that monitor physical event operations and event deletion
+  **Admin model management monitoring** - 2 alarms that monitor admin model download activity
+  **Model management monitoring** - a composite alarm that rolls up the model optimization and push-to-car alarms (handler errors, dead-letter-queue depth, and push-to-car Step Function failures)

Additionally, 3 email delivery alarms are provisioned when Amazon SES is selected as the delivery method.

 **API import workflow alarms**

These alarms monitor the various stages of importing models into the DeepRacer environment:

| Alarm Name | Purpose | Threshold |
| --- | --- | --- |
|  `ApiimportWorkflowCompletionErrorAlarm`  | Monitors completion errors in the API import workflow | ≥ 10 errors in 5 minutes |
|  `ApiimportWorkflowRewardValidationErrorAlarm`  | Monitors reward validation errors during import processing | ≥ 10 errors in 5 minutes |
|  `ApiimportWorkflowDlqProcessorErrorAlarm`  | Monitors dead letter queue (DLQ) processor errors | ≥ 10 errors in 5 minutes |
|  `ApiimportWorkflowImportAssetsErrorAlarm`  | Monitors asset import errors within the workflow | ≥ 10 errors in 5 minutes |
|  `ApiimportWorkflowModelValidationErrorAlarm`  | Monitors model validation errors during import | ≥ 10 errors in 5 minutes |
|  `ApiimportWorkflowImportModelLambdaErrorsAlarm`  | Composite alarm for Lambda function errors in the import workflow | Any associated alarm in ALARM state |

 **User authentication alarms**

These alarms monitor the Cognito User Pool operations and are more sensitive than workflow alarms:

| Alarm Name | Purpose | Threshold |
| --- | --- | --- |
|  `UserPoolPreSignUpErrorAlarm`  | Monitors errors in the pre-signup Lambda trigger function | ≥ 1 error in 1 minute |
|  `UserPoolPostSignUpErrorAlarm`  | Monitors errors in the post-signup Lambda trigger function | ≥ 1 error in 1 minute |

**Important**
User authentication alarms have very sensitive thresholds (1 error) and should be prioritized for notification setup.

 **Asset processing alarms**

This alarm monitors the asset packaging workflow:

| Alarm Name | Purpose | Threshold |
| --- | --- | --- |
|  `ApiAssetPackagingDLQAlarm`  | Monitors dead letter queue for asset packaging operations | ≥ 5 messages visible in 5 minutes |

 **Live race event alarms**

These alarms monitor the live race broadcasting infrastructure and IoT connectivity:

| Alarm Name | Purpose | Threshold |
| --- | --- | --- |
|  `BroadcastDLQAlarm`  | Monitors dead letter queue for live race broadcast events | > 0 messages visible in 1 minute |
|  `IoTPublishFailureAlarm`  | Monitors failures publishing live race updates to IoT Core | > 0 failures across 3 evaluation periods of 1 minute |
|  `IoTPublishLatencyAlarm`  | Monitors latency of live race event publishing to IoT Core | p99 latency > 1000ms across 3 evaluation periods of 1 minute |
|  `AttachPolicyLambdaErrorsAlarm`  | Monitors errors in the IoT policy attachment function for spectator connections | > 10 errors across 3 evaluation periods of 1 minute |

 **Live race workflow alarms**

These alarms monitor the Step Functions workflow that orchestrates live race evaluations:

| Alarm Name | Purpose | Threshold |
| --- | --- | --- |
|  `LiveRaceWorkflowErrorsAlarm`  | Monitors Step Function execution failures for live race evaluations | ≥ 1 failure in 5 minutes |
|  `StreamDLQAlarm`  | Monitors dead letter queue for the DynamoDB stream handler that triggers live race executions | ≥ 1 message visible in 1 minute |

 **Race management alarms**

These alarms monitor the handlers that support physical racing events, and the background removal of deleted events:

| Alarm Name | Purpose | Threshold |
| --- | --- | --- |
|  `EventManagementLambdaErrorsAlarm`  | Composite alarm covering errors in any Race Management handler. This includes event and track configuration, run lifecycle, lap recording, lap validity, lap time correction, statistics, and the event deletion worker | Any associated alarm in ALARM state |
|  `EventDeleteDLQAlarm`  | Monitors the dead letter queue for event deletion. Messages arriving here mean an event’s records could not be fully removed after three attempts, and some records may remain in the table | ≥ 1 message visible in 5 minutes |

**Important**
When `EventDeleteDLQAlarm` enters the ALARM state, the deleted event’s child records may be partially removed. Investigate the event deletion worker’s logs, then redrive the dead letter queue to retry the deletion.

 **Email delivery alarms**

The following alarms are created only when Amazon SES is selected as the delivery method for authentication emails:

| Alarm Name | Purpose | Threshold |
| --- | --- | --- |
|  `EmailVolumeAnomalyAlarm`  | Detects unusual email sending volume using anomaly detection | 2 of 3 hourly datapoints outside anomaly band |
|  `SesBounceRateAlarm`  | Monitors SES bounce rate to prevent sending suspension | > 5% average bounce rate in 5 minutes |
|  `SesComplaintRateAlarm`  | Monitors SES complaint rate to prevent sending suspension | > 0.1% average complaint rate in 5 minutes |

 **Admin model management alarms**

These alarms monitor the admin model management feature, which allows admins and race facilitators to view and download user models:

| Alarm Name | Purpose | Threshold |
| --- | --- | --- |
|  `AdminBulkDownloadAlarm`  | Monitors for unusually high volume of admin model downloads | ≥ 50 downloads in 5 minutes |
|  `AdminAuthFailureAlarm`  | Monitors for repeated authorization failures on admin endpoints | ≥ 10 failures in 5 minutes |

 **Model management alarms**

This composite alarm monitors the model management feature, which optimizes models for physical cars and delivers them to those cars:

| Alarm Name | Purpose | Threshold |
| --- | --- | --- |
|  `ModelManagementLambdaErrorsAlarm`  | Composite alarm that fires when any model management handler reports errors, the model-optimizer dead letter queue (DLQ) depth is elevated, the DLQ processor errors, or the push-to-car Step Function fails or times out | Any associated alarm in ALARM state |

### Configuring alarm actions
<a name="config-alarm-actions"></a>

By default, the solution creates alarms without automated actions. To receive notifications when alarms trigger:

1. Go to the CloudWatch console

1. Select **Alarms** from the left navigation

1. Choose an alarm from the list

1. Select **Actions** → **Edit**

1. Add notification actions such as:
   + SNS topic for email alerts
   + Auto Scaling actions
   + EC2 actions

### Viewing alarm status
<a name="view-alarm-status"></a>

To check status of an alarm:

1. Open the CloudWatch console

1. Select **Alarms** → **All alarms**

1. Filter by the alarm name prefix `deepracer-on-aws-`

1. Review the **State** column for any alarms in ALARM status

When an alarm enters the ALARM state, investigate the associated service logs and metrics to identify the root cause.

## Race management metrics
<a name="race-management-metrics"></a>

Physical racing events publish the following custom CloudWatch metrics. These are not shown on the provisioned dashboard. View them in the CloudWatch console under **Metrics**, or add them to a dashboard of your own.

| Metric | Namespace | What it tells you |
| --- | --- | --- |
|  `CombinedLeaderboardRecomputed`  |  `DeepRacerIndy`  | A combined leaderboard was successfully recalculated after a track result changed. Expect one for each submitted result in a multi-track event. |
|  `CombinedLeaderboardRecomputeFailed`  |  `DeepRacerIndy`  | A combined leaderboard could not be recalculated. Individual track leaderboards are unaffected, but the combined standings may be out of date until the next successful recalculation. |
|  `EventDeleteCompleted`  |  `DeepRacerIndyEventManagement`  | A deleted event and all of its records were fully removed. |
|  `EventDeleteFailed`  |  `DeepRacerIndyEventManagement`  | An attempt to remove a deleted event’s records failed. The attempt is retried; if it fails three times, the message moves to the dead letter queue and `EventDeleteDLQAlarm` fires. |

A sustained rise in `CombinedLeaderboardRecomputeFailed` during an event is worth investigating while the event is still running, because the combined standings shown to spectators will drift from the individual track results.
