---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_OmniDashboard.html
---

# OmniDashboard
<a name="API_OmniDashboard"></a>

A dashboard within a space, including its body.

## Contents
<a name="API_OmniDashboard_Contents"></a>

 ** arn **   <a name="cloudwatchomni-Type-OmniDashboard-arn"></a>
The Amazon Resource Name (ARN) of the dashboard.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:.+`
Required: Yes

 ** body **   <a name="cloudwatchomni-Type-OmniDashboard-body"></a>
The dashboard definition.
Type: String
Required: Yes

 ** createdAt **   <a name="cloudwatchomni-Type-OmniDashboard-createdAt"></a>
The timestamp when the dashboard was created.
Type: Timestamp
Required: Yes

 ** createdBy **   <a name="cloudwatchomni-Type-OmniDashboard-createdBy"></a>
The principal that created the dashboard.
Type: String
Required: Yes

 ** dashboardId **   <a name="cloudwatchomni-Type-OmniDashboard-dashboardId"></a>
The unique ID of the dashboard.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** name **   <a name="cloudwatchomni-Type-OmniDashboard-name"></a>
A name that identifies the dashboard.
Type: String
Required: Yes

 ** updatedAt **   <a name="cloudwatchomni-Type-OmniDashboard-updatedAt"></a>
The timestamp when the dashboard was last updated.
Type: Timestamp
Required: Yes

 ** description **   <a name="cloudwatchomni-Type-OmniDashboard-description"></a>
An optional description of the dashboard.
Type: String
Required: No

 ** tags **   <a name="cloudwatchomni-Type-OmniDashboard-tags"></a>
The tags associated with the dashboard.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_OmniDashboard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/OmniDashboard)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/OmniDashboard)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/OmniDashboard)
