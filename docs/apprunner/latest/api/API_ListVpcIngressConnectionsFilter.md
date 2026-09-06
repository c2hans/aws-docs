---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_ListVpcIngressConnectionsFilter.html
---

# ListVpcIngressConnectionsFilter
<a name="API_ListVpcIngressConnectionsFilter"></a>

Returns a list of VPC Ingress Connections based on the filter provided. It can return either `ServiceArn` or `VpcEndpointId`, or both.

## Contents
<a name="API_ListVpcIngressConnectionsFilter_Contents"></a>

 ** ServiceArn **   <a name="apprunner-Type-ListVpcIngressConnectionsFilter-ServiceArn"></a>
The Amazon Resource Name (ARN) of a service to filter by.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`
Required: No

 ** VpcEndpointId **   <a name="apprunner-Type-ListVpcIngressConnectionsFilter-VpcEndpointId"></a>
The ID of a VPC Endpoint to filter by.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 51200.
Pattern: `.*`
Required: No

## See Also
<a name="API_ListVpcIngressConnectionsFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/ListVpcIngressConnectionsFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/ListVpcIngressConnectionsFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/ListVpcIngressConnectionsFilter)
