---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateSecurityGroup.html
---

# CreateSecurityGroup
<a name="API_CreateSecurityGroup"></a>

Creates a security group.

A security group acts as a virtual firewall for your instance to control inbound and outbound traffic. For more information, see [Amazon EC2 security groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html) in the *Amazon EC2 User Guide* and [Security groups for your VPC](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_SecurityGroups.html) in the *Amazon VPC User Guide*.

When you create a security group, you specify a friendly name of your choice. You can't have two security groups for the same VPC with the same name.

You have a default security group for use in your VPC. If you don't specify a security group when you launch an instance, the instance is launched into the appropriate default security group. A default security group includes a default rule that grants instances unrestricted network access to each other.

You can add or remove rules from your security groups using [AuthorizeSecurityGroupIngress](API_AuthorizeSecurityGroupIngress.md), [AuthorizeSecurityGroupEgress](API_AuthorizeSecurityGroupEgress.md), [RevokeSecurityGroupIngress](API_RevokeSecurityGroupIngress.md), and [RevokeSecurityGroupEgress](API_RevokeSecurityGroupEgress.md).

For more information about VPC security group limits, see [Amazon VPC Limits](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html).

## Request Parameters
<a name="API_CreateSecurityGroup_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **GroupDescription**
A description for the security group.
Constraints: Up to 255 characters in length
Valid characters: a-z, A-Z, 0-9, spaces, and .\_-:/()\#,@[]\+=&;{}\!$\*
Type: String
Required: Yes

 **GroupName**
The name of the security group. Names are case-insensitive and must be unique within the VPC.
Constraints: Up to 255 characters in length. Can't start with `sg-`.
Valid characters: a-z, A-Z, 0-9, spaces, and .\_-:/()\#,@[]\+=&;{}\!$\*
Type: String
Required: Yes

 **TagSpecification.N**
The tags to assign to the security group.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **VpcId**
The ID of the VPC. Required for a nondefault VPC.
Type: String
Required: No

## Response Elements
<a name="API_CreateSecurityGroup_ResponseElements"></a>

The following elements are returned by the service.

 **groupId**
The ID of the security group.
Type: String

 **requestId**
The ID of the request.
Type: String

 **securityGroupArn**
The security group ARN.
Type: String

 **tagSet**
The tags assigned to the security group.
Type: Array of [Tag](API_Tag.md) objects

## Errors
<a name="API_CreateSecurityGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateSecurityGroup_Examples"></a>

### Example
<a name="API_CreateSecurityGroup_Example_1"></a>

This example creates a security group named `WebServerSG` for the specified VPC.

#### Sample Request
<a name="API_CreateSecurityGroup_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateSecurityGroup
&GroupName=WebServerSG
&GroupDescription=Web Servers
&VpcId=vpc-3325caf2
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateSecurityGroup_Example_1_Response"></a>

```
<CreateSecurityGroupResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
   <return>true</return>
   <groupId>sg-0a42d66a</groupId>
</CreateSecurityGroupResponse>
```

## See Also
<a name="API_CreateSecurityGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateSecurityGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateSecurityGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateSecurityGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateSecurityGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateSecurityGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateSecurityGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateSecurityGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateSecurityGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateSecurityGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateSecurityGroup)
