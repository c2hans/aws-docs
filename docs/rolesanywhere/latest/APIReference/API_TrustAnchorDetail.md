---
source_url: https://docs.aws.amazon.com/rolesanywhere/latest/APIReference/API_TrustAnchorDetail.html
---

# TrustAnchorDetail
<a name="API_TrustAnchorDetail"></a>

The state of the trust anchor after a read or write operation.

## Contents
<a name="API_TrustAnchorDetail_Contents"></a>

 ** aliasArn **   <a name="rolesanywhere-Type-TrustAnchorDetail-aliasArn"></a>
The alias ARN of the trust anchor, in the form `arn:partition:rolesanywhere:region:account:alias/trust-anchor/alias-name `. Present only if the trust anchor has an alias.
You can use the alias ARN in place of the resource ID or ARN in the request parameters whose descriptions say that they accept an alias ARN. Don't use the alias ARN in AWS Identity and Access Management (IAM) policies. A policy statement that names an alias ARN doesn't apply to the resource that holds the alias. Write policies with the ARN that contains the resource ID instead.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[^:]+)?:rolesanywhere(:.*){2}(:alias/trust-anchor/.*)`
Required: No

 ** aliasName **   <a name="rolesanywhere-Type-TrustAnchorDetail-aliasName"></a>
The alias of the trust anchor. Present only if the trust anchor has an alias.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(?!.*//)([A-Za-z]([A-Za-z0-9_/-]*[A-Za-z0-9_-])?)?`
Required: No

 ** createdAt **   <a name="rolesanywhere-Type-TrustAnchorDetail-createdAt"></a>
The ISO-8601 timestamp when the trust anchor was created.
Type: Timestamp
Required: No

 ** crlDpRevocationEnabled **   <a name="rolesanywhere-Type-TrustAnchorDetail-crlDpRevocationEnabled"></a>
Specifies whether the trust anchor checks certificate revocation status against CRL distribution points.
Type: Boolean
Required: No

 ** enabled **   <a name="rolesanywhere-Type-TrustAnchorDetail-enabled"></a>
Indicates whether the trust anchor is enabled.
Type: Boolean
Required: No

 ** name **   <a name="rolesanywhere-Type-TrustAnchorDetail-name"></a>
The name of the trust anchor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[ a-zA-Z0-9-_]*`
Required: No

 ** notificationSettings **   <a name="rolesanywhere-Type-TrustAnchorDetail-notificationSettings"></a>
A list of notification settings to be associated to the trust anchor.
Type: Array of [NotificationSettingDetail](API_NotificationSettingDetail.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** previousAliasName **   <a name="rolesanywhere-Type-TrustAnchorDetail-previousAliasName"></a>
The alias that the resource had before the update request. IAM Roles Anywhere returns this value only in the response to an update request that changed or removed an existing alias. It isn't returned when the alias was unchanged, when the resource had no alias before the request, or by other operations.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `(?!.*//)([A-Za-z]([A-Za-z0-9_/-]*[A-Za-z0-9_-])?)?`
Required: No

 ** source **   <a name="rolesanywhere-Type-TrustAnchorDetail-source"></a>
The trust anchor type and its related certificate data.
Type: [Source](API_Source.md) object
Required: No

 ** trustAnchorArn **   <a name="rolesanywhere-Type-TrustAnchorDetail-trustAnchorArn"></a>
The ARN of the trust anchor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[^:]+)?:rolesanywhere(:.*){2}(:trust-anchor/.*)`
Required: No

 ** trustAnchorId **   <a name="rolesanywhere-Type-TrustAnchorDetail-trustAnchorId"></a>
The unique identifier of the trust anchor.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `.*[a-f0-9]{8}-([a-z0-9]{4}-){3}[a-z0-9]{12}.*`
Required: No

 ** updatedAt **   <a name="rolesanywhere-Type-TrustAnchorDetail-updatedAt"></a>
The ISO-8601 timestamp when the trust anchor was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_TrustAnchorDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rolesanywhere-2018-05-10/TrustAnchorDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rolesanywhere-2018-05-10/TrustAnchorDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rolesanywhere-2018-05-10/TrustAnchorDetail)
