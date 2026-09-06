---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ConfigurationDetails.html
---

# ConfigurationDetails
<a name="API_ConfigurationDetails"></a>

Minimal details for a configuration resource.

## Contents
<a name="API_ConfigurationDetails_Contents"></a>

 ** arn **   <a name="omics-Type-ConfigurationDetails-arn"></a>
Unique resource identifier for the configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 190.
Pattern: `arn:.+`
Required: No

 ** name **   <a name="omics-Type-ConfigurationDetails-name"></a>
User-friendly name for the configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9][A-Za-z0-9\-\._]*`
Required: No

 ** uuid **   <a name="omics-Type-ConfigurationDetails-uuid"></a>
Unique identifier for the configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`
Required: No

## See Also
<a name="API_ConfigurationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ConfigurationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ConfigurationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ConfigurationDetails)
