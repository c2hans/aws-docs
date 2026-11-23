---
source_url: https://docs.aws.amazon.com/agent-discovery/latest/APIReference/API_PublicRecord.html
---

# PublicRecord

A public record returned by a search. Only the record's public descriptors are included.

## Contents
<a name="API_PublicRecord_Contents"></a>

 ** displayName **   <a name="agentdiscovery-Type-PublicRecord-displayName"></a>
The display name of the record.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** identifier **   <a name="agentdiscovery-Type-PublicRecord-identifier"></a>
The identifier of the record.
Type: [Identifier](API_Identifier.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** recordType **   <a name="agentdiscovery-Type-PublicRecord-recordType"></a>
The kind of resource the record describes, such as an agent, a tool, or a skill.
Type: String
Valid Values: `AGENT | TOOL | SKILL | CUSTOM | GATEWAY | WEB_BOT`
Required: Yes

 ** createdAt **   <a name="agentdiscovery-Type-PublicRecord-createdAt"></a>
The time when the record was created.
Type: Timestamp
Required: No

 ** description **   <a name="agentdiscovery-Type-PublicRecord-description"></a>
A description of the record.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** descriptors **   <a name="agentdiscovery-Type-PublicRecord-descriptors"></a>
The public descriptors of the record, keyed by descriptor type. This value is absent for a record discovered at a partner source.
Type: String to [DescriptorEntry](API_DescriptorEntry.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 32 items.
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** domain **   <a name="agentdiscovery-Type-PublicRecord-domain"></a>
The verified domain of the record's publisher.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `(?=.{1,253}$)([a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,63}`
Required: No

 ** recordVersion **   <a name="agentdiscovery-Type-PublicRecord-recordVersion"></a>
The version of the record, set by its publisher. This value is absent when the record has no version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** trustManifests **   <a name="agentdiscovery-Type-PublicRecord-trustManifests"></a>
Trust metadata about the record. Each manifest names a contributor and states how that contributor obtained the record. Manifests are not signed; they attribute a claim to the contributor but don't authenticate it. This value is absent when the source of the record can't be named.
Type: Array of [TrustManifest](API_TrustManifest.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** updatedAt **   <a name="agentdiscovery-Type-PublicRecord-updatedAt"></a>
The time when the record was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_PublicRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-discovery-2022-07-26/PublicRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-discovery-2022-07-26/PublicRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-discovery-2022-07-26/PublicRecord)
