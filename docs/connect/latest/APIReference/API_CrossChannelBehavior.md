---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CrossChannelBehavior.html
---

# CrossChannelBehavior
<a name="API_CrossChannelBehavior"></a>

Defines the cross-channel routing behavior that allows an agent working on a contact in one channel to be offered a contact from a different channel.

## Contents
<a name="API_CrossChannelBehavior_Contents"></a>

 ** BehaviorType **   <a name="connect-Type-CrossChannelBehavior-BehaviorType"></a>
Specifies the other channels that can be routed to an agent handling their current channel.
Type: String
Valid Values: `ROUTE_CURRENT_CHANNEL_ONLY | ROUTE_ANY_CHANNEL`
Required: Yes

## See Also
<a name="API_CrossChannelBehavior_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CrossChannelBehavior)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CrossChannelBehavior)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CrossChannelBehavior)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
