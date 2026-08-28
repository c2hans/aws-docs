---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeClientVpnIngress.html
---

# AuthorizeClientVpnIngress
<a name="API_AuthorizeClientVpnIngress"></a>

Adds an ingress authorization rule to a Client VPN endpoint. Ingress authorization rules act as firewall rules that grant access to networks. You must configure ingress authorization rules to enable clients to access resources in AWS or on-premises networks.

## Request Parameters
<a name="API_AuthorizeClientVpnIngress_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AccessGroupId**
The ID of the group to grant access to, for example, the Active Directory group or identity provider (IdP) group. Required if `AuthorizeAllGroups` is `false` or not specified.
Type: String
Required: No

 **AuthorizeAllGroups**
Indicates whether to grant access to all clients. Specify `true` to grant all clients who successfully establish a VPN connection access to the network. Must be set to `true` if `AccessGroupId` is not specified.
Type: Boolean
Required: No

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Required: No

 **ClientVpnEndpointId**
The ID of the Client VPN endpoint.
Type: String
Required: Yes

 **Description**
A brief description of the authorization rule.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **TargetNetworkCidr**
The IPv4 address range, in CIDR notation, of the network for which access is being authorized.
Type: String
Required: Yes

## Response Elements
<a name="API_AuthorizeClientVpnIngress_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **status**
The current state of the authorization rule.
Type: [ClientVpnAuthorizationRuleStatus](API_ClientVpnAuthorizationRuleStatus.md) object

## Errors
<a name="API_AuthorizeClientVpnIngress_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_AuthorizeClientVpnIngress_Examples"></a>

### Example
<a name="API_AuthorizeClientVpnIngress_Example_1"></a>

This example adds an authorization rule to a subnet and grants access to all users.

#### Sample Request
<a name="API_AuthorizeClientVpnIngress_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=AuthorizeClientVpnIngress
&ClientVpnEndpointId=cvpn-endpoint-00c5d11fc4EXAMPLE
&TargetNetworkCidr=10.0.0.0/16
&AuthorizeAllGroups=true
&AUTHPARAMS
```

#### Sample Response
<a name="API_AuthorizeClientVpnIngress_Example_1_Response"></a>

```
<AuthorizeClientVpnIngressResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>afafad8c-274c-4584-bbd1-75a21EXAMPLE</requestId>
    <status>
        <code>authorizing</code>
    </status>
</AuthorizeClientVpnIngressResponse>
```

## See Also
<a name="API_AuthorizeClientVpnIngress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/AuthorizeClientVpnIngress)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/AuthorizeClientVpnIngress)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AuthorizeClientVpnIngress)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/AuthorizeClientVpnIngress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AuthorizeClientVpnIngress)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/AuthorizeClientVpnIngress)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/AuthorizeClientVpnIngress)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/AuthorizeClientVpnIngress)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/AuthorizeClientVpnIngress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AuthorizeClientVpnIngress)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
