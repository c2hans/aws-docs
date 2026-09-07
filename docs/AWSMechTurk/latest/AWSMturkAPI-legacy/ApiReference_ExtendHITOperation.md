---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_ExtendHITOperation.html
---

|  |
| --- |
| ![WARNING](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# ExtendHIT
<a name="ApiReference_ExtendHITOperation"></a>

## Description
<a name="ApiReference_ExtendHITOperation-description"></a>

 The `ExtendHIT` operation increases the maximum number of assignments, or extends the expiration date, of an existing HIT.

 To extend the maximum number of assignments, specify the number of additional assignments.

 To extend the expiration date, specify an amount of time as a number of seconds. If the HIT has not yet expired, the new expiration date is the existing date plus the amount of time specified. If the HIT has already expired, the new expiration date is the current time plus the amount of time specified.

 Only the Requester who created a HIT can extend it.

**Note**
HITs created with fewer than 10 assignments cannot be extended to have 10 or more assignments. Attempting to add assignments in a way that brings the total number of assignments for a HIT from fewer than 10 assignments to 10 or more assignments will result in an `AWS.MechanicalTurk.InvalidMaximumAssignmentsIncrease` exception.
HITs that were created before July 22, 2015 cannot be extended. Attempting to extend HITs that were created before July 22, 2015 will result in an `AWS.MechanicalTurk.HITTooOldForExtension` exception.

## Request Parameters
<a name="ApiReference_ExtendHITOperation-request-parameters"></a>

 The `ExtendHIT` operation accepts parameters common to all operations. Some common parameters are required. See [Common Parameters](ApiReference_CommonParametersArticle.md) for more information.

 The following parameters are specific to the `ExtendHIT` operation:

| Name | Description | Required |
| --- | --- | --- |
|  `Operation`  | The name of the operation<br />Type: String<br />Valid Values: ExtendHIT<br />Default: None | Yes |
|  `HITId`  | The ID of the HIT to extend<br />Type: String<br />Default: None | Yes |
|  `MaxAssignmentsIncrement`  |  The number of assignments by which to increment the `MaxAssignments` parameter of the HIT. <br />Type: positive integer<br />Valid Values: any integer between 1 and 1000000000 (one billion)<br />Default: None | No |
|  `ExpirationIncrementInSeconds`  |  The amount of time, in seconds, by which to extend the expiration date. If the HIT has not yet expired, this amount is added to the HIT's expiration date. If the HIT has expired, the new expiration date is the current time plus this value. <br />Type: positive integer<br />Valid Values: any integer between 3600 (1 hour) and 31536000 (365 days)<br />Default: None | No |
|  `UniqueRequestToken`  | A unique identifier for this request, which allows you to retry the call on error without extending the HIT multiple times. This is useful in cases such as network timeouts where it is unclear whether or not the call succeeded on the server. If the extend HIT already exists in the system from a previous call using the same `UniqueRequestToken`, subsequent calls will return an error with a message containing the request ID.<br />Type: String<br />Default: None<br />Constraints: must not be longer than 64 characters in length.<br />Note: It is your responsibility to ensure uniqueness of the token. The unique token expires after 24 hours. Subsequent calls using the same `UniqueRequestToken` made after the 24 hour limit could extend the HIT multiple times. | No |

## Response Elements
<a name="ApiReference_ExtendHITOperation-response-elements"></a>

 A successful request for the `ExtendHIT` operation returns with no errors. The response includes the elements described in the following table. The operation returns no other data.

| Name | Description |
| --- | --- |
|  `ExtendHITResult`  |  Contains a `Request` element if the **Request** `ResponseGroup` is specified.  |

## Examples
<a name="ApiReference_ExtendHITOperation-examples"></a>

The following example shows how to use the `ExtendHIT` operation.

### Sample Request
<a name="ApiReference_ExtendHITOperation-examples-sample-request"></a>

 The following example extends the expiration date of a HIT by 5 days (432,000 seconds).

```
1. https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
2. &AWSAccessKeyId={{[the Requester's Access Key ID]}}
3. &Version=2017-01-17
4. &Operation=ExtendHIT
5. &Signature={{[signature for this request]}}
6. &Timestamp={{[your system's local time]}}
7. &HITId=123RVWYBAZW00EXAMPLE
8. &ExpirationIncrementInSeconds=432000
```

### Sample Response
<a name="ApiReference_ExtendHITOperation-examples-sample-response"></a>

The following is an example response.

```
<ExtendHITResult>
  <Request>
    <IsValid>True</IsValid>
  </Request>
</ExtendHITResult>
```
