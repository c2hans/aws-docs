---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_SetHITTypeNotificationOperation.html
---

**Amazon Mechanical Turk will permanently close on September 30, 2026.** For Workers and Requesters currently using the service, visit our [Amazon Mechanical Turk help page](https://www.mturk.com/help) to learn how you can prepare for this closure.

|  |
| --- |
| ![WARNING](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# SetHITTypeNotification
<a name="ApiReference_SetHITTypeNotificationOperation"></a>

## Description
<a name="ApiReference_SetHITTypeNotificationOperation-description"></a>

 The `SetHITTypeNotification` operation creates, updates, disables or re-enables notifications for a HIT type.

 If you call the `SetHITTypeNotification` operation for a HIT type that already has a notification specification, the operation replaces the old specification with a new one.

 You can call the `SetHITTypeNotification` operation to enable or disable notifications for the HIT type, without having to modify the notification specification itself.

 You can call this operation at any time to change the value of the of the `Active` parameter of a HIT type. You can specify changes to the `Active` status without specifying a new notification specification (the `Notification` parameter).

 To change the `Active` status of a HIT type's notifications, the HIT type must already have a notification specification, or one must be provided in the same call to `SetHITTypeNotification`.

**Note**
 After you make the call to `SetHITTypeNotification`, it can take up to five minutes for changes to a HIT type's notification specification to take effect.

## Request Parameters
<a name="ApiReference_SetHITTypeNotificationOperation-request-parameters"></a>

 The `SetHITTypeNotification` operation accepts parameters common to all operations. Some common parameters are required. See [Common Parameters](ApiReference_CommonParametersArticle.md) for more information.

 The following parameters are specific to the `SetHITTypeNotification` operation:

| Name | Description | Required |
| --- | --- | --- |
|  `Operation`  | The name of the operation<br />Type: String<br />Valid Values: SetHITTypeNotification<br />Default: None | Yes |
|  `HITTypeId`  |  The ID of the HIT type whose notification specification is being updated, as returned by the [RegisterHITType](ApiReference_RegisterHITTypeOperation.md) operation. <br />Type: String<br />Default: None | Yes |
|  `Notification`  | The notification specification for the HIT type.<br /> Type: a [Notification](ApiReference_NotificationDataStructureArticle.md) data structure. <br /> Default: None.<br /> Constraint: You must specify either the `Notification` parameter or the `Active` parameter for the call to `SetHITTypeNotification` to succeed.  | Yes |
|  `Active`  |  Specifies whether notifications are sent for HITs of this HIT type, according to the notification specification. <br />Type: Boolean<br />Valid Values: true \| false<br />Default: None. If omitted, the active status of the HIT type's notification specification is unchanged<br /> Constraint: You must specify either the `Notification` parameter or the `Active` parameter for the call to `SetHITTypeNotification` to succeed.  | No |

## Response Elements
<a name="ApiReference_SetHITTypeNotificationOperation-response-elements"></a>

 A successful request for the `SetHITTypeNotification` operation returns with no errors. The response includes the elements described in the following table. The operation returns no other data.

| Name | Description |
| --- | --- |
|  `SetHITTypeNotificationResult`  |  Contains a `Request` element if the **Request** `ResponseGroup` is specified.  |

## Examples
<a name="ApiReference_SetHITTypeNotificationOperation-examples"></a>

The following example shows how to use the `SetHITTypeNotification` operation.

### Sample Request
<a name="ApiReference_SetHITTypeNotificationOperation-examples-sample-request"></a>

 The following example sets the notification specification for a HIT type to send the Requester an email whenever a Worker submits an assignment for a HIT of the specified type.

```
https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
&AWSAccessKeyId={{[the Requester's Access Key ID]}}
&Operation=SetHITTypeNotification
&Signature={{[signature for this request]}}
&Timestamp={{[your system's local time]}}
&HITTypeId=T100CN9P324W00EXAMPLE
&Notification.1.Destination=janedoe@example.com
&Notification.1.Transport=Email
&Notification.1.Version=2006-05-05
&Notification.1.EventType=AssignmentSubmitted
```

### Sample Response
<a name="ApiReference_SetHITTypeNotificationOperation-examples-sample-response"></a>

The following is an example response.

```
<SetHITTypeNotificationResult>
  <Request>
    <IsValid>True</IsValid>
  </Request>
</SetHITTypeNotificationResult>
```
