---
source_url: https://docs.aws.amazon.com/finspace/latest/data-api/API_SchemaDefinition.html
---

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/data-api/amazon-finspace-end-of-support.html).

# SchemaDefinition
<a name="API_SchemaDefinition"></a>

Definition for a schema on a tabular Dataset.

## Contents
<a name="API_SchemaDefinition_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** columns **   <a name="finspace-Type-SchemaDefinition-columns"></a>
List of column definitions.
Type: Array of [ColumnDefinition](API_ColumnDefinition.md) objects
Required: No

 ** primaryKeyColumns **   <a name="finspace-Type-SchemaDefinition-primaryKeyColumns"></a>
List of column names used for primary key.
Type: Array of strings
Length Constraints: Maximum length of 126.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_SchemaDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2020-07-13/SchemaDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2020-07-13/SchemaDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2020-07-13/SchemaDefinition)
