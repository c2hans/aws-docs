---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_GetAccountBalanceOperation.html
---

|  |
| --- |
| ![WARNING](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# GetAccountBalance
<a name="ApiReference_GetAccountBalanceOperation"></a>

## Description
<a name="ApiReference_GetAccountBalanceOperation-description"></a>

 The `GetAccountBalance` operation retrieves the amount of money in your Amazon Mechanical Turk account.

## Request Parameters
<a name="ApiReference_GetAccountBalanceOperation-request-parameters"></a>

 The `GetAccountBalance` operation accepts parameters common to all operations. Some common parameters are required. See [Common Parameters](ApiReference_CommonParametersArticle.md) for more information.

 The following parameter is specific to the `GetAccountBalance` operation:

| Name | Description | Required |
| --- | --- | --- |
|  `Operation`  | The name of the operation<br />Type: String<br />Valid Values: GetAccountBalance<br />Default: None | Yes |

## Response Elements
<a name="ApiReference_GetAccountBalanceOperation-response-elements"></a>

 A successful request for the `GetAccountBalance` operation returns with a `GetAccountBalanceResult` element in the response.

 The `GetAccountBalanceResult` element contains the following elements:

| Name | Description |
| --- | --- |
| AvailableBalance |  The amount available to pay for assignments. This is your current balance minus any outstanding payments, fees or bonuses you owe. <br /> Type: [Price](ApiReference_PriceDataStructureArticle.md) data structure  |
| OnHoldBalance |  Not used. This value is always 0. <br /> Type: [Price](ApiReference_PriceDataStructureArticle.md) data structure  |

## Examples
<a name="ApiReference_GetAccountBalanceOperation-examples"></a>

The following example shows how to use the `GetAccountBalance` operation.

### Sample Request
<a name="ApiReference_GetAccountBalanceOperation-examples-sample-request"></a>

The following example retrieves the Requester's account balance.

```
1. https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
2. &AWSAccessKeyId={{[the Requester's Access Key ID]}}
3. &Version=2017-01-17
4. &Operation=GetAccountBalance
5. &Signature={{[signature for this request]}}
6. &Timestamp={{[your system's local time]}}
```

### Sample Response
<a name="ApiReference_GetAccountBalanceOperation-examples-sample-response"></a>

The following is an example response.

```
<GetAccountBalanceResult>
  <Request>
    <IsValid>True</IsValid>
  </Request>
  <AvailableBalance>
    <Amount>10000.000</Amount>
    <CurrencyCode>USD</CurrencyCode>
    <FormattedPrice>$10,000.00</FormattedPrice>
  </AvailableBalance>
</GetAccountBalanceResult>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
