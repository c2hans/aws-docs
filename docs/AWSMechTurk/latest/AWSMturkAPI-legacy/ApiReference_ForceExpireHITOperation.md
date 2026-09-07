---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_ForceExpireHITOperation.html
---

|  |
| --- |
| ![WARNING](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# ForceExpireHIT
<a name="ApiReference_ForceExpireHITOperation"></a>

## Description
<a name="ApiReference_ForceExpireHITOperation-description"></a>

 The `ForceExpireHIT` operation causes a HIT to expire immediately, as if the `LifetimeInSeconds` parameter of the HIT had elapsed.

 The effect is identical to the HIT expiring on its own; the HIT no longer appears on the Amazon Amazon Mechanical Turk web site, and no new Workers are allowed to accept the HIT. Workers who have accepted the HIT prior to expiration are allowed to complete it or return it, or allow the assignment duration to elapse (abandon the HIT). Once all remaining assignments have been submitted, the expired HIT becomes **Reviewable**, and will be returned by a call to the [GetReviewableHITs](ApiReference_GetReviewableHITsOperation.md) operation.

**Note**
 Unlike the [DisableHIT](ApiReference_DisableHITOperation.md) operation, the `ForceExpireHIT` operation does not have any effect on assignments. If assignments have been submitted for the HIT, your application still needs to approve or reject them before disposing of the HIT.

## Request Parameters
<a name="ApiReference_ForceExpireHITOperation-request-parameters"></a>

 The `ForceExpireHIT` operation accepts parameters common to all operations. Some common parameters are required. See [Common Parameters](ApiReference_CommonParametersArticle.md) for more information.

 The following parameters are specific to the `ForceExpireHIT` operation:

| Name | Description | Required |
| --- | --- | --- |
|  `Operation`  | The name of the operation<br />Type: String<br />Valid Values: ForceExpireHIT<br />Default: None | Yes |
|  `HITId`  | The ID of the HIT, as returned by the `CreateHIT` operation.<br />Type: String<br />Default: None | Yes |

## Response Elements
<a name="ApiReference_ForceExpireHITOperation-response-elements"></a>

 A successful request for the `ForceExpireHIT` operation returns with no errors. The response includes the elements described in the following table. The operation returns no other data.

| Name | Description |
| --- | --- |
|  `ForceExpireHITResult`  |  Contains a `Request` element if the **Request** `ResponseGroup` is specified.  |

## Examples
<a name="ApiReference_ForceExpireHITOperation-examples"></a>

The following example shows how to use the `ForceExpireHIT` operation.

### Sample Request
<a name="ApiReference_ForceExpireHITOperation-examples-sample-request"></a>

The following example causes the specified HIT to expire.

```
1. https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
2. &AWSAccessKeyId={{[the Requester's Access Key ID]}}
3. &Operation=ForceExpireHIT
4. &Signature={{[signature for this request]}}
5. &Timestamp={{[your system's local time]}}
6. &HITId=123RVWYBAZW00EXAMPLE
```

### Sample Response
<a name="ApiReference_ForceExpireHITOperation-examples-sample-response"></a>

The following is an example response.

```
<ForceExpireHITResult>
  <Request>
    <IsValid>True</IsValid>
  </Request>
</ForceExpireHITResult>
```
