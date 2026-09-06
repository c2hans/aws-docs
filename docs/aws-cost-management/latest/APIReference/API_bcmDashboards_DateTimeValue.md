---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_DateTimeValue.html
---

# DateTimeValue
<a name="API_bcmDashboards_DateTimeValue"></a>

Represents a point in time that can be specified as either an absolute date (for example, "2025-07-01") or a relative time period using ISO 8601 duration format (for example, "-P3M" for three months ago).

## Contents
<a name="API_bcmDashboards_DateTimeValue_Contents"></a>

 ** type **   <a name="awscostmanagement-Type-bcmDashboards_DateTimeValue-type"></a>
The type of date/time value: `ABSOLUTE` for specific dates or `RELATIVE` for dynamic time periods.
Type: String
Valid Values: `ABSOLUTE | RELATIVE`
Required: Yes

 ** value **   <a name="awscostmanagement-Type-bcmDashboards_DateTimeValue-value"></a>
The actual date/time value.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: Yes

## See Also
<a name="API_bcmDashboards_DateTimeValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-dashboards-2025-08-18/DateTimeValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-dashboards-2025-08-18/DateTimeValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-dashboards-2025-08-18/DateTimeValue)
