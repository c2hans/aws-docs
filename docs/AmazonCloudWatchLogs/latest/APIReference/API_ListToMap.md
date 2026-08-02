---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListToMap.html
---

# ListToMap
<a name="API_ListToMap"></a>

This processor takes a list of objects that contain key fields, and converts them into a map of target keys.

For more information about this processor including examples, see [ listToMap](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation-Processors.html#CloudWatch-Logs-Transformation-listToMap) in the *CloudWatch Logs User Guide*.

## Contents
<a name="API_ListToMap_Contents"></a>

 ** key **   <a name="CWL-Type-ListToMap-key"></a>
The key of the field to be extracted as keys in the generated map
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** source **   <a name="CWL-Type-ListToMap-source"></a>
The key in the log event that has a list of objects that will be converted to a map.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** flatten **   <a name="CWL-Type-ListToMap-flatten"></a>
A Boolean value to indicate whether the list will be flattened into single items. Specify `true` to flatten the list. The default is `false`
Type: Boolean
Required: No

 ** flattenedElement **   <a name="CWL-Type-ListToMap-flattenedElement"></a>
If you set `flatten` to `true`, use `flattenedElement` to specify which element, `first` or `last`, to keep.
You must specify this parameter if `flatten` is `true`
Type: String
Valid Values: `first | last`
Required: No

 ** target **   <a name="CWL-Type-ListToMap-target"></a>
The key of the field that will hold the generated map
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** valueKey **   <a name="CWL-Type-ListToMap-valueKey"></a>
If this is specified, the values that you specify in this parameter will be extracted from the `source` objects and put into the values of the generated map. Otherwise, original objects in the source list will be put into the values of the generated map.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_ListToMap_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/ListToMap)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/ListToMap)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/ListToMap)
