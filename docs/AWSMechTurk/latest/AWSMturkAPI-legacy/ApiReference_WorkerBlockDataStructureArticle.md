---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_WorkerBlockDataStructureArticle.html
---

|  |
| --- |
| ![WARNING](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# WorkerBlock
<a name="ApiReference_WorkerBlockDataStructureArticle"></a>

## Description
<a name="ApiReference_WorkerBlockDataStructureArticle-description"></a>

The `WorkerBlock` data structure represents a Worker who has been blocked. It has two elements: the `WorkerId` and the `Reason` for the block.

The `WorkerBlock` data structure is used in the results of the following operation:
+  [GetBlockedWorkers](ApiReference_GetBlockedWorkersOperation.md)

## Elements
<a name="ApiReference_WorkerBlockDataStructureArticle-elements"></a>

 The WorkerBlock structure contains the elements described in the following table.

| Name | Description |
| --- | --- |
|  `WorkerId`  | The ID of the Worker who accepted the HIT.<br /> Type: String <br />Default: None |
|  `Reason`  | A message explaining the reason the Worker was blocked.<br /> Type: String <br />Default: None |

## Example
<a name="ApiReference_WorkerBlockDataStructureArticle-example"></a>

 The following example shows a sample `WorkerBlock` data structure in a response from the [GetBlockedWorkers](ApiReference_GetBlockedWorkersOperation.md) operation.

In a SOAP request, the `WorkerBlock` data structure is specified as the WorkerBlock parameter in XML:

```
<WorkerBlock>
  <WorkerId>AZ3456EXAMPLE</WorkerId>
  <Reason>After several  warnings, he continued to submit answers without reading the instructions carefully.</Reason>
</WorkerBlock>
```

In a REST request, the components of the `WorkerBlock` data structure are specified as separate parameters:

```
https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
[...]
&WorkerBlock.1.WorkerId=AZ3456EXAMPLE
&WorkerBlock.1.Reason=After%20several%20warnings,%20he%20continued%20to%20submit%20answers%20without%20reading%20the%20instructions%20carefully
```
