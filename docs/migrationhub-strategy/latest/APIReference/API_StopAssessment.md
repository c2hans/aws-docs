---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_StopAssessment.html
---

# StopAssessment
<a name="API_StopAssessment"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

 Stops the assessment of an on-premises environment.

## Request Syntax
<a name="API_StopAssessment_RequestSyntax"></a>

```
POST /stop-assessment HTTP/1.1
Content-type: application/json

{
   "assessmentId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_StopAssessment_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StopAssessment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [assessmentId](#API_StopAssessment_RequestSyntax) **   <a name="migrationhubstrategy-StopAssessment-request-assessmentId"></a>
 The `assessmentId` returned by [StartAssessment](API_StartAssessment.md).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 52.
Pattern: `.*[0-9a-z-:]+.*`
Required: Yes

## Response Syntax
<a name="API_StopAssessment_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_StopAssessment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_StopAssessment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 The user does not have permission to perform the action. Check the AWS Identity and Access Management (IAM) policy associated with this user.
HTTP Status Code: 403

 ** InternalServerException **
 The server experienced an internal error. Try again.
HTTP Status Code: 500

 ** ThrottlingException **
 The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
 The request body isn't valid.
HTTP Status Code: 400

## See Also
<a name="API_StopAssessment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhubstrategy-2020-02-19/StopAssessment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhubstrategy-2020-02-19/StopAssessment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/StopAssessment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhubstrategy-2020-02-19/StopAssessment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/StopAssessment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhubstrategy-2020-02-19/StopAssessment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhubstrategy-2020-02-19/StopAssessment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhubstrategy-2020-02-19/StopAssessment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/migrationhubstrategy-2020-02-19/StopAssessment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/StopAssessment)
