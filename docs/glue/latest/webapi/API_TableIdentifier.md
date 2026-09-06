---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_TableIdentifier.html
---

# TableIdentifier
<a name="API_TableIdentifier"></a>

A structure that describes a target table for resource linking.

## Contents
<a name="API_TableIdentifier_Contents"></a>

 ** CatalogId **   <a name="Glue-Type-TableIdentifier-CatalogId"></a>
The ID of the Data Catalog in which the table resides.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** DatabaseName **   <a name="Glue-Type-TableIdentifier-DatabaseName"></a>
The name of the catalog database that contains the target table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Name **   <a name="Glue-Type-TableIdentifier-Name"></a>
The name of the target table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Region **   <a name="Glue-Type-TableIdentifier-Region"></a>
Region of the target table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_TableIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/TableIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/TableIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/TableIdentifier)
