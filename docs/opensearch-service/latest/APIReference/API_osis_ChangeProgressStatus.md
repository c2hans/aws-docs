---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_ChangeProgressStatus.html
---

# ChangeProgressStatus
<a name="API_osis_ChangeProgressStatus"></a>

The progress details of a pipeline configuration change.

## Contents
<a name="API_osis_ChangeProgressStatus_Contents"></a>

 ** ChangeProgressStages **   <a name="opensearchservice-Type-osis_ChangeProgressStatus-ChangeProgressStages"></a>
Information about the stages that the pipeline is going through to perform the configuration change.
Type: Array of [ChangeProgressStage](API_osis_ChangeProgressStage.md) objects
Required: No

 ** StartTime **   <a name="opensearchservice-Type-osis_ChangeProgressStatus-StartTime"></a>
The time at which the configuration change is made on the pipeline.
Type: Timestamp
Required: No

 ** Status **   <a name="opensearchservice-Type-osis_ChangeProgressStatus-Status"></a>
The overall status of the pipeline configuration change.
Type: String
Valid Values: `PENDING | IN_PROGRESS | COMPLETED | FAILED`
Required: No

 ** TotalNumberOfStages **   <a name="opensearchservice-Type-osis_ChangeProgressStatus-TotalNumberOfStages"></a>
The total number of stages required for the pipeline configuration change.
Type: Integer
Required: No

## See Also
<a name="API_osis_ChangeProgressStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/osis-2022-01-01/ChangeProgressStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/osis-2022-01-01/ChangeProgressStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/osis-2022-01-01/ChangeProgressStatus)
