---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ConnectorTypeFilter.html
---

# ConnectorTypeFilter
<a name="API_ConnectorTypeFilter"></a>

A filter that matches connectors by connector type.

## Contents
<a name="API_ConnectorTypeFilter_Contents"></a>

 ** comparison **   <a name="inspector2-Type-ConnectorTypeFilter-comparison"></a>
The comparison operator for the connector type filter.
Type: String
Valid Values: `EQUALS`
Required: Yes

 ** value **   <a name="inspector2-Type-ConnectorTypeFilter-value"></a>
The connector type value to filter by.
Type: String
Valid Values: `CUSTOMER_MANAGED | SERVICE_LINKED`
Required: Yes

## See Also
<a name="API_ConnectorTypeFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ConnectorTypeFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ConnectorTypeFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ConnectorTypeFilter)
