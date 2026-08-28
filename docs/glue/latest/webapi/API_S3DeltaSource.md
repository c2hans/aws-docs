---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_S3DeltaSource.html
---

# S3DeltaSource
<a name="API_S3DeltaSource"></a>

Specifies a Delta Lake data source stored in Amazon S3.

## Contents
<a name="API_S3DeltaSource_Contents"></a>

 ** Name **   <a name="Glue-Type-S3DeltaSource-Name"></a>
The name of the Delta Lake source.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** Paths **   <a name="Glue-Type-S3DeltaSource-Paths"></a>
A list of the Amazon S3 paths to read from.
Type: Array of strings
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** AdditionalDeltaOptions **   <a name="Glue-Type-S3DeltaSource-AdditionalDeltaOptions"></a>
Specifies additional connection options.
Type: String to string map
Key Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Value Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** AdditionalOptions **   <a name="Glue-Type-S3DeltaSource-AdditionalOptions"></a>
Specifies additional options for the connector.
Type: [S3DirectSourceAdditionalOptions](API_S3DirectSourceAdditionalOptions.md) object
Required: No

 ** OutputSchemas **   <a name="Glue-Type-S3DeltaSource-OutputSchemas"></a>
Specifies the data schema for the Delta Lake source.
Type: Array of [GlueSchema](API_GlueSchema.md) objects
Required: No

## See Also
<a name="API_S3DeltaSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/S3DeltaSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/S3DeltaSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/S3DeltaSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
