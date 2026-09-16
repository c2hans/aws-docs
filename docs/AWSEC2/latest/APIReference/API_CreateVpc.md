---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVpc.html
---

# CreateVpc
<a name="API_CreateVpc"></a>

Creates a VPC with the specified CIDR blocks.

A VPC must have an associated IPv4 CIDR block. You can choose an IPv4 CIDR block or an IPAM-allocated IPv4 CIDR block. You can optionally associate an IPv6 CIDR block with a VPC. You can choose an IPv6 CIDR block, an Amazon-provided IPv6 CIDR block, an IPAM-allocated IPv6 CIDR block, or an IPv6 CIDR block that you brought to AWS. For more information, see [IP addressing for your VPCs and subnets](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-ip-addressing.html) in the *Amazon VPC User Guide*.

By default, each instance that you launch in the VPC has the default DHCP options, which include only a default DNS server that we provide (AmazonProvidedDNS). For more information, see [DHCP option sets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html) in the *Amazon VPC User Guide*.

You can specify DNS options and tenancy for a VPC when you create it. You can't change the tenancy of a VPC after you create it. For more information, see [VPC configuration options](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc-options.html) in the *Amazon VPC User Guide*.

## Request Parameters
<a name="API_CreateVpc_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AmazonProvidedIpv6CidrBlock**
Requests an Amazon-provided IPv6 CIDR block with a /56 prefix length for the VPC. You cannot specify the range of IP addresses, or the size of the CIDR block.
Type: Boolean
Required: No

 **CidrBlock**
The IPv4 network range for the VPC, in CIDR notation. For example, `10.0.0.0/16`. We modify the specified CIDR block to its canonical form; for example, if you specify `100.68.0.18/18`, we modify it to `100.68.0.0/18`.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InstanceTenancy**
The tenancy options for instances launched into the VPC. For `default`, instances are launched with shared tenancy by default. You can launch instances with any tenancy into a shared tenancy VPC. For `dedicated`, instances are launched as dedicated tenancy instances by default. You can only launch instances with a tenancy of `dedicated` or `host` into a dedicated tenancy VPC.
 **Important:** The `host` value cannot be used with this parameter. Use the `default` or `dedicated` values only.
Default: `default`
Type: String
Valid Values: `default | dedicated | host`
Required: No

 **Ipv4IpamPoolId**
The ID of an IPv4 IPAM pool you want to use for allocating this VPC's CIDR. For more information, see [What is IPAM?](https://docs.aws.amazon.com/vpc/latest/ipam/what-is-it-ipam.html) in the *Amazon VPC IPAM User Guide*.
Type: String
Required: No

 **Ipv4NetmaskLength**
