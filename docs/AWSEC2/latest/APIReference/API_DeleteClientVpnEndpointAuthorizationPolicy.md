---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteClientVpnEndpointAuthorizationPolicy.html
---

# DeleteClientVpnEndpointAuthorizationPolicy
<a name="API_DeleteClientVpnEndpointAuthorizationPolicy"></a>

Deletes the authorization policy for a Client VPN endpoint.

## Request Parameters
<a name="API_DeleteClientVpnEndpointAuthorizationPolicy_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientVpnEndpointId**
The ID of the Client VPN endpoint.
Type: String
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

## Response Elements
<a name="API_DeleteClientVpnEndpointAuthorizationPolicy_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **status**
The current state of the authorization policy.
Type: String
Valid Values: `creating | updating | active | failed | deleting`

## Errors
<a name="API_DeleteClientVpnEndpointAuthorizationPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DeleteClientVpnEndpointAuthorizationPolicy_Examples"></a>

### Example
<a name="API_DeleteClientVpnEndpointAuthorizationPolicy_Example_1"></a>

This example deletes the authorization policy for a Client VPN endpoint.

#### Sample Request
<a name="API_DeleteClientVpnEndpointAuthorizationPolicy_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DeleteClientVpnEndpointAuthorizationPolicy
&ClientVpnEndpointId=cvpn-endpoint-00c5d11fc4EXAMPLE
&AUTHPARAMS
```

#### Sample Response
<a name="API_DeleteClientVpnEndpointAuthorizationPolicy_Example_1_Response"></a>

```
<DeleteClientVpnEndpointAuthorizationPolicyResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>00d80748-708d-40f7-8635-f34acEXAMPLE</requestId>
    <status>deleting</status>
</DeleteClientVpnEndpointAuthorizationPolicyResponse>
```

## See Also
<a name="API_DeleteClientVpnEndpointAuthorizationPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DeleteClientVpnEndpointAuthorizationPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DeleteClientVpnEndpointAuthorizationPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeleteClientVpnEndpointAuthorizationPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DeleteClientVpnEndpointAuthorizationPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeleteClientVpnEndpointAuthorizationPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DeleteClientVpnEndpointAuthorizationPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DeleteClientVpnEndpointAuthorizationPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DeleteClientVpnEndpointAuthorizationPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DeleteClientVpnEndpointAuthorizationPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeleteClientVpnEndpointAuthorizationPolicy)
