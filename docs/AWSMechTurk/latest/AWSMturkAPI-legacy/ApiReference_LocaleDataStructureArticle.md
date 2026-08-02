---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_LocaleDataStructureArticle.html
---

|  |
| --- |
| ![WARNING](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# Locale
<a name="ApiReference_LocaleDataStructureArticle"></a>

## Description
<a name="ApiReference_LocaleDataStructureArticle-description"></a>

 The Locale data structure represents a geographical region or location.

 The Locale data structure is used as part of the [ QualificationRequirement](ApiReference_QualificationRequirementDataStructureArticle.md) data structure when you specify a requirement based on the locale Qualification, and as part of the [Qualification](ApiReference_QualificationDataStructureArticle.md) data structure that describes the value of a locale Qualification.

 When used in a QualificationRequirement, the Locale data structure only needs to contain as much of the locale as the Worker needs to match to meet the requirement. For example, a requirement that the Worker be living anywhere in the United States would have only the `Country` field.

**Note**
 Currently, a Locale data structure only supports the `Country` field and `Subdivision` field. Please note that subdivisions or states are only available for the United States of America.

## Elements
<a name="ApiReference_LocaleDataStructureArticle-elements"></a>

 The Locale structure can contain the elements described in the following table. When the structure is used in a request, elements described as **Required** must be included for the request to succeed.

| Name | Description | Required |
| --- | --- | --- |
|  `Country`  | The country of the locale.<br /> Type: A valid [ ISO 3166 country code](http://www.iso.org/iso/country_codes/iso_3166_code_lists.htm). For example, the code **US** refers to the United States of America. <br />Default: none | Yes |
|  `Subdivision`  | The state or subdivision of the locale.<br /> Type: Type: A valid ISO 3166-2 subdivision code. For example, the code CA refers to the state of California <br />Default: none | Yes |

## Example
<a name="ApiReference_LocaleDataStructureArticle-example"></a>

 The following code sample indicates a locale in the United States.

```
<LocaleValue>
  <Country>US</Country>
</LocaleValue>
```

## Example
<a name="ApiReference_LocaleDataStructureArticle-example-subdivision"></a>

 The following code sample indicates a locale in the state of California in the United States of America.

```
<LocaleValue>
  <Country>US</Country>
  <Subdivision>CA</Subdivision>
</LocaleValue>
```
