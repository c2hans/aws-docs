---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_NotificationDataStructureArticle.html
---

|  |
| --- |
| ![WARNING](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# Notification
<a name="ApiReference_NotificationDataStructureArticle"></a>

## Description
<a name="ApiReference_NotificationDataStructureArticle-description"></a>

 The Notification data structure describes a HIT event notification for a HIT type.

 The Notification data structure is used as a parameter for the following operations:
+  [SetHITTypeNotification](ApiReference_SetHITTypeNotificationOperation.md)
+  [SendTestEventNotification](ApiReference_SendTestEventNotificationOperation.md)

**Note**
 The latest Amazon Mechanical Turk WSDL includes deprecated notification transport signature protocols for backwards compatibility.

## Elements
<a name="ApiReference_NotificationDataStructureArticle-elements"></a>

 The Notification structure can contain the elements described in the following table. When the structure is used in a request, elements described as **Required** must be included for the request to succeed.

| Name | Description | Required |
| --- | --- | --- |
|  `Destination`  | The destination for notification messages. <br />Type: +  For email notifications (if `Transport` is **Email**), this is an email address.  <br />+  For Amazon Simple Queue Service (Amazon SQS) notifications (if `Transport` is **SQS**), this is the URL for your Amazon SQS queue. For more information, see [Notification Handling Using Amazon SQS](ApiReference_NotificationReceptorAPI_SQSTransportArticle.md).  <br />Default: None | Yes |
|  `Transport`  | The method Amazon Mechanical Turk uses to send the notification.<br />Type: String<br />Valid Values: Email \| SQS<br />Default: None | Yes |
|  `Version`  | The version of the Notification API WSDL/schema, see [WSDL and Schema Locations](ApiReference_WsdlLocationArticle.md). <br />Type: String<br />Default: None | Yes |
|  `EventType`  | The events that should cause notifications to be sent. You can specify multiple events by repeating this element. The Ping event is only valid for the [SendTestEventNotification](ApiReference_SendTestEventNotificationOperation.md) operation.<br />Type: String<br />Valid Values: AssignmentAccepted \| AssignmentAbandoned \| AssignmentReturned \| AssignmentSubmitted \| HITReviewable \| HITExpired \| Ping<br />Default: None | Yes |

## Example
<a name="ApiReference_NotificationDataStructureArticle-example"></a>

In the following example the notification specification specifies that an event notification message will be sent by email when a Worker returns or abandons a HIT and the message will use the **2006-05-05** version of the notification message schema.

```
<Notification>
  <Destination>janedoe@example.com</Destination>
  <Transport>Email</Transport>
  <Version>2006-05-05</Version>
  <EventType>AssignmentAbandoned</EventType>
  <EventType>AssignmentReturned</EventType>
</Notification>
```
