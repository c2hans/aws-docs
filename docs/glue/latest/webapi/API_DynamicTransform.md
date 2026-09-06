---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DynamicTransform.html
---

# DynamicTransform
<a name="API_DynamicTransform"></a>

Specifies the set of parameters needed to perform the dynamic transform.

## Contents
<a name="API_DynamicTransform_Contents"></a>

 ** FunctionName **   <a name="Glue-Type-DynamicTransform-FunctionName"></a>
Specifies the name of the function of the dynamic transform.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** Inputs **   <a name="Glue-Type-DynamicTransform-Inputs"></a>
Specifies the inputs for the dynamic transform that are required.
Type: Array of strings
Array Members: Fixed number of 1 item.
Pattern: `[A-Za-z0-9_-]*`
Required: Yes

 ** Name **   <a name="Glue-Type-DynamicTransform-Name"></a>
Specifies the name of the dynamic transform.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** Path **   <a name="Glue-Type-DynamicTransform-Path"></a>
Specifies the path of the dynamic transform source and config files.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** TransformName **   <a name="Glue-Type-DynamicTransform-TransformName"></a>
Specifies the name of the dynamic transform as it appears in the AWS Glue Studio visual editor.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** OutputSchemas **   <a name="Glue-Type-DynamicTransform-OutputSchemas"></a>
Specifies the data schema for the dynamic transform.
Type: Array of [GlueSchema](API_GlueSchema.md) objects
Required: No

 ** Parameters **   <a name="Glue-Type-DynamicTransform-Parameters"></a>
Specifies the parameters of the dynamic transform.
Type: Array of [TransformConfigParameter](API_TransformConfigParameter.md) objects
Required: No

 ** Version **   <a name="Glue-Type-DynamicTransform-Version"></a>
This field is not used and will be deprecated in future release.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

## See Also
<a name="API_DynamicTransform_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DynamicTransform)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DynamicTransform)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DynamicTransform)
