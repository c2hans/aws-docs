---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_UpsertRedshiftTargetOptions.html
---

# UpsertRedshiftTargetOptions
<a name="API_UpsertRedshiftTargetOptions"></a>

The options to configure an upsert operation when writing to a Redshift target .

## Contents
<a name="API_UpsertRedshiftTargetOptions_Contents"></a>

 ** ConnectionName **   <a name="Glue-Type-UpsertRedshiftTargetOptions-ConnectionName"></a>
The name of the connection to use to write to Redshift.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** TableLocation **   <a name="Glue-Type-UpsertRedshiftTargetOptions-TableLocation"></a>
The physical location of the Redshift table.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** UpsertKeys **   <a name="Glue-Type-UpsertRedshiftTargetOptions-UpsertKeys"></a>
The keys used to determine whether to perform an update or insert.
Type: Array of strings
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

## See Also
<a name="API_UpsertRedshiftTargetOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/UpsertRedshiftTargetOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/UpsertRedshiftTargetOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/UpsertRedshiftTargetOptions)
