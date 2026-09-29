---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyClientVpnEndpointAuthorizationPolicy.html
---

# ModifyClientVpnEndpointAuthorizationPolicy
<a name="API_ModifyClientVpnEndpointAuthorizationPolicy"></a>

Creates or updates the authorization policy for a Client VPN endpoint. A Client VPN endpoint can have one authorization policy. If a policy already exists for the endpoint, the values that you specify replace the corresponding values in the existing policy, and values that you do not specify remain unchanged.

## Request Parameters
<a name="API_ModifyClientVpnEndpointAuthorizationPolicy_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Required: No

 **ClientVpnEndpointId**
The ID of the Client VPN endpoint.
Type: String
Required: Yes

 **Description**
A brief description of the authorization policy.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **PolicyDocument**
The authorization policy document, written in the Cedar policy language. This parameter is required when you create the authorization policy for a Client VPN endpoint that does not already have one.
Type: String
Required: No

 **ShadowMode**
Specifies whether the authorization policy is evaluated in shadow mode. Possible values include:
+  `enabled` - The authorization policy is evaluated and the results are logged, but access is not enforced.
+  `disabled` - The authorization policy is enforced.
The default value is `disabled`.
Type: String
Valid Values: `enabled | disabled`
Required: No

## Response Elements
<a name="API_ModifyClientVpnEndpointAuthorizationPolicy_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **status**
The current state of the authorization policy.
Type: String
Valid Values: `creating | updating | active | failed | deleting`

## Errors
<a name="API_ModifyClientVpnEndpointAuthorizationPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_ModifyClientVpnEndpointAuthorizationPolicy_Examples"></a>

### Example
<a name="API_ModifyClientVpnEndpointAuthorizationPolicy_Example_1"></a>

This example creates or updates the authorization policy for a Client VPN endpoint.

#### Sample Request
<a name="API_ModifyClientVpnEndpointAuthorizationPolicy_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=ModifyClientVpnEndpointAuthorizationPolicy
&ClientVpnEndpointId=cvpn-endpoint-00c5d11fc4EXAMPLE
&PolicyDocument=permit(principal,%20action,%20resource)%20when%20%7B%20context.crowdstrike.assessment.overall%20%3E%2080%20%7D;
&ShadowMode=disabled
&AUTHPARAMS
```

#### Sample Response
<a name="API_ModifyClientVpnEndpointAuthorizationPolicy_Example_1_Response"></a>

```
<ModifyClientVpnEndpointAuthorizationPolicyResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>5ef84b7f-505e-4e39-80cd-a11dbEXAMPLE</requestId>
    <status>updating</status>
</ModifyClientVpnEndpointAuthorizationPolicyResponse>
```

## See Also
<a name="API_ModifyClientVpnEndpointAuthorizationPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyClientVpnEndpointAuthorizationPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyClientVpnEndpointAuthorizationPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyClientVpnEndpointAuthorizationPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyClientVpnEndpointAuthorizationPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyClientVpnEndpointAuthorizationPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyClientVpnEndpointAuthorizationPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyClientVpnEndpointAuthorizationPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyClientVpnEndpointAuthorizationPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyClientVpnEndpointAuthorizationPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyClientVpnEndpointAuthorizationPolicy)
