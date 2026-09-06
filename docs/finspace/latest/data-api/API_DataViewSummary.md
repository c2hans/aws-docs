---
source_url: https://docs.aws.amazon.com/finspace/latest/data-api/API_DataViewSummary.html
---

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/data-api/amazon-finspace-end-of-support.html).

# DataViewSummary
<a name="API_DataViewSummary"></a>

Structure for the summary of a Dataview.

## Contents
<a name="API_DataViewSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** asOfTimestamp **   <a name="finspace-Type-DataViewSummary-asOfTimestamp"></a>
Time range to use for the Dataview. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Long
Required: No

 ** autoUpdate **   <a name="finspace-Type-DataViewSummary-autoUpdate"></a>
The flag to indicate Dataview should be updated automatically.
Type: Boolean
Required: No

 ** createTime **   <a name="finspace-Type-DataViewSummary-createTime"></a>
The timestamp at which the Dataview was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Long
Required: No

 ** datasetId **   <a name="finspace-Type-DataViewSummary-datasetId"></a>
Th unique identifier for the Dataview Dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Required: No

 ** dataViewArn **   <a name="finspace-Type-DataViewSummary-dataViewArn"></a>
The ARN identifier of the Dataview.
Type: String
Required: No

 ** dataViewId **   <a name="finspace-Type-DataViewSummary-dataViewId"></a>
The unique identifier for the Dataview.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Required: No

 ** destinationTypeProperties **   <a name="finspace-Type-DataViewSummary-destinationTypeProperties"></a>
Information about the Dataview destination.
Type: [DataViewDestinationTypeParams](API_DataViewDestinationTypeParams.md) object
Required: No

 ** errorInfo **   <a name="finspace-Type-DataViewSummary-errorInfo"></a>
The structure with error messages.
Type: [DataViewErrorInfo](API_DataViewErrorInfo.md) object
Required: No

 ** lastModifiedTime **   <a name="finspace-Type-DataViewSummary-lastModifiedTime"></a>
The last time that a Dataview was modified. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Long
Required: No

 ** partitionColumns **   <a name="finspace-Type-DataViewSummary-partitionColumns"></a>
Ordered set of column names used to partition data.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\s\S]*\S[\s\S]*`
Required: No

 ** sortColumns **   <a name="finspace-Type-DataViewSummary-sortColumns"></a>
Columns to be used for sorting the data.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\s\S]*\S[\s\S]*`
Required: No

 ** status **   <a name="finspace-Type-DataViewSummary-status"></a>
The status of a Dataview creation.
+  `RUNNING` – Dataview creation is running.
+  `STARTING` – Dataview creation is starting.
+  `FAILED` – Dataview creation has failed.
+  `CANCELLED` – Dataview creation has been cancelled.
+  `TIMEOUT` – Dataview creation has timed out.
+  `SUCCESS` – Dataview creation has succeeded.
+  `PENDING` – Dataview creation is pending.
+  `FAILED_CLEANUP_FAILED` – Dataview creation failed and resource cleanup failed.
Type: String
Valid Values: `RUNNING | STARTING | FAILED | CANCELLED | TIMEOUT | SUCCESS | PENDING | FAILED_CLEANUP_FAILED`
Required: No

## See Also
<a name="API_DataViewSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2020-07-13/DataViewSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2020-07-13/DataViewSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2020-07-13/DataViewSummary)
