---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ComplianceItemEntry.html
---

# ComplianceItemEntry
<a name="API_ComplianceItemEntry"></a>

Information about a compliance item.

## Contents
<a name="API_ComplianceItemEntry_Contents"></a>

 ** Severity **   <a name="systemsmanager-Type-ComplianceItemEntry-Severity"></a>
The severity of the compliance status. Severity can be one of the following: Critical, High, Medium, Low, Informational, Unspecified.
Type: String
Valid Values: `CRITICAL | HIGH | MEDIUM | LOW | INFORMATIONAL | UNSPECIFIED`
Required: Yes

 ** Status **   <a name="systemsmanager-Type-ComplianceItemEntry-Status"></a>
The status of the compliance item. An item is either COMPLIANT or NON\_COMPLIANT.
Type: String
Valid Values: `COMPLIANT | NON_COMPLIANT`
Required: Yes

 ** Details **   <a name="systemsmanager-Type-ComplianceItemEntry-Details"></a>
A "Key": "Value" tag combination for the compliance item.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Value Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** Id **   <a name="systemsmanager-Type-ComplianceItemEntry-Id"></a>
The compliance item ID. For example, if the compliance item is a Windows patch, the ID could be the number of the KB article.
Type: String
Required: No

 ** Title **   <a name="systemsmanager-Type-ComplianceItemEntry-Title"></a>
The title of the compliance item. For example, if the compliance item is a Windows patch, the title could be the title of the KB article for the patch; for example: Security Update for Active Directory Federation Services.
Type: String
Length Constraints: Maximum length of 500.
Required: No

## See Also
<a name="API_ComplianceItemEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ComplianceItemEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ComplianceItemEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ComplianceItemEntry)
