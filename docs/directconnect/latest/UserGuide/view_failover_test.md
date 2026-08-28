---
source_url: https://docs.aws.amazon.com/directconnect/latest/UserGuide/view_failover_test.html
---

# View AWS Direct Connect Resiliency Toolkit virtual interface failover test history
<a name="view_failover_test"></a>

You can view the virtual interface failover test history using the Direct Connect console, or the AWS CLI.

**To view the virtual interface failover test history from the Direct Connect console**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. Choose **Virtual interfaces**.

1. Select the virtual interface and then choose **View details**.

1. Choose **Test history**.

   The console displays the virtual interface tests that you performed for the virtual interface.

1. To view the details for a specific test, select the test id.

**To view the virtual interface failover test history using the AWS CLI**
Use [ListVirtualInterfaceTestHistory](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_ListVirtualInterfaceTestHistory.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Direct Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
