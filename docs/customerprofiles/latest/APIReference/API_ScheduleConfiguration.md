---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ScheduleConfiguration.html
---

# ScheduleConfiguration
<a name="API_connect-customer-profiles_ScheduleConfiguration"></a>

Configuration for scheduled segment membership event notifications.

## Contents
<a name="API_connect-customer-profiles_ScheduleConfiguration_Contents"></a>

 ** Interval **   <a name="connect-Type-connect-customer-profiles_ScheduleConfiguration-Interval"></a>
The interval between scheduled executions.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 24.
Required: Yes

 ** Unit **   <a name="connect-Type-connect-customer-profiles_ScheduleConfiguration-Unit"></a>
The unit for the interval. The following are valid values:
+  **HOURLY**: The interval is measured in hours.
Type: String
Valid Values: `HOURLY`
Required: No

## See Also
<a name="API_connect-customer-profiles_ScheduleConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/ScheduleConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/ScheduleConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/ScheduleConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
