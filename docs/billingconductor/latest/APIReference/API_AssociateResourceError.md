---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_AssociateResourceError.html
---

# AssociateResourceError
<a name="API_AssociateResourceError"></a>

A representation of a resource association error.

## Contents
<a name="API_AssociateResourceError_Contents"></a>

 ** Message **   <a name="billingconductor-Type-AssociateResourceError-Message"></a>
The reason why the resource association failed.
Type: String
Required: No

 ** Reason **   <a name="billingconductor-Type-AssociateResourceError-Reason"></a>
A static error code that's used to classify the type of failure.
Type: String
Valid Values: `INVALID_ARN | SERVICE_LIMIT_EXCEEDED | ILLEGAL_CUSTOMLINEITEM | INTERNAL_SERVER_EXCEPTION | INVALID_BILLING_PERIOD_RANGE`
Required: No

## See Also
<a name="API_AssociateResourceError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/AssociateResourceError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/AssociateResourceError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/AssociateResourceError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing Conductor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query billingconductor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
