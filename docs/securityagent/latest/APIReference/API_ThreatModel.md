---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_ThreatModel.html
---

# ThreatModel
<a name="API_ThreatModel"></a>

Represents a threat model configuration that defines the parameters for automated threat analysis, including target assets and logging configuration.

## Contents
<a name="API_ThreatModel_Contents"></a>

 ** agentSpaceId **   <a name="securityagent-Type-ThreatModel-agentSpaceId"></a>
The unique identifier of the agent space that contains the threat model.
Type: String
Required: Yes

 ** assets **   <a name="securityagent-Type-ThreatModel-assets"></a>
The assets included in the threat model.
Type: [Assets](API_Assets.md) object
Required: Yes

 ** threatModelId **   <a name="securityagent-Type-ThreatModel-threatModelId"></a>
The unique identifier of the threat model.
Type: String
Required: Yes

 ** title **   <a name="securityagent-Type-ThreatModel-title"></a>
The title of the threat model.
Type: String
Required: Yes

 ** createdAt **   <a name="securityagent-Type-ThreatModel-createdAt"></a>
The date and time the threat model was created, in UTC format.
Type: Timestamp
Required: No

 ** description **   <a name="securityagent-Type-ThreatModel-description"></a>
A description of the application or system being threat modeled.
Type: String
Required: No

 ** logConfig **   <a name="securityagent-Type-ThreatModel-logConfig"></a>
The CloudWatch Logs configuration for the threat model.
Type: [CloudWatchLog](API_CloudWatchLog.md) object
Required: No

 ** scopeDocs **   <a name="securityagent-Type-ThreatModel-scopeDocs"></a>
The scoped documents for the agent to focus on during threat modeling.
Type: Array of [DocumentInfo](API_DocumentInfo.md) objects
Required: No

 ** serviceRole **   <a name="securityagent-Type-ThreatModel-serviceRole"></a>
The IAM service role used for the threat model.
Type: String
Required: No

 ** updatedAt **   <a name="securityagent-Type-ThreatModel-updatedAt"></a>
The date and time the threat model was last updated, in UTC format.
Type: Timestamp
Required: No

## See Also
<a name="API_ThreatModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/ThreatModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/ThreatModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/ThreatModel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Agent. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityagent` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
