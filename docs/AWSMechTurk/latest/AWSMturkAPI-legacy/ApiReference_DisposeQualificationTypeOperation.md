---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_DisposeQualificationTypeOperation.html
---

**Amazon Mechanical Turk will permanently close on September 30, 2026.** For Workers and Requesters currently using the service, visit our [Amazon Mechanical Turk help page](https://www.mturk.com/help) to learn how you can prepare for this closure.

|  |
| --- |
| ![WARNING](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# DisposeQualificationType
<a name="ApiReference_DisposeQualificationTypeOperation"></a>

## Description
<a name="ApiReference_DisposeQualificationTypeOperation-description"></a>

 The `DisposeQualificationType` operation disposes a Qualification type and disposes any HIT types that are associated with the Qualification type. A Qualification type is represented by a [QualificationType](ApiReference_QualificationTypeDataStructureArticle.md) data structure.

 This operation does not revoke Qualifications already assigned to Workers because the Qualifications might be needed for active HITs. If there are any pending requests for the Qualification type, Amazon Mechanical Turk rejects those requests.

 After you dispose of a Qualification type, you can no longer use it to create HITs or HIT types.

**Note**
`DisposeQualificationType` must wait for all the HITs that use the disposed Qualification type to be disposed before completing. It may take up to 48 hours before `DisposeQualificationType` completes and the unique name of the disposed Qualification type is available for reuse with [CreateQualificationType](ApiReference_CreateQualificationTypeOperation.md).

## Request Parameters
<a name="ApiReference_DisposeQualificationTypeOperation-request-parameters"></a>

 A request to the Amazon Mechanical Turk Service includes parameters that control its behavior and the data it returns. Required parameters must be included for the request to succeed.

 `DisposeQualificationType` accepts parameters common to all operations. Some common parameters are required. See [Common Parameters](ApiReference_CommonParametersArticle.md) for more information.

 The following parameters are specific to the `DisposeQualificationType` operation:

| Name | Description | Required |
| --- | --- | --- |
|  Operation  | The operation you want to call. To access the `DisposeQualificationType` operation, set the `Operation` parameter to **DisposeQualificationType**.<br />Type: DisposeQualificationType<br />Default: None | Yes |
|  QualificationTypeId  | The ID of the [QualificationType](ApiReference_QualificationTypeDataStructureArticle.md) to dispose.<br />Type: String<br />Default: None<br />Constraint: A valid [QualificationType](ApiReference_QualificationTypeDataStructureArticle.md) ID. |  Yes  |

## Response Elements
<a name="ApiReference_DisposeQualificationTypeOperation-response-elements"></a>

A successful request for the `DisposeQualificationType` operation returns with no errors. The response includes the elements described in the following table. The operation returns no other data.

| Name | Description |
| --- | --- |
|  `DisposeQualificationTypeResult`  |  Contains a `Request` element if the **Request** `ResponseGroup` is specified.  |

## Examples
<a name="ApiReference_DisposeQualificationTypeOperation-examples"></a>

The following example shows how to use the `DisposeQualification` operation.

### Sample Request
<a name="ApiReference_DisposeQualificationTypeOperation-examples-sample-request-"></a>

The following example disposes a Qualification type and any HIT types that are associated with the Qualification type.

```
1. https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
2. &AWSAccessKeyId={{[the Requester's Access Key ID]}}
3. &Version=2017-01-17
4. &Operation=DisposeQualificationType
5. &Signature={{[signature for this request]}}
6. &Timestamp={{[your system's local time]}}
7. &QualificationTypeId=AZ34EXAMPLE
```

### Sample Response
<a name="ApiReference_DisposeQualificationTypeOperation-examples-sample-response"></a>

The following is an example response.

```
<DisposeQualificationTypeResult>
  <Request>
    <IsValid>True</IsValid>
  </Request>
</DisposeQualificationTypeResult>
```

## Related Operations
<a name="ApiReference_DisposeQualificationTypeOperation-related-operations"></a>
+ [AssignQualification](ApiReference_AssignQualificationOperation.md)
+ [CreateQualificationType](ApiReference_CreateQualificationTypeOperation.md)
+ [GetQualificationType](ApiReference_GetQualificationTypeOperation.md)
+ [UpdateQualificationType](ApiReference_UpdateQualificationTypeOperation.md)
