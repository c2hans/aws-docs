---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateDefaultSubnet.html
---

# CreateDefaultSubnet
<a name="API_CreateDefaultSubnet"></a>

Creates a default subnet with a size `/20` IPv4 CIDR block in the specified Availability Zone in your default VPC. You can have only one default subnet per Availability Zone. For more information, see [Create a default subnet](https://docs.aws.amazon.com/vpc/latest/userguide/work-with-default-vpc.html#create-default-subnet) in the *Amazon VPC User Guide*.

## Request Parameters
<a name="API_CreateDefaultSubnet_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AvailabilityZone**
The Availability Zone in which to create the default subnet.
Either `AvailabilityZone` or `AvailabilityZoneId` must be specified, but not both.
Type: String
Required: No

 **AvailabilityZoneId**
The ID of the Availability Zone.
Either `AvailabilityZone` or `AvailabilityZoneId` must be specified, but not both.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Ipv6Native**
Indicates whether to create an IPv6 only subnet. If you already have a default subnet for this Availability Zone, you must delete it before you can create an IPv6 only subnet.
Type: Boolean
Required: No

## Response Elements
<a name="API_CreateDefaultSubnet_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **subnet**
Information about the subnet.
Type: [Subnet](API_Subnet.md) object

## Errors
<a name="API_CreateDefaultSubnet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateDefaultSubnet_Examples"></a>

### Example
<a name="API_CreateDefaultSubnet_Example_1"></a>

This example creates a default subnet in Availability Zone `us-east-2a`.

#### Sample Request
<a name="API_CreateDefaultSubnet_Example_1_Request"></a>

```
https://ec2.us-east-2.amazonaws.com/?Action=CreateDefaultSubnet
&AvailabilityZone=us-east-2a
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateDefaultSubnet_Example_1_Response"></a>

```
<CreateDefaultSubnetResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>12e2fb2e-e566-488a-926d-4655example</requestId>
    <subnet>
        <assignIpv6AddressOnCreation>false</assignIpv6AddressOnCreation>
        <availabilityZone>us-east-2a</availabilityZone>
        <availableIpAddressCount>4091</availableIpAddressCount>
        <cidrBlock>172.31.32.0/20</cidrBlock>
        <defaultForAz>true</defaultForAz>
        <ipv6CidrBlockAssociationSet/>
        <mapPublicIpOnLaunch>true</mapPublicIpOnLaunch>
        <state>available</state>
        <subnetId>subnet-111f7123</subnetId>
        <tagSet/>
        <vpcId>vpc-8eaaeabc</vpcId>
    </subnet>
</CreateDefaultSubnetResponse>
```

## See Also
<a name="API_CreateDefaultSubnet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateDefaultSubnet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateDefaultSubnet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateDefaultSubnet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateDefaultSubnet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateDefaultSubnet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateDefaultSubnet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateDefaultSubnet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateDefaultSubnet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateDefaultSubnet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateDefaultSubnet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
