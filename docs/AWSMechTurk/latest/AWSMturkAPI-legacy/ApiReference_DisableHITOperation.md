---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_DisableHITOperation.html
---

**Amazon Mechanical Turk will permanently close on September 30, 2026.** For Workers and Requesters currently using the service, visit our [Amazon Mechanical Turk help page](https://www.mturk.com/help) to learn how you can prepare for this closure.

|  |
| --- |
| ![WARNING](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# DisableHIT
<a name="ApiReference_DisableHITOperation"></a>

## Description
<a name="ApiReference_DisableHITOperation-description"></a>

The `DisableHIT` operation removes a HIT from the Amazon Mechanical Turk marketplace, approves any submitted assignments pending approval or rejection, and disposes of the HIT and all assignment data. Assignment results data cannot be retrieved for a HIT that has been disposed.

Assignments in progress at the time of the call to the `DisableHIT` operation are approved once the assignments are submitted. You will be charged for approval of these assignments.

When either all of the HIT's assignments have been submitted by Workers, or the HIT has expired and all assignments have either been submitted, returned or abandoned, the HIT is considered **Reviewable**. For more information about the **Reviewable** state, see [Creating and Managing Assignments](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/Concepts_AssignmentsArticle.html).

The `DisableHIT` operation does not work on HITs in the **Reviewable** state. For HITs in the **Reviewable** state, call the [ApproveAssignment](ApiReference_ApproveAssignmentOperation.md) or the [RejectAssignment](ApiReference_RejectAssignmentOperation.md) operation for each submitted assignment for the HIT. Then call the [DisposeHIT](ApiReference_DisposeHITOperation.md) operation to dispose of the HIT.

Only the Requester who created the HIT can disable it.

## Request Parameters
<a name="ApiReference_DisableHITOperation-request-parameters"></a>

The `DisableHIT` operation accepts parameters common to all operations. Some common parameters are required. See [Common Parameters](ApiReference_CommonParametersArticle.md) for more information.

 The following parameters are specific to the `DisableHIT` operation:

| Name | Description | Required |
| --- | --- | --- |
|  `Operation`  | The name of the operation<br />Type: String<br />Valid Values: DisableHIT<br />Default: None | Yes |
|  `HITId`  |  The ID of the HIT, as returned by the [CreateHIT](ApiReference_CreateHITOperation.md) operation. <br />Type: String<br />Default: None | Yes |

## Response Elements
<a name="ApiReference_DisableHITOperation-response-elements"></a>

 A successful request for the `DisableHIT` operation returns with no errors. The response includes the elements in the following table. The operation returns no other data.

| Name | Description |
| --- | --- |
|  `DisableHITResult`  |  Contains a `Request` element if the **Request** `ResponseGroup` is specified.  |

## Examples
<a name="ApiReference_DisableHITOperation-examples"></a>

The following example shows how to use the `DisableHIT` operation.

### Sample Request
<a name="ApiReference_DisableHITOperation-examples-sample-request"></a>

 The following example disables a HIT with a specified HIT ID.

```
1. https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
2. &AWSAccessKeyId={{[the Requester's Access Key ID]}}
3. &Version=2017-01-17
4. &Operation=DisableHIT
5. &Signature={{[signature for this request]}}
6. &Timestamp={{[your system's local time]}}
7. &HITId=123RVWYBAZW00EXAMPLE
```

### Sample Response
<a name="ApiReference_DisableHITOperation-examples-sample-response"></a>

The following is an example response.

```
<DisableHITResult>
  <Request>
  <IsValid>True</IsValid>
  </Request>
</DisableHITResult>
```
