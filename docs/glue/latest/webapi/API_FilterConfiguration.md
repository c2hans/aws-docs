---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_FilterConfiguration.html
---

# FilterConfiguration
<a name="API_FilterConfiguration"></a>

Configuration that defines how filter predicates are applied to REST API requests, supporting both query parameter and filter string strategies.

## Contents
<a name="API_FilterConfiguration_Contents"></a>

 ** FilterMode **   <a name="Glue-Type-FilterConfiguration-FilterMode"></a>
The strategy for applying filters to requests. Use `QUERY_PARAMS` to pass filters as individual query parameters, or `FILTER_STRING` to construct a single filter expression string.
Type: String
Valid Values: `QUERY_PARAMS | FILTER_STRING`
Required: Yes

 ** BetweenConfiguration **   <a name="Glue-Type-FilterConfiguration-BetweenConfiguration"></a>
Configuration for handling BETWEEN range filter operations.
Type: [BetweenConfiguration](API_BetweenConfiguration.md) object
Required: No

 ** DateTimeFormat **   <a name="Glue-Type-FilterConfiguration-DateTimeFormat"></a>
The global date and time format for filter expressions. Accepts Java `DateTimeFormatter` patterns (for example, `EEE, d MMM yyyy HH:mm:ss Z`), `EPOCH_SECONDS` for Unix epoch seconds, or `EPOCH_MILLIS` for Unix epoch milliseconds. If not specified, values are passed as-is in ISO-8601 format.
Type: String
Required: No

 ** FilterStringConfiguration **   <a name="Glue-Type-FilterConfiguration-FilterStringConfiguration"></a>
Configuration for constructing filter expressions when `FilterMode` is set to `FILTER_STRING`.
Type: [FilterStringConfiguration](API_FilterStringConfiguration.md) object
Required: No

 ** OperatorMappings **   <a name="Glue-Type-FilterConfiguration-OperatorMappings"></a>
A map of logical filter operators to their API-specific string representations. Supported operator keys are: `EQUAL_TO`, `NOT_EQUAL_TO`, `LESS_THAN`, `GREATER_THAN`, `LESS_THAN_OR_EQUAL_TO`, `GREATER_THAN_OR_EQUAL_TO`, `CONTAINS`, `BETWEEN`, `AND`, and `OR`.
Type: String to string map
Required: No

 ** StripQuotes **   <a name="Glue-Type-FilterConfiguration-StripQuotes"></a>
Indicates whether surrounding double quotes should be stripped from filter values before processing.
Type: Boolean
Required: No

## See Also
<a name="API_FilterConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/FilterConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/FilterConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/FilterConfiguration)
