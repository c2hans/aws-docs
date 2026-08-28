---
source_url: https://docs.aws.amazon.com/security-lake/latest/userguide/opting-out-of-using-your-data.html
---

# Opting out of using your data for service improvement
<a name="opting-out-of-using-your-data"></a>

You can choose to opt out of having your data used to develop and improve Security Lake and other AWS security services by using the AWS Organizations opt-out policy. You can choose to opt out even if Security Lake doesn't currently collect any such data. For more information about how to opt out, see [AI services opt-out policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out.html) in the *AWS Organizations User Guide*.

Presently, Security Lake does not collect any of the security data that it processes on your behalf, or security data that you upload to your security data lake created by this service. To develop and improve the Security Lake service and the functionalities of other AWS security services, Security Lake may collect such data in the future, including data that you upload from third-party data sources. We will update this page when Security Lake intends on collecting any such data and describe how this will work. You will still have an opportunity to opt out at any time.

**Note**
For you to use the opt-out policy, your AWS accounts must be centrally managed by AWS Organizations. If you haven't already created an organization for your AWS accounts, see [Creating and managing an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org.html) in the *AWS Organizations User Guide*.

Opting out has the following effects:
+ Security Lake will delete the data that it collected and stored prior to your opt out (if any).
+ After you opt out, Security Lake will no longer collect or store this data.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Security Lake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-lake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
