---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_BlockWorkerOperation.html
---

**Amazon Mechanical Turk will permanently close on September 30, 2026.** For Workers and Requesters currently using the service, visit our [Amazon Mechanical Turk help page](https://www.mturk.com/help) to learn how you can prepare for this closure.

|  |
| --- |
| ![WARNING](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# BlockWorker
<a name="ApiReference_BlockWorkerOperation"></a>

## Description
<a name="ApiReference_BlockWorkerOperation-description"></a>

 The `BlockWorker` operation allows you to prevent a Worker from working on your HITs. For example, you can block a Worker who is producing poor quality work. You can block up to 100,000 Workers.

**Note**
`BlockWorker` prevents a Worker from accepting more of your HITs after you block them. However, `BlockWorker` does not prevent a Worker from submitting assignments that they accepted before you blocked them.

 You need the Worker ID to use this operation. You can get the Worker ID in the assignment data returned by a call to the [GetAssignmentsForHIT](ApiReference_GetAssignmentsForHITOperation.md) operation. If the Worker ID is missing or invalid, this operation returns with the failure message "WorkerId is invalid." If the Worker is already blocked, this operation returns successfully.

## Request Parameters
<a name="ApiReference_BlockWorkerOperation-request-parameters"></a>

 The `BlockWorker` operation accepts parameters common to all operations. Some common parameters are required. See [Common Parameters](ApiReference_CommonParametersArticle.md) for more information.

 The following parameters are specific to the `BlockWorker` operation:

| Name | Description | Required |
| --- | --- | --- |
|  `Operation`  | The name of the operation<br />Type: String<br />Valid Values: BlockWorker<br />Default: None | Yes |
|  `WorkerId`  |  The ID of the Worker to block. <br />Type: String<br />Default: None | Yes |
|  `Reason`  |  A message explaining the reason for blocking the Worker. This parameter enables you to keep track of your Workers. The Worker does not see this message. <br />Type: String<br />Default: None | Yes |

## Response Elements
<a name="ApiReference_BlockWorkerOperation-response-elements"></a>

 A successful request for the `BlockWorker` operation returns with no errors. The response includes the elements described in the following table. The operation returns no other data.

| Name | Description |
| --- | --- |
|  `BlockWorkerResult`  |  Contains a `Request` element if the **Request** `ResponseGroup` is specified.  |

## Examples
<a name="ApiReference_BlockWorkerOperation-examples"></a>

The following example shows how to use the `BlockWorker` operation.

### Sample Request
<a name="ApiReference_BlockWorkerOperation-examples-sample-request-"></a>

The following example blocks a Worker from working on your HITs.

```
1. https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
2. &AWSAccessKeyId={{[the Requester's Access Key ID]}}
3. &Version=2017-01-17
4. &Operation=BlockWorker
5. &Signature={{[signature for this request]}}
6. &Timestamp={{[your system's local time]}}
7. &WorkerId=AZ3456EXAMPLE
8. &Reason=After%20several%20warnings,%20he%20continued%20to%20submit%20answers%20without%20reading%20the%20instructions%20carefully.
```

### Sample Response
<a name="ApiReference_BlockWorkerOperation-examples-sample-response"></a>

The following is an example response.

```
<BlockWorkerResult>
  <Request>
    <IsValid>True</IsValid>
  </Request>
</BlockWorkerResult>
```

## Related Operations
<a name="ApiReference_BlockWorkerOperation-related-operations-"></a>

 To unblock a Worker use the [UnblockWorker](ApiReference_UnblockWorkerOperation.md) operation.
