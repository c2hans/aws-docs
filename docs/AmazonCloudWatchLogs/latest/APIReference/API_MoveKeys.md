---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_MoveKeys.html
---

# MoveKeys
<a name="API_MoveKeys"></a>

This processor moves a key from one field to another. The original key is deleted.

For more information about this processor including examples, see [ moveKeys](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-moveKeys) in the *CloudWatch Logs User Guide*.

## Contents
<a name="API_MoveKeys_Contents"></a>

 ** entries **   <a name="CWL-Type-MoveKeys-entries"></a>
An array of objects, where each object contains the information about one key to move.
Type: Array of [MoveKeyEntry](API_MoveKeyEntry.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: Yes

## See Also
<a name="API_MoveKeys_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/MoveKeys)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/MoveKeys)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/MoveKeys)
