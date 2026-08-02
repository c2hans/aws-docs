---
source_url: https://docs.aws.amazon.com/codestar-notifications/latest/APIReference/API_ListEventTypesFilter.html
---

# ListEventTypesFilter
<a name="API_ListEventTypesFilter"></a>

Information about a filter to apply to the list of returned event types. You can filter by resource type or service name.

## Contents
<a name="API_ListEventTypesFilter_Contents"></a>

 ** Name **   <a name="codestarnotifications-Type-ListEventTypesFilter-Name"></a>
The system-generated name of the filter type you want to filter by.
Type: String
Valid Values: `RESOURCE_TYPE | SERVICE_NAME`
Required: Yes

 ** Value **   <a name="codestarnotifications-Type-ListEventTypesFilter-Value"></a>
The name of the resource type (for example, pipeline) or service name (for example, CodePipeline) that you want to filter by.
Type: String
Required: Yes

## See Also
<a name="API_ListEventTypesFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codestar-notifications-2019-10-15/ListEventTypesFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codestar-notifications-2019-10-15/ListEventTypesFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codestar-notifications-2019-10-15/ListEventTypesFilter)
