---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_Task.html
---

# Task
<a name="API_connect-customer-profiles_Task"></a>

A class for modeling different type of tasks. Task implementation varies based on the TaskType.

## Contents
<a name="API_connect-customer-profiles_Task_Contents"></a>

 ** SourceFields **   <a name="connect-Type-connect-customer-profiles_Task-SourceFields"></a>
The source fields to which a particular task is applied.
Type: Array of strings
Length Constraints: Maximum length of 2048.
Pattern: `.*`
Required: Yes

 ** TaskType **   <a name="connect-Type-connect-customer-profiles_Task-TaskType"></a>
Specifies the particular task implementation that Amazon AppFlow performs.
Type: String
Valid Values: `Arithmetic | Filter | Map | Mask | Merge | Truncate | Validate`
Required: Yes

 ** ConnectorOperator **   <a name="connect-Type-connect-customer-profiles_Task-ConnectorOperator"></a>
The operation to be performed on the provided source fields.
Type: [ConnectorOperator](API_connect-customer-profiles_ConnectorOperator.md) object
Required: No

 ** DestinationField **   <a name="connect-Type-connect-customer-profiles_Task-DestinationField"></a>
A field in a destination connector, or a field value against which Amazon AppFlow validates a source field.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `.*`
Required: No

 ** TaskProperties **   <a name="connect-Type-connect-customer-profiles_Task-TaskProperties"></a>
A map used to store task-related information. The service looks for particular information based on the TaskType.
Type: String to string map
Valid Keys: `VALUE | VALUES | DATA_TYPE | UPPER_BOUND | LOWER_BOUND | SOURCE_DATA_TYPE | DESTINATION_DATA_TYPE | VALIDATION_ACTION | MASK_VALUE | MASK_LENGTH | TRUNCATE_LENGTH | MATH_OPERATION_FIELDS_ORDER | CONCAT_FORMAT | SUBFIELD_CATEGORY_MAP`
Value Length Constraints: Maximum length of 2048.
Value Pattern: `.+`
Required: No

## See Also
<a name="API_connect-customer-profiles_Task_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/Task)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/Task)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/Task)
