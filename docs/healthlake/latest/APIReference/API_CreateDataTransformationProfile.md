---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_CreateDataTransformationProfile.html
---

# CreateDataTransformationProfile
<a name="API_CreateDataTransformationProfile"></a>

Creates a data transformation profile in DRAFT state. Specify a built-in starter profile, an existing profile version, raw profile content, or a sample data file as the source.

## Request Syntax
<a name="API_CreateDataTransformationProfile_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "KmsKeyId": "{{string}}",
   "ProfileDescription": "{{string}}",
   "ProfileName": "{{string}}",
   "Source": { ... },
   "SourceFormat": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateDataTransformationProfile_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateDataTransformationProfile_RequestSyntax) **   <a name="HealthLake-CreateDataTransformationProfile-request-ClientToken"></a>
A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request but does not return an error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: No

 ** [KmsKeyId](#API_CreateDataTransformationProfile_RequestSyntax) **   <a name="HealthLake-CreateDataTransformationProfile-request-KmsKeyId"></a>
The AWS Key Management Service (AWS KMS) key identifier used to encrypt the profile content at rest.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [ProfileDescription](#API_CreateDataTransformationProfile_RequestSyntax) **   <a name="HealthLake-CreateDataTransformationProfile-request-ProfileDescription"></a>
A human-readable description of the profile's purpose.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** [ProfileName](#API_CreateDataTransformationProfile_RequestSyntax) **   <a name="HealthLake-CreateDataTransformationProfile-request-ProfileName"></a>
A name for the data transformation profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [Source](#API_CreateDataTransformationProfile_RequestSyntax) **   <a name="HealthLake-CreateDataTransformationProfile-request-Source"></a>
The source for the initial profile content. Specify a built-in starter profile, an existing profile version to clone, raw profile content for CI/CD workflows, or a sample data file in Amazon S3.
Type: [CreateDataTransformationProfileSource](API_CreateDataTransformationProfileSource.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [SourceFormat](#API_CreateDataTransformationProfile_RequestSyntax) **   <a name="HealthLake-CreateDataTransformationProfile-request-SourceFormat"></a>
The source data format that this profile converts from (Consolidated Clinical Document Architecture (C-CDA) or Comma-separated values (CSV)).
Type: String
Valid Values: `CCDA | CSV`
Required: Yes

 ** [Tags](#API_CreateDataTransformationProfile_RequestSyntax) **   <a name="HealthLake-CreateDataTransformationProfile-request-Tags"></a>
The tags to associate with the profile at creation time.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateDataTransformationProfile_ResponseSyntax"></a>

```
{
   "LastUpdatedAt": number,
   "ProfileId": "string",
   "ProfileName": "string",
   "SourceFormat": "string",
   "TargetFormat": "string",
   "Version": number
}
```

## Response Elements
<a name="API_CreateDataTransformationProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LastUpdatedAt](#API_CreateDataTransformationProfile_ResponseSyntax) **   <a name="HealthLake-CreateDataTransformationProfile-response-LastUpdatedAt"></a>
The timestamp when the profile was last updated.
Type: Timestamp

 ** [ProfileId](#API_CreateDataTransformationProfile_ResponseSyntax) **   <a name="HealthLake-CreateDataTransformationProfile-response-ProfileId"></a>
The unique identifier of the created profile.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[a-f0-9]{32}`

 ** [ProfileName](#API_CreateDataTransformationProfile_ResponseSyntax) **   <a name="HealthLake-CreateDataTransformationProfile-response-ProfileName"></a>
The name of the created profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [SourceFormat](#API_CreateDataTransformationProfile_ResponseSyntax) **   <a name="HealthLake-CreateDataTransformationProfile-response-SourceFormat"></a>
The source data format of the profile.
Type: String
Valid Values: `CCDA | CSV`

 ** [TargetFormat](#API_CreateDataTransformationProfile_ResponseSyntax) **   <a name="HealthLake-CreateDataTransformationProfile-response-TargetFormat"></a>
The target output format. Always `FHIR_R4`.
Type: String
Valid Values: `FHIR_R4`

 ** [Version](#API_CreateDataTransformationProfile_ResponseSyntax) **   <a name="HealthLake-CreateDataTransformationProfile-response-Version"></a>
The version number of the newly created profile. The starting version is always 0, which indicates the profile is in DRAFT state.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 99.

## Errors
<a name="API_CreateDataTransformationProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied. Your account is not authorized to perform this operation.
HTTP Status Code: 400

 ** ConflictException **
The data store is in a transition state and the user requested action cannot be performed.
HTTP Status Code: 400

 ** InternalServerException **
An unknown internal error occurred in the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested data store was not found.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
The request exceeds the service quota.
HTTP Status Code: 400

 ** ThrottlingException **
The user has exceeded their maximum number of allowed calls to the given API.
HTTP Status Code: 400

 ** ValidationException **
The user input parameter was invalid.
HTTP Status Code: 400

## See Also
<a name="API_CreateDataTransformationProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/healthlake-2017-07-01/CreateDataTransformationProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/healthlake-2017-07-01/CreateDataTransformationProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/CreateDataTransformationProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/healthlake-2017-07-01/CreateDataTransformationProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/CreateDataTransformationProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/healthlake-2017-07-01/CreateDataTransformationProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/healthlake-2017-07-01/CreateDataTransformationProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/healthlake-2017-07-01/CreateDataTransformationProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/healthlake-2017-07-01/CreateDataTransformationProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/CreateDataTransformationProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthLake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthlake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
