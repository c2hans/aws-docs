---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_OmniDashboardSummary.html
---

# OmniDashboardSummary
<a name="API_OmniDashboardSummary"></a>

Summary of a dashboard. Call GetOmniDashboard for the full dashboard.

## Contents
<a name="API_OmniDashboardSummary_Contents"></a>

 ** arn **   <a name="cloudwatchomni-Type-OmniDashboardSummary-arn"></a>
The Amazon Resource Name (ARN) of the dashboard.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.+`
Required: Yes

 ** createdAt **   <a name="cloudwatchomni-Type-OmniDashboardSummary-createdAt"></a>
The timestamp when the dashboard was created.
Type: Timestamp
Required: Yes

 ** createdBy **   <a name="cloudwatchomni-Type-OmniDashboardSummary-createdBy"></a>
The principal that created the dashboard.
Type: String
Required: Yes

 ** dashboardId **   <a name="cloudwatchomni-Type-OmniDashboardSummary-dashboardId"></a>
The unique ID of the dashboard.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** name **   <a name="cloudwatchomni-Type-OmniDashboardSummary-name"></a>
A name that identifies the dashboard.
Type: String
Required: Yes

 ** updatedAt **   <a name="cloudwatchomni-Type-OmniDashboardSummary-updatedAt"></a>
The timestamp when the dashboard was last updated.
Type: Timestamp
Required: Yes

 ** description **   <a name="cloudwatchomni-Type-OmniDashboardSummary-description"></a>
An optional description of the dashboard.
Type: String
Required: No

 ** tags **   <a name="cloudwatchomni-Type-OmniDashboardSummary-tags"></a>
The tags associated with the dashboard.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_OmniDashboardSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/OmniDashboardSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/OmniDashboardSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/OmniDashboardSummary)
