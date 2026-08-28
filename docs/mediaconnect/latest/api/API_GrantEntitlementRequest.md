---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_GrantEntitlementRequest.html
---

# GrantEntitlementRequest
<a name="API_GrantEntitlementRequest"></a>

 The entitlements that you want to grant on a flow.

## Contents
<a name="API_GrantEntitlementRequest_Contents"></a>

 ** subscribers **   <a name="mediaconnect-Type-GrantEntitlementRequest-subscribers"></a>
 The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flows using your content as the source.
Type: Array of strings
Required: Yes

 ** dataTransferSubscriberFeePercent **   <a name="mediaconnect-Type-GrantEntitlementRequest-dataTransferSubscriberFeePercent"></a>
 Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
Type: Integer
Required: No

 ** description **   <a name="mediaconnect-Type-GrantEntitlementRequest-description"></a>
 A description of the entitlement. This description appears only on the MediaConnect console and will not be seen by the subscriber or end user.
Type: String
Required: No

 ** encryption **   <a name="mediaconnect-Type-GrantEntitlementRequest-encryption"></a>
 The type of encryption that will be used on the output that is associated with this entitlement. Allowable encryption types: static-key, speke.
Type: [Encryption](API_Encryption.md) object
Required: No

 ** entitlementStatus **   <a name="mediaconnect-Type-GrantEntitlementRequest-entitlementStatus"></a>
 An indication of whether the new entitlement should be enabled or disabled as soon as it is created. If you don’t specify the entitlementStatus field in your request, MediaConnect sets it to ENABLED.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** entitlementTags **   <a name="mediaconnect-Type-GrantEntitlementRequest-entitlementTags"></a>
 The key-value pairs that can be used to tag and organize the entitlement.
Type: String to string map
Required: No

 ** name **   <a name="mediaconnect-Type-GrantEntitlementRequest-name"></a>
 The name of the entitlement. This value must be unique within the current flow.
Type: String
Required: No

## See Also
<a name="API_GrantEntitlementRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/GrantEntitlementRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/GrantEntitlementRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/GrantEntitlementRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
