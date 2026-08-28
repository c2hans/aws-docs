---
source_url: https://docs.aws.amazon.com/directconnect/latest/UserGuide/view-lag.html
---

# View LAG details at a Direct Connect endpoint
<a name="view-lag"></a>

After you create a LAG, you can view its details using either the Direct Connect console or using the command line or API.

**To view information about your LAG**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **LAGs**.

1. Select the LAG and choose **View details**.

1. You can view information about the LAG, including its ID, and the Direct Connect endpoint on which the connections terminate.

**To view information about your LAG using the command line or API**
+ [describe-lags](https://docs.aws.amazon.com/cli/latest/reference/directconnect/describe-lags.html) (AWS CLI)
+ [DescribeLags](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLags.html) (Direct Connect API)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Direct Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
