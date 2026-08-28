---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_CrossRegionDisasterRecoveryConfiguration.html
---

# CrossRegionDisasterRecoveryConfiguration
<a name="API_CrossRegionDisasterRecoveryConfiguration"></a>

The configuration for creating an Autonomous Database as a cross-Region disaster recovery peer.

## Contents
<a name="API_CrossRegionDisasterRecoveryConfiguration_Contents"></a>

 ** remoteDisasterRecoveryType **   <a name="odb-Type-CrossRegionDisasterRecoveryConfiguration-remoteDisasterRecoveryType"></a>
The type of remote disaster recovery to configure, either Autonomous Data Guard or backup-based.
Type: String
Valid Values: `ADG | BACKUP_BASED`
Required: Yes

 ** sourceAutonomousDatabaseArn **   <a name="odb-Type-CrossRegionDisasterRecoveryConfiguration-sourceAutonomousDatabaseArn"></a>
The Amazon Resource Name (ARN) of the source Autonomous Database for the cross-Region disaster recovery configuration.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** isReplicateAutomaticBackups **   <a name="odb-Type-CrossRegionDisasterRecoveryConfiguration-isReplicateAutomaticBackups"></a>
Indicates whether automatic backups are replicated to the disaster recovery database.
Type: Boolean
Required: No

## See Also
<a name="API_CrossRegionDisasterRecoveryConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/CrossRegionDisasterRecoveryConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/CrossRegionDisasterRecoveryConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/CrossRegionDisasterRecoveryConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Oracle Database@AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query odb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
