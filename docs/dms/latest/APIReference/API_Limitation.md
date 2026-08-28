---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_Limitation.html
---

# Limitation
<a name="API_Limitation"></a>

Provides information about the limitations of target AWS engines.

Your source database might include features that the target AWS engine doesn't support. Fleet Advisor lists these features as limitations. You should consider these limitations during database migration. For each limitation, Fleet Advisor recommends an action that you can take to address or avoid this limitation.

## Contents
<a name="API_Limitation_Contents"></a>

 ** DatabaseId **   <a name="DMS-Type-Limitation-DatabaseId"></a>
The identifier of the source database.
Type: String
Required: No

 ** Description **   <a name="DMS-Type-Limitation-Description"></a>
A description of the limitation. Provides additional information about the limitation, and includes recommended actions that you can take to address or avoid this limitation.
Type: String
Required: No

 ** EngineName **   <a name="DMS-Type-Limitation-EngineName"></a>
The name of the target engine that Fleet Advisor should use in the target engine recommendation. Valid values include `"rds-aurora-mysql"`, `"rds-aurora-postgresql"`, `"rds-mysql"`, `"rds-oracle"`, `"rds-sql-server"`, and `"rds-postgresql"`.
Type: String
Required: No

 ** Impact **   <a name="DMS-Type-Limitation-Impact"></a>
The impact of the limitation. You can use this parameter to prioritize limitations that you want to address. Valid values include `"Blocker"`, `"High"`, `"Medium"`, and `"Low"`.
Type: String
Required: No

 ** Name **   <a name="DMS-Type-Limitation-Name"></a>
The name of the limitation. Describes unsupported database features, migration action items, and other limitations.
Type: String
Required: No

 ** Type **   <a name="DMS-Type-Limitation-Type"></a>
The type of the limitation, such as action required, upgrade required, and limited feature.
Type: String
Required: No

## See Also
<a name="API_Limitation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/Limitation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/Limitation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/Limitation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
