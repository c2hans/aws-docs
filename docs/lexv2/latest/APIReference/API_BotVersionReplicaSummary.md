---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_BotVersionReplicaSummary.html
---

# BotVersionReplicaSummary
<a name="API_BotVersionReplicaSummary"></a>

Contains summary information for all the version replication statuses applicable for Global resiliency.

## Contents
<a name="API_BotVersionReplicaSummary_Contents"></a>

 ** botVersion **   <a name="lexv2-Type-BotVersionReplicaSummary-botVersion"></a>
The bot version for the summary information for all the version replication statuses.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^(DRAFT|[0-9]+)$`
Required: No

 ** botVersionReplicationStatus **   <a name="lexv2-Type-BotVersionReplicaSummary-botVersionReplicationStatus"></a>
The version replication status for all the replicated bots.
Type: String
Valid Values: `Creating | Available | Deleting | Failed`
Required: No

 ** creationDateTime **   <a name="lexv2-Type-BotVersionReplicaSummary-creationDateTime"></a>
The creation date and time of the replication status for all the replicated bots.
Type: Timestamp
Required: No

 ** failureReasons **   <a name="lexv2-Type-BotVersionReplicaSummary-failureReasons"></a>
The reasons for replication failure for all the replicated bots.
Type: Array of strings
Required: No

## See Also
<a name="API_BotVersionReplicaSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/BotVersionReplicaSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/BotVersionReplicaSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/BotVersionReplicaSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
