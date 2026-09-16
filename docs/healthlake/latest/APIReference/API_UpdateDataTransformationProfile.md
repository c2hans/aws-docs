---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_UpdateDataTransformationProfile.html
---

# UpdateDataTransformationProfile
<a name="API_UpdateDataTransformationProfile"></a>

Updates the DRAFT version (version 0) of a data transformation profile with new profile content. The update replaces all existing DRAFT content.

## Request Syntax
<a name="API_UpdateDataTransformationProfile_RequestSyntax"></a>

```
{
   "ChangeDescription": "{{string}}",
   "ProfileId": "{{string}}",
   "ProfileMapping": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_UpdateDataTransformationProfile_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ChangeDescription](#API_UpdateDataTransformationProfile_RequestSyntax) **   <a name="HealthLake-UpdateDataTransformationProfile-request-ChangeDescription"></a>
A description of what changed in this update.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** [ProfileId](#API_UpdateDataTransformationProfile_RequestSyntax) **   <a name="HealthLake-UpdateDataTransformationProfile-request-ProfileId"></a>
The unique identifier of the profile to update.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[a-f0-9]{32}`
Required: Yes

 ** [ProfileMapping](#API_UpdateDataTransformationProfile_RequestSyntax) **   <a name="HealthLake-UpdateDataTransformationProfile-request-ProfileMapping"></a>
The new profile content for the DRAFT version. This is a full replacement of all profile files.
Type: String to string map
Map Entries: Maximum number of 500 items.
Key Length Constraints: Minimum length of 1. Maximum length of 500.
Value Length Constraints: Minimum length of 0. Maximum length of 102400.
Required: Yes

## Response Syntax
<a name="API_UpdateDataTransformationProfile_ResponseSyntax"></a>

```
{
   "LastUpdatedAt": number,
   "ProfileId": "string",
   "ProfileName": "string",
   "SourceFormat": "string",
   "TargetFormat": "string"
}
```

## Response Elements
<a name="API_UpdateDataTransformationProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LastUpdatedAt](#API_UpdateDataTransformationProfile_ResponseSyntax) **   <a name="HealthLake-UpdateDataTransformationProfile-response-LastUpdatedAt"></a>
The timestamp when the profile was last updated.
Type: Timestamp

 ** [ProfileId](#API_UpdateDataTransformationProfile_ResponseSyntax) **   <a name="HealthLake-UpdateDataTransformationProfile-response-ProfileId"></a>
The unique identifier of the updated profile.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[a-f0-9]{32}`

 ** [ProfileName](#API_UpdateDataTransformationProfile_ResponseSyntax) **   <a name="HealthLake-UpdateDataTransformationProfile-response-ProfileName"></a>
The name of the updated profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [SourceFormat](#API_UpdateDataTransformationProfile_ResponseSyntax) **   <a name="HealthLake-UpdateDataTransformationProfile-response-SourceFormat"></a>
The source data format of the profile.
Type: String
Valid Values: `CCDA | CSV`

 ** [TargetFormat](#API_UpdateDataTransformationProfile_ResponseSyntax) **   <a name="HealthLake-UpdateDataTransformationProfile-response-TargetFormat"></a>
The target output format of the profile.
Type: String
Valid Values: `FHIR_R4`

## Errors
<a name="API_UpdateDataTransformationProfile_Errors"></a>

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
<a name="API_UpdateDataTransformationProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/healthlake-2017-07-01/UpdateDataTransformationProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/healthlake-2017-07-01/UpdateDataTransformationProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/UpdateDataTransformationProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/healthlake-2017-07-01/UpdateDataTransformationProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/UpdateDataTransformationProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/healthlake-2017-07-01/UpdateDataTransformationProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/healthlake-2017-07-01/UpdateDataTransformationProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/healthlake-2017-07-01/UpdateDataTransformationProfile)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/healthlake-2017-07-01/UpdateDataTransformationProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/UpdateDataTransformationProfile)
