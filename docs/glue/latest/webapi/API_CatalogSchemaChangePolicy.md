---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CatalogSchemaChangePolicy.html
---

# CatalogSchemaChangePolicy
<a name="API_CatalogSchemaChangePolicy"></a>

A policy that specifies update behavior for the crawler.

## Contents
<a name="API_CatalogSchemaChangePolicy_Contents"></a>

 ** EnableUpdateCatalog **   <a name="Glue-Type-CatalogSchemaChangePolicy-EnableUpdateCatalog"></a>
Whether to use the specified update behavior when the crawler finds a changed schema.
Type: Boolean
Required: No

 ** UpdateBehavior **   <a name="Glue-Type-CatalogSchemaChangePolicy-UpdateBehavior"></a>
The update behavior when the crawler finds a changed schema.
Type: String
Valid Values: `UPDATE_IN_DATABASE | LOG`
Required: No

## See Also
<a name="API_CatalogSchemaChangePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CatalogSchemaChangePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CatalogSchemaChangePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CatalogSchemaChangePolicy)
