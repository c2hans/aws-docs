---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/ag/cloudtrail.html
---

# Using AWS CloudTrail to log API calls
<a name="cloudtrail"></a>

The Amazon Chime SDK is integrated with AWS CloudTrail, a service that provides a record of actions taken in the Amazon Chime SDK by a user, role, or AWS service. CloudTrail captures all API calls for the Amazon Chime SDK as events, including calls from the Amazon Chime SDK console and code calls to the Amazon Chime SDK APIs.

If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for the Amazon Chime SDK. If you don't configure a trail, you can still view the most recent events in the CloudTrail console on the **Event history** page. The information includes each request, the IP addresses from which the requests were made, and who made the request.

CloudTrail is enabled on your AWS account when you create the account. When the Amazon Chime administration console makes an API call, CloudTrail records that activity in an event. To see the events, start the CloudTrail console and go to **Event history** . You can view, search, and download recent events in your AWS account. For more information, see [Viewing events with CloudTrail event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html).

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

## Creating a trail
<a name="create-trail"></a>

The following topics explain how to use the CloudTrail console to create a trail. By default, when you create a trail in the console, the trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify.

Follow these topics in the order listed.

1. [Overview for creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)

1. [CloudTrail supported services and integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html#cloudtrail-aws-service-specific-topics-integrations)

1. [Configuring Amazon SNS notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting_notifications_top_level.html)

1. [Receiving CloudTrail log files from multiple Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail log files from multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

## Data captured by a trail
<a name="cloudtrail-data"></a>

CloudTrail logs all Amazon Chime SDK actions. For information about the actions, refer to [*Amazon Chime SDK API Reference*](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/Welcome.html). For example, calls to the [CreateAttendee](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meetings-chime_CreateAttendee.html), action generate entries in the CloudTrail log files. Every event contains information about who generated the request. The identity information helps you determine the following:
+ Whether the request was made with root or IAM user credentials.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).

## Understanding Amazon Chime SDK log file entries
<a name="understanding-service-name-entries"></a>

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files are not an ordered stack trace of the public API calls, so they do not appear in any specific order.

Entries for the Amazon Chime SDK are identified by the **chime.amazonaws.com** event source.

If you have configured Active Directory for your Amazon Chime SDK account, see [Logging AWS Directory Service API calls using CloudTrail](https://docs.aws.amazon.com/directoryservice/latest/devguide/cloudtrail_logging.html). This describes how to monitor for issues that might affect your Amazon Chime SDK users’ ability to sign in.

The following example shows a CloudTrail log entry for Amazon Chime SDK:

```
{"eventVersion":"1.05",
         "userIdentity":{
            "type":"IAMUser",
            "principalId":"{{AAAAAABBBBBBBBEXAMPLE}}",
            "arn":"arn:aws:iam::{{123456789012}}:user/{{Alice}}",
            "accountId":"{{0123456789012}}",
            "accessKeyId":"{{AAAAAABBBBBBBBEXAMPLE}}",
            "sessionContext":{
               "attributes":{
                  "mfaAuthenticated":"false",
                  "creationDate":"{{2017-07-24T17:57:43}}Z"
               },
               "sessionIssuer":{
                  "type":"Role",
                  "principalId":"{{AAAAAABBBBBBBBEXAMPLE}}",
                  "arn":"arn:aws:iam::{{123456789012}}:role/{{Joe}}",
                  "accountId":"{{123456789012}}",
                  "userName":"{{Joe}}"
               }
            }
         } ,
         "eventTime":"{{2017-07-24T17:58:21}}Z",
         "eventSource":"chime.amazonaws.com",
         "eventName":"AddDomain",
         "awsRegion":"us-east-1",
         "sourceIPAddress":"{{72.21.198.64}}",
         "userAgent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
         "errorCode":"ConflictException",
         "errorMessage":"Request could not be completed due to a conflict",
         "requestParameters":{
            "domainName":"{{example.com}}",
            "accountId":"{{11aaaaaa1-1a11-1111-1a11-aaadd0a0aa00}}"
         },
         "responseElements":null,
         "requestID":"{{be1bee1d-1111-11e1-1eD1-0dc1111f1ac1}}",
         "eventID":"{{00fbeee1-123e-111e-93e3-11111bfbfcc1}}",
         "eventType":"AwsApiCall",
         "recipientAccountId":"{{123456789012}}"
      }
```
