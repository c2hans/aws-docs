---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_EndpointDetails.html
---

# EndpointDetails
<a name="API_EndpointDetails"></a>

The virtual private cloud (VPC) endpoint settings that are configured for your file transfer protocol-enabled server. With a VPC endpoint, you can restrict access to your server and resources only within your VPC. To control incoming internet traffic, invoke the `UpdateServer` API and attach an Elastic IP address to your server's endpoint.

**Note**
 After May 19, 2021, you won't be able to create a server using `EndpointType=VPC_ENDPOINT` in your AWS account if your account hasn't already done so before May 19, 2021. If you have already created servers with `EndpointType=VPC_ENDPOINT` in your AWS account on or before May 19, 2021, you will not be affected. After this date, use `EndpointType`=`VPC`.
For more information, see [Discontinuing the use of VPC\_ENDPOINT](https://docs.aws.amazon.com/transfer/latest/userguide/create-server-in-vpc.html#deprecate-vpc-endpoint).
It is recommended that you use `VPC` as the `EndpointType`. With this endpoint type, you have the option to directly associate up to three Elastic IPv4 addresses (BYO IP included) with your server's endpoint and use VPC security groups to restrict traffic by the client's public IP address. This is not possible with `EndpointType` set to `VPC_ENDPOINT`.

## Contents
<a name="API_EndpointDetails_Contents"></a>

 ** AddressAllocationIds **   <a name="TransferFamily-Type-EndpointDetails-AddressAllocationIds"></a>
A list of address allocation IDs that are required to attach an Elastic IP address to your server's endpoint.
An address allocation ID corresponds to the allocation ID of an Elastic IP address. This value can be retrieved from the `allocationId` field from the Amazon EC2 [Address](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Address.html) data type. One way to retrieve this value is by calling the EC2 [DescribeAddresses](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAddresses.html) API.
This parameter is optional. Set this parameter if you want to make your VPC endpoint public-facing. For details, see [Create an internet-facing endpoint for your server](https://docs.aws.amazon.com/transfer/latest/userguide/create-server-in-vpc.html#create-internet-facing-endpoint).
This property can only be set as follows:
+  `EndpointType` must be set to `VPC`
+ The Transfer Family server must be offline.
+ You cannot set this parameter for Transfer Family servers that use the FTP protocol.
+ The server must already have `SubnetIds` populated (`SubnetIds` and `AddressAllocationIds` cannot be updated simultaneously).
+  `AddressAllocationIds` can't contain duplicates, and must be equal in length to `SubnetIds`. For example, if you have three subnet IDs, you must also specify three address allocation IDs.
+ Call the `UpdateServer` API to set or change this parameter.
+ You can't set address allocation IDs for servers that have an `IpAddressType` set to `DUALSTACK` You can only set this property if `IpAddressType` is set to `IPV4`.
Type: Array of strings
Required: No

 ** SecurityGroupIds **   <a name="TransferFamily-Type-EndpointDetails-SecurityGroupIds"></a>
A list of security groups IDs that are available to attach to your server's endpoint.
While `SecurityGroupIds` appears in the response syntax for consistency with `CreateServer` and `UpdateServer` operations, this field is not populated in `DescribeServer` responses. Security groups are managed at the VPC endpoint level and can be modified outside of the Transfer Family service. To retrieve current security group information, use the EC2 `DescribeVpcEndpoints` API with the `VpcEndpointId` returned in the response.
This property can only be set when `EndpointType` is set to `VPC`.
You can edit the `SecurityGroupIds` property in the [UpdateServer](https://docs.aws.amazon.com/transfer/latest/userguide/API_UpdateServer.html) API only if you are changing the `EndpointType` from `PUBLIC` or `VPC_ENDPOINT` to `VPC`. To change security groups associated with your server's VPC endpoint after creation, use the Amazon EC2 [ModifyVpcEndpoint](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcEndpoint.html) API.
Type: Array of strings
Length Constraints: Minimum length of 11. Maximum length of 20.
Pattern: `sg-[0-9a-f]{8,17}`
Required: No

 ** SubnetIds **   <a name="TransferFamily-Type-EndpointDetails-SubnetIds"></a>
A list of subnet IDs that are required to host your server endpoint in your VPC.
This property can only be set when `EndpointType` is set to `VPC`.
Type: Array of strings
Required: No

 ** VpcEndpointId **   <a name="TransferFamily-Type-EndpointDetails-VpcEndpointId"></a>
The identifier of the VPC endpoint.
This property can only be set when `EndpointType` is set to `VPC_ENDPOINT`.
For more information, see [Discontinuing the use of VPC\_ENDPOINT](https://docs.aws.amazon.com/transfer/latest/userguide/create-server-in-vpc.html#deprecate-vpc-endpoint).
Type: String
Length Constraints: Fixed length of 22.
Pattern: `vpce-[0-9a-f]{17}`
Required: No

 ** VpcId **   <a name="TransferFamily-Type-EndpointDetails-VpcId"></a>
The VPC identifier of the VPC in which a server's endpoint will be hosted.
This property can only be set when `EndpointType` is set to `VPC`.
Type: String
Required: No

## See Also
<a name="API_EndpointDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/EndpointDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/EndpointDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/EndpointDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transfer Family. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transfer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
