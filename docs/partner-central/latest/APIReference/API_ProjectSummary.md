---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_ProjectSummary.html
---

# ProjectSummary
<a name="API_ProjectSummary"></a>

An object that contains a `Project` object's subset of fields.

## Contents
<a name="API_ProjectSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DeliveryModels **   <a name="AWSPartnerCentral-Type-ProjectSummary-DeliveryModels"></a>
Specifies your solution or service's deployment or consumption model in the `Opportunity`'s context. You can select multiple options.
Options' descriptions from the `Delivery Model` field are:
+ SaaS or PaaS: Your AWS based solution deployed as SaaS or PaaS in your AWS environment.
+ BYOL or AMI: Your AWS based solution deployed as BYOL or AMI in the end customer's AWS environment.
+ Managed Services: The end customer's AWS business management (For example: Consulting, design, implementation, billing support, cost optimization, technical support).
+ Professional Services: Offerings to help enterprise end customers achieve specific business outcomes for enterprise cloud adoption (For example: Advisory or transformation planning).
+ Resell: AWS accounts and billing management for your customers.
+ Other: Delivery model not described above.
Type: Array of strings
Valid Values: `SaaS or PaaS | BYOL or AMI | Managed Services | Professional Services | Resell | Other`
Required: No

 ** ExpectedContractDuration **   <a name="AWSPartnerCentral-Type-ProjectSummary-ExpectedContractDuration"></a>
Optional. The expected contract duration for this opportunity, representing the anticipated length of the contract in the unit specified by `Term`.
Type: [ExpectedContractDuration](API_ExpectedContractDuration.md) object
Required: No

 ** ExpectedCustomerSpend **   <a name="AWSPartnerCentral-Type-ProjectSummary-ExpectedCustomerSpend"></a>
Provides a summary of the expected customer spend for the project, offering a high-level view of the potential financial impact.
Type: Array of [ExpectedCustomerSpend](API_ExpectedCustomerSpend.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

## See Also
<a name="API_ProjectSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/ProjectSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/ProjectSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/ProjectSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
