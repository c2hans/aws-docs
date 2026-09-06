---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_Task.html
---

# Task
<a name="API_Task"></a>

 A class for modeling different type of tasks. Task implementation varies based on the `TaskType`.

## Contents
<a name="API_Task_Contents"></a>

 ** sourceFields **   <a name="appflow-Type-Task-sourceFields"></a>
 The source fields to which a particular task is applied.
Type: Array of strings
Length Constraints: Maximum length of 2048.
Pattern: `.*`
Required: Yes

 ** taskType **   <a name="appflow-Type-Task-taskType"></a>
 Specifies the particular task implementation that Amazon AppFlow performs.
Type: String
Valid Values: `Arithmetic | Filter | Map | Map_all | Mask | Merge | Passthrough | Truncate | Validate | Partition`
Required: Yes

 ** connectorOperator **   <a name="appflow-Type-Task-connectorOperator"></a>
 The operation to be performed on the provided source fields.
Type: [ConnectorOperator](API_ConnectorOperator.md) object
Required: No

 ** destinationField **   <a name="appflow-Type-Task-destinationField"></a>
 A field in a destination connector, or a field value against which Amazon AppFlow validates a source field.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `.*`
Required: No

 ** taskProperties **   <a name="appflow-Type-Task-taskProperties"></a>
 A map used to store task-related information. The execution service looks for particular information based on the `TaskType`.
Type: String to string map
Valid Keys: `VALUE | VALUES | DATA_TYPE | UPPER_BOUND | LOWER_BOUND | SOURCE_DATA_TYPE | DESTINATION_DATA_TYPE | VALIDATION_ACTION | MASK_VALUE | MASK_LENGTH | TRUNCATE_LENGTH | MATH_OPERATION_FIELDS_ORDER | CONCAT_FORMAT | SUBFIELD_CATEGORY_MAP | EXCLUDE_SOURCE_FIELDS_LIST | INCLUDE_NEW_FIELDS | ORDERED_PARTITION_KEYS_LIST`
Value Length Constraints: Maximum length of 2048.
Value Pattern: `.+`
Required: No

## See Also
<a name="API_Task_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/Task)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/Task)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/Task)
