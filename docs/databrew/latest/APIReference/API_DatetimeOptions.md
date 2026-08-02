---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_DatetimeOptions.html
---

# DatetimeOptions
<a name="API_DatetimeOptions"></a>

Represents additional options for correct interpretation of datetime parameters used in the Amazon S3 path of a dataset.

## Contents
<a name="API_DatetimeOptions_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Format **   <a name="databrew-Type-DatetimeOptions-Format"></a>
Required option, that defines the datetime format used for a date parameter in the Amazon S3 path. Should use only supported datetime specifiers and separation characters, all literal a-z or A-Z characters should be escaped with single quotes. E.g. "MM.dd.yyyy-'at'-HH:mm".
Type: String
Length Constraints: Minimum length of 2. Maximum length of 100.
Required: Yes

 ** LocaleCode **   <a name="databrew-Type-DatetimeOptions-LocaleCode"></a>
Optional value for a non-US locale code, needed for correct interpretation of some date formats.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `^[A-Za-z0-9_\.#@\-]+$`
Required: No

 ** TimezoneOffset **   <a name="databrew-Type-DatetimeOptions-TimezoneOffset"></a>
Optional value for a timezone offset of the datetime parameter value in the Amazon S3 path. Shouldn't be used if Format for this parameter includes timezone fields. If no offset specified, UTC is assumed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 6.
Pattern: `^(Z|[-+](\d|\d{2}|\d{2}:?\d{2}))$`
Required: No

## See Also
<a name="API_DatetimeOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/DatetimeOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/DatetimeOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/DatetimeOptions)
