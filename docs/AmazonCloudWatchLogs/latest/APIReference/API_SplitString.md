---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_SplitString.html
---

# SplitString
<a name="API_SplitString"></a>

Use this processor to split a field into an array of strings using a delimiting character.

For more information about this processor including examples, see [ splitString](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-splitString) in the *CloudWatch Logs User Guide*.

## Contents
<a name="API_SplitString_Contents"></a>

 ** entries **   <a name="CWL-Type-SplitString-entries"></a>
An array of `SplitStringEntry` objects, where each object contains the information about one field to split.
Type: Array of [SplitStringEntry](API_SplitStringEntry.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

## See Also
<a name="API_SplitString_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/SplitString)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/SplitString)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/SplitString)
