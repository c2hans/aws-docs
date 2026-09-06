---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_DataTransformationProfileSummary.html
---

# DataTransformationProfileSummary
<a name="API_DataTransformationProfileSummary"></a>

Contains summary information about a data transformation profile. To retrieve profile content, call `GetDataTransformationProfile`.

## Contents
<a name="API_DataTransformationProfileSummary_Contents"></a>

 ** ProfileId **   <a name="HealthLake-Type-DataTransformationProfileSummary-ProfileId"></a>
The unique identifier of the profile.
Type: String
Length Constraints: Fixed length of 32.
Pattern: `[a-f0-9]{32}`
Required: Yes

 ** SourceFormat **   <a name="HealthLake-Type-DataTransformationProfileSummary-SourceFormat"></a>
The source data format that this profile converts from.
Type: String
Valid Values: `CCDA | CSV`
Required: Yes

 ** TargetFormat **   <a name="HealthLake-Type-DataTransformationProfileSummary-TargetFormat"></a>
The target output format of the profile.
Type: String
Valid Values: `FHIR_R4`
Required: Yes

 ** Version **   <a name="HealthLake-Type-DataTransformationProfileSummary-Version"></a>
The latest version number of the profile.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 99.
Required: Yes

 ** LastUpdatedAt **   <a name="HealthLake-Type-DataTransformationProfileSummary-LastUpdatedAt"></a>
The timestamp when the profile was last updated.
Type: Timestamp
Required: No

 ** ProfileDescription **   <a name="HealthLake-Type-DataTransformationProfileSummary-ProfileDescription"></a>
A description of the profile's purpose.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** ProfileName **   <a name="HealthLake-Type-DataTransformationProfileSummary-ProfileName"></a>
The name of the profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_DataTransformationProfileSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/DataTransformationProfileSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/DataTransformationProfileSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/DataTransformationProfileSummary)
