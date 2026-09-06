---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_Entitlement.html
---

# Entitlement
<a name="API_Entitlement"></a>

 The settings for a flow entitlement.

## Contents
<a name="API_Entitlement_Contents"></a>

 ** entitlementArn **   <a name="mediaconnect-Type-Entitlement-entitlementArn"></a>
 The ARN of the entitlement.
Type: String
Required: Yes

 ** name **   <a name="mediaconnect-Type-Entitlement-name"></a>
 The name of the entitlement.
Type: String
Required: Yes

 ** subscribers **   <a name="mediaconnect-Type-Entitlement-subscribers"></a>
 The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flow using your content as the source.
Type: Array of strings
Required: Yes

 ** dataTransferSubscriberFeePercent **   <a name="mediaconnect-Type-Entitlement-dataTransferSubscriberFeePercent"></a>
 Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
Type: Integer
Required: No

 ** description **   <a name="mediaconnect-Type-Entitlement-description"></a>
 A description of the entitlement.
Type: String
Required: No

 ** encryption **   <a name="mediaconnect-Type-Entitlement-encryption"></a>
 The type of encryption that will be used on the output that is associated with this entitlement.
Type: [Encryption](API_Encryption.md) object
Required: No

 ** entitlementStatus **   <a name="mediaconnect-Type-Entitlement-entitlementStatus"></a>
 An indication of whether the entitlement is enabled.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_Entitlement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/Entitlement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/Entitlement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/Entitlement)
