---
source_url: https://docs.aws.amazon.com/directconnect/latest/UserGuide/viewdetails.html
---

# View Direct Connect connection details
<a name="viewdetails"></a>

You can view the current status of your connection using either the Direct Connect console or using the command line or API. You can also view your connection ID (for example, `dxcon-12nikabc`) and verify that it matches the connection ID on the LOA-CFA that you received or downloaded.

For information on monitoring connections, see [Monitoring and visibility with Direct Connect](monitoring-overview.md).

**To view details about a connection**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the left pane, choose **Connections**.

1. Select a connection, and then choose **View details**.

**To describe a connection using the command line or API**
+ [describe-connections](https://docs.aws.amazon.com/cli/latest/reference/directconnect/describe-connections.html) (AWS CLI)
+ [DescribeConnections](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeConnections.html) (Direct Connect API)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Direct Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
