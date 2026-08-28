---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/optimization-apis.html
---

# Private optimization APIs for Connect Customer forecasting, capacity planning, and scheduling
<a name="optimization-apis"></a>

Connect Customer forecasting, capacity planning, and scheduling uses the following private API resources as actions in its IAM policy:
+ `connect:BatchAssociateAnalyticsDataSet`. Grants access permissions and associates the specified datasets for the specified Connect Customer instance with the specified AWS account.
+ `connect:BatchDisassociateAnalyticsDataSet`. Revokes access permissions and disassociates the specified datasets for the specified Connect Customer instance with the specified AWS account.

If you remove these actions from the preview role policy, the forecasting, capacity planning, and scheduling features won't work.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
