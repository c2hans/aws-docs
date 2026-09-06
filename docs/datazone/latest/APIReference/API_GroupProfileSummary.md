---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_GroupProfileSummary.html
---

# GroupProfileSummary
<a name="API_GroupProfileSummary"></a>

The details of a group profile.

## Contents
<a name="API_GroupProfileSummary_Contents"></a>

 ** domainId **   <a name="datazone-Type-GroupProfileSummary-domainId"></a>
The ID of the Amazon DataZone domain of a group profile.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: No

 ** groupName **   <a name="datazone-Type-GroupProfileSummary-groupName"></a>
The group name of a group profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[a-zA-Z_0-9+=,.@-]+`
Required: No

 ** id **   <a name="datazone-Type-GroupProfileSummary-id"></a>
The ID of a group profile.
Type: String
Pattern: `([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}`
Required: No

 ** rolePrincipalArn **   <a name="datazone-Type-GroupProfileSummary-rolePrincipalArn"></a>
The ARN of the IAM role principal. This role is associated with the group profile.
Type: String
Required: No

 ** rolePrincipalId **   <a name="datazone-Type-GroupProfileSummary-rolePrincipalId"></a>
The unique identifier of the IAM role principal. This principal is associated with the group profile.
Type: String
Required: No

 ** status **   <a name="datazone-Type-GroupProfileSummary-status"></a>
The status of a group profile.
Type: String
Valid Values: `ASSIGNED | NOT_ASSIGNED`
Required: No

## See Also
<a name="API_GroupProfileSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/GroupProfileSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/GroupProfileSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/GroupProfileSummary)
