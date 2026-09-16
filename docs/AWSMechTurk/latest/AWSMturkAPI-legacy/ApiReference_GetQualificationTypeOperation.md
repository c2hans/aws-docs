---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_GetQualificationTypeOperation.html
---

**Amazon Mechanical Turk will permanently close on September 30, 2026.** For Workers and Requesters currently using the service, visit our [Amazon Mechanical Turk help page](https://www.mturk.com/help) to learn how you can prepare for this closure.

|  |
| --- |
| ![WARNING](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# GetQualificationType
<a name="ApiReference_GetQualificationTypeOperation"></a>

## Description
<a name="ApiReference_GetQualificationTypeOperation-description"></a>

 The `GetQualificationType` operation retrieves information about a Qualification type using its ID.

## Request Parameters
<a name="ApiReference_GetQualificationTypeOperation-request-parameters"></a>

 The `GetQualificationType` operation accepts parameters common to all operations. Some common parameters are required. See [Common Parameters](ApiReference_CommonParametersArticle.md) for more information.

 The following parameters are specific to the `GetQualificationType` operation:

| Name | Description | Required |
| --- | --- | --- |
|  `Operation`  | The name of the operation.<br />Type: String<br />Valid Values: GetQualificationType<br />Default: None | Yes |
|  `QualificationTypeId`  |  The ID of the Qualification type, as returned by the [CreateQualificationType](ApiReference_CreateQualificationTypeOperation.md) operation. <br />Type: String<br />Default: None | Yes |

## Response Elements
<a name="ApiReference_GetQualificationTypeOperation-response-elements"></a>

 A successful request for the `GetQualificationType` operation returns the elements described in the following table:

| Name | Description |
| --- | --- |
|  `QualificationType`  |  For information about the data structure of a Qualification type, see [ QualificationType](ApiReference_QualificationTypeDataStructureArticle.md) data structure.  |

## Examples
<a name="ApiReference_GetQualificationTypeOperation-examples"></a>

The following example shows how to use the `GetQualificationType` operation.

### Sample Request
<a name="ApiReference_GetQualificationTypeOperation-examples-sample-request"></a>

 The following example gets a Qualification type by its ID.

```
https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
&AWSAccessKeyId={{[the Requester's Access Key ID]}}
&Version=2017-01-17
&Operation=GetQualificationType
&Signature={{[signature for this request]}}
&Timestamp={{[your system's local time]}}
&QualificationTypeId=789RVWYBAZW00EXAMPLE
```

### Sample Response
<a name="ApiReference_GetQualificationTypeOperation-examples-sample-response"></a>

The following is an example response.

```
<GetQualificationTypeResult>
  <QualificationType>
    <QualificationTypeId>789RVWYBAZW00EXAMPLE</QualificationTypeId>
    <CreationTime>2005-01-31T23:59:59Z</CreationTime>
    <Name>EnglishWritingAbility</Name>
    <Description>The ability to write and edit text...</Description>
    <Keywords>English, text, write, edit, language</Keywords>
    <QualificationTypeStatus>Active</QualificationTypeStatus>
    <RetryDelayInSeconds>86400</RetryDelayInSeconds>
    <IsRequestable>true</IsRequestable>
  </QualificationType>
</GetQualificationTypeResult>
```
