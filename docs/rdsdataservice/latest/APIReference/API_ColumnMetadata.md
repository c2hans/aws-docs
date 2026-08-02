---
source_url: https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_ColumnMetadata.html
---

# ColumnMetadata
<a name="API_ColumnMetadata"></a>

Contains the metadata for a column.

## Contents
<a name="API_ColumnMetadata_Contents"></a>

 ** arrayBaseColumnType **   <a name="rdsdtataservice-Type-ColumnMetadata-arrayBaseColumnType"></a>
The type of the column.
Type: Integer
Required: No

 ** isAutoIncrement **   <a name="rdsdtataservice-Type-ColumnMetadata-isAutoIncrement"></a>
A value that indicates whether the column increments automatically.
Type: Boolean
Required: No

 ** isCaseSensitive **   <a name="rdsdtataservice-Type-ColumnMetadata-isCaseSensitive"></a>
A value that indicates whether the column is case-sensitive.
Type: Boolean
Required: No

 ** isCurrency **   <a name="rdsdtataservice-Type-ColumnMetadata-isCurrency"></a>
A value that indicates whether the column contains currency values.
Type: Boolean
Required: No

 ** isSigned **   <a name="rdsdtataservice-Type-ColumnMetadata-isSigned"></a>
A value that indicates whether an integer column is signed.
Type: Boolean
Required: No

 ** label **   <a name="rdsdtataservice-Type-ColumnMetadata-label"></a>
The label for the column.
Type: String
Required: No

 ** name **   <a name="rdsdtataservice-Type-ColumnMetadata-name"></a>
The name of the column.
Type: String
Required: No

 ** nullable **   <a name="rdsdtataservice-Type-ColumnMetadata-nullable"></a>
A value that indicates whether the column is nullable.
Type: Integer
Required: No

 ** precision **   <a name="rdsdtataservice-Type-ColumnMetadata-precision"></a>
The precision value of a decimal number column.
Type: Integer
Required: No

 ** scale **   <a name="rdsdtataservice-Type-ColumnMetadata-scale"></a>
The scale value of a decimal number column.
Type: Integer
Required: No

 ** schemaName **   <a name="rdsdtataservice-Type-ColumnMetadata-schemaName"></a>
The name of the schema that owns the table that includes the column.
Type: String
Required: No

 ** tableName **   <a name="rdsdtataservice-Type-ColumnMetadata-tableName"></a>
The name of the table that includes the column.
Type: String
Required: No

 ** type **   <a name="rdsdtataservice-Type-ColumnMetadata-type"></a>
The type of the column.
Type: Integer
Required: No

 ** typeName **   <a name="rdsdtataservice-Type-ColumnMetadata-typeName"></a>
The database-specific data type of the column.
Type: String
Required: No

## See Also
<a name="API_ColumnMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-data-2018-08-01/ColumnMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-data-2018-08-01/ColumnMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-data-2018-08-01/ColumnMetadata)
