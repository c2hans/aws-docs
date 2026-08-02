---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_S3HudiSource.html
---

# S3HudiSource
<a name="API_S3HudiSource"></a>

Specifies a Hudi data source stored in Amazon S3.

## Contents
<a name="API_S3HudiSource_Contents"></a>

 ** Name **   <a name="Glue-Type-S3HudiSource-Name"></a>
The name of the Hudi source.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** Paths **   <a name="Glue-Type-S3HudiSource-Paths"></a>
A list of the Amazon S3 paths to read from.
Type: Array of strings
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** AdditionalHudiOptions **   <a name="Glue-Type-S3HudiSource-AdditionalHudiOptions"></a>
Specifies additional connection options.
Type: String to string map
Key Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Value Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** AdditionalOptions **   <a name="Glue-Type-S3HudiSource-AdditionalOptions"></a>
Specifies additional options for the connector.
Type: [S3DirectSourceAdditionalOptions](API_S3DirectSourceAdditionalOptions.md) object
Required: No

 ** OutputSchemas **   <a name="Glue-Type-S3HudiSource-OutputSchemas"></a>
Specifies the data schema for the Hudi source.
Type: Array of [GlueSchema](API_GlueSchema.md) objects
Required: No

## See Also
<a name="API_S3HudiSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/S3HudiSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/S3HudiSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/S3HudiSource)
