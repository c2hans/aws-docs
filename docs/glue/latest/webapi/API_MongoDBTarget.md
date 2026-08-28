---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_MongoDBTarget.html
---

# MongoDBTarget
<a name="API_MongoDBTarget"></a>

Specifies an Amazon DocumentDB or MongoDB data store to crawl.

## Contents
<a name="API_MongoDBTarget_Contents"></a>

 ** ConnectionName **   <a name="Glue-Type-MongoDBTarget-ConnectionName"></a>
The name of the connection to use to connect to the Amazon DocumentDB or MongoDB target.
Type: String
Required: No

 ** Path **   <a name="Glue-Type-MongoDBTarget-Path"></a>
The path of the Amazon DocumentDB or MongoDB target (database/collection).
Type: String
Required: No

 ** ScanAll **   <a name="Glue-Type-MongoDBTarget-ScanAll"></a>
Indicates whether to scan all the records, or to sample rows from the table. Scanning all the records can take a long time when the table is not a high throughput table.
A value of `true` means to scan all records, while a value of `false` means to sample the records. If no value is specified, the value defaults to `true`.
Type: Boolean
Required: No

## See Also
<a name="API_MongoDBTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/MongoDBTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/MongoDBTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/MongoDBTarget)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
