---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_SubstituteString.html
---

# SubstituteString
<a name="API_SubstituteString"></a>

This processor matches a key’s value against a regular expression and replaces all matches with a replacement string.

For more information about this processor including examples, see [ substituteString](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-substituteString) in the *CloudWatch Logs User Guide*.

## Contents
<a name="API_SubstituteString_Contents"></a>

 ** entries **   <a name="CWL-Type-SubstituteString-entries"></a>
An array of objects, where each object contains the information about one key to match and replace.
Type: Array of [SubstituteStringEntry](API_SubstituteStringEntry.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

## See Also
<a name="API_SubstituteString_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/SubstituteString)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/SubstituteString)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/SubstituteString)
