---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_BotReplicaSummary.html
---

# BotReplicaSummary
<a name="API_BotReplicaSummary"></a>

Contains summary information about all the replication statuses applicable for global resiliency.

## Contents
<a name="API_BotReplicaSummary_Contents"></a>

 ** botReplicaStatus **   <a name="lexv2-Type-BotReplicaSummary-botReplicaStatus"></a>
The operation status for the replicated bot applicable.
Type: String
Valid Values: `Enabling | Enabled | Deleting | Failed`
Required: No

 ** creationDateTime **   <a name="lexv2-Type-BotReplicaSummary-creationDateTime"></a>
The creation time and date for the replicated bots.
Type: Timestamp
Required: No

 ** failureReasons **   <a name="lexv2-Type-BotReplicaSummary-failureReasons"></a>
The reasons for the failure for the replicated bot.
Type: Array of strings
Required: No

 ** replicaRegion **   <a name="lexv2-Type-BotReplicaSummary-replicaRegion"></a>
The replica region used in the replication statuses summary.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 25.
Required: No

## See Also
<a name="API_BotReplicaSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/BotReplicaSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/BotReplicaSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/BotReplicaSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
