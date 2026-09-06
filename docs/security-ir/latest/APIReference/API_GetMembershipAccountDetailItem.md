---
source_url: https://docs.aws.amazon.com/security-ir/latest/APIReference/API_GetMembershipAccountDetailItem.html
---

# GetMembershipAccountDetailItem
<a name="API_GetMembershipAccountDetailItem"></a>

## Contents
<a name="API_GetMembershipAccountDetailItem_Contents"></a>

 ** accountId **   <a name="securityir-Type-GetMembershipAccountDetailItem-accountId"></a>

Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** relationshipStatus **   <a name="securityir-Type-GetMembershipAccountDetailItem-relationshipStatus"></a>

Type: String
Valid Values: `Associated | Disassociated | Unassociated`
Required: No

 ** relationshipType **   <a name="securityir-Type-GetMembershipAccountDetailItem-relationshipType"></a>

Type: String
Valid Values: `Organization | Unrelated`
Required: No

## See Also
<a name="API_GetMembershipAccountDetailItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/security-ir-2018-05-10/GetMembershipAccountDetailItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/security-ir-2018-05-10/GetMembershipAccountDetailItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/security-ir-2018-05-10/GetMembershipAccountDetailItem)
