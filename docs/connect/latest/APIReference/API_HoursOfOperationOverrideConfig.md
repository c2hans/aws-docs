---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_HoursOfOperationOverrideConfig.html
---

# HoursOfOperationOverrideConfig
<a name="API_HoursOfOperationOverrideConfig"></a>

Information about the hours of operation override config: day, start time, and end time.

## Contents
<a name="API_HoursOfOperationOverrideConfig_Contents"></a>

 ** Day **   <a name="connect-Type-HoursOfOperationOverrideConfig-Day"></a>
The day that the hours of operation override applies to.
Type: String
Valid Values: `SUNDAY | MONDAY | TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY`
Required: No

 ** EndTime **   <a name="connect-Type-HoursOfOperationOverrideConfig-EndTime"></a>
The end time that your contact center closes if overrides are applied.
Type: [OverrideTimeSlice](API_OverrideTimeSlice.md) object
Required: No

 ** StartTime **   <a name="connect-Type-HoursOfOperationOverrideConfig-StartTime"></a>
The start time when your contact center opens if overrides are applied.
Type: [OverrideTimeSlice](API_OverrideTimeSlice.md) object
Required: No

## See Also
<a name="API_HoursOfOperationOverrideConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/HoursOfOperationOverrideConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/HoursOfOperationOverrideConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/HoursOfOperationOverrideConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
