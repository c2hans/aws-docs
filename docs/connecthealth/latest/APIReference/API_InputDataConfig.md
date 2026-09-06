---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_InputDataConfig.html
---

# InputDataConfig
<a name="API_InputDataConfig"></a>

Configuration details for input patient data

## Contents
<a name="API_InputDataConfig_Contents"></a>

 ** fhirServer **   <a name="connecthealth-Type-InputDataConfig-fhirServer"></a>
FHIR server configuration to retrieve patient data.
Type: [FHIRServer](API_FHIRServer.md) object
Required: No

 ** s3Sources **   <a name="connecthealth-Type-InputDataConfig-s3Sources"></a>
List of S3 sources containing patient data.
Type: Array of [S3Source](API_S3Source.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

## See Also
<a name="API_InputDataConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/InputDataConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/InputDataConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/InputDataConfig)
