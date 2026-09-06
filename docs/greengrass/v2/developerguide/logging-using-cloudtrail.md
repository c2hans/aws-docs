---
source_url: https://docs.aws.amazon.com/greengrass/v2/developerguide/logging-using-cloudtrail.html
---

# Log AWS IoT Greengrass V2 API calls with AWS CloudTrail
<a name="logging-using-cloudtrail"></a>

AWS IoT Greengrass V2 is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in AWS IoT Greengrass Version 2. CloudTrail captures all API calls for AWS IoT Greengrass as events. The calls that are captured include calls from the AWS IoT Greengrass console and code calls to the AWS IoT Greengrass API operations.

If you create a trail, you can enable continuous delivery of CloudTrail events to an S3 bucket, including events for AWS IoT Greengrass. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**. Using the information collected by CloudTrail, you can determine the request that was made to AWS IoT Greengrass, the IP address from which the request was made, who made the request, when it was made, and additional details.

For more information about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html).

**Topics**
+ [AWS IoT Greengrass V2 information in CloudTrail](#service-name-info-in-cloudtrail)
+ [AWS IoT Greengrass data events in CloudTrail](#greengrass-data-events-cloudtrail)
+ [AWS IoT Greengrass management events in CloudTrail](#greengrass-management-events-cloudtrail)
+ [Understanding AWS IoT Greengrass V2 log file entries](#understanding-service-name-entries)

## AWS IoT Greengrass V2 information in CloudTrail
<a name="service-name-info-in-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in AWS IoT Greengrass, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Viewing events with CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html).

For an ongoing record of events in your AWS account, including events for AWS IoT Greengrass, create a trail. A *trail* enables CloudTrail to deliver log files to an S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following:
+ [Overview for creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail supported services and integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html)
+ [Configuring Amazon SNS notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.html)
+ [Receiving CloudTrail log files from multiple regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail log files from multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

All AWS IoT Greengrass V2 actions are logged by CloudTrail and are documented in the [AWS IoT Greengrass V2 API Reference](https://docs.aws.amazon.com/greengrass/v2/APIReference/Welcome.html). For example, calls to the `CreateComponentVersion`, `CreateDeployment` and `CancelDeployment` actions generate entries in the CloudTrail log files.

Every event or log entry contains information about who generated the request. The identity information helps you determine the following:
+ Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).

## AWS IoT Greengrass data events in CloudTrail
<a name="greengrass-data-events-cloudtrail"></a>

[Data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#logging-data-events) provide information about the resource operations performed on or in a resource (for example, getting a component version or the configuration of a deployment). These are also known as data plane operations. Data events are often high-volume activities. By default, CloudTrail doesn’t log data events. The CloudTrail **Event history** doesn't record data events.

Additional charges apply for data events. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/).

You can log data events for the AWS IoT Greengrass resource types by using the CloudTrail console, AWS CLI, or CloudTrail API operations. The [table](#data-events-table) in this section shows the resource types available for AWS IoT Greengrass.
+ To log data events using the CloudTrail console, create a [trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-a-trail-using-the-console-first-time.html#creating-a-trail-in-the-console) or [event data store](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-event-data-store-cloudtrail.html) to log data events, or [update an existing trail or event data store](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#logging-data-events-console) to log data events.

  1. Choose **Data events** to log data events.

  1. From the **Data event type** list, choose the resource type for which you want to log data events.

  1. Choose the log selector template you want to use. You can log all data events for the resource type, log all `readOnly` events, log all `writeOnly` events, or create a custom log selector template to filter on the `readOnly`, `eventName`, and `resources.ARN` fields.
+ To log data events using the AWS CLI, configure the `--advanced-event-selectors` parameter to set the `eventCategory` field equal to `Data` and the `resources.type` field equal to the resource type value (see [table](#data-events-table)). You can add conditions to filter on the values of the `readOnly`, `eventName`, and `resources.ARN` fields.
  + To configure a trail to log data events, run the [put-event-selectors](https://docs.aws.amazon.com/cli/latest/reference/cloudtrail/put-event-selectors.html) command. For more information, see [Logging data events for trails with the AWS CLI](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#logging-data-events-CLI-trail-examples).
  + To configure an event data store to log data events, run the [create-event-data-store](https://docs.aws.amazon.com/cli/latest/reference/cloudtrail/create-event-data-store.html) command to create a new event data store to log data events, or run the [update-event-data-store](https://docs.aws.amazon.com/cli/latest/reference/cloudtrail/update-event-data-store.html) command to update an existing event data store. For more information, see [Logging data events for event data stores with the AWS CLI](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#logging-data-events-CLI-eds-examples).

The following table lists the AWS IoT Greengrass resource types. The **Data event type (console)** column shows the value to choose from the **Data event type** list on the CloudTrail console. The **resources.type value** column shows the `resources.type` value, which you would specify when configuring advanced event selectors using the AWS CLI or CloudTrail APIs. The **Data APIs logged to CloudTrail** column shows the API calls logged to CloudTrail for the resource type.

| Data event type (console) | resources.type value | Data APIs logged to CloudTrail |
| --- | --- | --- |
| IoT certificate | AWS::IoT::Certificate |  +  VerifyClientDeviceIdentity <br />+  VerifyClientDeviceIoTCertificateAssociation   |
| IoT Greengrass component version |  AWS::GreengrassV2::ComponentVersion  |  +  [ResolveComponentCandidates](https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ResolveComponentCandidates.html)   |
| IoT Greengrass deployment |  AWS::GreengrassV2::Deployment  |  +  GetDeploymentConfiguration   |
| IoT thing | AWS::IoT::Thing |  +  ListThingGroupsForCoreDevices <br />+  PutCertificateAuthorities <br />+  VerifyClientDeviceIoTCertificateAssociation   |

You can configure advanced event selectors to filter on the `eventName`, `readOnly`, and `resources.ARN` fields to log only those events that are important to you.

Add a filter on `eventName` to include or exclude specific data APIs.

For more information about these fields, see [AdvancedFieldSelector](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.html).

The following examples show how to configure advanced selectors using the AWS CLI. Replace {{TrailName}} and {{region}} with your own information.

**Example – Log data events for IoT things**

```
aws cloudtrail put-event-selectors --trail-name {{TrailName}} --region {{region}} \
--advanced-event-selectors \
‘[
    {
            “Name”: “Log all thing data events”,
            “FieldSelectors”: [
                { “Field”: “eventCategory”, “Equals”: [“Data”] },
                { “Field”: “resources.type”, “Equals”: [“AWS::IoT::Thing”] }
            ]
        }
]’
```

**Example – Filter on a specific IoT thing API**

```
aws cloudtrail put-event-selectors --trail-name {{TrailName}} --region {{region}} \
--advanced-event-selectors \
‘[
    {
            “Name”: “Log IoT Greengrass PutCertificateAuthorities API calls”,
            “FieldSelectors”: [
                { “Field”: “eventCategory”, “Equals”: [“Data”] },
                { “Field”: “resources.type”, “Equals”: [“AWS::IoT::Thing”] },
                { “Field”: “eventName”, “Equals”: [“PutCertificateAuthorities”] }
            ]
    }
]’
```

**Example – Log all Greengrass data events**

```
aws cloudtrail put-event-selectors --trail-name {{TrailName}} --region {{region}} \
--advanced-event-selectors \
‘[
    {
        “Name”: “Log all certificate data events”,
        “FieldSelectors”: [
            {
                “Field”: “eventCategory”,
                “Equals”: [
                    “Data”
                ]
            },
            {
                “Field”: “resources.type”,
                “Equals”: [
                    “AWS::IoT::Certificate”
                ]
            }
        ]
    },
    {
        “Name”: “Log all component version data events”,
        “FieldSelectors”: [
            {
                “Field”: “eventCategory”,
                “Equals”: [
                    “Data”
                ]
            },
            {
                “Field”: “resources.type”,
                “Equals”: [
                    “AWS::GreengrassV2::ComponentVersion”
                ]
            }
        ]
    },
    {
        “Name”: “Log all deployment version”,
        “FieldSelectors”: [
            {
                “Field”: “eventCategory”,
                “Equals”: [
                    “Data”
                ]
            },
            {
                “Field”: “resources.type”,
                “Equals”: [
                    “AWS::GreengrassV2::Deployment”
                ]
            }
        ]
    },
    {
        “Name”: “Log all thing data events”,
        “FieldSelectors”: [
            {
                “Field”: “eventCategory”,
                “Equals”: [
                    “Data”
                ]
            },
            {
                “Field”: “resources.type”,
                “Equals”: [
                    “AWS::IoT::Thing”
                ]
            }
        ]
    }
]’
```

## AWS IoT Greengrass management events in CloudTrail
<a name="greengrass-management-events-cloudtrail"></a>

[Management events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html#logging-management-events) provide information about management operations that are performed on resources in your AWS account. These are also known as control plane operations. By default, CloudTrail logs management events.

AWS IoT Greengrass logs all AWS IoT Greengrass control plane operations as management events. For a list of the AWS IoT Greengrass control plane operations that AWS IoT Greengrass logs to CloudTrail, see the [AWS IoT Greengrass API reference, version 2](https://docs.aws.amazon.com/greengrass/v2/APIReference/Welcome.html).

## Understanding AWS IoT Greengrass V2 log file entries
<a name="understanding-service-name-entries"></a>

A trail is a configuration that enables delivery of events as log files to an S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source. It includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't appear in any specific order.

The following example shows a CloudTrail log entry that demonstrates the `CreateDeployment` action.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE",
        "arn": "arn:aws:iam::123456789012:user/Administrator",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "Administrator"
    },
    "eventTime": "2021-01-06T02:38:05Z",
    "eventSource": "greengrass.amazonaws.com",
    "eventName": "CreateDeployment",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "203.0.113.0",
    "userAgent": "aws-cli/2.1.9 Python/3.7.9 Windows/10 exe/AMD64 prompt/off command/greengrassv2.create-deployment",
    "requestParameters": {
        "deploymentPolicies": {
            "failureHandlingPolicy": "DO_NOTHING",
            "componentUpdatePolicy": {
                "timeoutInSeconds": 60,
                "action": "NOTIFY_COMPONENTS"
            },
            "configurationValidationPolicy": {
                "timeoutInSeconds": 60
            }
        },
        "deploymentName": "Deployment for MyGreengrassCoreGroup",
        "components": {
            "aws.greengrass.Cli": {
                "componentVersion": "2.0.3"
            }
        },
        "iotJobConfiguration": {},
        "targetArn": "arn:aws:iot:us-west-2:123456789012:thinggroup/MyGreengrassCoreGroup"
    },
    "responseElements": {
        "iotJobArn": "arn:aws:iot:us-west-2:123456789012:job/fdfeba1d-ac6d-44ef-ab28-54f684ea578d",
        "iotJobId": "fdfeba1d-ac6d-44ef-ab28-54f684ea578d",
        "deploymentId": "4196dddc-0a21-4c54-a985-66a525f6946e"
    },
    "requestID": "311b9529-4aad-42ac-8408-c06c6fec79a9",
    "eventID": "c0f3aa2c-af22-48c1-8161-bad4a2ab1841",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "123456789012"
}
```
