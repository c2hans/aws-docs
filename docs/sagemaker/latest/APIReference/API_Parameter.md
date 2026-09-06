---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Parameter.html
---

# Parameter
<a name="API_Parameter"></a>

Assigns a value to a named Pipeline parameter.

## Contents
<a name="API_Parameter_Contents"></a>

 ** Name **   <a name="sagemaker-Type-Parameter-Name"></a>
The name of the parameter to assign a value to. This parameter name must match a named parameter in the pipeline definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9\-_]*`
Required: Yes

 ** Value **   <a name="sagemaker-Type-Parameter-Value"></a>
The literal value for the parameter.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: Yes

## See Also
<a name="API_Parameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/Parameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/Parameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/Parameter)
