---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_Statistics.html
---

# Statistics
<a name="API_Statistics"></a>

A list of statistics for a session.

## Contents
<a name="API_Statistics_Contents"></a>

 ** costInUsd **   <a name="deadlinecloud-Type-Statistics-costInUsd"></a>
How the statistics should appear in USD. Options include: minimum, maximum, average or sum.
Type: [Stats](API_Stats.md) object
Required: Yes

 ** count **   <a name="deadlinecloud-Type-Statistics-count"></a>
The number of instances in a list of statistics.
Type: Integer
Required: Yes

 ** runtimeInSeconds **   <a name="deadlinecloud-Type-Statistics-runtimeInSeconds"></a>
The total aggregated runtime.
Type: [Stats](API_Stats.md) object
Required: Yes

 ** aggregationEndTime **   <a name="deadlinecloud-Type-Statistics-aggregationEndTime"></a>
The end time for the aggregation.
Type: Timestamp
Required: No

 ** aggregationStartTime **   <a name="deadlinecloud-Type-Statistics-aggregationStartTime"></a>
The start time for the aggregation.
Type: Timestamp
Required: No

 ** fleetId **   <a name="deadlinecloud-Type-Statistics-fleetId"></a>
The fleet ID.
Type: String
Pattern: `fleet-[0-9a-f]{32}`
Required: No

 ** instanceType **   <a name="deadlinecloud-Type-Statistics-instanceType"></a>
The type of instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** jobId **   <a name="deadlinecloud-Type-Statistics-jobId"></a>
The job ID.
Type: String
Pattern: `job-[0-9a-f]{32}`
Required: No

 ** jobName **   <a name="deadlinecloud-Type-Statistics-jobName"></a>
The job name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** licenseProduct **   <a name="deadlinecloud-Type-Statistics-licenseProduct"></a>
The licensed product.
Type: String
Required: No

 ** queueId **   <a name="deadlinecloud-Type-Statistics-queueId"></a>
The queue ID.
Type: String
Pattern: `queue-[0-9a-f]{32}`
Required: No

 ** usageType **   <a name="deadlinecloud-Type-Statistics-usageType"></a>
The type of usage for the statistics.
Type: String
Valid Values: `COMPUTE | LICENSE | PERSISTENT_VOLUME`
Required: No

 ** userId **   <a name="deadlinecloud-Type-Statistics-userId"></a>
The user ID.
Type: String
Required: No

## See Also
<a name="API_Statistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/Statistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/Statistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/Statistics)
