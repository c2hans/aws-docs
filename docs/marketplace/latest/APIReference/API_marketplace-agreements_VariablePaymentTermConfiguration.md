---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_VariablePaymentTermConfiguration.html
---

# VariablePaymentTermConfiguration
<a name="API_marketplace-agreements_VariablePaymentTermConfiguration"></a>

Additional parameters specified by the acceptor while accepting the variable payment term.

## Contents
<a name="API_marketplace-agreements_VariablePaymentTermConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** paymentRequestApprovalStrategy **   <a name="AWSMarketplaceService-Type-marketplace-agreements_VariablePaymentTermConfiguration-paymentRequestApprovalStrategy"></a>
Defines the strategy for approving payment requests. Values include `AUTO_APPROVE_ON_EXPIRATION` and `WAIT_FOR_APPROVAL`
Type: String
Valid Values: `AUTO_APPROVE_ON_EXPIRATION | WAIT_FOR_APPROVAL`
Required: Yes

 ** expirationDuration **   <a name="AWSMarketplaceService-Type-marketplace-agreements_VariablePaymentTermConfiguration-expirationDuration"></a>
Defines the duration after which a payment request is automatically approved if no further action is taken. This only applies when the payment request approval strategy is set to `AUTO_APPROVE_ON_EXPIRATION`. The duration is represented in the ISO\_8601 format (e.g., P10D for 10 days).
Type: String
Pattern: `([-+]?)P(?:([-+]?[0-9]+)D)?(T(?:([-+]?[0-9]+)H)?(?:([-+]?[0-9]+)M)?(?:([-+]?[0-9]+)(?:[.,]([0-9]{0,9}))?S)?)?`
Required: No

## See Also
<a name="API_marketplace-agreements_VariablePaymentTermConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/VariablePaymentTermConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/VariablePaymentTermConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/VariablePaymentTermConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
