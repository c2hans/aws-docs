---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_CreateProfile.html
---

# CreateProfile
<a name="API_CreateProfile"></a>

Create a profile.

## Request Syntax
<a name="API_CreateProfile_RequestSyntax"></a>

```
POST /profiles HTTP/1.1
Content-type: application/json

{
   "ClientRequestToken": "{{string}}",
   "ProfileDescription": "{{string}}",
   "ProfileName": "{{string}}",
   "ProfileQuestions": [
      {
         "QuestionId": "{{string}}",
         "SelectedChoiceIds": [ "{{string}}" ]
      }
   ],
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateProfile_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_CreateProfile_RequestSyntax) **   <a name="wellarchitected-CreateProfile-request-ClientRequestToken"></a>
A unique case-sensitive string used to ensure that this request is idempotent (executes only once).
You should not reuse the same token for other requests. If you retry a request with the same client request token and the same parameters after the original request has completed successfully, the result of the original request is returned.
This token is listed as required, however, if you do not specify it, the AWS SDKs automatically generate one for you. If you are not using the AWS SDK or the AWS CLI, you must provide this token or the request will fail.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\x00-\x7F]*`
Required: Yes

 ** [ProfileDescription](#API_CreateProfile_RequestSyntax) **   <a name="wellarchitected-CreateProfile-request-ProfileDescription"></a>
The profile description.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 100.
Required: Yes

 ** [ProfileName](#API_CreateProfile_RequestSyntax) **   <a name="wellarchitected-CreateProfile-request-ProfileName"></a>
Name of the profile.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 100.
Required: Yes

 ** [ProfileQuestions](#API_CreateProfile_RequestSyntax) **   <a name="wellarchitected-CreateProfile-request-ProfileQuestions"></a>
The profile questions.
Type: Array of [ProfileQuestionUpdate](API_ProfileQuestionUpdate.md) objects
Required: Yes

 ** [Tags](#API_CreateProfile_RequestSyntax) **   <a name="wellarchitected-CreateProfile-request-Tags"></a>
The tags assigned to the profile.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\p{L}\p{N}\p{Z}_.:/=+@-]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ProfileArn": "string",
   "ProfileVersion": "string"
}
```

## Response Elements
<a name="API_CreateProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProfileArn](#API_CreateProfile_ResponseSyntax) **   <a name="wellarchitected-CreateProfile-response-ProfileArn"></a>
The profile ARN.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2084.
Pattern: `arn:aws[-a-z]*:wellarchitected:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:profile/[a-z0-9]+`

 ** [ProfileVersion](#API_CreateProfile_ResponseSyntax) **   <a name="wellarchitected-CreateProfile-response-ProfileVersion"></a>
Version of the profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[A-Za-z0-9-]+`

## Errors
<a name="API_CreateProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
 ** Message **
Description of the error.
HTTP Status Code: 403

 ** ConflictException **
The resource has already been processed, was deleted, or is too large.
 ** Message **
Description of the error.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
HTTP Status Code: 409

 ** InternalServerException **
There is a problem with the AWS Well-Architected Tool API service.
 ** Message **
Description of the error.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The user has reached their resource quota.
 ** Message **
Description of the error.
 ** QuotaCode **
Service Quotas requirement to identify originating quota.
 ** ResourceId **
Identifier of the resource affected.
 ** ResourceType **
Type of the resource affected.
 ** ServiceCode **
Service Quotas requirement to identify originating service.
HTTP Status Code: 402

 ** ThrottlingException **
Request was denied due to request throttling.
 ** Message **
Description of the error.
 ** QuotaCode **
Service Quotas requirement to identify originating quota.
 ** ServiceCode **
Service Quotas requirement to identify originating service.
HTTP Status Code: 429

 ** ValidationException **
The user input is not valid.
 ** Fields **
The fields that caused the error, if applicable.
 ** Message **
Description of the error.
 ** Reason **
The reason why the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_CreateProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/wellarchitected-2020-03-31/CreateProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/wellarchitected-2020-03-31/CreateProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/CreateProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/wellarchitected-2020-03-31/CreateProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/CreateProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/wellarchitected-2020-03-31/CreateProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/wellarchitected-2020-03-31/CreateProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/wellarchitected-2020-03-31/CreateProfile)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/wellarchitected-2020-03-31/CreateProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/CreateProfile)
