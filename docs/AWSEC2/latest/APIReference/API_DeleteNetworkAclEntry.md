---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteNetworkAclEntry.html
---

# DeleteNetworkAclEntry
<a name="API_DeleteNetworkAclEntry"></a>

Deletes the specified ingress or egress entry (rule) from the specified network ACL.

## Request Parameters
<a name="API_DeleteNetworkAclEntry_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Egress**
Indicates whether the rule is an egress rule.
Type: Boolean
Required: Yes

 **NetworkAclId**
The ID of the network ACL.
Type: String
Required: Yes

 **RuleNumber**
The rule number of the entry to delete.
Type: Integer
Required: Yes

## Response Elements
<a name="API_DeleteNetworkAclEntry_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **return**
Is `true` if the request succeeds, and an error otherwise.
Type: Boolean

## Errors
<a name="API_DeleteNetworkAclEntry_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DeleteNetworkAclEntry_Examples"></a>

### Example
<a name="API_DeleteNetworkAclEntry_Example_1"></a>

This example deletes ingress rule number 100 from the specified network ACL.

#### Sample Request
<a name="API_DeleteNetworkAclEntry_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DeleteNetworkAclEntry
&NetworkAclId=acl-2cb85d45
&RuleNumber=100
&AUTHPARAMS
```

#### Sample Response
<a name="API_DeleteNetworkAclEntry_Example_1_Response"></a>

```
<DeleteNetworkAclEntryResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
   <requestId>59dbff89-35bd-4eac-99ed-be587EXAMPLE</requestId>
   <return>true</return>
</DeleteNetworkAclEntryResponse>
```

## See Also
<a name="API_DeleteNetworkAclEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DeleteNetworkAclEntry)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DeleteNetworkAclEntry)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeleteNetworkAclEntry)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DeleteNetworkAclEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeleteNetworkAclEntry)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DeleteNetworkAclEntry)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DeleteNetworkAclEntry)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DeleteNetworkAclEntry)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DeleteNetworkAclEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeleteNetworkAclEntry)
