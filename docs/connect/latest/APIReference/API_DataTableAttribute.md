---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DataTableAttribute.html
---

# DataTableAttribute
<a name="API_DataTableAttribute"></a>

Represents an attribute (column) in a data table. Attributes define the schema and validation rules for values that can be stored in the table. They specify the data type, constraints, and whether the attribute is used as a primary key for record identification.

## Contents
<a name="API_DataTableAttribute_Contents"></a>

 ** Name **   <a name="connect-Type-DataTableAttribute-Name"></a>
The human-readable name of the attribute. Must be unique within the data table and conform to Connect naming standards.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `^[\p{L}\p{Z}\p{N}\-_.:=@'|]+$`
Required: Yes

 ** ValueType **   <a name="connect-Type-DataTableAttribute-ValueType"></a>
The type of value allowed for this attribute. Must be one of TEXT, TEXT\_LIST, NUMBER, NUMBER\_LIST, or BOOLEAN. Determines how values are validated and processed.
Type: String
Valid Values: `TEXT | NUMBER | BOOLEAN | TEXT_LIST | NUMBER_LIST`
Required: Yes

 ** AttributeId **   <a name="connect-Type-DataTableAttribute-AttributeId"></a>
The unique identifier for the attribute within the data table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** DataTableArn **   <a name="connect-Type-DataTableAttribute-DataTableArn"></a>
The Amazon Resource Name (ARN) of the data table that contains this attribute.
Type: String
Required: No

 ** DataTableId **   <a name="connect-Type-DataTableAttribute-DataTableId"></a>
The unique identifier of the data table that contains this attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** Description **   <a name="connect-Type-DataTableAttribute-Description"></a>
An optional description explaining the purpose and usage of this attribute.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 250.
Pattern: `^[\\P{C}\r\n\t]+$`
Required: No

 ** LastModifiedRegion **   <a name="connect-Type-DataTableAttribute-LastModifiedRegion"></a>
The AWS Region where this attribute was last modified, used for region replication.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** LastModifiedTime **   <a name="connect-Type-DataTableAttribute-LastModifiedTime"></a>
The timestamp when this attribute was last modified.
Type: Timestamp
Required: No

 ** LockVersion **   <a name="connect-Type-DataTableAttribute-LockVersion"></a>
The lock version for this attribute, used for optimistic locking to prevent concurrent modification conflicts.
Type: [DataTableLockVersion](API_DataTableLockVersion.md) object
Required: No

 ** Primary **   <a name="connect-Type-DataTableAttribute-Primary"></a>
Boolean indicating whether this attribute is used as a primary key for record identification. Primary attributes must have unique value combinations and cannot contain expressions.
Type: Boolean
Required: No

 ** Validation **   <a name="connect-Type-DataTableAttribute-Validation"></a>
The validation rules applied to values of this attribute. Based on JSON Schema Draft 2020-12 with additional Connect-specific validations for data integrity.
Type: [Validation](API_Validation.md) object
Required: No

 ** Version **   <a name="connect-Type-DataTableAttribute-Version"></a>
The version identifier for this attribute, used for versioning and change tracking.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

## See Also
<a name="API_DataTableAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DataTableAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DataTableAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DataTableAttribute)
