---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_FilterOverrides.html
---

# FilterOverrides
<a name="API_FilterOverrides"></a>

Configuration that defines per-field overrides for filter behavior, allowing individual fields to customize how filter operations are applied.

## Contents
<a name="API_FilterOverrides_Contents"></a>

 ** BetweenConfiguration **   <a name="Glue-Type-FilterOverrides-BetweenConfiguration"></a>
Field-specific configuration for handling BETWEEN range filter operations.
Type: [BetweenConfiguration](API_BetweenConfiguration.md) object
Required: No

 ** DateTimeFormat **   <a name="Glue-Type-FilterOverrides-DateTimeFormat"></a>
The date and time format for filter expressions on this field, overriding the global `DateTimeFormat`. Accepts Java `DateTimeFormatter` patterns (for example, `EEE, d MMM yyyy HH:mm:ss Z`), `EPOCH_SECONDS` for Unix epoch seconds, or `EPOCH_MILLIS` for Unix epoch milliseconds.
Type: String
Required: No

 ** FieldName **   <a name="Glue-Type-FilterOverrides-FieldName"></a>
An override for the field name to use in filter expressions, if different from the schema field name.
Type: String
Required: No

 ** OperatorMappings **   <a name="Glue-Type-FilterOverrides-OperatorMappings"></a>
A map of logical filter operators to their field-specific API representations, overriding the global operator mappings. Supported operator keys are: `EQUAL_TO`, `NOT_EQUAL_TO`, `LESS_THAN`, `GREATER_THAN`, `LESS_THAN_OR_EQUAL_TO`, `GREATER_THAN_OR_EQUAL_TO`, `CONTAINS`, `BETWEEN`, `AND`, and `OR`.
Type: String to string map
Required: No

## See Also
<a name="API_FilterOverrides_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/FilterOverrides)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/FilterOverrides)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/FilterOverrides)
