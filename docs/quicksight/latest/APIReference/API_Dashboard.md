---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Dashboard.html
---

# Dashboard
<a name="API_Dashboard"></a>

Dashboard.

## Contents
<a name="API_Dashboard_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-Dashboard-Arn"></a>
The Amazon Resource Name (ARN) of the resource.
Type: String
Required: No

 ** CreatedTime **   <a name="QS-Type-Dashboard-CreatedTime"></a>
The time that this dashboard was created.
Type: Timestamp
Required: No

 ** DashboardId **   <a name="QS-Type-Dashboard-DashboardId"></a>
Dashboard ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: No

 ** LastPublishedTime **   <a name="QS-Type-Dashboard-LastPublishedTime"></a>
The last time that this dashboard was published.
Type: Timestamp
Required: No

 ** LastUpdatedTime **   <a name="QS-Type-Dashboard-LastUpdatedTime"></a>
The last time that this dashboard was updated.
Type: Timestamp
Required: No

 ** LinkEntities **   <a name="QS-Type-Dashboard-LinkEntities"></a>
A list of analysis Amazon Resource Names (ARNs) to be linked to the dashboard.
Type: Array of strings
Array Members: Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^arn:aws[\w\-]*:quicksight:[\w\-]+:\d+:analysis/[\w\-]{1,512}`
Required: No

 ** Name **   <a name="QS-Type-Dashboard-Name"></a>
A display name for the dashboard.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** Version **   <a name="QS-Type-Dashboard-Version"></a>
Version.
Type: [DashboardVersion](API_DashboardVersion.md) object
Required: No

## See Also
<a name="API_Dashboard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/Dashboard)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/Dashboard)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/Dashboard)
