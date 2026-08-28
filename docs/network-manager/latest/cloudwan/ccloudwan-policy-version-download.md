---
source_url: https://docs.aws.amazon.com/network-manager/latest/cloudwan/ccloudwan-policy-version-download.html
---

# Download an AWS Cloud WAN core network policy
<a name="ccloudwan-policy-version-download"></a>

Download any policy version or your current LIVE policy as a JSON file. You can open the downloaded file in any JSON editor.

**To download a core policy**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Core network**, and then choose **Policy versions**.

1. Under **Policy version ID**, choose the policy version that you want to download, and then choose **Download**.

   The policy downloads to your system as a JSON file. You can make changes to this JSON file as needed. You can create a new policy version using the contents of this file by pasting them into the Cloud WAN JSON editor. For the steps to create a policy using the JSON editor, see [Create an AWS Cloud WAN core network policy version using JSON](cloudwan-create-policy-json.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
