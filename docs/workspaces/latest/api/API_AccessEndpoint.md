---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_AccessEndpoint.html
---

# AccessEndpoint
<a name="API_AccessEndpoint"></a>

Describes the access type and endpoint for a WorkSpace.

## Contents
<a name="API_AccessEndpoint_Contents"></a>

 ** AccessEndpointType **   <a name="WorkSpaces-Type-AccessEndpoint-AccessEndpointType"></a>
Indicates the type of access endpoint.
Type: String
Valid Values: `STREAMING_WSP`
Required: No

 ** VpcEndpointId **   <a name="WorkSpaces-Type-AccessEndpoint-VpcEndpointId"></a>
Indicates the VPC endpoint to use for access.
Type: String
Pattern: `^[a-zA-Z0-9\_\-]{1,1000}$`
Required: No

## See Also
<a name="API_AccessEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/AccessEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/AccessEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/AccessEndpoint)
