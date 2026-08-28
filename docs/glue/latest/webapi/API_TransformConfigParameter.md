---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_TransformConfigParameter.html
---

# TransformConfigParameter
<a name="API_TransformConfigParameter"></a>

Specifies the parameters in the config file of the dynamic transform.

## Contents
<a name="API_TransformConfigParameter_Contents"></a>

 ** Name **   <a name="Glue-Type-TransformConfigParameter-Name"></a>
Specifies the name of the parameter in the config file of the dynamic transform.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** Type **   <a name="Glue-Type-TransformConfigParameter-Type"></a>
Specifies the parameter type in the config file of the dynamic transform.
Type: String
Valid Values: `str | int | float | complex | bool | list | null`
Required: Yes

 ** IsOptional **   <a name="Glue-Type-TransformConfigParameter-IsOptional"></a>
Specifies whether the parameter is optional or not in the config file of the dynamic transform.
Type: Boolean
Required: No

 ** ListType **   <a name="Glue-Type-TransformConfigParameter-ListType"></a>
Specifies the list type of the parameter in the config file of the dynamic transform.
Type: String
Valid Values: `str | int | float | complex | bool | list | null`
Required: No

 ** ValidationMessage **   <a name="Glue-Type-TransformConfigParameter-ValidationMessage"></a>
Specifies the validation message in the config file of the dynamic transform.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** ValidationRule **   <a name="Glue-Type-TransformConfigParameter-ValidationRule"></a>
Specifies the validation rule in the config file of the dynamic transform.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** Value **   <a name="Glue-Type-TransformConfigParameter-Value"></a>
Specifies the value of the parameter in the config file of the dynamic transform.
Type: Array of strings
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

## See Also
<a name="API_TransformConfigParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/TransformConfigParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/TransformConfigParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/TransformConfigParameter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
