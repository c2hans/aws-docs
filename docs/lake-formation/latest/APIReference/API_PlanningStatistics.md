---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_PlanningStatistics.html
---

# PlanningStatistics
<a name="API_PlanningStatistics"></a>

Statistics related to the processing of a query statement.

## Contents
<a name="API_PlanningStatistics_Contents"></a>

 ** EstimatedDataToScanBytes **   <a name="lakeformation-Type-PlanningStatistics-EstimatedDataToScanBytes"></a>
An estimate of the data that was scanned in bytes.
Type: Long
Required: No

 ** PlanningTimeMillis **   <a name="lakeformation-Type-PlanningStatistics-PlanningTimeMillis"></a>
The time that it took to process the request.
Type: Long
Required: No

 ** QueueTimeMillis **   <a name="lakeformation-Type-PlanningStatistics-QueueTimeMillis"></a>
The time the request was in queue to be processed.
Type: Long
Required: No

 ** WorkUnitsGeneratedCount **   <a name="lakeformation-Type-PlanningStatistics-WorkUnitsGeneratedCount"></a>
The number of work units generated.
Type: Long
Required: No

## See Also
<a name="API_PlanningStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/PlanningStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/PlanningStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/PlanningStatistics)
