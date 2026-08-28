---
source_url: https://docs.aws.amazon.com/directconnect/latest/UserGuide/interface-set-mtu.html
---

# Set the MTU of a Direct Connect private virtual interface
<a name="interface-set-mtu"></a>

If your virtual interface has both an IPv4 and IPv6 BGP peering session, you can delete one of the BGP peering sessions (but not both). For more information about MTUs and private virtual interfaces, see [MTUs for private virtual interfaces or transit virtual interfaces](WorkingWithVirtualInterfaces.md#set-jumbo-frames-vif.title).

You can set the MTU of a private virtual interface using either the Direct Connect console or using the command line or API.

**To set the MTU of a private virtual interface**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Virtual Interfaces**.

1.  Select the virtual interface and then choose **Edit**.

1. Under **Jumbo MTU (MTU size 8500)**, select **Enabled**.

1. Under **Acknowledge**, select **I understand the selected connection(s) will go down for a brief period**. The state of the virtual interface is `pending` until the update is complete.

**To set the MTU of a private virtual interface using the command line or API**
+ [update-virtual-interface-attributes](https://docs.aws.amazon.com/cli/latest/reference/directconnect/update-virtual-interface-attributes.html) (AWS CLI)
+ [UpdateVirtualInterfaceAttributes](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_UpdateVirtualInterfaceAttributes.html) (Direct Connect API)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Direct Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
