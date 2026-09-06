---
source_url: https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_AccessControlEntry.html
---

# AccessControlEntry
<a name="API_AccessControlEntry"></a>

 An access control entry allows or denies Active Directory groups based on their security identifiers (SIDs) from enrolling and/or autoenrolling with the template.

## Contents
<a name="API_AccessControlEntry_Contents"></a>

 ** AccessRights **   <a name="PcaConnectorAd-Type-AccessControlEntry-AccessRights"></a>
Permissions to allow or deny an Active Directory group to enroll or autoenroll certificates issued against a template.
Type: [AccessRights](API_AccessRights.md) object
Required: No

 ** CreatedAt **   <a name="PcaConnectorAd-Type-AccessControlEntry-CreatedAt"></a>
The date and time that the Access Control Entry was created.
Type: Timestamp
Required: No

 ** GroupDisplayName **   <a name="PcaConnectorAd-Type-AccessControlEntry-GroupDisplayName"></a>
Name of the Active Directory group. This name does not need to match the group name in Active Directory.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\x20-\x7E]+`
Required: No

 ** GroupSecurityIdentifier **   <a name="PcaConnectorAd-Type-AccessControlEntry-GroupSecurityIdentifier"></a>
Security identifier (SID) of the group object from Active Directory. The SID starts with "S-".
Type: String
Length Constraints: Minimum length of 7. Maximum length of 256.
Pattern: `S-[0-9]-([0-9]+-){1,14}[0-9]+`
Required: No

 ** TemplateArn **   <a name="PcaConnectorAd-Type-AccessControlEntry-TemplateArn"></a>
The Amazon Resource Name (ARN) that was returned when you called [CreateTemplate](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html).
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w-]+:pca-connector-ad:[\w-]+:[0-9]+:connector\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}\/template\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}`
Required: No

 ** UpdatedAt **   <a name="PcaConnectorAd-Type-AccessControlEntry-UpdatedAt"></a>
The date and time that the Access Control Entry was updated.
Type: Timestamp
Required: No

## See Also
<a name="API_AccessControlEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-ad-2018-05-10/AccessControlEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-ad-2018-05-10/AccessControlEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-ad-2018-05-10/AccessControlEntry)
