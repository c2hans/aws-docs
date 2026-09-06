---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_Mapping.html
---

# Mapping
<a name="API_Mapping"></a>

Specifies the mapping template for the transformer. This template is used to map the parsed EDI file using JSONata or XSLT.

## Contents
<a name="API_Mapping_Contents"></a>

 ** templateLanguage **   <a name="b2bi-Type-Mapping-templateLanguage"></a>
The transformation language for the template, either XSLT or JSONATA.
Type: String
Valid Values: `XSLT | JSONATA`
Required: Yes

 ** template **   <a name="b2bi-Type-Mapping-template"></a>
A string that represents the mapping template, in the transformation language specified in `templateLanguage`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 350000.
Required: No

## See Also
<a name="API_Mapping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/Mapping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/Mapping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/Mapping)
