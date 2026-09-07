---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_PriceDataStructureArticle.html
---

|  |
| --- |
| ![WARNING](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# Price
<a name="ApiReference_PriceDataStructureArticle"></a>

## Description
<a name="ApiReference_PriceDataStructureArticle-description"></a>

 The Price data structure represents an amount of money in a given currency.

 The Price data structure is used in the [HIT data structure](ApiReference_HITDataStructureArticle.md).

 The Price data structure is used as a parameter for the following operations:
+  `CreateHIT`

 When you call the [CreateHIT](ApiReference_CreateHITOperation.md) operation, you must specify the `Amount` and `CurrencyCode` elements. The `FormattedPrice` element is only used in responses sent by the service.

## Elements
<a name="ApiReference_PriceDataStructureArticle-elements"></a>

 The Price structure can contain the elements described in the following table:

| Name | Description | Required |
| --- | --- | --- |
|  `Amount`  |  The amount of money, as a number. The amount is in the currency specified by the `CurrencyCode`. For example, if `CurrencyCode` is **USD**, the amount will be in United States dollars (e.g. **12.75** is $12.75 US). <br />Type: Number<br />Default: None | No |
|  `CurrencyCode`  |  A code that represents the country and units of the currency. Its value is <br /> Type an [ISO 4217](http://en.wikipedia.org/wiki/ISO_4217) currency code, such as **USD** for United States dollars. <br />Default: None<br />Constraints: Currently, only **USD** is supported. | No |
|  `FormattedPrice`  |  A textual representation of the price, using symbols and formatting appropriate for the currency. Symbols are represented using the Unicode character set. You do not need to specify `FormattedPrice` in a request. It is only provided by the service in responses, as a convenience to your application. <br />Type: String<br />Default: None | No |

## Example
<a name="ApiReference_PriceDataStructureArticle-example"></a>

 The following example shows how you can pass a Price data structure in a call to the [CreateHIT](ApiReference_CreateHITOperation.md) operation. The [CreateHIT](ApiReference_CreateHITOperation.md) operation accepts parameters that describe the HIT being created, including the reward the Worker will be paid for completing the HIT successfully. For [CreateHIT](ApiReference_CreateHITOperation.md), the parameter name is **Reward**, and the value is a Price data structure.

 In a SOAP request, the Price data structure is specified as the `Reward` parameter in XML:

```
<Reward>
  <Amount>0.32</Amount>
  <CurrencyCode>USD</CurrencyCode>
</Reward>
```

 In a REST request, the components of the Price data structure are specified as separate parameters:

```
https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
{{[...]}}
&Reward.1.Amount=0.32
&Reward.1.CurrencyCode=USD
```
