---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_NotificationAPI_ElementsOfANotification.html
---

**Amazon Mechanical Turk will permanently close on September 30, 2026.** For Workers and Requesters currently using the service, visit our [Amazon Mechanical Turk help page](https://www.mturk.com/help) to learn how you can prepare for this closure.

|  |
| --- |
| ![WARNING](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# Elements of a Notification Message
<a name="ApiReference_NotificationAPI_ElementsOfANotification"></a>

Notification messages contain one or more `Event` data structures that describe recent activity for HITs of a HIT type.

## The Notification API Version
<a name="ApiReference_NotificationAPI_ElementsOfANotification-the-notification-api-version"></a>

Similar to how a REST request that is sent to the Amazon Mechanical Turk Requester service must include a `Version` parameter to indicate which version of the service API the client is expecting to use, a notification message must also include a `Version` parameter. This version string is identical to the version that is included in the notification specification for the HIT type.

**Tip**
 Your application may need to accommodate receiving notification messages of different versions at the same time if you want to upgrade your notification specifications to a new version without missing messages. You can avoid having to accommodate multiple API versions by first disabling the notification specifications that use the old version, upgrading your application to use the new version, then updating the notification specifications to use the new version and re-enable notifications.

 When a new version of the notification API is made available, all existing notification specifications will continue to use the API versions they were using previously. You must update your notification specifications to use a new version of the API.

## Events
<a name="ApiReference_NotificationAPI_ElementsOfANotification-events"></a>

 A notification message describes one or more events that happened in regards to a HIT type. Each event includes:
+ the event type (`EventType`), a value corresponding to the `EventType` value in the [notification specification data structure](ApiReference_NotificationDataStructureArticle.md)
+ the time of the event (`EventTime`), as a [dateTime](http://www.w3.org/TR/xmlschema-2/#dateTime) in the Coordinated Universal Time time zone, such as **2005-01-31T23:59:59Z**
+ the HIT type ID for the event (`HITTypeId`)
+ the HIT ID for the event (`HITId`)
+ the assignment ID for the event, if applicable (`AssignmentId`)

 Multiple events may be batched into a single notification message.
