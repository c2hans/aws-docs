---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DBMajorEngineVersion.html
---

# DBMajorEngineVersion
<a name="API_DBMajorEngineVersion"></a>

This data type is used as a response element in the operation `DescribeDBMajorEngineVersions`.

## Contents
<a name="API_DBMajorEngineVersion_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Engine **
The name of the database engine.
Type: String
Required: No

 ** MajorEngineVersion **
The major version number of the database engine.
Type: String
Required: No

 ** SupportedEngineLifecycles.SupportedEngineLifecycle.N **
A list of the lifecycles supported by this engine for the `DescribeDBMajorEngineVersions` operation.
Type: Array of [SupportedEngineLifecycle](API_SupportedEngineLifecycle.md) objects
Required: No

## See Also
<a name="API_DBMajorEngineVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/DBMajorEngineVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/DBMajorEngineVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/DBMajorEngineVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Relational Database Service (RDS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
