---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CustomCode.html
---

# CustomCode
<a name="API_CustomCode"></a>

Specifies a transform that uses custom code you provide to perform the data transformation. The output is a collection of DynamicFrames.

## Contents
<a name="API_CustomCode_Contents"></a>

 ** ClassName **   <a name="Glue-Type-CustomCode-ClassName"></a>
The name defined for the custom code node class.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** Code **   <a name="Glue-Type-CustomCode-Code"></a>
The custom code that is used to perform the data transformation.
Type: String
Pattern: `[\s\S]*`
Required: Yes

 ** Inputs **   <a name="Glue-Type-CustomCode-Inputs"></a>
The data inputs identified by their node names.
Type: Array of strings
Array Members: Minimum number of 1 item.
Pattern: `[A-Za-z0-9_-]*`
Required: Yes

 ** Name **   <a name="Glue-Type-CustomCode-Name"></a>
The name of the transform node.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** OutputSchemas **   <a name="Glue-Type-CustomCode-OutputSchemas"></a>
Specifies the data schema for the custom code transform.
Type: Array of [GlueSchema](API_GlueSchema.md) objects
Required: No

## See Also
<a name="API_CustomCode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CustomCode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CustomCode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CustomCode)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
