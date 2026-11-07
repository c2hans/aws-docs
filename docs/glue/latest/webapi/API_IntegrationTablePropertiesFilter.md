---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_IntegrationTablePropertiesFilter.html
---

# IntegrationTablePropertiesFilter
<a name="API_IntegrationTablePropertiesFilter"></a>

A key-value filter used to narrow the list of integration table properties returned by ListIntegrationTableProperties. Specify a filter key and one or more values to match.

## Contents
<a name="API_IntegrationTablePropertiesFilter_Contents"></a>

 ** Name **   <a name="Glue-Type-IntegrationTablePropertiesFilter-Name"></a>
The name of the filter. Supported filter keys are `SourceArn`, `TargetArn`, `SourceTableName`, and `TargetTableName`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** Values **   <a name="Glue-Type-IntegrationTablePropertiesFilter-Values"></a>
A list of filter values.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

## See Also
<a name="API_IntegrationTablePropertiesFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/IntegrationTablePropertiesFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/IntegrationTablePropertiesFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/IntegrationTablePropertiesFilter)
