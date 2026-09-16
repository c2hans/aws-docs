---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateNetworkAcl.html
---

# CreateNetworkAcl
<a name="API_CreateNetworkAcl"></a>

Creates a network ACL in a VPC. Network ACLs provide an optional layer of security (in addition to security groups) for the instances in your VPC.

For more information, see [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) in the *Amazon VPC User Guide*.

## Request Parameters
<a name="API_CreateNetworkAcl_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **TagSpecification.N**
The tags to assign to the network ACL.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

 **VpcId**
The ID of the VPC.
Type: String
Required: Yes

## Response Elements
<a name="API_CreateNetworkAcl_ResponseElements"></a>

The following elements are returned by the service.

 **clientToken**
Unique, case-sensitive identifier to ensure the idempotency of the request. Only returned if a client token was provided in the request.
Type: String

 **networkAcl**
Information about the network ACL.
Type: [NetworkAcl](API_NetworkAcl.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CreateNetworkAcl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_CreateNetworkAcl_Examples"></a>

### Example
<a name="API_CreateNetworkAcl_Example_1"></a>

This example creates a network ACL in the specified IPv6-enabled VPC. The response includes default IPv4 and IPv6 entries for egress and ingress traffic, each with a high rule number. These are the last entries we process to decide whether traffic is allowed in or out of an associated subnet. If the traffic doesn't match any rules with a lower rule number, then these default entries ultimately deny the traffic.

#### Sample Request
<a name="API_CreateNetworkAcl_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=CreateNetworkAcl
&VpcId=vpc-11ad4878
&AUTHPARAMS
```

#### Sample Response
<a name="API_CreateNetworkAcl_Example_1_Response"></a>

```
<CreateNetworkAclResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
   <networkAcl>
      <networkAclId>acl-5fb85d36</networkAclId>
      <vpcId>vpc-11ad4878</vpcId>
      <default>false</default>
      <entrySet>
         <item>
            <ruleNumber>32767</ruleNumber>
            <protocol>all</protocol>
            <ruleAction>deny</ruleAction>
            <egress>true</egress>
            <cidrBlock>0.0.0.0/0</cidrBlock>
         </item>
         <item>
            <ruleNumber>32767</ruleNumber>
            <protocol>all</protocol>
            <ruleAction>deny</ruleAction>
            <egress>false</egress>
            <cidrBlock>0.0.0.0/0</cidrBlock>
         </item>
        <item>
           <ruleNumber>32768</ruleNumber>
           <protocol>all</protocol>
           <ruleAction>deny</ruleAction>
           <egress>true</egress>
           <ipv6CidrBlock>::/0</ipv6CidrBlock>
        </item>
        <item>
           <ruleNumber>32768</ruleNumber>
           <protocol>all</protocol>
           <ruleAction>deny</ruleAction>
           <egress>false</egress>
           <ipv6CidrBlock>::/0</ipv6CidrBlock>
        </item>
      </entrySet>
      <associationSet/>
      <tagSet/>
   </networkAcl>
</CreateNetworkAclResponse>
```

## See Also
<a name="API_CreateNetworkAcl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateNetworkAcl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateNetworkAcl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateNetworkAcl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateNetworkAcl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateNetworkAcl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateNetworkAcl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateNetworkAcl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateNetworkAcl)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateNetworkAcl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateNetworkAcl)
