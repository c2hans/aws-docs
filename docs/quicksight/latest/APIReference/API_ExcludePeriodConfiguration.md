---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ExcludePeriodConfiguration.html
---

# ExcludePeriodConfiguration
<a name="API_ExcludePeriodConfiguration"></a>

The exclude period of `TimeRangeFilter` or `RelativeDatesFilter`.

## Contents
<a name="API_ExcludePeriodConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Amount **   <a name="QS-Type-ExcludePeriodConfiguration-Amount"></a>
The amount or number of the exclude period.
Type: Integer
Required: Yes

 ** Granularity **   <a name="QS-Type-ExcludePeriodConfiguration-Granularity"></a>
The granularity or unit (day, month, year) of the exclude period.
Type: String
Valid Values: `YEAR | QUARTER | MONTH | WEEK | DAY | HOUR | MINUTE | SECOND | MILLISECOND`
Required: Yes

 ** Status **   <a name="QS-Type-ExcludePeriodConfiguration-Status"></a>
The status of the exclude period. Choose from the following options:
+  `ENABLED`
+  `DISABLED`
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_ExcludePeriodConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ExcludePeriodConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ExcludePeriodConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ExcludePeriodConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
