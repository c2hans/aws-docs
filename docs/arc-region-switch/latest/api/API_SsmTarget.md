---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_SsmTarget.html
---

# SsmTarget
<a name="API_SsmTarget"></a>

A single `SendCommand` target filter, consisting of a target key and the values matched by that key.

## Contents
<a name="API_SsmTarget_Contents"></a>

 ** key **   <a name="regionswitch-Type-SsmTarget-key"></a>
The target key, such as `tag:Environment` or `InstanceIds`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 163.
Pattern: `[\p{L}\p{Z}\p{N}_.:/=\-@]*`
Required: Yes

 ** values **   <a name="regionswitch-Type-SsmTarget-values"></a>
The values matched by this target key. Multiple values combine with a logical OR.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_SsmTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/SsmTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/SsmTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/SsmTarget)
