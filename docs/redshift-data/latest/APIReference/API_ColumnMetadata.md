---
source_url: https://docs.aws.amazon.com/redshift-data/latest/APIReference/API_ColumnMetadata.html
---

# ColumnMetadata
<a name="API_ColumnMetadata"></a>

The properties (metadata) of a column.

## Contents
<a name="API_ColumnMetadata_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** columnDefault **   <a name="redshiftdata-Type-ColumnMetadata-columnDefault"></a>
The default value of the column.
Type: String
Required: No

 ** isCaseSensitive **   <a name="redshiftdata-Type-ColumnMetadata-isCaseSensitive"></a>
A value that indicates whether the column is case-sensitive.
Type: Boolean
Required: No

 ** isCurrency **   <a name="redshiftdata-Type-ColumnMetadata-isCurrency"></a>
A value that indicates whether the column contains currency values.
Type: Boolean
Required: No

 ** isSigned **   <a name="redshiftdata-Type-ColumnMetadata-isSigned"></a>
A value that indicates whether an integer column is signed.
Type: Boolean
Required: No

 ** label **   <a name="redshiftdata-Type-ColumnMetadata-label"></a>
The label for the column.
Type: String
Required: No

 ** length **   <a name="redshiftdata-Type-ColumnMetadata-length"></a>
The length of the column.
Type: Integer
Required: No

 ** name **   <a name="redshiftdata-Type-ColumnMetadata-name"></a>
The name of the column.
Type: String
Required: No

 ** nullable **   <a name="redshiftdata-Type-ColumnMetadata-nullable"></a>
A value that indicates whether the column is nullable.
Type: Integer
Required: No

 ** precision **   <a name="redshiftdata-Type-ColumnMetadata-precision"></a>
The precision value of a decimal number column, or the column length for a non-numeric column.
Type: Integer
Required: No

 ** scale **   <a name="redshiftdata-Type-ColumnMetadata-scale"></a>
The scale value of a decimal number column.
Type: Integer
Required: No

 ** schemaName **   <a name="redshiftdata-Type-ColumnMetadata-schemaName"></a>
The name of the schema that contains the table that includes the column.
Type: String
Required: No

 ** tableName **   <a name="redshiftdata-Type-ColumnMetadata-tableName"></a>
The name of the table that includes the column.
Type: String
Required: No

 ** typeName **   <a name="redshiftdata-Type-ColumnMetadata-typeName"></a>
The database-specific data type of the column.
Type: String
Required: No

## See Also
<a name="API_ColumnMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-data-2019-12-20/ColumnMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-data-2019-12-20/ColumnMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-data-2019-12-20/ColumnMetadata)
