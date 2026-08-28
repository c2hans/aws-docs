---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_ListResourcesAssociatedToCustomLineItemResponseElement.html
---

# ListResourcesAssociatedToCustomLineItemResponseElement
<a name="API_ListResourcesAssociatedToCustomLineItemResponseElement"></a>

 A representation of a resource association for a custom line item.

## Contents
<a name="API_ListResourcesAssociatedToCustomLineItemResponseElement_Contents"></a>

 ** Arn **   <a name="billingconductor-Type-ListResourcesAssociatedToCustomLineItemResponseElement-Arn"></a>
 The ARN of the associated resource.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:(customlineitem|billinggroup)/)?[a-zA-Z0-9]{10,12}`
Required: No

 ** EndBillingPeriod **   <a name="billingconductor-Type-ListResourcesAssociatedToCustomLineItemResponseElement-EndBillingPeriod"></a>
The end billing period of the associated resource.
Type: String
Pattern: `\d{4}-(0?[1-9]|1[012])`
Required: No

 ** Relationship **   <a name="billingconductor-Type-ListResourcesAssociatedToCustomLineItemResponseElement-Relationship"></a>
 The type of relationship between the custom line item and the associated resource.
Type: String
Valid Values: `PARENT | CHILD`
Required: No

## See Also
<a name="API_ListResourcesAssociatedToCustomLineItemResponseElement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/ListResourcesAssociatedToCustomLineItemResponseElement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/ListResourcesAssociatedToCustomLineItemResponseElement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/ListResourcesAssociatedToCustomLineItemResponseElement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing Conductor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query billingconductor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
