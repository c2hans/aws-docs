---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_TargetDataSetting.html
---

# TargetDataSetting
<a name="API_TargetDataSetting"></a>

Defines settings for a target data provider for a data migration.

## Contents
<a name="API_TargetDataSetting_Contents"></a>

 ** TablePreparationMode **   <a name="DMS-Type-TargetDataSetting-TablePreparationMode"></a>
This setting determines how DMS handles the target tables before starting a data migration, either by leaving them untouched, dropping and recreating them, or truncating the existing data in the target tables.
Type: String
Valid Values: `drop-tables-on-target | truncate | do-nothing`
Required: No

## See Also
<a name="API_TargetDataSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/TargetDataSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/TargetDataSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/TargetDataSetting)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
