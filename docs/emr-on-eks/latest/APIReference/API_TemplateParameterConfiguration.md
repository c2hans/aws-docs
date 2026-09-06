---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_TemplateParameterConfiguration.html
---

# TemplateParameterConfiguration
<a name="API_TemplateParameterConfiguration"></a>

The configuration of a job template parameter.

## Contents
<a name="API_TemplateParameterConfiguration_Contents"></a>

 ** defaultValue **   <a name="emroneks-Type-TemplateParameterConfiguration-defaultValue"></a>
The default value for the job template parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: No

 ** type **   <a name="emroneks-Type-TemplateParameterConfiguration-type"></a>
The type of the job template parameter. Allowed values are: ‘STRING’, ‘NUMBER’.
Type: String
Valid Values: `NUMBER | STRING`
Required: No

## See Also
<a name="API_TemplateParameterConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/TemplateParameterConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/TemplateParameterConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/TemplateParameterConfiguration)
