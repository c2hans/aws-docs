---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_AgentAccessSetting.html
---

# AgentAccessSetting
<a name="API_AgentAccessSetting"></a>

A permission setting for an agent action. Each setting specifies an agent action and whether it is enabled or disabled.

## Contents
<a name="API_AgentAccessSetting_Contents"></a>

 ** AgentAction **   <a name="WorkSpacesApplications-Type-AgentAccessSetting-AgentAction"></a>
The agent action to configure. Valid values are COMPUTER\_VISION, COMPUTER\_INPUT, and FORWARD\_MCP\_TOOLS. If you enable COMPUTER\_INPUT, you must also enable COMPUTER\_VISION.
Type: String
Valid Values: `COMPUTER_VISION | COMPUTER_INPUT | FORWARD_MCP_TOOLS`
Required: Yes

 ** Permission **   <a name="WorkSpacesApplications-Type-AgentAccessSetting-Permission"></a>
Whether the agent action is enabled or disabled.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

## See Also
<a name="API_AgentAccessSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/AgentAccessSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/AgentAccessSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/AgentAccessSetting)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
