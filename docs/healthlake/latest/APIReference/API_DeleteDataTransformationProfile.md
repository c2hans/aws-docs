---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_DeleteDataTransformationProfile.html
---

# DeleteDataTransformationProfile
<a name="API_DeleteDataTransformationProfile"></a>

Deletes a data transformation profile and all its versions, including the DRAFT and all published versions.

## Request Syntax
<a name="API_DeleteDataTransformationProfile_RequestSyntax"></a>

```
{
   "ProfileId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteDataTransformationProfile_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ProfileId](#API_DeleteDataTransformationProfile_RequestSyntax) **   <a name="HealthLake-DeleteDataTransformationProfile-request-ProfileId"></a>
The unique identifier of the profile to delete.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[a-f0-9]{32}`
Required: Yes

## Response Syntax
<a name="API_DeleteDataTransformationProfile_ResponseSyntax"></a>

```
{
   "DeletionTime": number,
   "ProfileId": "string",
   "ProfileName": "string"
}
```

## Response Elements
<a name="API_DeleteDataTransformationProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DeletionTime](#API_DeleteDataTransformationProfile_ResponseSyntax) **   <a name="HealthLake-DeleteDataTransformationProfile-response-DeletionTime"></a>
The timestamp when the profile was deleted.
Type: Timestamp

 ** [ProfileId](#API_DeleteDataTransformationProfile_ResponseSyntax) **   <a name="HealthLake-DeleteDataTransformationProfile-response-ProfileId"></a>
The unique identifier of the deleted profile.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[a-f0-9]{32}`

 ** [ProfileName](#API_DeleteDataTransformationProfile_ResponseSyntax) **   <a name="HealthLake-DeleteDataTransformationProfile-response-ProfileName"></a>
The name of the deleted profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_DeleteDataTransformationProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied. Your account is not authorized to perform this operation.
HTTP Status Code: 400

 ** InternalServerException **
An unknown internal error occurred in the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested data store was not found.
HTTP Status Code: 400

 ** ThrottlingException **
The user has exceeded their maximum number of allowed calls to the given API.
HTTP Status Code: 400

 ** ValidationException **
The user input parameter was invalid.
HTTP Status Code: 400

## See Also
<a name="API_DeleteDataTransformationProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/healthlake-2017-07-01/DeleteDataTransformationProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/healthlake-2017-07-01/DeleteDataTransformationProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/DeleteDataTransformationProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/healthlake-2017-07-01/DeleteDataTransformationProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/DeleteDataTransformationProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/healthlake-2017-07-01/DeleteDataTransformationProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/healthlake-2017-07-01/DeleteDataTransformationProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/healthlake-2017-07-01/DeleteDataTransformationProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/healthlake-2017-07-01/DeleteDataTransformationProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/DeleteDataTransformationProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthLake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthlake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
