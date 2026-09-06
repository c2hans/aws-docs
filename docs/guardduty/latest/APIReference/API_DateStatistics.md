---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DateStatistics.html
---

# DateStatistics
<a name="API_DateStatistics"></a>

Represents list a map of dates with a count of total findings generated on each date.

## Contents
<a name="API_DateStatistics_Contents"></a>

 ** date **   <a name="guardduty-Type-DateStatistics-date"></a>
The timestamp when the total findings count is observed.
For example, `Date` would look like `"2024-09-05T17:00:00-07:00"` whereas `LastGeneratedAt` would look like 2024-09-05T17:12:29-07:00".
Type: Timestamp
Required: No

 ** lastGeneratedAt **   <a name="guardduty-Type-DateStatistics-lastGeneratedAt"></a>
The timestamp at which the last finding in the findings count, was generated.
Type: Timestamp
Required: No

 ** severity **   <a name="guardduty-Type-DateStatistics-severity"></a>
The severity of the findings generated on each date.
Type: Double
Required: No

 ** totalFindings **   <a name="guardduty-Type-DateStatistics-totalFindings"></a>
The total number of findings that were generated per severity level on each date.
Type: Integer
Required: No

## See Also
<a name="API_DateStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/DateStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/DateStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/DateStatistics)
