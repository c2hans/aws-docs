---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_ChangeProgressStage.html
---

# ChangeProgressStage
<a name="API_osis_ChangeProgressStage"></a>

Progress details for a specific stage of a pipeline configuration change.

## Contents
<a name="API_osis_ChangeProgressStage_Contents"></a>

 ** Description **   <a name="opensearchservice-Type-osis_ChangeProgressStage-Description"></a>
A description of the stage.
Type: String
Required: No

 ** LastUpdatedAt **   <a name="opensearchservice-Type-osis_ChangeProgressStage-LastUpdatedAt"></a>
The most recent updated timestamp of the stage.
Type: Timestamp
Required: No

 ** Name **   <a name="opensearchservice-Type-osis_ChangeProgressStage-Name"></a>
The name of the stage.
Type: String
Required: No

 ** Status **   <a name="opensearchservice-Type-osis_ChangeProgressStage-Status"></a>
The current status of the stage that the change is in.
Type: String
Valid Values: `PENDING | IN_PROGRESS | COMPLETED | FAILED`
Required: No

## See Also
<a name="API_osis_ChangeProgressStage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/osis-2022-01-01/ChangeProgressStage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/osis-2022-01-01/ChangeProgressStage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/osis-2022-01-01/ChangeProgressStage)
