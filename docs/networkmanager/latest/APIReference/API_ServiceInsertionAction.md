---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_ServiceInsertionAction.html
---

# ServiceInsertionAction
<a name="API_ServiceInsertionAction"></a>

Describes the action that the service insertion will take for any segments associated with it.

## Contents
<a name="API_ServiceInsertionAction_Contents"></a>

 ** Action **   <a name="networkmanager-Type-ServiceInsertionAction-Action"></a>
The action the service insertion takes for traffic. `send-via` sends east-west traffic between attachments. `send-to` sends north-south traffic to the security appliance, and then from that to either the Internet or to an on-premesis location.
Type: String
Valid Values: `send-via | send-to`
Required: No

 ** Mode **   <a name="networkmanager-Type-ServiceInsertionAction-Mode"></a>
Describes the mode packets take for the `send-via` action. This is not used when the action is `send-to`. `dual-hop` packets traverse attachments in both the source to the destination core network edges. This mode requires that an inspection attachment must be present in all Regions of the service insertion-enabled segments. For `single-hop`, packets traverse a single intermediate inserted attachment. You can use `EdgeOverride` to specify a specific edge to use.
Type: String
Valid Values: `dual-hop | single-hop`
Required: No

 ** Via **   <a name="networkmanager-Type-ServiceInsertionAction-Via"></a>
The list of network function groups and any edge overrides for the chosen service insertion action. Used for both `send-to` or `send-via`.
Type: [Via](API_Via.md) object
Required: No

 ** WhenSentTo **   <a name="networkmanager-Type-ServiceInsertionAction-WhenSentTo"></a>
The list of destination segments if the service insertion action is `send-via`.
Type: [WhenSentTo](API_WhenSentTo.md) object
Required: No

## See Also
<a name="API_ServiceInsertionAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/ServiceInsertionAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/ServiceInsertionAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/ServiceInsertionAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Global Networks for Transit Gateways. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
