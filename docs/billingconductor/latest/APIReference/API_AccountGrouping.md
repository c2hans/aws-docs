---
source_url: https://docs.aws.amazon.com/billingconductor/latest/APIReference/API_AccountGrouping.html
---

# AccountGrouping
<a name="API_AccountGrouping"></a>

The set of accounts that will be under the billing group. The set of accounts resemble the linked accounts in a consolidated billing family.

## Contents
<a name="API_AccountGrouping_Contents"></a>

 ** AutoAssociate **   <a name="billingconductor-Type-AccountGrouping-AutoAssociate"></a>
Specifies if this billing group will automatically associate newly added AWS accounts that join your consolidated billing family.
Type: Boolean
Required: No

 ** LinkedAccountIds **   <a name="billingconductor-Type-AccountGrouping-LinkedAccountIds"></a>
The account IDs that make up the billing group. Account IDs must be a part of the consolidated billing family, and not associated with another billing group.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 30 items.
Pattern: `[0-9]{12}`
Required: No

 ** ResponsibilityTransferArn **   <a name="billingconductor-Type-AccountGrouping-ResponsibilityTransferArn"></a>
 The Amazon Resource Name (ARN) that identifies the transfer relationship owned by the Bill Transfer account (caller account). When specified, the PrimaryAccountId is no longer required.
Type: String
Pattern: `arn:[a-z0-9][a-z0-9-.]{0,62}:organizations::\d{12}:transfer/o-[a-z0-9]{10,32}/(billing)/(inbound|outbound)/rt-[0-9a-z]{8,32}`
Required: No

## See Also
<a name="API_AccountGrouping_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/billingconductor-2021-07-30/AccountGrouping)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/billingconductor-2021-07-30/AccountGrouping)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/billingconductor-2021-07-30/AccountGrouping)
