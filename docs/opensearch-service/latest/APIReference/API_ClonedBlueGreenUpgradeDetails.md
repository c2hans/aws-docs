---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ClonedBlueGreenUpgradeDetails.html
---

# ClonedBlueGreenUpgradeDetails
<a name="API_ClonedBlueGreenUpgradeDetails"></a>

The state of a cloned blue/green upgrade. Members that don't apply are omitted.

## Contents
<a name="API_ClonedBlueGreenUpgradeDetails_Contents"></a>

 ** RetentionInHours **   <a name="opensearchservice-Type-ClonedBlueGreenUpgradeDetails-RetentionInHours"></a>
The retention period, in hours, for the cluster that you cut over from.
Type: Integer
Required: No

 ** ScheduledAction **   <a name="opensearchservice-Type-ClonedBlueGreenUpgradeDetails-ScheduledAction"></a>
The action that the service takes automatically if you don't act before the scheduled time.
Type: [ClonedBlueGreenScheduledAction](API_ClonedBlueGreenScheduledAction.md) object
Required: No

 ** TrafficSplit **   <a name="opensearchservice-Type-ClonedBlueGreenUpgradeDetails-TrafficSplit"></a>
The current split of search traffic between the primary and cloned clusters.
Type: [TrafficPercents](API_TrafficPercents.md) object
Required: No

## See Also
<a name="API_ClonedBlueGreenUpgradeDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/ClonedBlueGreenUpgradeDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/ClonedBlueGreenUpgradeDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/ClonedBlueGreenUpgradeDetails)
