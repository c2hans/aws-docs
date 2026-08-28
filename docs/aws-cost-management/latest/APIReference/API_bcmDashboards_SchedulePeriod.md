---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_bcmDashboards_SchedulePeriod.html
---

# SchedulePeriod
<a name="API_bcmDashboards_SchedulePeriod"></a>

Defines the active time period for execution of the scheduled report.

## Contents
<a name="API_bcmDashboards_SchedulePeriod_Contents"></a>

 ** endTime **   <a name="awscostmanagement-Type-bcmDashboards_SchedulePeriod-endTime"></a>
The end time of the schedule period. If not specified, defaults to 3 years from the time of the create or update request. The maximum allowed value is 3 years from the current time. Setting an end time beyond this limit returns a `ValidationException`.
Type: Timestamp
Required: No

 ** startTime **   <a name="awscostmanagement-Type-bcmDashboards_SchedulePeriod-startTime"></a>
The start time of the schedule period. If not specified, defaults to the time of the create or update request. The start time cannot be more than 5 minutes before the time of the request.
Type: Timestamp
Required: No

## See Also
<a name="API_bcmDashboards_SchedulePeriod_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-dashboards-2025-08-18/SchedulePeriod)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-dashboards-2025-08-18/SchedulePeriod)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-dashboards-2025-08-18/SchedulePeriod)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
