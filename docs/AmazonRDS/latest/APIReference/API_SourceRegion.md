---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_SourceRegion.html
---

# SourceRegion
<a name="API_SourceRegion"></a>

Contains an AWS Region name as the result of a successful call to the `DescribeSourceRegions` action.

## Contents
<a name="API_SourceRegion_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Endpoint **
The endpoint for the source AWS Region endpoint.
Type: String
Required: No

 ** RegionName **
The name of the source AWS Region.
Type: String
Required: No

 ** Status **
The status of the source AWS Region.
Type: String
Required: No

 ** SupportsDBInstanceAutomatedBackupsReplication **
Indicates whether the source AWS Region supports replicating automated backups to the current AWS Region.
Type: Boolean
Required: No

## See Also
<a name="API_SourceRegion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/SourceRegion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/SourceRegion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/SourceRegion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Relational Database Service (RDS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
