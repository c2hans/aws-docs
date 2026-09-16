---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTransitGatewayMulticastDomain.html
---

# CreateTransitGatewayMulticastDomain
<a name="API_CreateTransitGatewayMulticastDomain"></a>

Creates a multicast domain using the specified transit gateway.

The transit gateway must be in the available state before you create a domain. Use [DescribeTransitGateways](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGateways.html) to see the state of transit gateway.

## Request Parameters
<a name="API_CreateTransitGatewayMulticastDomain_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Options**
The options for the transit gateway multicast domain.
Type: [CreateTransitGatewayMulticastDomainRequestOptions](API_CreateTransitGatewayMulticastDomainRequestOptions.md) object
Required: No

 **TagSpecification.N**
The tags for the transit gateway multicast domain.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **TransitGatewayId**
The ID of the transit gateway.
Type: String
Required: Yes

## Response Elements
<a name="API_CreateTransitGatewayMulticastDomain_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **transitGatewayMulticastDomain**
Information about the transit gateway multicast domain.
Type: [TransitGatewayMulticastDomain](API_TransitGatewayMulticastDomain.md) object

## Errors
<a name="API_CreateTransitGatewayMulticastDomain_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateTransitGatewayMulticastDomain_Examples"></a>

### Example 1
<a name="API_CreateTransitGatewayMulticastDomain_Example_1"></a>

This example creates a multicast domain for the specified transit gateway.

#### Sample Request
<a name="API_CreateTransitGatewayMulticastDomain_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateTransitMulticastDomain
&TransitGatewayId=tgw-0d88d2d0d5EXAMPLE
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateTransitGatewayMulticastDomain_Example_1_Response"></a>

```
<CreateTransitGatewayMulticastDomainResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>763fb04b-258f-4710-8f91-b202aEXAMPLE</requestId>
    <transitGatewayMulticastDomain>
        <creationTime>2019-11-20T22:02:03.000Z</creationTime>
        <state>pending</state>
        <transitGatewayId>tgw-0d88d2d0d5EXAMPLE</transitGatewayId>
        <transitGatewayMulticastDomainId>tgw-mcast-domain-02bb79002EXAMPLE</transitGatewayMulticastDomainId>
    </transitGatewayMulticastDomain>
</CreateTransitGatewayMulticastDomainResponse>
```

## See Also
<a name="API_CreateTransitGatewayMulticastDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateTransitGatewayMulticastDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateTransitGatewayMulticastDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateTransitGatewayMulticastDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateTransitGatewayMulticastDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateTransitGatewayMulticastDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateTransitGatewayMulticastDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateTransitGatewayMulticastDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateTransitGatewayMulticastDomain)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateTransitGatewayMulticastDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateTransitGatewayMulticastDomain)
