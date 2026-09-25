---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_TemplateSummary.html
---

# TemplateSummary
<a name="API_TemplateSummary"></a>

Summary information about a template.

## Contents
<a name="API_TemplateSummary_Contents"></a>

 ** templateArn **   <a name="networksecuritymanager-Type-TemplateSummary-templateArn"></a>
The Amazon Resource Name (ARN) of the template.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1010.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:(.+)`
Required: Yes

 ** templateId **   <a name="networksecuritymanager-Type-TemplateSummary-templateId"></a>
The service-generated id of the template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]{1,64}`
Required: Yes

 ** templateName **   <a name="networksecuritymanager-Type-TemplateSummary-templateName"></a>
The name of the template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9 _.:/=+\-@]*`
Required: Yes

 ** firewallType **   <a name="networksecuritymanager-Type-TemplateSummary-firewallType"></a>
The firewall type associated with the resource.
Type: String
Valid Values: `WAF`
Required: No

 ** hasPublishedVersion **   <a name="networksecuritymanager-Type-TemplateSummary-hasPublishedVersion"></a>
Specifies whether a published version of the resource exists.
Type: Boolean
Required: No

 ** status **   <a name="networksecuritymanager-Type-TemplateSummary-status"></a>
The current status of the resource: `DRAFT` (unpublished, editable) or `ACTIVE` (published, in use).
Type: String
Valid Values: `DRAFT | ACTIVE | DISABLED`
Required: No

 ** updatedAt **   <a name="networksecuritymanager-Type-TemplateSummary-updatedAt"></a>
The time when the resource was last updated. For a snapshot, this is the time when the snapshot was created.
Type: Timestamp
Required: No

 ** version **   <a name="networksecuritymanager-Type-TemplateSummary-version"></a>
The version of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `[1-9][0-9]*`
Required: No

## See Also
<a name="API_TemplateSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/TemplateSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/TemplateSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/TemplateSummary)
