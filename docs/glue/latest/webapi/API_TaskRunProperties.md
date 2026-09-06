---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_TaskRunProperties.html
---

# TaskRunProperties
<a name="API_TaskRunProperties"></a>

The configuration properties for the task run.

## Contents
<a name="API_TaskRunProperties_Contents"></a>

 ** ExportLabelsTaskRunProperties **   <a name="Glue-Type-TaskRunProperties-ExportLabelsTaskRunProperties"></a>
The configuration properties for an exporting labels task run.
Type: [ExportLabelsTaskRunProperties](API_ExportLabelsTaskRunProperties.md) object
Required: No

 ** FindMatchesTaskRunProperties **   <a name="Glue-Type-TaskRunProperties-FindMatchesTaskRunProperties"></a>
The configuration properties for a find matches task run.
Type: [FindMatchesTaskRunProperties](API_FindMatchesTaskRunProperties.md) object
Required: No

 ** ImportLabelsTaskRunProperties **   <a name="Glue-Type-TaskRunProperties-ImportLabelsTaskRunProperties"></a>
The configuration properties for an importing labels task run.
Type: [ImportLabelsTaskRunProperties](API_ImportLabelsTaskRunProperties.md) object
Required: No

 ** LabelingSetGenerationTaskRunProperties **   <a name="Glue-Type-TaskRunProperties-LabelingSetGenerationTaskRunProperties"></a>
The configuration properties for a labeling set generation task run.
Type: [LabelingSetGenerationTaskRunProperties](API_LabelingSetGenerationTaskRunProperties.md) object
Required: No

 ** TaskType **   <a name="Glue-Type-TaskRunProperties-TaskType"></a>
The type of task run.
Type: String
Valid Values: `EVALUATION | LABELING_SET_GENERATION | IMPORT_LABELS | EXPORT_LABELS | FIND_MATCHES`
Required: No

## See Also
<a name="API_TaskRunProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/TaskRunProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/TaskRunProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/TaskRunProperties)
