---
source_url: https://docs.aws.amazon.com/verified-access/latest/ug/modify-endpoint-policy.html
---

# Modify a Verified Access endpoint policy
<a name="modify-endpoint-policy"></a>

Use the following procedures to modify the policy for a Verified Access endpoint. After you make the changes, it takes several minutes before they take effect.

**To modify a Verified Access endpoint policy using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Verified Access endpoints**.

1. Select the endpoint.

1. Choose **Actions**, **Modify Verified Access endpoint policy**.

1. (Optional) Turn on or off **Enable policy** as needed.

1. (Optional) For **Policy**, enter the Verified Access policy to apply to the endpoint.

1. Choose **Modify Verified Access endpoint policy**.

**To modify a Verified Access endpoint policy using the AWS CLI**
Use the [modify-verified-access-endpoint-policy](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-verified-access-endpoint-policy.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Verified Access. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verified-access` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
