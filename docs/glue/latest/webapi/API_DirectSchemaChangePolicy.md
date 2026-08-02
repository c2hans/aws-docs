---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DirectSchemaChangePolicy.html
---

# DirectSchemaChangePolicy
<a name="API_DirectSchemaChangePolicy"></a>

A policy that specifies update behavior for the crawler.

## Contents
<a name="API_DirectSchemaChangePolicy_Contents"></a>

 ** Database **   <a name="Glue-Type-DirectSchemaChangePolicy-Database"></a>
Specifies the database that the schema change policy applies to.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** EnableUpdateCatalog **   <a name="Glue-Type-DirectSchemaChangePolicy-EnableUpdateCatalog"></a>
Whether to use the specified update behavior when the crawler finds a changed schema.
Type: Boolean
Required: No

 ** Table **   <a name="Glue-Type-DirectSchemaChangePolicy-Table"></a>
Specifies the table in the database that the schema change policy applies to.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** UpdateBehavior **   <a name="Glue-Type-DirectSchemaChangePolicy-UpdateBehavior"></a>
The update behavior when the crawler finds a changed schema.
Type: String
Valid Values: `UPDATE_IN_DATABASE | LOG`
Required: No

## See Also
<a name="API_DirectSchemaChangePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DirectSchemaChangePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DirectSchemaChangePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DirectSchemaChangePolicy)
