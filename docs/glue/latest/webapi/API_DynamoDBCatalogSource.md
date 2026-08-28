---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DynamoDBCatalogSource.html
---

# DynamoDBCatalogSource
<a name="API_DynamoDBCatalogSource"></a>

Specifies a DynamoDB data source in the AWS Glue Data Catalog.

## Contents
<a name="API_DynamoDBCatalogSource_Contents"></a>

 ** Database **   <a name="Glue-Type-DynamoDBCatalogSource-Database"></a>
The name of the database to read from.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** Name **   <a name="Glue-Type-DynamoDBCatalogSource-Name"></a>
The name of the data source.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** Table **   <a name="Glue-Type-DynamoDBCatalogSource-Table"></a>
The name of the table in the database to read from.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** AdditionalOptions **   <a name="Glue-Type-DynamoDBCatalogSource-AdditionalOptions"></a>
Specifies additional connection options for the DynamoDB data source.
Type: [DDBELTCatalogAdditionalOptions](API_DDBELTCatalogAdditionalOptions.md) object
Required: No

 ** PitrEnabled **   <a name="Glue-Type-DynamoDBCatalogSource-PitrEnabled"></a>
Specifies whether Point-in-Time Recovery (PITR) is enabled for the DynamoDB table. When set to `true`, allows reading from a specific point in time. The default value is `false`.
Type: Boolean
Required: No

## See Also
<a name="API_DynamoDBCatalogSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DynamoDBCatalogSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DynamoDBCatalogSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DynamoDBCatalogSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
