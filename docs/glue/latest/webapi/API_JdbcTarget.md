---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_JdbcTarget.html
---

# JdbcTarget
<a name="API_JdbcTarget"></a>

Specifies a JDBC data store to crawl.

## Contents
<a name="API_JdbcTarget_Contents"></a>

 ** ConnectionName **   <a name="Glue-Type-JdbcTarget-ConnectionName"></a>
The name of the connection to use to connect to the JDBC target.
Type: String
Required: No

 ** EnableAdditionalMetadata **   <a name="Glue-Type-JdbcTarget-EnableAdditionalMetadata"></a>
Specify a value of `RAWTYPES` or `COMMENTS` to enable additional metadata in table responses. `RAWTYPES` provides the native-level datatype. `COMMENTS` provides comments associated with a column or table in the database.
If you do not need additional metadata, keep the field empty.
Type: Array of strings
Valid Values: `COMMENTS | RAWTYPES`
Required: No

 ** Exclusions **   <a name="Glue-Type-JdbcTarget-Exclusions"></a>
A list of glob patterns used to exclude from the crawl. For more information, see [Catalog Tables with a Crawler](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html).
Type: Array of strings
Required: No

 ** Path **   <a name="Glue-Type-JdbcTarget-Path"></a>
The path of the JDBC target.
Type: String
Required: No

## See Also
<a name="API_JdbcTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/JdbcTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/JdbcTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/JdbcTarget)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
