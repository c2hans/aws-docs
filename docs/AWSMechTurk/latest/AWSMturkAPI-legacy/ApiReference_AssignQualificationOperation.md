---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_AssignQualificationOperation.html
---

|  |
| --- |
| ![WARNING](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# AssignQualification
<a name="ApiReference_AssignQualificationOperation"></a>

## Description
<a name="ApiReference_AssignQualificationOperation-description"></a>

 The `AssignQualification` operation gives a Worker a Qualification. `AssignQualification` does not require that the Worker submit a Qualification request. It gives the Qualification directly to the Worker.

 You can only assign a Qualification of a Qualification type that you created (using the [CreateQualificationType](ApiReference_CreateQualificationTypeOperation.md) operation).

**Tip**
 `AssignQualification` does not affect any pending Qualification requests for the Qualification by the Worker. If you assign a Qualification to a Worker, then later grant a Qualification request made by the Worker, the granting of the request may modify the Qualification score. To resolve a pending Qualification request without affecting the Qualification the Worker already has, reject the request with the [ RejectQualificationRequest](ApiReference_RejectQualificationRequestOperation.md) operation.

## Request Parameters
<a name="ApiReference_AssignQualificationOperation-request-parameters"></a>

 The `AssignQualification` operation accepts parameters common to all operations. Some common parameters are required. See [CommonParameters](ApiReference_CommonParametersArticle.md) for more information.

 The following parameters are specific to the `AssignQualification` operation:

| Name | Description | Required |
| --- | --- | --- |
|  `Operation`  | The name of the operation<br />Type: String<br />Valid Values: AssignQualifcation<br />Default: None | Yes |
|  `QualificationTypeId`  | The ID of the Qualification type to use for the assigned Qualification.<br />Type: String<br />Default: None<br /> Constraints: must be a valid Qualification type ID, as returned by the [ CreateQualificationType](ApiReference_CreateQualificationTypeOperation.md) operation.  | Yes |
|  `WorkerId`  |  The ID of the Worker to whom the Qualification is being assigned. Worker IDs are included with submitted HIT assignments and Qualification requests. <br />Type: String<br />Default: None | Yes |
|  `IntegerValue`  | The value of the Qualification to assign.<br />Type: Integer<br />Default: 1 | No |
|  `SendNotification`  |  Specifies whether to send a notification email message to the Worker saying that the qualification was assigned to the Worker. <br />Type: Boolean<br /> Valid Values: `true` \| `false`. <br />Default: `true` | No |

## Response Elements
<a name="ApiReference_AssignQualificationOperation-response-elements"></a>

 A successful request for the AssignQualification operation returns with no errors. The response includes the elements described in the following table. The operation returns no other data.

| Name | Description |
| --- | --- |
|  `AssignQualificationResult`  |  Contains a `Request` element if the **Request** `ResponseGroup` is specified.  |

## Examples
<a name="ApiReference_AssignQualificationOperation-examples"></a>

The following example shows how to use the `AssignQualification` operation.

### Sample Request
<a name="ApiReference_AssignQualificationOperation-examples-sample-request"></a>

 The following example assigns a Qualification of a specified type to a Worker with the specified ID, using the specified Qualification value. By default, Amazon Mechanical Turk sends the Worker an e-mail message saying that the Worker has received the Qualification.

```
1. https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
2. &AWSAccessKeyId={{[the Requester's Access Key ID]}}
3. &Version=2017-01-17
4. &Operation=AssignQualification
5. &Signature={{[signature for this request]}}
6. &Timestamp={{[your system's local time]}}
7. &QualificationTypeId=789RVWYBAZW00EXAMPLE
8. &WorkerId=AZ3456EXAMPLE
9. &IntegerValue=800
```

### Sample Response
<a name="ApiReference_AssignQualificationOperation-examples-sample-response"></a>

The following is an example response.

```
<AssignQualificationResult>
  <Request>
    <IsValid>True</IsValid>
  </Request>
</AssignQualificationResult>
```
