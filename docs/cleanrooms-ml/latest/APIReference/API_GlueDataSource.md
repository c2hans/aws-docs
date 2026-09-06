---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_GlueDataSource.html
---

# GlueDataSource
<a name="API_GlueDataSource"></a>

Defines the Glue data source that contains the training data.

## Contents
<a name="API_GlueDataSource_Contents"></a>

 ** databaseName **   <a name="API-Type-GlueDataSource-databaseName"></a>
The Glue database that contains the training data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_](([a-zA-Z0-9_]+-)*([a-zA-Z0-9_]+))?`
Required: Yes

 ** tableName **   <a name="API-Type-GlueDataSource-tableName"></a>
The Glue table that contains the training data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_](([a-zA-Z0-9_ ]+-)*([a-zA-Z0-9_ ]+))?`
Required: Yes

 ** catalogId **   <a name="API-Type-GlueDataSource-catalogId"></a>
The Glue catalog that contains the training data.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

## See Also
<a name="API_GlueDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/GlueDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/GlueDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/GlueDataSource)
