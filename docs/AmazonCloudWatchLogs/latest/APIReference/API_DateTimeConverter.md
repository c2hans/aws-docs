---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DateTimeConverter.html
---

# DateTimeConverter
<a name="API_DateTimeConverter"></a>

This processor converts a datetime string into a format that you specify.

For more information about this processor including examples, see [ datetimeConverter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-datetimeConverter) in the *CloudWatch Logs User Guide*.

## Contents
<a name="API_DateTimeConverter_Contents"></a>

 ** matchPatterns **   <a name="CWL-Type-DateTimeConverter-matchPatterns"></a>
A list of patterns to match against the `source` field.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1.
Required: Yes

 ** source **   <a name="CWL-Type-DateTimeConverter-source"></a>
The key to apply the date conversion to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** target **   <a name="CWL-Type-DateTimeConverter-target"></a>
The JSON field to store the result in.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** locale **   <a name="CWL-Type-DateTimeConverter-locale"></a>
The locale of the source field. If you omit this, the default of `locale.ROOT` is used.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** sourceTimezone **   <a name="CWL-Type-DateTimeConverter-sourceTimezone"></a>
The time zone of the source field. If you omit this, the default used is the UTC zone.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** targetFormat **   <a name="CWL-Type-DateTimeConverter-targetFormat"></a>
The datetime format to use for the converted data in the target field.
If you omit this, the default of ` yyyy-MM-dd'T'HH:mm:ss.SSS'Z` is used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** targetTimezone **   <a name="CWL-Type-DateTimeConverter-targetTimezone"></a>
The time zone of the target field. If you omit this, the default used is the UTC zone.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_DateTimeConverter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/DateTimeConverter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/DateTimeConverter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/DateTimeConverter)
