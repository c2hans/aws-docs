---
source_url: https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetAssessment.html
---

# GetAssessment
<a name="API_GetAssessment"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

 Retrieves the status of an on-going assessment.

## Request Syntax
<a name="API_GetAssessment_RequestSyntax"></a>

```
GET /get-assessment/{{id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAssessment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_GetAssessment_RequestSyntax) **   <a name="migrationhubstrategy-GetAssessment-request-uri-id"></a>
 The `assessmentid` returned by [StartAssessment](API_StartAssessment.md).
Length Constraints: Minimum length of 0. Maximum length of 52.
Pattern: `.*[0-9a-z-:]+.*`
Required: Yes

## Request Body
<a name="API_GetAssessment_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAssessment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "assessmentTargets": [
      {
         "condition": "string",
         "name": "string",
         "values": [ "string" ]
      }
   ],
   "dataCollectionDetails": {
      "completionTime": number,
      "failed": number,
      "inProgress": number,
      "servers": number,
      "startTime": number,
      "status": "string",
      "statusMessage": "string",
      "success": number
   },
   "id": "string"
}
```

## Response Elements
<a name="API_GetAssessment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assessmentTargets](#API_GetAssessment_ResponseSyntax) **   <a name="migrationhubstrategy-GetAssessment-response-assessmentTargets"></a>
List of criteria for assessment.
Type: Array of [AssessmentTarget](API_AssessmentTarget.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [dataCollectionDetails](#API_GetAssessment_ResponseSyntax) **   <a name="migrationhubstrategy-GetAssessment-response-dataCollectionDetails"></a>
 Detailed information about the assessment.
Type: [DataCollectionDetails](API_DataCollectionDetails.md) object

 ** [id](#API_GetAssessment_ResponseSyntax) **   <a name="migrationhubstrategy-GetAssessment-response-id"></a>
 The ID for the specific assessment task.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 52.
Pattern: `.*[0-9a-z-:]+.*`

## Errors
<a name="API_GetAssessment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 The user does not have permission to perform the action. Check the AWS Identity and Access Management (IAM) policy associated with this user.
HTTP Status Code: 403

 ** InternalServerException **
 The server experienced an internal error. Try again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The specified ID in the request is not found.
HTTP Status Code: 404

 ** ThrottlingException **
 The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_GetAssessment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migrationhubstrategy-2020-02-19/GetAssessment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migrationhubstrategy-2020-02-19/GetAssessment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migrationhubstrategy-2020-02-19/GetAssessment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migrationhubstrategy-2020-02-19/GetAssessment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migrationhubstrategy-2020-02-19/GetAssessment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migrationhubstrategy-2020-02-19/GetAssessment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migrationhubstrategy-2020-02-19/GetAssessment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migrationhubstrategy-2020-02-19/GetAssessment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migrationhubstrategy-2020-02-19/GetAssessment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migrationhubstrategy-2020-02-19/GetAssessment)
