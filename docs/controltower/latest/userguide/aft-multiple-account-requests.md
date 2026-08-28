---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/aft-multiple-account-requests.html
---

# Submit multiple account requests
<a name="aft-multiple-account-requests"></a>

 AFT processes account requests one at a time, but you can submit multiple account requests to the AFT pipeline. When you submit multiple account requests to the AFT pipeline, AFT queues and processes the account requests in a first-in, first-out order.

**Note**
 You can create an account request Terraform file for each account that you want AFT to provision or cascade multiple account requests in a single account request Terraform file.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
