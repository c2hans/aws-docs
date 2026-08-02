---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_AssociateThirdPartyFirewall.html
---

# AssociateThirdPartyFirewall
<a name="API_AssociateThirdPartyFirewall"></a>

Sets the Firewall Manager policy administrator as a tenant administrator of a third-party firewall service. A tenant is an instance of the third-party firewall service that's associated with your AWS customer account.

## Request Syntax
<a name="API_AssociateThirdPartyFirewall_RequestSyntax"></a>

```
{
   "ThirdPartyFirewall": "{{string}}"
}
```

## Request Parameters
<a name="API_AssociateThirdPartyFirewall_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ThirdPartyFirewall](#API_AssociateThirdPartyFirewall_RequestSyntax) **   <a name="fms-AssociateThirdPartyFirewall-request-ThirdPartyFirewall"></a>
The name of the third-party firewall vendor.
Type: String
Valid Values: `PALO_ALTO_NETWORKS_CLOUD_NGFW | FORTIGATE_CLOUD_NATIVE_FIREWALL`
Required: Yes

## Response Syntax
<a name="API_AssociateThirdPartyFirewall_ResponseSyntax"></a>

```
{
   "ThirdPartyFirewallStatus": "string"
}
```

## Response Elements
<a name="API_AssociateThirdPartyFirewall_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ThirdPartyFirewallStatus](#API_AssociateThirdPartyFirewall_ResponseSyntax) **   <a name="fms-AssociateThirdPartyFirewall-response-ThirdPartyFirewallStatus"></a>
The current status for setting a Firewall Manager policy administrator's account as an administrator of the third-party firewall tenant.
+  `ONBOARDING` - The Firewall Manager policy administrator is being designated as a tenant administrator.
+  `ONBOARD_COMPLETE` - The Firewall Manager policy administrator is designated as a tenant administrator.
+  `OFFBOARDING` - The Firewall Manager policy administrator is being removed as a tenant administrator.
+  `OFFBOARD_COMPLETE` - The Firewall Manager policy administrator has been removed as a tenant administrator.
+  `NOT_EXIST` - The Firewall Manager policy administrator doesn't exist as a tenant administrator.
Type: String
Valid Values: `ONBOARDING | ONBOARD_COMPLETE | OFFBOARDING | OFFBOARD_COMPLETE | NOT_EXIST`

## Errors
<a name="API_AssociateThirdPartyFirewall_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **
The operation failed because of a system problem, even though the request was valid. Retry your request.
HTTP Status Code: 400

 ** InvalidInputException **
The parameters of the request were invalid.
HTTP Status Code: 400

 ** InvalidOperationException **
The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an `AssociateAdminAccount` request for an account ID that was already set as the AWS Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for AWS Organizations before you can access it.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_AssociateThirdPartyFirewall_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fms-2018-01-01/AssociateThirdPartyFirewall)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fms-2018-01-01/AssociateThirdPartyFirewall)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/AssociateThirdPartyFirewall)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fms-2018-01-01/AssociateThirdPartyFirewall)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/AssociateThirdPartyFirewall)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fms-2018-01-01/AssociateThirdPartyFirewall)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fms-2018-01-01/AssociateThirdPartyFirewall)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fms-2018-01-01/AssociateThirdPartyFirewall)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fms-2018-01-01/AssociateThirdPartyFirewall)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/AssociateThirdPartyFirewall)
