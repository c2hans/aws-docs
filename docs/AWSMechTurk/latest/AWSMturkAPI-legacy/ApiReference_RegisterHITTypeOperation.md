---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_RegisterHITTypeOperation.html
---

|  |
| --- |
| ![WARNING](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# RegisterHITType
<a name="ApiReference_RegisterHITTypeOperation"></a>

## Description
<a name="ApiReference_RegisterHITTypeOperation-description"></a>

 The `RegisterHITType` operation creates a new HIT type.

 The `RegisterHITType` operation lets you be explicit about which HITs ought to be the same type. It also gives you error checking, to ensure that you call the [CreateHIT](ApiReference_CreateHITOperation.md) operation with a valid HIT type ID.

 If you register a HIT type with values that match an existing HIT type, the HIT type ID of the existing type will be returned.

## Request Parameters
<a name="ApiReference_RegisterHITTypeOperation-request-parameters"></a>

 The `RegisterHITType` operation accepts parameters common to all operations. Some common parameters are required. See [Common Parameters](ApiReference_CommonParametersArticle.md) for more information.

 The following parameters are specific to the `RegisterHITType` operation:

| Name | Description | Required |
| --- | --- | --- |
|  `Operation`  | The name of the operation<br />Type: String<br />Valid Values: RegisterHITType<br />Default: None | Yes |
|  `Title`  | The title for HITs of this type.<br /> A `Title` parameter should be short and descriptive about the kind of task the HIT contains. On the Amazon Mechanical Turk web site, the HIT title appears in search results, and everywhere the HIT is mentioned. <br />Type: String<br />Default: None<br />Constraints: can be up to 128 characters in length | Yes |
|  `Description`  | A general description of HITs of this type<br /> A `Description` includes detailed information about the kind of task the HIT contains. On the Amazon Mechanical Turk web site, the HIT description appears in the expanded view of search results, and in the HIT and assignment screens. A good description gives the user enough information to evaluate the HIT before accepting it. It should not include instructions for completing the HIT. <br />Type: String<br />Default: None<br />Constraints: must be less than 2,000 characters in length | Yes |
|  `Reward`  |  The amount of money the Requester will pay a user for successfully completing a HIT of this type. <br />Type: a [Price](ApiReference_PriceDataStructureArticle.md) data structure<br />Default: None | Yes |
|  `AssignmentDurationInSeconds`  |  The amount of time a Worker has to complete a HIT of this type after accepting it. <br />Type: positive integer<br />Default: None<br />Constraints: any integer between 30 (30 seconds) and 3153600 (365 days) | Yes |
|  `Keywords`  |  One or more words or phrases that describe a HIT of this type, separated by commas. Searches for words similar to the keywords are more likely to return the HIT in the search results. <br />Type: String<br />Default: None<br /> Constraints: The complete string, including commas and spaces, must be fewer than 1,000 characters.  | No |
|  `AutoApprovalDelayInSeconds`  |  An amount of time, in seconds, after an assignment for a HIT of this type has been submitted, that the assignment becomes **Approved** automatically, unless the Requester explicitly rejects it. <br />Type: positive integer<br />Default: 2592000 (30 days)<br />Constraints: must be between 0 (immediate) and 2592000 (30 days). | No |
|  `QualificationRequirement`  |  A condition that a Worker's Qualifications must meet before the Worker is allowed to accept and complete a HIT of this type. <br /> Type: a [ QualificationRequirement](ApiReference_QualificationRequirementDataStructureArticle.md) data structure. <br />Default: None<br /> Constraints: there can be no more than 10 `QualificationRequirement` data structures for each HIT.  | No |

## Response Elements
<a name="ApiReference_RegisterHITTypeOperation-response-elements"></a>

 A successful request for the `RegisterHITType` operation has a `RegisterHITTypeResult` element in the response.

 The `RegisterHITTypeResult` element contains the following elements:

| Name | Description |
| --- | --- |
|  `HITTypeId`  | The ID of the newly registered HIT type<br />Type: String<br />Default: None |

## Examples
<a name="ApiReference_RegisterHITTypeOperation-examples"></a>

The following example shows how to use the `GetHITsForQualificationType` operation.

### Sample Request
<a name="ApiReference_RegisterHITTypeOperation-examples-sample-request"></a>

 The following example registers a new HIT type.

```
https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
&AWSAccessKeyId={{[the Requester's Access Key ID]}}
&Version=2017-01-17
&Operation=RegisterHITType
&Signature={{[signature for this request]}}
&Timestamp={{[your system's local time]}}
&Title=Location%20and%20Photograph%20Identification
&Description=Select%20the%20image%20that%20best%20represents...
&Reward.1.Amount=5
&Reward.1.CurrencyCode=USD
&AssignmentDurationInSeconds=30
&Keywords=location,%20photograph,%20image,%20identification,%20opinion
```

### Sample Response
<a name="ApiReference_RegisterHITTypeOperation-examples-sample-response"></a>

The following is an example response.

```
<RegisterHITTypeResult>
  <Request>
    <IsValid>True</IsValid>
  </Request>
  <HITTypeId>KZ3GKTRXBWGYX8WXBW60</HITTypeId>
</RegisterHITTypeResult>
```
