---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_NotificationReceptorAPIArticle.html
---

|  |
| --- |
| ![WARNING](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# The Notification API
<a name="ApiReference_NotificationReceptorAPIArticle"></a>

**Topics**
+ [Elements of a Notification Message](ApiReference_NotificationAPI_ElementsOfANotification.md)
+ [Notification Handling Using Amazon SQS](ApiReference_NotificationReceptorAPI_SQSTransportArticle.md)

This section describes how to set up and handle Amazon Mechanical Turk event notification messages. A notification message describes one or more events that happened in regards to a HIT type. For more information, see [Elements of a Notification Message](ApiReference_NotificationAPI_ElementsOfANotification.md).

You can configure Amazon Mechanical Turk to notify you whenever certain events occur during the life cycle of a HIT. Mechanical Turk can send you a notification message when a Worker accepts, abandons, returns, or submits an assignment, when a HIT becomes "reviewable", or when a HIT expires, for any HIT of a given HIT type.

Notifications are specified as part of a HIT type. To set up notifications for a HIT type, you call the [SetHITTypeNotification](ApiReference_SetHITTypeNotificationOperation.md) operation with a HIT type ID and a notification specification. For more information about HIT types, see [Understanding HIT Types](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/Concepts_HITTypesArticle.html).

A notification specification is defined by a [Notification](ApiReference_NotificationDataStructureArticle.md) data structure, which describes a HIT event notification for the HIT type. The notification specification is passed as the `Notification` parameter when calling [SetHITTypeNotification](ApiReference_SetHITTypeNotificationOperation.md).

Amazon Mechanical Turk can send a notification to an email address or to an Amazon Simple Queue Service (Amazon SQS) queue. For more information, see [Notification Handling Using Amazon SQS](ApiReference_NotificationReceptorAPI_SQSTransportArticle.md).

For more information about setting up and handling notifications, see [Creating and Managing Notifications](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/Concepts_NotificationsArticle.html).

You can test your application's ability to receive notifications using [SendTestEventNotification](ApiReference_SendTestEventNotificationOperation.md).

**Note**
 The latest Amazon Mechanical Turk WSDL includes deprecated notification transport signature protocols for backwards compatibility.
