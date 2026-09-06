---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Route.html
---

# Route
<a name="API_Route"></a>

Specifies a route node that directs data to different output paths based on defined filtering conditions.

## Contents
<a name="API_Route_Contents"></a>

 ** GroupFiltersList **   <a name="Glue-Type-Route-GroupFiltersList"></a>
A list of group filters that define the routing conditions and criteria for directing data to different output paths.
Type: Array of [GroupFilters](API_GroupFilters.md) objects
Required: Yes

 ** Inputs **   <a name="Glue-Type-Route-Inputs"></a>
The input connection for the route node.
Type: Array of strings
Array Members: Fixed number of 1 item.
Pattern: `[A-Za-z0-9_-]*`
Required: Yes

 ** Name **   <a name="Glue-Type-Route-Name"></a>
The name of the route node.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

## See Also
<a name="API_Route_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Route)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Route)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Route)
