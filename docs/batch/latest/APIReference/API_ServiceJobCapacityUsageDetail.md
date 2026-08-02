---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_ServiceJobCapacityUsageDetail.html
---

# ServiceJobCapacityUsageDetail
<a name="API_ServiceJobCapacityUsageDetail"></a>

The capacity usage for a service job, including the unit of measure and quantity of resources being consumed.

## Contents
<a name="API_ServiceJobCapacityUsageDetail_Contents"></a>

 ** capacityUnit **   <a name="Batch-Type-ServiceJobCapacityUsageDetail-capacityUnit"></a>
The unit of measure for the service job capacity usage. For service jobs, this is the instance type.
Type: String
Required: No

 ** quantity **   <a name="Batch-Type-ServiceJobCapacityUsageDetail-quantity"></a>
The quantity of capacity being used by the service job, measured in the units specified by `capacityUnit`.
Type: Double
Required: No

## See Also
<a name="API_ServiceJobCapacityUsageDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/ServiceJobCapacityUsageDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/ServiceJobCapacityUsageDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/ServiceJobCapacityUsageDetail)
