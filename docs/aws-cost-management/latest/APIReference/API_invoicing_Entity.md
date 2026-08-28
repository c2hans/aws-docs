---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_Entity.html
---

# Entity
<a name="API_invoicing_Entity"></a>

The organization name providing AWS services.

## Contents
<a name="API_invoicing_Entity_Contents"></a>

 ** BillingEntity **   <a name="awscostmanagement-Type-invoicing_Entity-BillingEntity"></a>
Helps you identify whether your invoices are for AWS Marketplace or for purchases of other AWS services.
Type: String
Valid Values: `AWS | AWS_MARKETPLACE`
Required: No

 ** InvoicingEntity **   <a name="awscostmanagement-Type-invoicing_Entity-InvoicingEntity"></a>
The name of the entity that issues the AWS invoice.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_invoicing_Entity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/invoicing-2024-12-01/Entity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/invoicing-2024-12-01/Entity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/invoicing-2024-12-01/Entity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
