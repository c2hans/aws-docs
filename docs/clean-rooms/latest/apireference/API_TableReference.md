---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_TableReference.html
---

# TableReference
<a name="API_TableReference"></a>

A pointer to the dataset that underlies this table.

## Contents
<a name="API_TableReference_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** athena **   <a name="API-Type-TableReference-athena"></a>
 If present, a reference to the Athena table referred to by this table reference.
Type: [AthenaTableReference](API_AthenaTableReference.md) object
Required: No

 ** glue **   <a name="API-Type-TableReference-glue"></a>
If present, a reference to the AWS Glue table referred to by this table reference.
Type: [GlueTableReference](API_GlueTableReference.md) object
Required: No

 ** snowflake **   <a name="API-Type-TableReference-snowflake"></a>
 If present, a reference to the Snowflake table referred to by this table reference.
Type: [SnowflakeTableReference](API_SnowflakeTableReference.md) object
Required: No

## See Also
<a name="API_TableReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/TableReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/TableReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/TableReference)
