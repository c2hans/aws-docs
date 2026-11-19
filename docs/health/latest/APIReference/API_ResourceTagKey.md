---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_ResourceTagKey.html
---

# ResourceTagKey

A resource tag key configured for Health event tracking.

## Contents
<a name="API_ResourceTagKey_Contents"></a>

 ** enabledForEventBridge **   <a name="AWSHealth-Type-ResourceTagKey-enabledForEventBridge"></a>
Whether this tag key is enabled for EventBridge notifications.
Type: Boolean
Required: No

 ** key **   <a name="AWSHealth-Type-ResourceTagKey-key"></a>
The tag key name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[a-zA-Z0-9 _.:\/=+\-@]{1,127}`
Required: No

 ** status **   <a name="AWSHealth-Type-ResourceTagKey-status"></a>
The current status of the tag key configuration.
Type: String
Valid Values: `PENDING | ACTIVE`
Required: No

## See Also
<a name="API_ResourceTagKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/ResourceTagKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/ResourceTagKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/ResourceTagKey)
