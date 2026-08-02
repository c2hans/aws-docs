---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcEndpointServicePermissions.html
---

# ModifyVpcEndpointServicePermissions
<a name="API_ModifyVpcEndpointServicePermissions"></a>

Modifies the permissions for your VPC endpoint service. You can add or remove permissions for service consumers (AWS accounts, users, and IAM roles) to connect to your endpoint service. Principal ARNs with path components aren't supported.

If you grant permissions to all principals, the service is public. Any users who know the name of a public service can send a request to attach an endpoint. If the service does not require manual approval, attachments are automatically approved.

## Request Parameters
<a name="API_ModifyVpcEndpointServicePermissions_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AddAllowedPrincipals.N**
The Amazon Resource Names (ARN) of the principals. Permissions are granted to the principals in this list. To grant permissions to all principals, specify an asterisk (\*).
Type: Array of strings
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **RemoveAllowedPrincipals.N**
The Amazon Resource Names (ARN) of the principals. Permissions are revoked for principals in this list.
Type: Array of strings
Required: No

 **ServiceId**
The ID of the service.
Type: String
Required: Yes

## Response Elements
<a name="API_ModifyVpcEndpointServicePermissions_ResponseElements"></a>

The following elements are returned by the service.

 **addedPrincipalSet**
Information about the added principals.
Type: Array of [AddedPrincipal](API_AddedPrincipal.md) objects

 **requestId**
The ID of the request.
Type: String

 **return**
Returns `true` if the request succeeds; otherwise, it returns an error.
Type: Boolean

## Errors
<a name="API_ModifyVpcEndpointServicePermissions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ModifyVpcEndpointServicePermissions_Examples"></a>

### Example
<a name="API_ModifyVpcEndpointServicePermissions_Example_1"></a>

This example permits all principals in AWS account `123456789012` to connect to your endpoint service `vpce-svc-03d5ebb7d9579a2b3`.

#### Sample Request
<a name="API_ModifyVpcEndpointServicePermissions_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyVpcEndpointServicePermissions
&ServiceId=vpce-svc-03d5ebb7d9579a2b3
&AddAllowedPrincipals.1=arn:aws:iam::123456789012:root
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyVpcEndpointServicePermissions_Example_1_Response"></a>

```
<ModifyVpcEndpointServicePermissionsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>08d80840-f750-42db-a6f8-2cd32example</requestId>
    <return>true</return>
</ModifyVpcEndpointServicePermissionsResponse>
```

## See Also
<a name="API_ModifyVpcEndpointServicePermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyVpcEndpointServicePermissions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyVpcEndpointServicePermissions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyVpcEndpointServicePermissions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyVpcEndpointServicePermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyVpcEndpointServicePermissions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyVpcEndpointServicePermissions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyVpcEndpointServicePermissions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyVpcEndpointServicePermissions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyVpcEndpointServicePermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyVpcEndpointServicePermissions)
