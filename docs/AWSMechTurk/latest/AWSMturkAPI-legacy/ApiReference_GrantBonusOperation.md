---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_GrantBonusOperation.html
---

|  |
| --- |
| ![WARNING](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# GrantBonus
<a name="ApiReference_GrantBonusOperation"></a>

## Description
<a name="ApiReference_GrantBonusOperation-description"></a>

 The `GrantBonus` operation issues a payment of money from your account to a Worker. This payment happens separately from the reward you pay to the Worker when you approve the Worker's assignment.

 The `GrantBonus` operation requires the Worker's ID and the assignment ID as parameters to initiate payment of the bonus.

 You must include a message that explains the reason for the bonus payment, as the Worker may not be expecting the payment.

 Amazon Mechanical Turk collects a fee for bonus payments, similar to the HIT listing fee. This operation fails if your account does not have enough funds to pay for both the bonus and the fees.

 For information about Amazon Mechanical Turk pricing and fee amounts, see [Amazon Mechanical Turk Pricing](https://requester.mturk.com/pricing).

## Request Parameters
<a name="ApiReference_GrantBonusOperation-request-parameters"></a>

 The `GrantBonus` operation accepts parameters common to all operations. Some common parameters are required. See [Common Parameters](ApiReference_CommonParametersArticle.md) for more information.

 The following parameters are specific to the `GrantBonus` operation:

| Name | Description | Required |
| --- | --- | --- |
|  `Operation`  | The name of the operation<br />Type: String<br />Valid Values: GrantBonus<br />Default: None | Yes |
|  `WorkerId`  |  The ID of the Worker being paid the bonus, as returned in the assignment data of the [GetAssignmentsForHIT](ApiReference_GetAssignmentsForHITOperation.md) operation. <br />Type: String<br />Default: None | Yes |
|  `AssignmentId`  |  The ID of the assignment for which this bonus is paid, as returned in the assignment data of the [GetAssignmentsForHIT](ApiReference_GetAssignmentsForHITOperation.md) operation. <br />Type: String<br />Default: None | Yes |
|  `BonusAmount`  |  The bonus amount to pay. <br /> Type: [Price](ApiReference_PriceDataStructureArticle.md) data structure <br />Default: None | Yes |
|  `Reason`  |  A message that explains the reason for the bonus payment. The Worker receiving the bonus can see this message. <br />Type: String<br />Default: None | Yes |
|  `UniqueRequestToken`  | A unique identifier for this request, which allows you to retry the call on error without granting multiple bonuses. This is useful in cases such as network timeouts where it is unclear whether or not the call succeeded on the server. If the bonus already exists in the system from a previous call using the same `UniqueRequestToken`, subsequent calls will return an error with a message containing the request ID.<br />Type: String<br />Default: None<br />Constraints: must not be longer than 64 characters in length.<br />Note: It is your responsibility to ensure uniqueness of the token. The unique token expires after 24 hours. Subsequent calls using the same `UniqueRequestToken` made after the 24 hour limit could grant multiple bonuses. | No |

## Response Elements
<a name="ApiReference_GrantBonusOperation-response-elements"></a>

 A successful request for the `GrantBonus` operation returns with no errors. The response includes the elements described in the following table. The operation returns no other data.

| Name | Description |
| --- | --- |
|  `GrantBonusResult`  |  Contains a `Request` element if the **Request** `ResponseGroup` is specified.  |

## Examples
<a name="ApiReference_GrantBonusOperation-examples"></a>

The following example shows how to use the `GrantBonus` operation.

### Sample Request
<a name="ApiReference_GrantBonusOperation-examples-sample-request"></a>

 The following example of a call to the `GrantBonus` operation pays a bonus of $5 to a Worker.

```
https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
&AWSAccessKeyId={{[the Requester's Access Key ID]}}
&Version=2017-01-17
&Operation=GrantBonus
&Signature={{[signature for this request]}}
&Timestamp={{[your system's local time]}}
&WorkerId=AZ3456EXAMPLE
&AssignmentId=123RVWYBAZW00EXAMPLE456RVWYBAZW00EXAMPLE
&BonusAmount.1.Amount=5
&BonusAmount.1.CurrencyCode=USD
&Reason=Thanks%20for%20doing%20great%20work!
```

### Sample Response
<a name="ApiReference_GrantBonusOperation-examples-sample-response"></a>

The following is an example response.

```
<GrantBonusResult>
  <Request>
    <IsValid>True</IsValid>
  </Request>
</GrantBonusResult>
```
