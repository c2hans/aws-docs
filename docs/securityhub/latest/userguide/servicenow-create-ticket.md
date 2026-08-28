---
source_url: https://docs.aws.amazon.com/securityhub/latest/userguide/servicenow-create-ticket.html
---

# Creating a ticket for a ServiceNow ITSM integration
<a name="servicenow-create-ticket"></a>

 After you create an integration with ServiceNow ITSM, you can create a ticket for a finding.

**Note**
 A finding will always be associated with a single ticket through its entire lifecycle. Security Hub sends all subsequent updates to a finding to the same ticket after initial creation. If a connector associated with an automation rule is changed, the updated connector is used only for new and incoming findings that match the rule criteria.

**To create a ticket for a finding**

1.  Sign in to your AWS account with your credentials, and open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home?region=us-east-1](https://console.aws.amazon.com/securityhub/v2/home?region=us-east-1).

1.  From the navigation pane, under **Inventory**, choose **Findings**.

1.  Choose a finding. In the finding, choose **Create ticket**.

1.  For **Integration**, open the dropdown menu, and choose an integration.

1.  Choose **Create**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
