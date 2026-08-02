---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_VpcEndpoint.html
---

# VpcEndpoint
<a name="API_VpcEndpoint"></a>

The connection endpoint for connecting to Amazon Redshift Serverless through the proxy.

## Contents
<a name="API_VpcEndpoint_Contents"></a>

 ** networkInterfaces **   <a name="redshiftserverless-Type-VpcEndpoint-networkInterfaces"></a>
One or more network interfaces of the endpoint. Also known as an interface endpoint.
Type: Array of [NetworkInterface](API_NetworkInterface.md) objects
Required: No

 ** vpcEndpointId **   <a name="redshiftserverless-Type-VpcEndpoint-vpcEndpointId"></a>
The connection endpoint ID for connecting to Amazon Redshift Serverless.
Type: String
Required: No

 ** vpcId **   <a name="redshiftserverless-Type-VpcEndpoint-vpcId"></a>
The VPC identifier that the endpoint is associated with.
Type: String
Required: No

## See Also
<a name="API_VpcEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/VpcEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/VpcEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/VpcEndpoint)
