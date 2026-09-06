---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DashboardSummary.html
---

# DashboardSummary
<a name="API_DashboardSummary"></a>

Contains a dashboard summary.

## Contents
<a name="API_DashboardSummary_Contents"></a>

 ** id **   <a name="iotsitewise-Type-DashboardSummary-id"></a>
The ID of the dashboard.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** name **   <a name="iotsitewise-Type-DashboardSummary-name"></a>
The name of the dashboard
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** creationDate **   <a name="iotsitewise-Type-DashboardSummary-creationDate"></a>
The date the dashboard was created, in Unix epoch time.
Type: Timestamp
Required: No

 ** description **   <a name="iotsitewise-Type-DashboardSummary-description"></a>
The dashboard's description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: No

 ** lastUpdateDate **   <a name="iotsitewise-Type-DashboardSummary-lastUpdateDate"></a>
The date the dashboard was last updated, in Unix epoch time.
Type: Timestamp
Required: No

## See Also
<a name="API_DashboardSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DashboardSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DashboardSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DashboardSummary)
