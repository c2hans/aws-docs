---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_UpdateQualificationTypeOperation.html
---

|  |
| --- |
| ![WARNING](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# UpdateQualificationType
<a name="ApiReference_UpdateQualificationTypeOperation"></a>

## Description
<a name="ApiReference_UpdateQualificationTypeOperation-description"></a>

 The `UpdateQualificationType` operation modifies the attributes of an existing Qualification type, which is represented by a [QualificationType](ApiReference_QualificationTypeDataStructureArticle.md) data structure. Only the owner of a Qualification type can modify its attributes.

 Most attributes of a Qualification type can be changed after the type has been created. However, the `Name` and `Keywords` fields cannot be modified. The `RetryDelayInSeconds` parameter can be modified or added to change the delay or to enable retries, but `RetryDelayInSeconds` cannot be used to disable retries.

Each Qualification type name must be unique across all of your Qualification types. If you want to reuse the name of an existing Qualification type, you must first dispose of the existing Qualification type using [DisposeQualificationType](ApiReference_DisposeQualificationTypeOperation.md) and then create a new Qualification type with the name of the disposed type using [CreateQualificationType](ApiReference_CreateQualificationTypeOperation.md).

 If you want to disable retries, you must dispose of the existing retry-enabled Qualification type using [DisposeQualificationType](ApiReference_DisposeQualificationTypeOperation.md) and then create a new Qualification type with retries disabled using [CreateQualificationType](ApiReference_CreateQualificationTypeOperation.md).

 You can use this operation to update the test for a Qualification type. The test is updated based on the values specified for the `Test`, `TestDurationInSeconds` and `AnswerKey` parameters. All three parameters specify the updated test. If you are updating the test for a type, you must specify the `Test` and `TestDurationInSeconds` parameters. The `AnswerKey` parameter is optional; omitting it specifies that the updated test does not have an answer key.

 If you omit the `Test` parameter, the test for the Qualification type is unchanged. There is no way to remove a test from a Qualification type that has one. If the type already has a test, you cannot update it to be `AutoGranted`. If the Qualification type does not have a test and one is provided by an update, the type will henceforth have a test.

If you want to update the test duration or answer key for an existing test without changing the questions, you must specify a `Test` parameter with the original questions, along with the updated values.

 If you provide an `AnswerKey` parameter, Amazon Mechanical Turk processes requests for the Qualification automatically, and assigns the Worker a Qualification with a value calculated from the `AnswerKey` and the answers submitted by the Worker.

 If you provide an updated `Test` but no `AnswerKey`, the new test will not have an answer key. Requests for such Qualifications must be granted manually.

 You can also update the `AutoGranted` and `AutoGrantedValue` attributes of the Qualification type.

**Note**
 A Qualification type cannot be configured with both the `Test` parameter specified and the `AutoGranted` parameter set to **true**. Currently, there is no way to remove a test from a Qualification type that has one. A Qualification type with a test cannot be re-configured to use the auto-granting feature.

## Request Parameters
<a name="ApiReference_UpdateQualificationTypeOperation-request-parameters"></a>

 The `UpdateQualificationType` operation accepts parameters common to all operations. Some common parameters are required. See [Common Parameters](ApiReference_CommonParametersArticle.md) for more information.

**Note**
If an optional request parameter is not specified, the `UpdateQualificationType` operation does not modify the corresponding field of the [QualificationType](ApiReference_QualificationTypeDataStructureArticle.md) being updated.

 The following parameters are specific to the `UpdateQualificationType` operation:

| Name | Description | Required |
| --- | --- | --- |
|  `Operation`  | The name of the operation.<br />Type: String<br />Valid Values: UpdateQualificationType<br />Default: None | Yes |
|  `QualificationTypeId`  | The ID of the Qualification type to update.<br />Type: String<br />Default: None | Yes |
|  `RetryDelayInSeconds`  |  The amount of time, in seconds, that Workers must wait after requesting a Qualification of the specified Qualification type before they can retry the Qualification request. <br />It is not possible to disable retries for a Qualification type after it has been created with retries enabled. If you want to disable retries, you must dispose of the existing retry-enabled Qualification type using [DisposeQualificationType](ApiReference_DisposeQualificationTypeOperation.md) and then create a new Qualification type with retries disabled using [CreateQualificationType](ApiReference_CreateQualificationTypeOperation.md). <br />Type: Non-negative integer<br />Default: None. If not specified, the `RetryDelayInSeconds` value of the specified Qualification type will not be changed. | No |
|  `QualificationTypeStatus`  | The new status of the Qualification type.<br />Type: String<br />Valid Values: Active \| Inactive<br />Default: None | No |
|  `Description`  | The new description of the Qualification type.<br />Type: String<br />Default: None | No |
|  `Test`  |  The questions for a Qualification test a Worker must answer correctly to obtain a Qualification of this type. <br /> Type: A [QuestionForm](ApiReference_QuestionFormDataStructureArticle.md) data structure. <br /> Default: None <br /> Constraints: Must not be longer than 65535 bytes. Cannot be specified if `AutoGranted` is **true**. If you update the `AnswerKey`, you must provide the `Test` parameter, even if the test has not changed. If you update the `TestDurationInSeconds`, you must provide the `Test` parameter, even if the test has not changed.  | No |
|  `AnswerKey`  |  The answers to the Qualification test specified in the `Test` parameter. <br />Type: An [AnswerKey](ApiReference_AnswerKeyDataStructureArticle.md) data structure.<br />Default: None<br />Constraints: Must not be longer than 65535 bytes.  | No |
|  `TestDurationInSeconds`  |  The amount of time, in seconds, that a Worker has to complete the Qualification test, starting from when the Worker requested the Qualification. <br />Type: Positive integer<br />Default: None<br />Conditions: Required if the `Test` parameter is specified. | Conditional |
|  `AutoGranted`  |  Specifies whether requests for the Qualification type will be granted immediately, without prompting the Worker with a Qualification test. <br />Type: Boolean<br />Valid Values: true \| false<br />Default: None<br />Conditions: Cannot be **true** if `Test` is specified. | Conditional |
| AutoGrantedValue |  The Qualification value to use if `AutoGranted` is **true**. <br />Type: Integer<br />Default: 1 | No |

## Response Elements
<a name="ApiReference_UpdateQualificationTypeOperation-response-elements"></a>

 A successful request for the `UpdateQualificationType` operation has a `QualificationType` element in the response, as described in the following table:

| Name | Description |
| --- | --- |
|  `QualificationType`  |  Contains a [QualificationType](ApiReference_QualificationTypeDataStructureArticle.md) data structure. <br /> Type: A [QualificationType](ApiReference_QualificationTypeDataStructureArticle.md) data structure.  |

## Examples
<a name="ApiReference_UpdateQualificationTypeOperation-examples"></a>

The following example shows how to use the `UpdateQualificationType` operation.

### Sample Request
<a name="ApiReference_UpdateQualificationTypeOperation-examples-sample-request"></a>

 The following example changes the `QualificationTypeStatus` of a Qualification type.

```
https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
&AWSAccessKeyId={{[the Requester's Access Key ID]}}
&Version=2017-01-17
&Operation=UpdateQualificationType
&Signature={{[signature for this request]}}
&Timestamp={{[your system's local time]}}
&QualificationTypeId=789RVWYBAZW00EXAMPLE
&QualificationTypeStatus=Inactive
```

### Sample Response
<a name="ApiReference_UpdateQualificationTypeOperation-examples-sample-response"></a>

The following is an example response.

```
<UpdateQualificationTypeResult>
  <Request>
    <IsValid>True</IsValid>
  </Request>
  <QualificationType>
    <QualificationTypeId>789RVWYBAZW00EXAMPLE</QualificationTypeId>
    <CreationTime>2009-06-15T12:00:01Z</CreationTime>
    <Name>EnglishWritingAbility</Name>
    <Description>The ability to write and edit text...</Description>
    <Keywords>English, text, write, edit, language</Keywords>
    <QualificationTypeStatus>Active</QualificationTypeStatus>
    <RetryDelayInSeconds>86400</RetryDelayInSeconds>
    <IsRequestable>true</IsRequestable>
  </QualificationType>
</UpdateQualificationTypeResult>
```

## Related Operations
<a name="ApiReference_UpdateQualificationTypeOperation-related-operations"></a>
+ [AssignQualification](ApiReference_AssignQualificationOperation.md)
+ [CreateQualificationType](ApiReference_CreateQualificationTypeOperation.md)
+ [DisposeQualificationType](ApiReference_DisposeQualificationTypeOperation.md)
+ [GetQualificationType](ApiReference_GetQualificationTypeOperation.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
