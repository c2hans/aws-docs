---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_GetBlockedWorkersOperation.html
---

**Amazon Mechanical Turk will permanently close on September 30, 2026.** For Workers and Requesters currently using the service, visit our [Amazon Mechanical Turk help page](https://www.mturk.com/help) to learn how you can prepare for this closure.

|  |
| --- |
| ![WARNING](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# GetBlockedWorkers
<a name="ApiReference_GetBlockedWorkersOperation"></a>

## Description
<a name="ApiReference_GetBlockedWorkersOperation-description2"></a>

 The `GetBlockedWorkers` operation retrieves a list of Workers who are blocked from working on your HITs.

## Request Parameters
<a name="ApiReference_GetBlockedWorkersOperation-request-parameters2"></a>

 The `GetBlockedWorkers` operation accepts parameters that are common to all operations. Some common parameters are required. For more information, see [Common Parameters](ApiReference_CommonParametersArticle.md).

 The following parameters are specific to the `GetBlockedWorkers` operation:

| Name | Description | Required |
| --- | --- | --- |
|  `Operation`  | The name of the operation.<br />Type: String<br />Valid Values: GetBlockedWorkers<br />Default: None | Yes |
|  `PageNumber`  | The page of results to return. Once the assignments have been filtered, sorted, and divided into pages of size `PageSize`, the page corresponding to `PageSize` is returned as the results of the operation.<br />Type: Positive integer <br />Default: 1  | No |
|  `PageSize`  | The number of assignments to include in a page of results. The complete sorted result set is divided into pages of this many assignments.<br />Type: Positive integer<br />Valid Values: Any integer between 1 and 65535<br />Default: 10 <br />  | No |

## Response Elements
<a name="ApiReference_GetBlockedWorkersOperation-response-elements2"></a>

 A successful request for the `GetBlockedWorkers` operation has a `GetBlockedWorkersResult` element in the response.

The `GetBlockedWorkersResult` element contains the elements described in the following table:

| Name | Description |
| --- | --- |
|  `Request`  | This element is present only if the **Request** `ResponseGroup` is specified. |
|  `PageNumber`  | The number of the page in the filtered results list being returned.<br />Type: Positive integer |
|  `NumResults`  | The number of assignments on the page in the filtered results list, equivalent to the number of assignments returned by this call.<br />Type: Non-negative integer |
|  `TotalNumResults`  | The total number of HITs in the filtered results list based on this call.<br />Type: Positive integer |
|  `WorkerBlock`  | The workers who have been blocked, along with the reason for the block. The response includes one WorkerBlock element for each worker. <br />Type: A [WorkerBlock](ApiReference_WorkerBlockDataStructureArticle.md) data structure |

## Examples
<a name="ApiReference_GetBlockedWorkersOperation-examples2"></a>

The following example shows how to use the `GetBlockedWorkers` operation.

### Sample Request
<a name="ApiReference_GetBlockedWorkersOperation-examples2-sample-request"></a>

The following example blocks a Worker from working on your HITs.

```
https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
&AWSAccessKeyId={{[the Requester's Access Key ID]}}
&Version=2017-01-17
&Operation=GetBlockedWorkers
&Signature={{[signature for this request]}}
&Timestamp={{[your system's local time]}}
&PageNumber=1
&PageSize=10
```

### Sample Response
<a name="ApiReference_GetBlockedWorkersOperation-examples2-sample-response"></a>

The following is an example response.

```
<GetBlockedWorkersResult>
  <Request>
    <IsValid>True</IsValid>
  </Request>
  <PageNumber>1</PageNumber>
  <NumResults>2</NumResults>
  <TotalNumResults>2</TotalNumResults>
  <WorkerBlock>
    <WorkerId>A2QWESAMPLE1</WorkerId>
    <Reason>Poor quality work</Reason>
  </WorkerBlock>
  <WorkerBlock>
    <WorkerId>A2QWESAMPLE2</WorkerId>
    <Reason>Poor quality work</Reason>
  </WorkerBlock>
</GetBlockedWorkersResult>
```

### Related Operations
<a name="ApiReference_GetBlockedWorkersOperation-related-operations-"></a>

 To unblock a Worker, use the [UnblockWorker](ApiReference_UnblockWorkerOperation.md) operation.
