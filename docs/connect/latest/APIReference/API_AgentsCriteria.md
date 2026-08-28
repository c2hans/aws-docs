---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_AgentsCriteria.html
---

# AgentsCriteria
<a name="API_AgentsCriteria"></a>

Can be used to define a list of preferred agents to target the contact to within the queue. Note that agents must have the queue in their routing profile in order to be offered the contact.

## Contents
<a name="API_AgentsCriteria_Contents"></a>

 ** AgentIds **   <a name="connect-Type-AgentsCriteria-AgentIds"></a>
An object to specify a list of agents, by user ID.
Type: Array of strings
Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_AgentsCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/AgentsCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/AgentsCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/AgentsCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
