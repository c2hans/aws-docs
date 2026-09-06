---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReplaceNetworkAclAssociation.html
---

# ReplaceNetworkAclAssociation
<a name="API_ReplaceNetworkAclAssociation"></a>

Changes which network ACL a subnet is associated with. By default when you create a subnet, it's automatically associated with the default network ACL. For more information, see [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) in the *Amazon VPC User Guide*.

This is an idempotent operation.

## Request Parameters
<a name="API_ReplaceNetworkAclAssociation_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AssociationId**
The ID of the current association between the original network ACL and the subnet.
Type: String
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **NetworkAclId**
The ID of the new network ACL to associate with the subnet.
Type: String
Required: Yes

## Response Elements
<a name="API_ReplaceNetworkAclAssociation_ResponseElements"></a>

The following elements are returned by the service.

 **newAssociationId**
The ID of the new association.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_ReplaceNetworkAclAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ReplaceNetworkAclAssociation_Examples"></a>

### Example
<a name="API_ReplaceNetworkAclAssociation_Example_1"></a>

This example starts with a network ACL associated with a subnet, and a corresponding association ID `aclassoc-e5b95c8c`. You want to associate a different network ACL (`acl-5fb85d36`) with the subnet. The result is a new association ID representing the new association.

#### Sample Request
<a name="API_ReplaceNetworkAclAssociation_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ReplaceNetworkAclAssociation
&AssociationId=aclassoc-e5b95c8c
&NetworkAclId=acl-5fb85d36
&AUTHPARAMS
```

#### Sample Response
<a name="API_ReplaceNetworkAclAssociation_Example_1_Response"></a>

```
<ReplaceNetworkAclAssociationResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
   <newAssociationId>aclassoc-17b85d7e</newAssociationId>
</ReplaceNetworkAclAssociationResponse>
```

## See Also
<a name="API_ReplaceNetworkAclAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ReplaceNetworkAclAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ReplaceNetworkAclAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ReplaceNetworkAclAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ReplaceNetworkAclAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ReplaceNetworkAclAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ReplaceNetworkAclAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ReplaceNetworkAclAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ReplaceNetworkAclAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ReplaceNetworkAclAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ReplaceNetworkAclAssociation)
