---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_AccountAssociationsListElement.html
---

# AccountAssociationsListElement
<a name="API_AccountAssociationsListElement"></a>

A representation of a linked account.

## Contents
<a name="API_AccountAssociationsListElement_Contents"></a>

 ** AccountEmail **   <a name="billingconductor-Type-AccountAssociationsListElement-AccountEmail"></a>
The AWS account email.
Type: String
Required: No

 ** AccountId **   <a name="billingconductor-Type-AccountAssociationsListElement-AccountId"></a>
The associating array of account IDs.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** AccountName **   <a name="billingconductor-Type-AccountAssociationsListElement-AccountName"></a>
The AWS account name.
Type: String
Required: No

 ** BillingGroupArn **   <a name="billingconductor-Type-AccountAssociationsListElement-BillingGroupArn"></a>
The Billing Group Arn that the linked account is associated to.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:billinggroup/)?[a-zA-Z0-9]{10,12}`
Required: No

## See Also
<a name="API_AccountAssociationsListElement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/AccountAssociationsListElement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/AccountAssociationsListElement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/AccountAssociationsListElement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing Conductor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query billingconductor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
