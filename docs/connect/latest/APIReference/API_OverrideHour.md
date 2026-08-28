---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_OverrideHour.html
---

# OverrideHour
<a name="API_OverrideHour"></a>

Information about hours of operation override

## Contents
<a name="API_OverrideHour_Contents"></a>

 ** End **   <a name="connect-Type-OverrideHour-End"></a>
The start time or end time for an hours of operation override.
Type: [OverrideTimeSlice](API_OverrideTimeSlice.md) object
Required: No

 ** OperationalStatus **   <a name="connect-Type-OverrideHour-OperationalStatus"></a>
Indicates whether the status is open or closed during the override period. This status determines how the override modifies the base hours of operation schedule.
Type: String
Valid Values: `OPEN | CLOSED`
Required: No

 ** OverrideName **   <a name="connect-Type-OverrideHour-OverrideName"></a>
Unique identifier name for the override.
Type: String
Pattern: `^[\P{C}\r\n\t]{1,127}$`
Required: No

 ** Start **   <a name="connect-Type-OverrideHour-Start"></a>
The start time or end time for an hours of operation override.
Type: [OverrideTimeSlice](API_OverrideTimeSlice.md) object
Required: No

## See Also
<a name="API_OverrideHour_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/OverrideHour)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/OverrideHour)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/OverrideHour)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
