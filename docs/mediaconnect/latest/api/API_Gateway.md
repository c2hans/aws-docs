---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_Gateway.html
---

# Gateway
<a name="API_Gateway"></a>

The settings for a gateway, including its networks.

## Contents
<a name="API_Gateway_Contents"></a>

 ** egressCidrBlocks **   <a name="mediaconnect-Type-Gateway-egressCidrBlocks"></a>
 The range of IP addresses that contribute content or initiate output requests for flows communicating with this gateway. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
Type: Array of strings
Required: Yes

 ** gatewayArn **   <a name="mediaconnect-Type-Gateway-gatewayArn"></a>
 The Amazon Resource Name (ARN) of the gateway.
Type: String
Required: Yes

 ** name **   <a name="mediaconnect-Type-Gateway-name"></a>
 The name of the gateway. This name can not be modified after the gateway is created.
Type: String
Required: Yes

 ** networks **   <a name="mediaconnect-Type-Gateway-networks"></a>
 The list of networks in the gateway.
Type: Array of [GatewayNetwork](API_GatewayNetwork.md) objects
Required: Yes

 ** gatewayMessages **   <a name="mediaconnect-Type-Gateway-gatewayMessages"></a>
Messages with information about the gateway.
Type: Array of [MessageDetail](API_MessageDetail.md) objects
Required: No

 ** gatewayState **   <a name="mediaconnect-Type-Gateway-gatewayState"></a>
 The current status of the gateway.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | ERROR | DELETING | DELETED`
Required: No

## See Also
<a name="API_Gateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/Gateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/Gateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/Gateway)
