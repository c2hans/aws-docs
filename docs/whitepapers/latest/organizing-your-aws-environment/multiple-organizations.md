---
source_url: https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/multiple-organizations.html
---

# Multiple organizations
<a name="multiple-organizations"></a>

 Most customers are best served using a single production organization and a test organization. This allows you to ensure consistency across accounts in your environment because centrally-applied policies or service-level configurations are programmatically applied across accounts within your organization. Separating your workload accounts across organizations requires additional overhead or customization to ensure central standards are applied within each organization.

 There are certain exceptions, outlined in this section, where you might need to work across multiple organizations.

## Test changes to your overall AWS environment
<a name="test-changes-to-your-overall-aws-environment"></a>

 It is recommended to develop infrastructure as code that interacts with APIs and other mechanisms fundamental to the management of your AWS Organization. In these cases, to determine whether your changes break something without having to make the changes in your production organization, we recommend that you test your changes in an organization different from the one running your production workloads.

 For example, you might need to either modify the automation that creates new accounts to change the configuration baseline of accounts it creates or change the configuration of a workflow management system you're using to modify SCPs. In addition, you might want to test the delegated administration capabilities of various AWS services prior to applying them in your production organization.

 In these circumstances, we recommend that you establish an additional AWS Organization for testing that closely resembles your production organization. You can perform testing of changes to how you manage your organization in your test organization before applying those changes to be applied to your production organization.

## Support acquisitions and divestments
<a name="support-acquisitions-and-divestments"></a>

 You might acquire an entity that has already established an organization. If you decide to merge the acquired entity's AWS environment with your AWS environment, you can move member accounts from the acquired organization to your mainstream organization. In this case, you can later decommission the acquired entity's organization.

 If you plan to potentially divest a portion of your portfolio, you can manage the workloads and supporting AWS accounts for that portion of your portfolio in a separate organization to support simpler divesture and isolated billing.

## Support large AWS environments
<a name="support-large-aws-environments"></a>

 You can request a [quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) if your AWS Organization reaches its maximum account limit. Support can help expand your organization's capacity beyond the default number of accounts. For more details about the maximum number of accounts supported in an organization, refer to [Quotas for AWS Organizations.](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_limits.html)

## Align with your billing requirements
<a name="align-with-your-billing-requirements"></a>

 An organization gathers billing information from all member accounts into a single consolidated AWS bill. If you have use cases where different sets of accounts require distinct bills or payments, then multiple organizations might be required. Ensure you have reviewed AWS Billing and Cost Management Conductor and Billing and Management Credit sharing options for your AWS accounts to understand the configurations that are supported within a single AWS Organization.

## Different classification levels for government applications
<a name="different-classification-levels-for-government-applications"></a>

 Some customers in government, critical national infrastructure providers, and defense industries need to handle data with defined classification levels. These customers require high-assurance mechanisms to keep data (and, in most cases, metadata) associated with at least some of those markings, separate from each other. Assets within a single account should all handle data at the same protective marking.

 As noted in this section, an organization itself contains collective data from multiple accounts. Data such as account names, billing data, organizational unit names, and activity logs can be accessed centrally for those with appropriate permissions, such as a cloud administrator or audit team. This means that commingling of billing and logging data from accounts that are processing data might not meet a customer's requirements for separation by classification levels.

 An organization's configuration could be modified to have customized separation for protective marking with proper tags, logging customization (based on protective markings), and defined permissions for administrative users. However, this might be more easily achieved with separate organizations.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
