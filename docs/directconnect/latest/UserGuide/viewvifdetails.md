---
source_url: https://docs.aws.amazon.com/directconnect/latest/UserGuide/viewvifdetails.html
---

# View Direct Connect virtual interface details
<a name="viewvifdetails"></a>

You can view the current status of your virtual interface using either the Direct Connect console or using the command line or API. Details include:
+ Connection state
+ Name
+ Location
+ VLAN
+ BGP details
+ Peer IP addresses

**To view details about a virtual interface**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the left pane, choose **Virtual Interfaces**.

1. Select the virtual interface and then choose **View details**.

**To describe virtual interfaces using the command line or API**
+ [describe-virtual-interfaces](https://docs.aws.amazon.com/cli/latest/reference/directconnect/describe-virtual-interfaces.html) (AWS CLI)
+ [DescribeVirtualInterfaces](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeVirtualInterfaces.html) (Direct Connect API)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Direct Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
