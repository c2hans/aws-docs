---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_CustomerProjectsContext.html
---

# CustomerProjectsContext
<a name="API_CustomerProjectsContext"></a>

The CustomerProjects structure in Engagements offers a flexible framework for managing customer-project relationships. It supports multiple customers per Engagement and multiple projects per customer, while also allowing for customers without projects and projects without specific customers.

All Engagement members have full visibility of customers and their associated projects, enabling the capture of relevant context even when project details are not fully defined. This structure also facilitates targeted invitations, allowing partners to focus on specific customers and their business problems when sending Engagement invitations.

## Contents
<a name="API_CustomerProjectsContext_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Customer **   <a name="AWSPartnerCentral-Type-CustomerProjectsContext-Customer"></a>
Contains details about the customer associated with the Engagement Invitation, including company information and industry.
Type: [EngagementCustomer](API_EngagementCustomer.md) object
Required: No

 ** Project **   <a name="AWSPartnerCentral-Type-CustomerProjectsContext-Project"></a>
Information about the customer project associated with the Engagement.
Type: [EngagementCustomerProjectDetails](API_EngagementCustomerProjectDetails.md) object
Required: No

## See Also
<a name="API_CustomerProjectsContext_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-selling-2022-07-26/CustomerProjectsContext)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-selling-2022-07-26/CustomerProjectsContext)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-selling-2022-07-26/CustomerProjectsContext)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
