---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ClonedBlueGreenScheduledAction.html
---

# ClonedBlueGreenScheduledAction
<a name="API_ClonedBlueGreenScheduledAction"></a>

An action that the service takes automatically at a scheduled time during a cloned blue/green upgrade.

## Contents
<a name="API_ClonedBlueGreenScheduledAction_Contents"></a>

 ** Action **   <a name="opensearchservice-Type-ClonedBlueGreenScheduledAction-Action"></a>
The action that the service takes.
Type: String
Valid Values: `AutomaticCutoverToPrimaryCluster | DeletePrimaryCluster`
Required: No

 ** ScheduledTime **   <a name="opensearchservice-Type-ClonedBlueGreenScheduledAction-ScheduledTime"></a>
The time at which the service takes the action.
Type: Timestamp
Required: No

## See Also
<a name="API_ClonedBlueGreenScheduledAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/ClonedBlueGreenScheduledAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/ClonedBlueGreenScheduledAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/ClonedBlueGreenScheduledAction)
