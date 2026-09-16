---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetTransitGatewayMulticastDomainAssociations.html
---

# GetTransitGatewayMulticastDomainAssociations
<a name="API_GetTransitGatewayMulticastDomainAssociations"></a>

Gets information about the associations for the transit gateway multicast domain.

## Request Parameters
<a name="API_GetTransitGatewayMulticastDomainAssociations_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
One or more filters. The possible values are:
+  `resource-id` - The ID of the resource.
+  `resource-type` - The type of resource. The valid value is: `vpc`.
+  `state` - The state of the subnet association. Valid values are `associated` \| `associating` \| `disassociated` \| `disassociating`.
+  `subnet-id` - The ID of the subnet.
+  `transit-gateway-attachment-id` - The id of the transit gateway attachment.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MaxResults**
The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned `nextToken` value.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 1000.
Required: No

 **NextToken**
The token for the next page of results.
Type: String
Required: No

 **TransitGatewayMulticastDomainId**
The ID of the transit gateway multicast domain.
Type: String
Required: Yes

## Response Elements
<a name="API_GetTransitGatewayMulticastDomainAssociations_ResponseElements"></a>

The following elements are returned by the service.

 **multicastDomainAssociations**
Information about the multicast domain associations.
Type: Array of [TransitGatewayMulticastDomainAssociation](API_TransitGatewayMulticastDomainAssociation.md) objects

 **nextToken**
The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_GetTransitGatewayMulticastDomainAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_GetTransitGatewayMulticastDomainAssociations_Examples"></a>

### Example 1
<a name="API_GetTransitGatewayMulticastDomainAssociations_Example_1"></a>

This example gets the multicast domain `tgw-attach-028c1dd0f8EXAMPLE` associations.

#### Sample Request
<a name="API_GetTransitGatewayMulticastDomainAssociations_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=GetTransitGatewayMulticastDomainAssociations
&TransitGatewayMulticastDomainId=tgw-attach-028c1dd0f8EXAMPLE
&AUTHPARAMS
```

#### Sample Response
<a name="API_GetTransitGatewayMulticastDomainAssociations_Example_1_Response"></a>

```
<GetTransitGatewayMulticastDomainAssociationsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>ca392437-3f6c-4193-92cd-24404EXAMPLE</requestId>
    <multicastDomainAssociations>
        <item>
            <resourceId>vpc-01128d2c24EXAMPLE</resourceId>
            <resourceType>vpc</resourceType>
            <subnet>
                <state>associated</state>
                <subnetId>subnet-000de86e3bEXAMPLE</subnetId>
            </subnet>
            <transitGatewayAttachmentId>tgw-attach-028c1dd0f8EXAMPLE</transitGatewayAttachmentId>
        </item>
        <item>
            <resourceId>vpc-7EXAMPLE</resourceId>
            <resourceType>vpc</resourceType>
            <subnet>
                <state>associated</state>
                <subnetId>subnet-4EXAMPLE</subnetId>
            </subnet>
            <transitGatewayAttachmentId>tgw-attach-070e571cd1EXAMPLE</transitGatewayAttachmentId>
        </item>
        <item>
            <resourceId>vpc-7f67ec07</resourceId>
            <resourceType>vpc</resourceType>
            <subnet>
                <state>associated</state>
                <subnetId>subnet-5EXAMPLE</subnetId>
            </subnet>
            <transitGatewayAttachmentId>tgw-attach-070e571cd1EXAMPLE</transitGatewayAttachmentId>
        </item>
        <item>
            <resourceId>vpc-7EXAMPLE</resourceId>
            <resourceType>vpc</resourceType>
            <subnet>
                <state>associated</state>
                <subnetId>subnet-aEXAMPLE</subnetId>
            </subnet>
            <transitGatewayAttachmentId>tgw-attach-070e571cd1d3ee8e6</transitGatewayAttachmentId>
        </item>
        <item>
            <resourceId>vpc-7f67ec07</resourceId>
            <resourceType>vpc</resourceType>
            <subnet>
                <state>associated</state>
                <subnetId>subnet-fEXAMPLE</subnetId>
            </subnet>
            <transitGatewayAttachmentId>tgw-attach-070e571cd1EXAMPLE</transitGatewayAttachmentId>
        </item>
    </multicastDomainAssociations>
</GetTransitGatewayMulticastDomainAssociationsResponse>
```

## See Also
<a name="API_GetTransitGatewayMulticastDomainAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetTransitGatewayMulticastDomainAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetTransitGatewayMulticastDomainAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetTransitGatewayMulticastDomainAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetTransitGatewayMulticastDomainAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetTransitGatewayMulticastDomainAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetTransitGatewayMulticastDomainAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetTransitGatewayMulticastDomainAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetTransitGatewayMulticastDomainAssociations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetTransitGatewayMulticastDomainAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetTransitGatewayMulticastDomainAssociations)
