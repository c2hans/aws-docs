---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_BillingGroupListElement.html
---

# BillingGroupListElement
<a name="API_BillingGroupListElement"></a>

A representation of a billing group.

## Contents
<a name="API_BillingGroupListElement_Contents"></a>

 ** AccountGrouping **   <a name="billingconductor-Type-BillingGroupListElement-AccountGrouping"></a>
Specifies if the billing group has automatic account association (`AutoAssociate`) enabled.
Type: [ListBillingGroupAccountGrouping](API_ListBillingGroupAccountGrouping.md) object
Required: No

 ** Arn **   <a name="billingconductor-Type-BillingGroupListElement-Arn"></a>
The Amazon Resource Number (ARN) that can be used to uniquely identify the billing group.
Type: String
Pattern: `(arn:aws(-cn)?:billingconductor::[0-9]{12}:billinggroup/)?[a-zA-Z0-9]{10,12}`
Required: No

 ** BillingGroupType **   <a name="billingconductor-Type-BillingGroupListElement-BillingGroupType"></a>
 The type of billing group.
Type: String
Valid Values: `STANDARD | TRANSFER_BILLING`
Required: No

 ** ComputationPreference **   <a name="billingconductor-Type-BillingGroupListElement-ComputationPreference"></a>
The preferences and settings that will be used to compute the AWS charges for a billing group.
Type: [ComputationPreference](API_ComputationPreference.md) object
Required: No

 ** CreationTime **   <a name="billingconductor-Type-BillingGroupListElement-CreationTime"></a>
The time when the billing group was created.
Type: Long
Required: No

 ** Description **   <a name="billingconductor-Type-BillingGroupListElement-Description"></a>
The description of the billing group.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** LastModifiedTime **   <a name="billingconductor-Type-BillingGroupListElement-LastModifiedTime"></a>
The most recent time when the billing group was modified.
Type: Long
Required: No

 ** Name **   <a name="billingconductor-Type-BillingGroupListElement-Name"></a>
The name of the billing group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_\+=\.\-@]+`
Required: No

 ** PrimaryAccountId **   <a name="billingconductor-Type-BillingGroupListElement-PrimaryAccountId"></a>
The account ID that serves as the main account in a billing group.
Type: String
Pattern: `[0-9]{12}`
Required: No

 ** Size **   <a name="billingconductor-Type-BillingGroupListElement-Size"></a>
The number of accounts in the particular billing group.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** Status **   <a name="billingconductor-Type-BillingGroupListElement-Status"></a>
The billing group status. Only one of the valid values can be used.
Type: String
Valid Values: `ACTIVE | PRIMARY_ACCOUNT_MISSING | PENDING`
Required: No

 ** StatusReason **   <a name="billingconductor-Type-BillingGroupListElement-StatusReason"></a>
The reason why the billing group is in its current status.
Type: String
Required: No

## See Also
<a name="API_BillingGroupListElement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/BillingGroupListElement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/BillingGroupListElement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/BillingGroupListElement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing Conductor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query billingconductor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
