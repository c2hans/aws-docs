---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_CreateQualificationTypeOperation.html
---

**Amazon Mechanical Turk will permanently close on September 30, 2026.** For Workers and Requesters currently using the service, visit our [Amazon Mechanical Turk help page](https://www.mturk.com/help) to learn how you can prepare for this closure.

|  |
| --- |
| ![WARNING](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# CreateQualificationType
<a name="ApiReference_CreateQualificationTypeOperation"></a>

## Description
<a name="ApiReference_CreateQualificationTypeOperation-description"></a>

The `CreateQualificationType` operation creates a new Qualification type, which is represented by a [QualificationType](ApiReference_QualificationTypeDataStructureArticle.md) data structure.

## Request Parameters
<a name="ApiReference_CreateQualificationTypeOperation-request-parameters"></a>

 `CreateQualificationType` accepts parameters common to all operations. Some common parameters are required. See [Common Parameters](ApiReference_CommonParametersArticle.md) for more information.

 The following parameters are specific to the `CreateQualificationType` operation:

| Name | Description | Required |
| --- | --- | --- |
|  `Operation`  | The name of the operation.<br />Type: String<br />Valid Values: CreateQualificationType<br />Default: None | Yes |
|  `Name`  |  The name you give to the Qualification type. The type name is used to represent the Qualification to Workers, and to find the type using a Qualification type search. <br />Type: String<br />Default: None<br />Constraints: Must be unique across all of your Qualification types. | Yes |
|  `Description`  |  A long description for the Qualification type. On the Amazon Mechanical Turk website, the long description is displayed when a Worker examines a Qualification type. <br />Type: String<br />Default: None<br />Constraints: Must be less than or equal to 2000 characters. | Yes |
|  `Keywords`  |  One or more words or phrases that describe the Qualification type, separated by commas. The keywords of a type make the type easier to find during a search. <br />Type: String<br />Default: None<br />Constraints: Must be less than or equal to 1000 characters, including commas and spaces. | No |
|  `RetryDelayInSeconds`  |  The number of seconds that a Worker must wait after requesting a Qualification of the Qualification type before the worker can retry the Qualification request.<br />Type: Non-negative integer<br /> Default: None. If not specified, retries are disabled and Workers can request a Qualification of this type only once, even if the Worker has not been granted the Qualification. <br />It is not possible to disable retries for a Qualification type after it has been created with retries enabled. If you want to disable retries, you must dispose of the existing retry-enabled Qualification type using [DisposeQualificationType](ApiReference_DisposeQualificationTypeOperation.md) and then create a new Qualification type with retries disabled.  | No |
|  `QualificationTypeStatus`  |  The initial status of the Qualification type. <br />Type: String<br />Valid Values: Active \| Inactive<br />Default: None | Yes |
|  `Test`  |  The questions for the Qualification test a Worker must answer correctly to obtain a Qualification of this type. <br /> If this parameter is specified, `TestDurationInSeconds` must also be specified. <br /> Type: String <br /> Default: None. If not specified, the Worker may request the Qualification without answering any questions. <br /> Constraints: Must not be longer than 65535 bytes. Must be a [QuestionForm](ApiReference_QuestionFormDataStructureArticle.md) data structure. This parameter cannot be specified if `AutoGranted` is `true`.  | No |
|  `AnswerKey`  |  The answers to the Qualification test specified in the `Test` parameter, in the form of an [AnswerKey](ApiReference_AnswerKeyDataStructureArticle.md) data structure. <br /> Type: String <br />Default: None. If not specified, you must process Qualification requests manually.<br /> Constraints: Must not be longer than 65535 bytes. | No |
|  `TestDurationInSeconds`  |  The number of seconds the Worker has to complete the Qualification test, starting from the time the Worker requests the Qualification. <br />Type: Integer<br />Valid Values: Positive integer<br />Default: None<br /> Conditions: Required if the `Test` parameter is specified.  | Conditional |
|  `AutoGranted`  |  Specifies whether requests for the Qualification type are granted immediately, without prompting the Worker with a Qualification test.<br />Type: Boolean<br />Valid Values: `true` \| `false`<br />Default: None<br /> Constraints: If the `Test` parameter is specified, this parameter cannot be `true`.  | No |
|  `AutoGrantedValue`  |  The Qualification value to use for automatically granted Qualifications. This parameter is used only if the `AutoGranted` parameter is `true`. <br />Type: Integer<br />Default: 1 | No |

## Response Elements
<a name="ApiReference_CreateQualificationTypeOperation-response-elements"></a>

 A successful request for the `CreateQualificationType` operation includes the elements found in the following table:

| Name | Description |
| --- | --- |
|  `QualificationType`  |  The created Qualification type. <br /> Type: A [QualificationType](ApiReference_QualificationTypeDataStructureArticle.md) data structure.  |

## Examples
<a name="ApiReference_CreateQualificationTypeOperation-examples"></a>

The following example shows how to use the `CreateQualificationType` operation.

### Sample Request
<a name="ApiReference_CreateQualificationTypeOperation-examples-sample-request"></a>

The following example creates a Qualification type.

```
1. https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
2. &AWSAccessKeyId={{[the Requester's Access Key ID]}}
3. &Version=2017-01-17
4. &Operation=CreateQualificationType
5. &Signature={{[signature for this request]}}
6. &Timestamp={{[your system's local time]}}
7. &Name=EnglishWritingAbility
8. &Description=The%20ability%20to%20write%20and%20edit%20text...
9. &QualificationTypeStatus=Active
```

### Sample Response
<a name="ApiReference_CreateQualificationTypeOperation-examples-sample-response"></a>

The following is an example response.

```
<CreateQualificationTypeResponse>
  <OperationRequest>
    <RequestId>5218189c-1d7e-49a3-abbf-672fb5e77c66</RequestId>
  </OperationRequest>
  <QualificationType>
    <Request>
      <IsValid>True</IsValid>
    </Request>
    <QualificationTypeId>ZSPJXD4F1SFZP7YNJWR0</QualificationTypeId>
    <CreationTime>2009-07-13T17:26:33Z</CreationTime>
    <Name>SampleQualificationTest</Name>
    <Description>Description of my qualification test.</Description>
    <QualificationTypeStatus>Active</QualificationTypeStatus>
    <AutoGranted>0</AutoGranted>
  </QualificationType>
</CreateQualificationTypeResponse>
```

## Related Operations
<a name="ApiReference_CreateQualificationTypeOperation-related-operations"></a>
+ [AssignQualification](ApiReference_AssignQualificationOperation.md)
+ [DisposeQualificationType](ApiReference_DisposeQualificationTypeOperation.md)
+ [GetQualificationType](ApiReference_GetQualificationTypeOperation.md)
+ [UpdateQualificationType](ApiReference_UpdateQualificationTypeOperation.md)
