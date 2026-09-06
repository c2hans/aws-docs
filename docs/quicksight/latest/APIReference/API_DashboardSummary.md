---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DashboardSummary.html
---

# DashboardSummary
<a name="API_DashboardSummary"></a>

Dashboard summary.

## Contents
<a name="API_DashboardSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-DashboardSummary-Arn"></a>
The Amazon Resource Name (ARN) of the resource.
Type: String
Required: No

 ** CreatedTime **   <a name="QS-Type-DashboardSummary-CreatedTime"></a>
The time that this dashboard was created.
Type: Timestamp
Required: No

 ** DashboardId **   <a name="QS-Type-DashboardSummary-DashboardId"></a>
Dashboard ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: No

 ** LastPublishedTime **   <a name="QS-Type-DashboardSummary-LastPublishedTime"></a>
The last time that this dashboard was published.
Type: Timestamp
Required: No

 ** LastUpdatedTime **   <a name="QS-Type-DashboardSummary-LastUpdatedTime"></a>
The last time that this dashboard was updated.
Type: Timestamp
Required: No

 ** Name **   <a name="QS-Type-DashboardSummary-Name"></a>
A display name for the dashboard.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** PublishedVersionNumber **   <a name="QS-Type-DashboardSummary-PublishedVersionNumber"></a>
Published version number.
Type: Long
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_DashboardSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DashboardSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DashboardSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DashboardSummary)
