---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_ApproveRejectedAssignmentOperation.html
---

|  |
| --- |
| ![WARNING](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# ApproveRejectedAssignment
<a name="ApiReference_ApproveRejectedAssignmentOperation"></a>

## Description
<a name="ApiReference_ApproveRejectedAssignmentOperation-description"></a>

The `ApproveRejectedAssignment` operation approves an assignment that was previously rejected.

`ApproveRejectedAssignment` works only on rejected assignments that were submitted within the previous 30 days and only if the assignment's related HIT has not been disposed.

Approving the rejected assignment initiates two payments from the Requester's Amazon.com account: one payment to the Worker who submitted the results for the reward amount specified in the HIT and one payment for Amazon Mechanical Turk fees. For the operation to succeed, a Requester must have sufficient funds in their account to pay the Worker and the fees.

If the assignment is not currently rejected, or if the Requester does not have sufficient funds in their account to pay the Worker and the Mechanical Turk fees, then the `ApproveRejectedAssignment` operation returns an exception and the approval is not processed.

You can include an optional feedback message with the approval, which the Worker can see in the Status section of the Amazon Mechanical Turk website.

## Request Parameters
<a name="ApiReference_ApproveRejectedAssignmentOperation-request-parameters"></a>

 The `ApproveRejectedAssignment` operation accepts parameters common to all operations. Some common parameters are required. For more information, see [Common Parameters](ApiReference_CommonParametersArticle.md).

 The following parameters are specific to the `ApproveRejectedAssignment` operation:

| Name | Description | Required |
| --- | --- | --- |
|  `Operation`  | The name of the operation.<br />Type: String<br />Valid Values: ApproveRejectedAssignment<br />Default: None | Yes |
|  `AssignmentId`  | The ID of the assignment. This parameter must correspond to a HIT created by the Requester.<br />Type: String<br />Default: None.  | Yes |
|  `RequesterFeedback`  | A message for the Worker, which the Worker can see in the Status section of the Mechanical Turk website. <br />Type: String<br />Default: None. <br />Constraints: Can be up to 1024 characters (including multi-byte characters). <br />The `RequesterFeedback` parameter cannot contain ASCII characters 0-8, 11,12, or 14-31. If these characters are present, the operation throws an **InvalidParameterValue** error.  | No |

## Response Elements
<a name="ApiReference_ApproveRejectedAssignmentOperation-response-elements"></a>

 A successful request for the `ApproveRejectedAssignment` operation returns with no errors. The response includes the elements described in the following table. The operation returns no other data.

| Name | Description |
| --- | --- |
|  `ApproveRejectedAssignmentResult`  | Contains a Request element if the **Request** `ResponseGroup` is specified.<br /> |

## Examples
<a name="ApiReference_ApproveRejectedAssignmentOperation-examples"></a>

The following example shows how to use the `ApproveRejectedAssignment` operation.

### Sample Request
<a name="ApiReference_ApproveRejectedAssignmentOperation-examples-sample-request"></a>

The following example approves a previously rejected assignment identified by its assignment ID.

```
https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
&AWSAccessKeyId={{[the Requester's Access Key ID]}}
&Version=2017-01-17
&Operation=ApproveRejectedAssignment
&Signature={{[signature for this request]}}
&Timestamp={{[your system's local time]}}
&AssignmentId=123RVWYBAZW00EXAMPLE456RVWYBAZW00EXAMPLE
```

### Sample Response
<a name="ApiReference_ApproveRejectedAssignmentOperation-examples-sample-response"></a>

The following is an example response.

```
<ApproveRejectedAssignmentResult>
  <Request>
    <IsValid>True</IsValid>
  </Request>
</ApproveRejectedAssignmentResult>
```
