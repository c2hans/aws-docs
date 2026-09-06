---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CatalogImportStatus.html
---

# CatalogImportStatus
<a name="API_CatalogImportStatus"></a>

A structure containing migration status information.

## Contents
<a name="API_CatalogImportStatus_Contents"></a>

 ** ImportCompleted **   <a name="Glue-Type-CatalogImportStatus-ImportCompleted"></a>
 `True` if the migration has completed, or `False` otherwise.
Type: Boolean
Required: No

 ** ImportedBy **   <a name="Glue-Type-CatalogImportStatus-ImportedBy"></a>
The name of the person who initiated the migration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** ImportTime **   <a name="Glue-Type-CatalogImportStatus-ImportTime"></a>
The time that the migration was started.
Type: Timestamp
Required: No

## See Also
<a name="API_CatalogImportStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CatalogImportStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CatalogImportStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CatalogImportStatus)
