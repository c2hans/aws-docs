---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_DisassociateResourceResponseElement.html
---

# DisassociateResourceResponseElement
<a name="API_DisassociateResourceResponseElement"></a>

A resource disassociation result for a percentage custom line item.

## Contents
<a name="API_DisassociateResourceResponseElement_Contents"></a>

 ** Arn **   <a name="billingconductor-Type-DisassociateResourceResponseElement-Arn"></a>
The resource ARN that was disassociated from the custom line item.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:(customlineitem|billinggroup)/)?[a-zA-Z0-9]{10,12}`
Required: No

 ** Error **   <a name="billingconductor-Type-DisassociateResourceResponseElement-Error"></a>
 An `AssociateResourceError` that's shown if the resource disassociation fails.
Type: [AssociateResourceError](API_AssociateResourceError.md) object
Required: No

## See Also
<a name="API_DisassociateResourceResponseElement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/DisassociateResourceResponseElement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/DisassociateResourceResponseElement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/DisassociateResourceResponseElement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing Conductor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query billingconductor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
