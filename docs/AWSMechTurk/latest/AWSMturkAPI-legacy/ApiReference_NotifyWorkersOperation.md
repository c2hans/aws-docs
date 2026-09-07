---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_NotifyWorkersOperation.html
---

|  |
| --- |
| ![WARNING](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# NotifyWorkers
<a name="ApiReference_NotifyWorkersOperation"></a>

## Description
<a name="ApiReference_NotifyWorkersOperation-description"></a>

 The `NotifyWorkers` operation sends an email to one or more Workers that you specify with the Worker ID.

 You can specify up to 100 Worker IDs to send the same message with a single call to the `NotifyWorkers` operation.

**Note**
The `NotifyWorkers` operation will send a notification email to a Worker only if you have previously approved or rejected work from the Worker.

## Request Parameters
<a name="ApiReference_NotifyWorkersOperation-request-parameters"></a>

 The `NotifyWorkers` operation accepts parameters common to all operations. Some common parameters are required. See [Common Parameters](ApiReference_CommonParametersArticle.md) for more information.

 The following parameters are specific to the `NotifyWorkers` operation:

| Name | Description | Required |
| --- | --- | --- |
|  `Operation`  | The name of the operation<br />Type: String<br />Valid Values: NotifyWorkers<br />Default: None | Yes |
|  `Subject`  | The subject line of the email message to send.<br />Type: String<br />Default: None<br />Constraints: can include up to 200 characters. | Yes |
|  `MessageText`  | The text of the email message to send<br />Type: String<br />Default: None<br />Constraints: can include up to 4,096 characters | Yes |
|  `WorkerId`  |  The ID of the Worker to notify, as returned by the [ GetAssignmentsForHIT](ApiReference_GetAssignmentsForHITOperation.md) operation. <br />Type: String<br />Default: None<br />Constraints: You can repeat this parameter up to 100 times to notify multiple Workers. | Yes |

## Response Elements
<a name="ApiReference_NotifyWorkersOperation-response-elements"></a>

 A successful request for the `NotifyWorkers` operation returns with no errors. The response includes the elements described in the following table. The operation returns no other data.

| Name | Description |
| --- | --- |
|  `NotifyWorkersResult`  |  Contains a `Request` element if the **Request** `ResponseGroup` is specified.  |

## Examples
<a name="ApiReference_NotifyWorkersOperation-examples"></a>

The following example shows how to use the `NotifyWorkers` operation.

### Sample Request
<a name="ApiReference_NotifyWorkersOperation-examples-sample-request"></a>

The following example sends an email message to three Workers.

```
https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
&AWSAccessKeyId={{[the Requester's Access Key ID]}}
&Version=2017-01-17
&Operation=NotifyWorkers
&Signature={{[signature for this request]}}
&Timestamp={{[your system's local time]}}
&Subject=Thank%20you
&MessageText=Hello!%20Just%20wanted%20to%20say%20thank%20you...
&WorkerId.1=AZ3123EXAMPLE
&WorkerId.2=AZ3456EXAMPLE
&WorkerId.3=AZ3789EXAMPLE
```

### Sample Response
<a name="ApiReference_NotifyWorkersOperation-examples-sample-response"></a>

The following is an example response.

```
<NotifyWorkersResult>
  <Request>
    <IsValid>True</IsValid>
  </Request>
</NotifyWorkersResult>
```
