---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_OracleSQLCatalogTarget.html
---

# OracleSQLCatalogTarget
<a name="API_OracleSQLCatalogTarget"></a>

Specifies a target that uses Oracle SQL.

## Contents
<a name="API_OracleSQLCatalogTarget_Contents"></a>

 ** Database **   <a name="Glue-Type-OracleSQLCatalogTarget-Database"></a>
The name of the database to write to.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** Inputs **   <a name="Glue-Type-OracleSQLCatalogTarget-Inputs"></a>
The nodes that are inputs to the data target.
Type: Array of strings
Array Members: Fixed number of 1 item.
Pattern: `[A-Za-z0-9_-]*`
Required: Yes

 ** Name **   <a name="Glue-Type-OracleSQLCatalogTarget-Name"></a>
The name of the data target.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** Table **   <a name="Glue-Type-OracleSQLCatalogTarget-Table"></a>
The name of the table in the database to write to.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

## See Also
<a name="API_OracleSQLCatalogTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/OracleSQLCatalogTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/OracleSQLCatalogTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/OracleSQLCatalogTarget)
