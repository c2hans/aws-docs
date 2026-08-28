---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_TenantDatabasePendingModifiedValues.html
---

# TenantDatabasePendingModifiedValues
<a name="API_TenantDatabasePendingModifiedValues"></a>

A response element in the `ModifyTenantDatabase` operation that describes changes that will be applied. Specific changes are identified by subelements.

## Contents
<a name="API_TenantDatabasePendingModifiedValues_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** MasterUserPassword **
The master password for the tenant database.
Type: String
Required: No

 ** TenantDBName **
The name of the tenant database.
Type: String
Required: No

## See Also
<a name="API_TenantDatabasePendingModifiedValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/TenantDatabasePendingModifiedValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/TenantDatabasePendingModifiedValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/TenantDatabasePendingModifiedValues)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Relational Database Service (RDS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
