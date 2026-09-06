---
source_url: https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_ProtectionGroupLimits.html
---

# ProtectionGroupLimits
<a name="API_ProtectionGroupLimits"></a>

Limits settings on protection groups for your subscription.

## Contents
<a name="API_ProtectionGroupLimits_Contents"></a>

 ** MaxProtectionGroups **   <a name="AWSShield-Type-ProtectionGroupLimits-MaxProtectionGroups"></a>
The maximum number of protection groups that you can have at one time.
Type: Long
Required: Yes

 ** PatternTypeLimits **   <a name="AWSShield-Type-ProtectionGroupLimits-PatternTypeLimits"></a>
Limits settings by pattern type in the protection groups for your subscription.
Type: [ProtectionGroupPatternTypeLimits](API_ProtectionGroupPatternTypeLimits.md) object
Required: Yes

## See Also
<a name="API_ProtectionGroupLimits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/ProtectionGroupLimits)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/ProtectionGroupLimits)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/ProtectionGroupLimits)
