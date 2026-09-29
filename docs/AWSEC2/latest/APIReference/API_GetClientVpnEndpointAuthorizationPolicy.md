---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetClientVpnEndpointAuthorizationPolicy.html
---

# GetClientVpnEndpointAuthorizationPolicy
<a name="API_GetClientVpnEndpointAuthorizationPolicy"></a>

Describes the authorization policy for a Client VPN endpoint.

## Request Parameters
<a name="API_GetClientVpnEndpointAuthorizationPolicy_RequestParameters"></a>

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
<a name="API_GetClientVpnEndpointAuthorizationPolicy_ResponseElements"></a>

The following elements are returned by the service.

 **clientVpnEndpointId**
The ID of the Client VPN endpoint.
Type: String

 **description**
A brief description of the authorization policy.
Type: String

 **policyDocument**
The authorization policy document, written in the Cedar policy language.
Type: String

 **requestId**
The ID of the request.
Type: String

 **shadowMode**
Specifies whether the authorization policy is evaluated in shadow mode. Possible values include:
+  `enabled` - The authorization policy is evaluated and the results are logged, but access is not enforced.
+  `disabled` - The authorization policy is enforced.
Type: String
Valid Values: `enabled | disabled`

 **status**
The current state of the authorization policy.
Type: String
Valid Values: `creating | updating | active | failed | deleting`

## Errors
<a name="API_GetClientVpnEndpointAuthorizationPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_GetClientVpnEndpointAuthorizationPolicy_Examples"></a>

### Example
<a name="API_GetClientVpnEndpointAuthorizationPolicy_Example_1"></a>

This example describes the authorization policy for a Client VPN endpoint.

#### Sample Request
<a name="API_GetClientVpnEndpointAuthorizationPolicy_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=GetClientVpnEndpointAuthorizationPolicy
&ClientVpnEndpointId=cvpn-endpoint-00c5d11fc4EXAMPLE
&AUTHPARAMS
```

#### Sample Response
<a name="API_GetClientVpnEndpointAuthorizationPolicy_Example_1_Response"></a>

```
<GetClientVpnEndpointAuthorizationPolicyResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>691de4ea-32ef-447b-b4f8-d8463EXAMPLE</requestId>
    <clientVpnEndpointId>cvpn-endpoint-00c5d11fc4EXAMPLE</clientVpnEndpointId>
    <policyDocument>permit(principal, action, resource) when { context.crowdstrike.assessment.overall > 80 };</policyDocument>
    <description>Allow devices with a CrowdStrike overall assessment score above 80</description>
    <shadowMode>disabled</shadowMode>
    <status>active</status>
</GetClientVpnEndpointAuthorizationPolicyResponse>
```

## See Also
<a name="API_GetClientVpnEndpointAuthorizationPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetClientVpnEndpointAuthorizationPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetClientVpnEndpointAuthorizationPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetClientVpnEndpointAuthorizationPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetClientVpnEndpointAuthorizationPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetClientVpnEndpointAuthorizationPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetClientVpnEndpointAuthorizationPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetClientVpnEndpointAuthorizationPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetClientVpnEndpointAuthorizationPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetClientVpnEndpointAuthorizationPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetClientVpnEndpointAuthorizationPolicy)
