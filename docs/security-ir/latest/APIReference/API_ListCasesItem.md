---
source_url: https://docs.aws.amazon.com/security-ir/latest/APIReference/API_ListCasesItem.html
---

# ListCasesItem
<a name="API_ListCasesItem"></a>

## Contents
<a name="API_ListCasesItem_Contents"></a>

 ** caseId **   <a name="securityir-Type-ListCasesItem-caseId"></a>

Type: String
Length Constraints: Minimum length of 10. Maximum length of 32.
Pattern: `\d{10,32}.*`
Required: Yes

 ** caseArn **   <a name="securityir-Type-ListCasesItem-caseArn"></a>

Type: String
Length Constraints: Minimum length of 12. Maximum length of 80.
Pattern: `arn:aws:security-ir:\w+?-\w+?-\d+:[0-9]{12}:case/[0-9]{10}`
Required: No

 ** caseStatus **   <a name="securityir-Type-ListCasesItem-caseStatus"></a>

Type: String
Valid Values: `Submitted | Acknowledged | Detection and Analysis | Containment, Eradication and Recovery | Post-incident Activities | Ready to Close | Closed`
Required: No

 ** closedDate **   <a name="securityir-Type-ListCasesItem-closedDate"></a>

Type: Timestamp
Required: No

 ** createdDate **   <a name="securityir-Type-ListCasesItem-createdDate"></a>

Type: Timestamp
Required: No

 ** engagementType **   <a name="securityir-Type-ListCasesItem-engagementType"></a>

Type: String
Valid Values: `Security Incident | Investigation`
Required: No

 ** lastUpdatedDate **   <a name="securityir-Type-ListCasesItem-lastUpdatedDate"></a>

Type: Timestamp
Required: No

 ** pendingAction **   <a name="securityir-Type-ListCasesItem-pendingAction"></a>

Type: String
Valid Values: `Customer | None`
Required: No

 ** resolverType **   <a name="securityir-Type-ListCasesItem-resolverType"></a>

Type: String
Valid Values: `AWS | Self`
Required: No

 ** title **   <a name="securityir-Type-ListCasesItem-title"></a>

Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: No

## See Also
<a name="API_ListCasesItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/security-ir-2018-05-10/ListCasesItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/security-ir-2018-05-10/ListCasesItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/security-ir-2018-05-10/ListCasesItem)
