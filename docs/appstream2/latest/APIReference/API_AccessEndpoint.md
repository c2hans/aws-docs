---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_AccessEndpoint.html
---

# AccessEndpoint
<a name="API_AccessEndpoint"></a>

Describes an interface VPC endpoint (interface endpoint) that lets you create a private connection between the virtual private cloud (VPC) that you specify and WorkSpaces Applications. When you specify an interface endpoint for a stack, users of the stack can connect to WorkSpaces Applications only through that endpoint. When you specify an interface endpoint for an image builder, administrators can connect to the image builder only through that endpoint.

## Contents
<a name="API_AccessEndpoint_Contents"></a>

 ** EndpointType **   <a name="WorkSpacesApplications-Type-AccessEndpoint-EndpointType"></a>
The type of interface endpoint.
Type: String
Valid Values: `STREAMING`
Required: Yes

 ** VpceId **   <a name="WorkSpacesApplications-Type-AccessEndpoint-VpceId"></a>
The identifier (ID) of the VPC in which the interface endpoint is used.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_AccessEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/AccessEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/AccessEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/AccessEndpoint)
