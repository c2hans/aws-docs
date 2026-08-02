---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_Parameter.html
---

# Parameter
<a name="API_Parameter"></a>

A list of parameter values to add to the resource. A parameter is specified as a key-value pair. A valid parameter value must exist for any parameter that is marked as required in the multi-tenant distribution.

## Contents
<a name="API_Parameter_Contents"></a>

 ** Name **   <a name="cloudfront-Type-Parameter-Name"></a>
The parameter name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]+`
Required: Yes

 ** Value **   <a name="cloudfront-Type-Parameter-Value"></a>
The parameter value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_Parameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/Parameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/Parameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/Parameter)
