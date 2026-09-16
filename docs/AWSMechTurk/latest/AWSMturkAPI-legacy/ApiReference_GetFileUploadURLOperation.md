---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_GetFileUploadURLOperation.html
---

**Amazon Mechanical Turk will permanently close on September 30, 2026.** For Workers and Requesters currently using the service, visit our [Amazon Mechanical Turk help page](https://www.mturk.com/help) to learn how you can prepare for this closure.

|  |
| --- |
| ![WARNING](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# GetFileUploadURL
<a name="ApiReference_GetFileUploadURLOperation"></a>

## Description
<a name="ApiReference_GetFileUploadURLOperation-description"></a>

 The `GetFileUploadURL` operation generates and returns a temporary URL. You use the temporary URL to retrieve a file uploaded by a Worker as an answer to a `FileUploadAnswer` question for a HIT. For information about the `FileUploadAnswer` answer, see [QuestionForm](ApiReference_QuestionFormDataStructureArticle.md).

 The temporary URL is generated the instant the `GetFileUploadURL` operation is called, and is valid for 60 seconds.

**Note**
 URL expiration allows your application to retrieve the file without credentials, but still retain control over who can access your data, because you need an access key ID and signature to get the temporary URL. If you need to retrieve the file after the URL has expired, call `GetFileUploadURL` again to get a new URL.

 You can get a temporary file upload URL any time until the HIT is disposed. After the HIT is disposed, any uploaded files are deleted, and cannot be retrieved.

## Request Parameters
<a name="ApiReference_GetFileUploadURLOperation-request-parameters"></a>

 The `GetFileUploadURL` operation accepts parameters common to all operations. Some common parameters are required. See [Common Parameters](ApiReference_CommonParametersArticle.md) for more information.

 The following parameters are specific to the `GetFileUploadURL` operation:

| Name | Description | Required |
| --- | --- | --- |
|  `Operation`  | The name of the operation<br />Type: String<br />Valid Values: GetFileUploadURL<br />Default: None | Yes |
|  `AssignmentId`  |  The ID of the assignment that contains the question with a `FileUploadAnswer`. <br />Type: String<br />Default: None | Yes |
|  `QuestionIdentifier`  |  The identifier of the question with a `FileUploadAnswer`, as specified in the [QuestionForm](ApiReference_QuestionFormDataStructureArticle.md) of the HIT. <br />Type: String<br />Default: None | Yes |

## Response Elements
<a name="ApiReference_GetFileUploadURLOperation-response-elements"></a>

 A successful request for the `GetFileUploadURL` operation has a `GetFileUploadURLResult` element in the response.

 The `GetFileUploadURLResult` element includes the elements described in the following table.

| Name | Description |
| --- | --- |
|  `FileUploadURL`  |  A temporary URL for the file that the Worker uploaded for the answer. <br />Type: URL |

## Examples
<a name="ApiReference_GetFileUploadURLOperation-examples"></a>

The following example shows how to use the `GetFileUploadURL` operation.

### Sample Request
<a name="ApiReference_GetFileUploadURLOperation-examples-sample-request-"></a>

 The following example of a call to the `GetFileUploadURL` operation retrieves the temporary URL for a file-upload answer to the given question in the given assignment.

```
https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
&AWSAccessKeyId={{[the Requester's Access Key ID]}}
&Version=2017-01-17
&Operation=GetFileUploadURL
&Signature={{[signature for this request]}}
&Timestamp={{[your system's local time]}}
&AssignmentId=123RVWYBAZW00EXAMPLE456RVWYBAZW00EXAMPLE
&QuestionIdentifier=ReadAloudAudio
```

### Sample Response
<a name="ApiReference_GetFileUploadURLOperation-examples-sample-response"></a>

The following is an example response.

```
<GetFileUploadURLResult>
  <Request>
    <IsValid>True</IsValid>
  </Request>
  <FileUploadURL>http://s3.amazonaws.com/amzn-s3-demo-bucket1/puppy.jpg</FileUploadURL>
</GetFileUploadURLResult>
```
