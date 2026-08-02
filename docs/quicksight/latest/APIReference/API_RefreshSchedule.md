---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RefreshSchedule.html
---

# RefreshSchedule
<a name="API_RefreshSchedule"></a>

The refresh schedule of a dataset.

## Contents
<a name="API_RefreshSchedule_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** RefreshType **   <a name="QS-Type-RefreshSchedule-RefreshType"></a>
The type of refresh that a datset undergoes. Valid values are as follows:
+  `FULL_REFRESH`: A complete refresh of a dataset.
+  `INCREMENTAL_REFRESH`: A partial refresh of some rows of a dataset, based on the time window specified.
For more information on full and incremental refreshes, see [Refreshing SPICE data](https://docs.aws.amazon.com/quicksight/latest/user/refreshing-imported-data.html) in the *Amazon Quick Suite User Guide*.
Type: String
Valid Values: `INCREMENTAL_REFRESH | FULL_REFRESH`
Required: Yes

 ** ScheduleFrequency **   <a name="QS-Type-RefreshSchedule-ScheduleFrequency"></a>
The frequency for the refresh schedule.
Type: [RefreshFrequency](API_RefreshFrequency.md) object
Required: Yes

 ** ScheduleId **   <a name="QS-Type-RefreshSchedule-ScheduleId"></a>
An identifier for the refresh schedule.
Type: String
Required: Yes

 ** Arn **   <a name="QS-Type-RefreshSchedule-Arn"></a>
The Amazon Resource Name (ARN) for the refresh schedule.
Type: String
Required: No

 ** StartAfterDateTime **   <a name="QS-Type-RefreshSchedule-StartAfterDateTime"></a>
Time after which the refresh schedule can be started, expressed in `YYYY-MM-DDTHH:MM:SS` format.
Type: Timestamp
Required: No

## See Also
<a name="API_RefreshSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/RefreshSchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/RefreshSchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/RefreshSchedule)
