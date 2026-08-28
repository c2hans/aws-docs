---
source_url: https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_Action.html
---

# Action
<a name="API_Action"></a>

An action to take when a gateway rule's conditions are met.

## Contents
<a name="API_Action_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** configurationBundle **   <a name="bedrockagentcorecontrol-Type-Action-configurationBundle"></a>
An action that applies a configuration bundle override to the request.
Type: [ConfigurationBundleAction](API_ConfigurationBundleAction.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** routeToTarget **   <a name="bedrockagentcorecontrol-Type-Action-routeToTarget"></a>
An action that routes the request to a specific target.
Type: [RouteToTargetAction](API_RouteToTargetAction.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_Action_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/Action)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/Action)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/Action)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore Control Plane. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore-control` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
