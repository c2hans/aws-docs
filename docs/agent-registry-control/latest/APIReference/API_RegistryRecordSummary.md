---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_RegistryRecordSummary.html
---

# RegistryRecordSummary
<a name="API_RegistryRecordSummary"></a>

A summary of a registry record returned by list operations. Contains identifying and lifecycle fields but omits descriptor content.

## Contents
<a name="API_RegistryRecordSummary_Contents"></a>

 ** createdAt **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-createdAt"></a>
The timestamp when the registry record was created.
Type: Timestamp
Required: Yes

 ** name **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-name"></a>
The name of the registry record. Names are unique within a registry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_\-\.\/]*`
Required: Yes

 ** recordArn **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-recordArn"></a>
The Amazon Resource Name (ARN) of the registry record.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/[a-zA-Z0-9]{12}`
Required: Yes

 ** recordId **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-recordId"></a>
The unique identifier of the registry record.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[a-zA-Z0-9]{12}`
Required: Yes

 ** recordType **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-recordType"></a>
The type of the registry record, such as MCP, AGENT, SKILL, or CUSTOM.
Type: String
Valid Values: `MCP | AGENT | CUSTOM | SKILL`
Required: Yes

 ** recordVersion **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-recordVersion"></a>
The version identifier of the registry record.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9.-]+`
Required: Yes

 ** registryArn **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-registryArn"></a>
The Amazon Resource Name (ARN) of the parent registry that owns the record.
Type: String
Length Constraints: Minimum length of 46. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}`
Required: Yes

 ** status **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-status"></a>
The lifecycle status of the registry record.
Type: String
Valid Values: `DRAFT | PENDING_APPROVAL | APPROVED | REJECTED | DEPRECATED | CREATING | UPDATING | CREATE_FAILED | UPDATE_FAILED`
Required: Yes

 ** updatedAt **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-updatedAt"></a>
The timestamp when the registry record was last updated.
Type: Timestamp
Required: Yes

 ** description **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-description"></a>
A description of the registry record.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** displayName **   <a name="agentregistrycontrol-Type-RegistryRecordSummary-displayName"></a>
The human-readable display name of the registry record.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_RegistryRecordSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/RegistryRecordSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/RegistryRecordSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/RegistryRecordSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AgentRegistry Control Plane API Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agent-registry-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
