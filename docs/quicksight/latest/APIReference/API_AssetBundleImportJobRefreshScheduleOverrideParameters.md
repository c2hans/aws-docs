---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AssetBundleImportJobRefreshScheduleOverrideParameters.html
---

# AssetBundleImportJobRefreshScheduleOverrideParameters
<a name="API_AssetBundleImportJobRefreshScheduleOverrideParameters"></a>

A list of overrides for a specific `RefreshsSchedule` resource that is present in the asset bundle that is imported.

## Contents
<a name="API_AssetBundleImportJobRefreshScheduleOverrideParameters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** DataSetId **   <a name="QS-Type-AssetBundleImportJobRefreshScheduleOverrideParameters-DataSetId"></a>
A partial identifier for the specific `RefreshSchedule` resource that is being overridden. This structure is used together with the `ScheduleID` structure.
Type: String
Required: Yes

 ** ScheduleId **   <a name="QS-Type-AssetBundleImportJobRefreshScheduleOverrideParameters-ScheduleId"></a>
A partial identifier for the specific `RefreshSchedule` resource being overridden. This structure is used together with the `DataSetId` structure.
Type: String
Required: Yes

 ** StartAfterDateTime **   <a name="QS-Type-AssetBundleImportJobRefreshScheduleOverrideParameters-StartAfterDateTime"></a>
An override for the `StartAfterDateTime` of a `RefreshSchedule`. Make sure that the `StartAfterDateTime` is set to a time that takes place in the future.
Type: Timestamp
Required: No

## See Also
<a name="API_AssetBundleImportJobRefreshScheduleOverrideParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AssetBundleImportJobRefreshScheduleOverrideParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AssetBundleImportJobRefreshScheduleOverrideParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AssetBundleImportJobRefreshScheduleOverrideParameters)
