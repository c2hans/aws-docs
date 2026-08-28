---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_BotAliasReplicaSummary.html
---

# BotAliasReplicaSummary
<a name="API_BotAliasReplicaSummary"></a>

Contains information about all the aliases replication statuses applicable for global resiliency.

## Contents
<a name="API_BotAliasReplicaSummary_Contents"></a>

 ** botAliasId **   <a name="lexv2-Type-BotAliasReplicaSummary-botAliasId"></a>
The bot alias ID for all the alias bot replications.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^(\bTSTALIASID\b|[0-9a-zA-Z]+)$`
Required: No

 ** botAliasReplicationStatus **   <a name="lexv2-Type-BotAliasReplicaSummary-botAliasReplicationStatus"></a>
The replication statuses for all the alias bot replications.
Type: String
Valid Values: `Creating | Updating | Available | Deleting | Failed`
Required: No

 ** botVersion **   <a name="lexv2-Type-BotAliasReplicaSummary-botVersion"></a>
The bot version for all the alias bot replications.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^(DRAFT|[0-9]+)$`
Required: No

 ** creationDateTime **   <a name="lexv2-Type-BotAliasReplicaSummary-creationDateTime"></a>
The creation time and date for all the alias bot replications.
Type: Timestamp
Required: No

 ** failureReasons **   <a name="lexv2-Type-BotAliasReplicaSummary-failureReasons"></a>
The reasons for failure for the aliases bot replications.
Type: Array of strings
Required: No

 ** lastUpdatedDateTime **   <a name="lexv2-Type-BotAliasReplicaSummary-lastUpdatedDateTime"></a>
The last time and date updated for all the alias bot replications.
Type: Timestamp
Required: No

## See Also
<a name="API_BotAliasReplicaSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/BotAliasReplicaSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/BotAliasReplicaSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/BotAliasReplicaSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
