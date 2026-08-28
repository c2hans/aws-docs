---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_DataReplicationInitiation.html
---

# DataReplicationInitiation
<a name="API_DataReplicationInitiation"></a>

Data replication initiation.

## Contents
<a name="API_DataReplicationInitiation_Contents"></a>

 ** nextAttemptDateTime **   <a name="drs-Type-DataReplicationInitiation-nextAttemptDateTime"></a>
The date and time of the next attempt to initiate data replication.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** startDateTime **   <a name="drs-Type-DataReplicationInitiation-startDateTime"></a>
The date and time of the current attempt to initiate data replication.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** steps **   <a name="drs-Type-DataReplicationInitiation-steps"></a>
The steps of the current attempt to initiate data replication.
Type: Array of [DataReplicationInitiationStep](API_DataReplicationInitiationStep.md) objects
Required: No

## See Also
<a name="API_DataReplicationInitiation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/DataReplicationInitiation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/DataReplicationInitiation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/DataReplicationInitiation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
