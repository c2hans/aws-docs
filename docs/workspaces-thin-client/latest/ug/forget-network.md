---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/forget-network.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/workspacesthinclient-end-of-support.html).

# Forgetting a network
<a name="forget-network"></a>

Your WorkSpaces Thin Client will automatically sign on to your set Wi-Fi network. If you're currently using or you have joined a network that you no longer use, your device can forget this network.

Your device can only forget known Wi-Fi networks. If your device has never joined a Wi-Fi network, you don't have the option to forget that network.

Your device can not forget Ethernet connected networks.

![Network settings page showing a connected Mobile network with options to Forget or Disconnect.](http://docs.aws.amazon.com/workspaces-thin-client/latest/ug/images/forgetnetwork.png)

1. Go to **Settings**, **Network**, **Known Networks**.

1. Select **Forget** from the desired network.

The network is removed from the **Known Networks** list. If you want to join this network again, please use [ Show Available Networks](show-available-networks.md) or [Add New Network](add-new-network.md) to connect to the network again.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Thin Client. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-thin-client` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
