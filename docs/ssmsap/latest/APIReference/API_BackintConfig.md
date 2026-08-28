---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_BackintConfig.html
---

# BackintConfig
<a name="API_BackintConfig"></a>

Configuration parameters for AWS Backint Agent for SAP HANA. You can backup your SAP HANA database with AWS Backup or Amazon S3.

## Contents
<a name="API_BackintConfig_Contents"></a>

 ** BackintMode **   <a name="ssmsap-Type-BackintConfig-BackintMode"></a>
AWS service for your database backup.
Type: String
Valid Values: `AWSBackup`
Required: Yes

 ** EnsureNoBackupInProcess **   <a name="ssmsap-Type-BackintConfig-EnsureNoBackupInProcess"></a>

Type: Boolean
Required: Yes

## See Also
<a name="API_BackintConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/BackintConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/BackintConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/BackintConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager for SAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ssmsap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
