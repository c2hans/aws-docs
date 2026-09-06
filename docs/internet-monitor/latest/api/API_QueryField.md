---
source_url: https://docs.aws.amazon.com/internet-monitor/latest/api/API_QueryField.html
---

# QueryField
<a name="API_QueryField"></a>

Defines a field to query for your application's Internet Monitor data. You create a data repository by running a query of a specific type. Each `QueryType` includes a specific set of fields and datatypes to retrieve data for.

## Contents
<a name="API_QueryField_Contents"></a>

 ** Name **   <a name="internetmonitor-Type-QueryField-Name"></a>
The name of a field to query your application's Internet Monitor data for, such as `availability_score`.
Type: String
Required: No

 ** Type **   <a name="internetmonitor-Type-QueryField-Type"></a>
The data type for a query field, which must correspond to the field you're defining for `QueryField`. For example, if the query field name is `availability_score`, the data type is `float`.
Type: String
Required: No

## See Also
<a name="API_QueryField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/internetmonitor-2021-06-03/QueryField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/internetmonitor-2021-06-03/QueryField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/internetmonitor-2021-06-03/QueryField)
