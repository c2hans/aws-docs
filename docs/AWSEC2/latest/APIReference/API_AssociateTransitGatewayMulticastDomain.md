---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateTransitGatewayMulticastDomain.html
---

# AssociateTransitGatewayMulticastDomain
<a name="API_AssociateTransitGatewayMulticastDomain"></a>

Associates the specified subnets and transit gateway attachments with the specified transit gateway multicast domain.

The transit gateway attachment must be in the available state before you can add a resource. Use [DescribeTransitGatewayAttachments](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGatewayAttachments.html) to see the state of the attachment.

## Request Parameters
<a name="API_AssociateTransitGatewayMulticastDomain_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **SubnetIds.N**
The IDs of the subnets to associate with the transit gateway multicast domain.
Type: Array of strings
Required: Yes

 **TransitGatewayAttachmentId**
The ID of the transit gateway attachment to associate with the transit gateway multicast domain.
Type: String
Required: Yes

 **TransitGatewayMulticastDomainId**
The ID of the transit gateway multicast domain.
Type: String
Required: Yes

## Response Elements
<a name="API_AssociateTransitGatewayMulticastDomain_ResponseElements"></a>

The following elements are returned by the service.

 **associations**
Information about the transit gateway multicast domain associations.
Type: [TransitGatewayMulticastDomainAssociations](API_TransitGatewayMulticastDomainAssociations.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_AssociateTransitGatewayMulticastDomain_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_AssociateTransitGatewayMulticastDomain_Examples"></a>

### Example 1
<a name="API_AssociateTransitGatewayMulticastDomain_Example_1"></a>

This example associates the transit gateway attachment `tgw-attach-028c1dd0f8EXAMPLE` with the multicast domain `tgw-mcast-domain-0c4905cef7EXAMPLE`.

#### Sample Request
<a name="API_AssociateTransitGatewayMulticastDomain_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=AssociateTransitGatewayMulticastDomain
&TransitGatewayAttachmentId=tgw-attach-028c1dd0f8EXAMPLE
&TransitGatewayMulticastDomainId=tgw-mcast-domain-0c4905cef7EXAMPLE
&AUTHPARAMS
```

#### Sample Response
<a name="API_AssociateTransitGatewayMulticastDomain_Example_1_Response"></a>

```
<AssociateTransitGatewayMulticastDomainResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>fa968e66-0290-4479-a8ca-e5c83EXAMPLE</requestId>
    <associations>
        <resourceId>vpc-01128d2c24EXAMPLE</resourceId>
        <resourceType>vpc</resourceType>
        <subnets>
            <item>
                <state>associating</state>
                <subnetId>subnet-000de86e3bEXAMPLE</subnetId>
            </item>
        </subnets>
        <transitGatewayAttachmentId>tgw-attach-028c1dd0f8EXAMPLE</transitGatewayAttachmentId>
        <transitGatewayMulticastDomainId>tgw-mcast-domain-0c4905cef7EXAMPLE</transitGatewayMulticastDomainId>
    </associations>
</AssociateTransitGatewayMulticastDomainResponse>
```

## See Also
<a name="API_AssociateTransitGatewayMulticastDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/AssociateTransitGatewayMulticastDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/AssociateTransitGatewayMulticastDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AssociateTransitGatewayMulticastDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/AssociateTransitGatewayMulticastDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AssociateTransitGatewayMulticastDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/AssociateTransitGatewayMulticastDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/AssociateTransitGatewayMulticastDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/AssociateTransitGatewayMulticastDomain)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/AssociateTransitGatewayMulticastDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AssociateTransitGatewayMulticastDomain)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
