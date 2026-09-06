---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_SourceConnection.html
---

# SourceConnection
<a name="API_SourceConnection"></a>

A top level `ProductViewDetail` response containing details about the product’s connection. AWS Service Catalog returns this field for the `CreateProduct`, `UpdateProduct`, `DescribeProductAsAdmin`, and `SearchProductAsAdmin` APIs. This response contains the same fields as the `ConnectionParameters` request, with the addition of the `LastSync` response.

## Contents
<a name="API_SourceConnection_Contents"></a>

 ** ConnectionParameters **   <a name="servicecatalog-Type-SourceConnection-ConnectionParameters"></a>
The connection details based on the connection `Type`.
Type: [SourceConnectionParameters](API_SourceConnectionParameters.md) object
Required: Yes

 ** Type **   <a name="servicecatalog-Type-SourceConnection-Type"></a>
The only supported `SourceConnection` type is Codestar.
Type: String
Valid Values: `CODESTAR`
Required: No

## See Also
<a name="API_SourceConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/SourceConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/SourceConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/SourceConnection)
