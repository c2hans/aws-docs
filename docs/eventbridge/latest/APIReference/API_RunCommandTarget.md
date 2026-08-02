---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_RunCommandTarget.html
---

# RunCommandTarget
<a name="API_RunCommandTarget"></a>

Information about the EC2 instances that are to be sent the command, specified as key-value pairs. Each `RunCommandTarget` block can include only one key, but this key may specify multiple values.

## Contents
<a name="API_RunCommandTarget_Contents"></a>

 ** Key **   <a name="eventbridge-Type-RunCommandTarget-Key"></a>
Can be either `tag:` *tag-key* or `InstanceIds`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Required: Yes

 ** Values **   <a name="eventbridge-Type-RunCommandTarget-Values"></a>
If `Key` is `tag:` *tag-key*, `Values` is a list of tag values. If `Key` is `InstanceIds`, `Values` is a list of Amazon EC2 instance IDs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_RunCommandTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/RunCommandTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/RunCommandTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/RunCommandTarget)
