---
source_url: https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ImplementationFilter.html
---

# ImplementationFilter
<a name="API_ImplementationFilter"></a>

A structure that defines filtering criteria for control implementations. You can use this filter to find controls that are implemented by specific AWS services or with specific service identifiers.

## Contents
<a name="API_ImplementationFilter_Contents"></a>

 ** Identifiers **   <a name="controlcatalog-Type-ImplementationFilter-Identifiers"></a>
A list of service-specific identifiers that can serve as filters. For example, you can filter for controls with specific AWS Config Rule IDs or Security Hub Control IDs.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_\.-]+`
Required: No

 ** Types **   <a name="controlcatalog-Type-ImplementationFilter-Types"></a>
A list of implementation types that can serve as filters. For example, you can filter for controls implemented as AWS Config Rules by specifying AWS::Config::ConfigRule as a type.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 7. Maximum length of 2048.
Pattern: `[A-Za-z0-9]+(::[A-Za-z0-9_]+){2,3}`
Required: No

## See Also
<a name="API_ImplementationFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controlcatalog-2018-05-10/ImplementationFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controlcatalog-2018-05-10/ImplementationFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controlcatalog-2018-05-10/ImplementationFilter)
