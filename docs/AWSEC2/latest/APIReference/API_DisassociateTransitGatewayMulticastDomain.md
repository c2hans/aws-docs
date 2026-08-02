---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateTransitGatewayMulticastDomain.html
---

# DisassociateTransitGatewayMulticastDomain
<a name="API_DisassociateTransitGatewayMulticastDomain"></a>

Disassociates the specified subnets from the transit gateway multicast domain.

## Request Parameters
<a name="API_DisassociateTransitGatewayMulticastDomain_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **SubnetIds.N**
The IDs of the subnets;
Type: Array of strings
Required: Yes

 **TransitGatewayAttachmentId**
The ID of the attachment.
Type: String
Required: Yes

 **TransitGatewayMulticastDomainId**
The ID of the transit gateway multicast domain.
Type: String
Required: Yes

## Response Elements
<a name="API_DisassociateTransitGatewayMulticastDomain_ResponseElements"></a>

The following elements are returned by the service.

 **associations**
Information about the association.
Type: [TransitGatewayMulticastDomainAssociations](API_TransitGatewayMulticastDomainAssociations.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DisassociateTransitGatewayMulticastDomain_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DisassociateTransitGatewayMulticastDomain_Examples"></a>

### Example 1
<a name="API_DisassociateTransitGatewayMulticastDomain_Example_1"></a>

This example disassociates the subnet `subnet-000de86e3bEXAMPLE` from the multicast domain `tgw-mcast-domain-0c4905cef7EXAMPLE`.

#### Sample Request
<a name="API_DisassociateTransitGatewayMulticastDomain_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DisassociateTransitGatewayMulticastDomain
&TransitGatewayAttachmentId=tgw-attach-070e571cd1EXAMPLE
&SubnetId=subnet-000de86e3bEXAMPLE
&TransitGatewayMulticastDomainId=tgw-mcast-domain-0c4905cef7EXAMPLE
&AUTHPARAMS
```

#### Sample Response
<a name="API_DisassociateTransitGatewayMulticastDomain_Example_1_Response"></a>

```
<DisassociateTransitGatewayMulticastDomainResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>0008db4a-b98a-46f7-b047-e262aEXAMPLE</requestId>
    <associations>
        <resourceId>vpc-7EXAMPLE</resourceId>
        <resourceType>vpc</resourceType>
        <subnets>
            <item>
                <state>disassociating</state>
                <subnetId>subnet-000de86e3bEXAMPLE</subnetId>
            </item>
        </subnets>
        <transitGatewayAttachmentId>tgw-attach-070e571cd1EXAMPLE</transitGatewayAttachmentId>
        <transitGatewayMulticastDomainId>tgw-mcast-domain-0c4905cef7EXAMPLE</transitGatewayMulticastDomainId>
    </associations>
</DisassociateTransitGatewayMulticastDomainResponse>
```

## See Also
<a name="API_DisassociateTransitGatewayMulticastDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DisassociateTransitGatewayMulticastDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DisassociateTransitGatewayMulticastDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DisassociateTransitGatewayMulticastDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DisassociateTransitGatewayMulticastDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DisassociateTransitGatewayMulticastDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DisassociateTransitGatewayMulticastDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DisassociateTransitGatewayMulticastDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DisassociateTransitGatewayMulticastDomain)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DisassociateTransitGatewayMulticastDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DisassociateTransitGatewayMulticastDomain)
