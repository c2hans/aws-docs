---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_SendTestEventNotificationOperation.html
---

|  |
| --- |
| ![WARNING](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# SendTestEventNotification
<a name="ApiReference_SendTestEventNotificationOperation"></a>

## Description
<a name="ApiReference_SendTestEventNotificationOperation-description"></a>

 The `SendTestEventNotification` operation causes Amazon Mechanical Turk to send a notification message as if a HIT event occurred, according to the provided notification specification. This allows you to test notifications without setting up notifications for a real HIT type and trying to trigger them using the website.

 When you call this operation, the service sends the test notification immediately.

## Request Parameters
<a name="ApiReference_SendTestEventNotificationOperation-request-parameters"></a>

 The `SendTestEventNotification` operation accepts parameters common to all operations. Some common parameters are required. See [Common Parameters](ApiReference_CommonParametersArticle.md) for more information.

 The following parameters are specific to the `SendTestEventNotification` operation:

| Name | Description | Required |
| --- | --- | --- |
|  `Operation`  | The name of the operation.<br />Type: String<br />Valid Values: SendTestEventNotification<br />Default: None | Yes |
|  `Notification`  |  The notification specification to test. This value is identical to the value you would provide to the [SetHITTypeNotification](ApiReference_SetHITTypeNotificationOperation.md) operation when you establish the notification specification for a HIT type. <br />Type: a [Notification](ApiReference_NotificationDataStructureArticle.md) data structure<br />Default: None | Yes |
|  `TestEventType`  |  The event to simulate to test the notification specification. This event is included in the test message even if the notification specification does not include the event type. The notification specification does not filter out the test event. <br /> Type: an `EventType` element of the [Notification](ApiReference_NotificationDataStructureArticle.md) data structure. <br />Default: None | Yes |

## Response Elements
<a name="ApiReference_SendTestEventNotificationOperation-response-elements"></a>

 A successful request for the `SendTestEventNotification` operation returns with no errors. The response includes the elements described in the following table. The operation returns no other data.

| Name | Description |
| --- | --- |
|  `SendTestEventNotificationResult`  |  Contains a `Request` element if the **Request** `ResponseGroup` is specified.  |

## Examples
<a name="ApiReference_SendTestEventNotificationOperation-examples"></a>

The following example shows how to use the `SendTestEventNotification` operation.

### Sample Request
<a name="ApiReference_SendTestEventNotificationOperation-examples-sample-request"></a>

 The following example sends a notification message for a simulated `AssignmentSubmitted` event to an email address.

```
https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
&AWSAccessKeyId={{[the Requester's Access Key ID]}}
&Operation=SendTestEventNotification
&Signature={{[signature for this request]}}
&Timestamp={{[your system's local time]}}
&Notification.1.Destination=janedoe@example.com
&Notification.1.Transport=Email
&Notification.1.Version=2006-05-05
&Notification.1.EventType=AssignmentSubmitted
&TestEventType=AssignmentSubmitted
```

### Sample Response
<a name="ApiReference_SendTestEventNotificationOperation-examples-sample-response"></a>

The following is an example response.

```
<SendTestEventNotificationResult>
  <Request>
    <IsValid>True</IsValid>
  </Request>
</SendTestEventNotificationResult>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