The netmask length of the IPv4 CIDR you want to allocate to this VPC from an Amazon VPC IP Address Manager (IPAM) pool. For more information about IPAM, see [What is IPAM?](https://docs.aws.amazon.com/vpc/latest/ipam/what-is-it-ipam.html) in the *Amazon VPC IPAM User Guide*.
Type: Integer
Required: No

 **Ipv6CidrBlock**
The IPv6 CIDR block from the IPv6 address pool. You must also specify `Ipv6Pool` in the request.
To let Amazon choose the IPv6 CIDR block for you, omit this parameter.
Type: String
Required: No

 **Ipv6CidrBlockNetworkBorderGroup**
The name of the location from which we advertise the IPV6 CIDR block. Use this parameter to limit the address to this location.
 You must set `AmazonProvidedIpv6CidrBlock` to `true` to use this parameter.
Type: String
Required: No

 **Ipv6IpamPoolId**
The ID of an IPv6 IPAM pool which will be used to allocate this VPC an IPv6 CIDR. IPAM is a VPC feature that you can use to automate your IP address management workflows including assigning, tracking, troubleshooting, and auditing IP addresses across AWS Regions and accounts throughout your AWS Organization. For more information, see [What is IPAM?](https://docs.aws.amazon.com/vpc/latest/ipam/what-is-it-ipam.html) in the *Amazon VPC IPAM User Guide*.
Type: String
Required: No

 **Ipv6NetmaskLength**
The netmask length of the IPv6 CIDR you want to allocate to this VPC from an Amazon VPC IP Address Manager (IPAM) pool. For more information about IPAM, see [What is IPAM?](https://docs.aws.amazon.com/vpc/latest/ipam/what-is-it-ipam.html) in the *Amazon VPC IPAM User Guide*.
Type: Integer
Required: No

 **Ipv6Pool**
The ID of an IPv6 address pool from which to allocate the IPv6 CIDR block.
Type: String
Required: No

 **TagSpecification.N**
The tags to assign to the VPC.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **VpcEncryptionControl**
Specifies the encryption control configuration to apply to the VPC during creation. VPC Encryption Control enables you to enforce encryption for all data in transit within and between VPCs to meet compliance requirements.
For more information, see [Enforce VPC encryption in transit](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-encryption-controls.html) in the *Amazon VPC User Guide*.
Type: [VpcEncryptionControlConfiguration](API_VpcEncryptionControlConfiguration.md) object
Required: No

## Response Elements
<a name="API_CreateVpc_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **vpc**
Information about the VPC.
Type: [Vpc](API_Vpc.md) object

## Errors
<a name="API_CreateVpc_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateVpc_Examples"></a>

### Example 1
<a name="API_CreateVpc_Example_1"></a>

This example creates a VPC with the IPv4 CIDR block `10.0.0.0/16` and a tag with the key set to `tag` and the value set to `example`.

#### Sample Request
<a name="API_CreateVpc_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateVpc
&CidrBlock=10.0.0.0/16
&TagSpecification.1.ResourceType=vpc
&TagSpecification.1.Key=vpc
&TagSpecification.1.Value=example
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateVpc_Example_1_Response"></a>

```
<CreateVpcResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>63c5a2ed-4195-4445-b841-294629e7d8bd</requestId>
    <vpc>
        <vpcId>vpc-06b7830650EXAMPLE</vpcId>
        <ownerId>111122223333</ownerId>
        <state>pending</state>
        <cidrBlock>10.0.0.0/16</cidrBlock>
        <cidrBlockAssociationSet>
            <item>
                <cidrBlock>10.0.0.0/16</cidrBlock>
                <associationId>vpc-cidr-assoc-017043e963EXAMPLE</associationId>
                <cidrBlockState>
                    <state>associated</state>
                </cidrBlockState>
            </item>
        </cidrBlockAssociationSet>
        <ipv6CidrBlockAssociationSet/>
        <dhcpOptionsId>dopt-19edf471</dhcpOptionsId>
        <tagSet/>
        <instanceTenancy>default</instanceTenancy>
        <isDefault>false</isDefault>
        <tagSet>
            <item>
                <key>example</key>
                <value>tag</value>
            </item>
        </tagSet>
    </vpc>
</CreateVpcResponse>
```

### Example 2
<a name="API_CreateVpc_Example_2"></a>

This example creates a VPC with the `dedicated` tenancy option.

#### Sample Request
<a name="API_CreateVpc_Example_2_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateVpc
&CidrBlock=10.32.0.0/16
&InstanceTenancy=dedicated
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateVpc_Example_2_Response"></a>

```
<CreateVpcResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>1d536f17-5a03-4030-95b4-4d051e65e7bb</requestId>
    <vpc>
        <vpcId>vpc-07ddea827dEXAMPLE</vpcId>
        <ownerId>111122223333</ownerId>
        <state>pending</state>
        <cidrBlock>10.32.0.0/16</cidrBlock>
        <cidrBlockAssociationSet>
            <item>
                <cidrBlock>10.32.0.0/16</cidrBlock>
                <associationId>vpc-cidr-assoc-0cc7b90dfeEXAMPLE</associationId>
                <cidrBlockState>
                    <state>associated</state>
                </cidrBlockState>
            </item>
        </cidrBlockAssociationSet>
        <ipv6CidrBlockAssociationSet/>
        <dhcpOptionsId>dopt-19edf471</dhcpOptionsId>
        <tagSet/>
        <instanceTenancy>dedicated</instanceTenancy>
        <isDefault>false</isDefault>
    </vpc>
</CreateVpcResponse>
```

### Example 3
<a name="API_CreateVpc_Example_3"></a>

This example creates a VPC and requests an IPv6 CIDR block for the VPC.

#### Sample Request
<a name="API_CreateVpc_Example_3_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateVpc
&CidrBlock=10.0.0.0/16
&AmazonProvidedIpv6CidrBlock=true
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateVpc_Example_3_Response"></a>

```
<CreateVpcResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>b1a2b2b5-5806-4e24-824b-0c8996c608c1</requestId>
    <vpc>
        <vpcId>vpc-03914afb3ed6c7632</vpcId>
        <ownerId>111122223333</ownerId>
        <state>pending</state>
        <cidrBlock>10.0.0.0/16</cidrBlock>
        <cidrBlockAssociationSet>
            <item>
                <cidrBlock>10.0.0.0/16</cidrBlock>
                <associationId>vpc-cidr-assoc-03ca48bbbeEXAMPLE</associationId>
                <cidrBlockState>
                    <state>associated</state>
                </cidrBlockState>
            </item>
        </cidrBlockAssociationSet>
        <ipv6CidrBlockAssociationSet>
            <item>
                <ipv6CidrBlock></ipv6CidrBlock>
                <associationId>vpc-cidr-assoc-0bd6cc7621EXAMPLE</associationId>
                <ipv6CidrBlockState>
                    <state>associating</state>
                </ipv6CidrBlockState>
            </item>
        </ipv6CidrBlockAssociationSet>
        <dhcpOptionsId>dopt-19edf471</dhcpOptionsId>
        <tagSet/>
        <instanceTenancy>default</instanceTenancy>
        <isDefault>false</isDefault>
    </vpc>
</CreateVpcResponse>
```

### Example 4
<a name="API_CreateVpc_Example_4"></a>

This example creates a VPC and requests an IPv6 CIDR block for the VPC for the specified Network Border Group.

#### Sample Request
<a name="API_CreateVpc_Example_4_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateVpc
&CidrBlock=10.0.0.0/16
&AmazonProvidedIpv6CidrBlock=true
&Ipv6CidrBlockNetworkBorderGroup=us-west-2-lax-1
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateVpc_Example_4_Response"></a>

```
<CreateVpcResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>b1a2b2b5-5806-4e24-824b-0c8996c608c1</requestId>
    <vpc>
        <vpcId>vpc-03914afb3ed6c7632</vpcId>
        <ownerId>111122223333</ownerId>
        <state>pending</state>
        <cidrBlock>10.0.0.0/16</cidrBlock>
        <cidrBlockAssociationSet>
            <item>
                <cidrBlock>10.0.0.0/16</cidrBlock>
                <associationId>vpc-cidr-assoc-03ca48bbbeEXAMPLE</associationId>
                <cidrBlockState>
                    <state>associated</state>
                </cidrBlockState>
            </item>
        </cidrBlockAssociationSet>
        <ipv6CidrBlockAssociationSet>
            <item>
                <ipv6CidrBlock></ipv6CidrBlock>
                <associationId>vpc-cidr-assoc-0bd6cc7621EXAMPLE</associationId>
                <ipv6CidrBlockState>
                    <state>associating</state>
                </ipv6CidrBlockState>
                <Ipv6CidrBlockNetworkBorderGroup>us-west-2-lax-1</Ipv6CidrBlockNetworkBorderGroup>
            </item>
        </ipv6CidrBlockAssociationSet>
        <dhcpOptionsId>dopt-19edf471</dhcpOptionsId>
        <tagSet/>
        <instanceTenancy>default</instanceTenancy>
        <isDefault>false</isDefault>
        <availabilityZone>us-west-2-lax-1a</availabilityZone>
    </vpc>
</CreateVpcResponse>
```

## See Also
<a name="API_CreateVpc_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateVpc)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateVpc)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateVpc)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateVpc)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateVpc)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateVpc)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateVpc)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateVpc)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateVpc)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateVpc)
