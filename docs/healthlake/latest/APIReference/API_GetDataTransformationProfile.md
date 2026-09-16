---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_GetDataTransformationProfile.html
---

# GetDataTransformationProfile
<a name="API_GetDataTransformationProfile"></a>

Retrieves a data transformation profile's metadata and profile content at a specific version. Specify version 0 to retrieve the DRAFT, a version number between 1 and 99 to retrieve a specific published version, or omit the version to retrieve the latest published version.

## Request Syntax
<a name="API_GetDataTransformationProfile_RequestSyntax"></a>

```
{
   "ProfileId": "{{string}}",
   "ProfileVersion": {{number}}
}
```

## Request Parameters
<a name="API_GetDataTransformationProfile_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ProfileId](#API_GetDataTransformationProfile_RequestSyntax) **   <a name="HealthLake-GetDataTransformationProfile-request-ProfileId"></a>
The unique identifier of the profile to retrieve.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[a-f0-9]{32}`
Required: Yes

 ** [ProfileVersion](#API_GetDataTransformationProfile_RequestSyntax) **   <a name="HealthLake-GetDataTransformationProfile-request-ProfileVersion"></a>
The version number to retrieve. Specify 0 to retrieve the DRAFT version. If you omit this parameter, the service returns the latest published version.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 99.
Required: No

## Response Syntax
<a name="API_GetDataTransformationProfile_ResponseSyntax"></a>

```
{
   "ChangeDescription": "string",
   "LastUpdatedAt": number,
   "ProfileDescription": "string",
   "ProfileId": "string",
   "ProfileMapping": {
      "string" : "string"
   },
   "ProfileName": "string",
   "SourceFormat": "string",
   "TargetFormat": "string",
   "Version": number
}
```

## Response Elements
<a name="API_GetDataTransformationProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChangeDescription](#API_GetDataTransformationProfile_ResponseSyntax) **   <a name="HealthLake-GetDataTransformationProfile-response-ChangeDescription"></a>
A description of what changed in this version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [LastUpdatedAt](#API_GetDataTransformationProfile_ResponseSyntax) **   <a name="HealthLake-GetDataTransformationProfile-response-LastUpdatedAt"></a>
The timestamp when this version was last updated.
Type: Timestamp

 ** [ProfileDescription](#API_GetDataTransformationProfile_ResponseSyntax) **   <a name="HealthLake-GetDataTransformationProfile-response-ProfileDescription"></a>
The description of the profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [ProfileId](#API_GetDataTransformationProfile_ResponseSyntax) **   <a name="HealthLake-GetDataTransformationProfile-response-ProfileId"></a>
The unique identifier of the profile.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[a-f0-9]{32}`

 ** [ProfileMapping](#API_GetDataTransformationProfile_ResponseSyntax) **   <a name="HealthLake-GetDataTransformationProfile-response-ProfileMapping"></a>
The profile content as a map of file paths to content strings.
Type: String to string map
Map Entries: Maximum number of 500 items.
Key Length Constraints: Minimum length of 1. Maximum length of 500.
Value Length Constraints: Minimum length of 0. Maximum length of 102400.

 ** [ProfileName](#API_GetDataTransformationProfile_ResponseSyntax) **   <a name="HealthLake-GetDataTransformationProfile-response-ProfileName"></a>
The name of the profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [SourceFormat](#API_GetDataTransformationProfile_ResponseSyntax) **   <a name="HealthLake-GetDataTransformationProfile-response-SourceFormat"></a>
The source data format of the profile.
Type: String
Valid Values: `CCDA | CSV`

 ** [TargetFormat](#API_GetDataTransformationProfile_ResponseSyntax) **   <a name="HealthLake-GetDataTransformationProfile-response-TargetFormat"></a>
The target output format of the profile.
Type: String
Valid Values: `FHIR_R4`

 ** [Version](#API_GetDataTransformationProfile_ResponseSyntax) **   <a name="HealthLake-GetDataTransformationProfile-response-Version"></a>
The version number of the retrieved profile.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 99.

## Errors
<a name="API_GetDataTransformationProfile_Errors"></a>

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
<a name="API_GetDataTransformationProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/healthlake-2017-07-01/GetDataTransformationProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/healthlake-2017-07-01/GetDataTransformationProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/GetDataTransformationProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/healthlake-2017-07-01/GetDataTransformationProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/GetDataTransformationProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/healthlake-2017-07-01/GetDataTransformationProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/healthlake-2017-07-01/GetDataTransformationProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/healthlake-2017-07-01/GetDataTransformationProfile)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/healthlake-2017-07-01/GetDataTransformationProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/GetDataTransformationProfile)
