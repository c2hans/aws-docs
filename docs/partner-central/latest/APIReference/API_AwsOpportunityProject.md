---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_AwsOpportunityProject.html
---

# AwsOpportunityProject
<a name="API_AwsOpportunityProject"></a>

Captures details about the project associated with the opportunity, including objectives, scope, and customer requirements.

## Contents
<a name="API_AwsOpportunityProject_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AwsPartition **   <a name="AWSPartnerCentral-Type-AwsOpportunityProject-AwsPartition"></a>
AWS partition where the opportunity will be deployed. Possible values: `aws-eusc` for AWS European Sovereign Cloud, `null` for all other partitions.
Type: String
Valid Values: `aws-eusc`
Required: No

 ** ExpectedCustomerSpend **   <a name="AWSPartnerCentral-Type-AwsOpportunityProject-ExpectedCustomerSpend"></a>
Indicates the expected spending by the customer over the course of the project. This value helps partners and AWS estimate the financial impact of the opportunity. Use the [AWS Pricing Calculator](https://calculator.aws/#/) to create an estimate of the customer’s total spend. If only annual recurring revenue (ARR) is available, distribute it across 12 months to provide an average monthly value.
Type: Array of [ExpectedCustomerSpend](API_ExpectedCustomerSpend.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

## See Also
<a name="API_AwsOpportunityProject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/AwsOpportunityProject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/AwsOpportunityProject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/AwsOpportunityProject)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
