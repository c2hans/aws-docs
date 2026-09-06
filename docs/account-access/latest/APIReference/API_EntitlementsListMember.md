---
source_url: https://docs.aws.amazon.com/account-access/latest/APIReference/API_EntitlementsListMember.html
---

# EntitlementsListMember
<a name="API_EntitlementsListMember"></a>

Contains information about an entitlement in a list result.

## Contents
<a name="API_EntitlementsListMember_Contents"></a>

 ** createdAt **   <a name="accountaccess-Type-EntitlementsListMember-createdAt"></a>
The date and time when the entitlement was created.
Type: Timestamp
Required: Yes

 ** entitlement **   <a name="accountaccess-Type-EntitlementsListMember-entitlement"></a>
The summary information for the entitlement.
Type: [EntitlementSummary](API_EntitlementSummary.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** entitlementId **   <a name="accountaccess-Type-EntitlementsListMember-entitlementId"></a>
The unique identifier of the entitlement.
Type: String
Required: Yes

## See Also
<a name="API_EntitlementsListMember_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/account-access-2018-05-10/EntitlementsListMember)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/account-access-2018-05-10/EntitlementsListMember)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/account-access-2018-05-10/EntitlementsListMember)
