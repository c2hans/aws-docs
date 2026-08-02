---
source_url: https://docs.aws.amazon.com/finspace/latest/data-api/API_ColumnDefinition.html
---

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/data-api/amazon-finspace-end-of-support.html).

# ColumnDefinition
<a name="API_ColumnDefinition"></a>

The definition of a column in a tabular Dataset.

## Contents
<a name="API_ColumnDefinition_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** columnDescription **   <a name="finspace-Type-ColumnDefinition-columnDescription"></a>
Description for a column.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `[\s\S]*`
Required: No

 ** columnName **   <a name="finspace-Type-ColumnDefinition-columnName"></a>
The name of a column.
Type: String
Length Constraints: Maximum length of 126.
Pattern: `.*\S.*`
Required: No

 ** dataType **   <a name="finspace-Type-ColumnDefinition-dataType"></a>
Data type of a column.
+  `STRING` – A String data type.

   `CHAR` – A char data type.

   `INTEGER` – An integer data type.

   `TINYINT` – A tinyint data type.

   `SMALLINT` – A smallint data type.

   `BIGINT` – A bigint data type.

   `FLOAT` – A float data type.

   `DOUBLE` – A double data type.

   `DATE` – A date data type.

   `DATETIME` – A datetime data type.

   `BOOLEAN` – A boolean data type.

   `BINARY` – A binary data type.
Type: String
Valid Values: `STRING | CHAR | INTEGER | TINYINT | SMALLINT | BIGINT | FLOAT | DOUBLE | DATE | DATETIME | BOOLEAN | BINARY`
Required: No

## See Also
<a name="API_ColumnDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2020-07-13/ColumnDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2020-07-13/ColumnDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2020-07-13/ColumnDefinition)
