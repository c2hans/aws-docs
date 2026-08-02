---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ViewDefinitionInput.html
---

# ViewDefinitionInput
<a name="API_ViewDefinitionInput"></a>

A structure containing details for creating or updating an AWS Glue view.

## Contents
<a name="API_ViewDefinitionInput_Contents"></a>

 ** Definer **   <a name="Glue-Type-ViewDefinitionInput-Definer"></a>
The definer of a view in SQL.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** IsProtected **   <a name="Glue-Type-ViewDefinitionInput-IsProtected"></a>
You can set this flag as true to instruct the engine not to push user-provided operations into the logical plan of the view during query planning. However, setting this flag does not guarantee that the engine will comply. Refer to the engine's documentation to understand the guarantees provided, if any.
Type: Boolean
Required: No

 ** LastRefreshType **   <a name="Glue-Type-ViewDefinitionInput-LastRefreshType"></a>
The type of the materialized view's last refresh. Valid values: `Full`, `Incremental`.
Type: String
Valid Values: `FULL | INCREMENTAL`
Required: No

 ** RefreshSeconds **   <a name="Glue-Type-ViewDefinitionInput-RefreshSeconds"></a>
Auto refresh interval in seconds for the materialized view. If not specified, the view will not automatically refresh.
Type: Long
Required: No

 ** Representations **   <a name="Glue-Type-ViewDefinitionInput-Representations"></a>
A list of structures that contains the dialect of the view, and the query that defines the view.
Type: Array of [ViewRepresentationInput](API_ViewRepresentationInput.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** SubObjects **   <a name="Glue-Type-ViewDefinitionInput-SubObjects"></a>
A list of base table ARNs that make up the view.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** SubObjectVersionIds **   <a name="Glue-Type-ViewDefinitionInput-SubObjectVersionIds"></a>
List of the Apache Iceberg table versions referenced by the materialized view.
Type: Array of longs
Array Members: Minimum number of 0 items. Maximum number of 250 items.
Valid Range: Minimum value of -1.
Required: No

 ** ViewVersionId **   <a name="Glue-Type-ViewDefinitionInput-ViewVersionId"></a>
The ID value that identifies this view's version. For materialized views, the version ID is the Apache Iceberg table's snapshot ID.
Type: Long
Valid Range: Minimum value of -1.
Required: No

 ** ViewVersionToken **   <a name="Glue-Type-ViewDefinitionInput-ViewVersionToken"></a>
The version ID of the Apache Iceberg table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

## See Also
<a name="API_ViewDefinitionInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ViewDefinitionInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ViewDefinitionInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ViewDefinitionInput)
