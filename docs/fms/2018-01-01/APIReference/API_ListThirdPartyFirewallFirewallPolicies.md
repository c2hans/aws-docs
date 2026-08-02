---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ListThirdPartyFirewallFirewallPolicies.html
---

# ListThirdPartyFirewallFirewallPolicies
<a name="API_ListThirdPartyFirewallFirewallPolicies"></a>

Retrieves a list of all of the third-party firewall policies that are associated with the third-party firewall administrator's account.

## Request Syntax
<a name="API_ListThirdPartyFirewallFirewallPolicies_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ThirdPartyFirewall": "{{string}}"
}
```

## Request Parameters
<a name="API_ListThirdPartyFirewallFirewallPolicies_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListThirdPartyFirewallFirewallPolicies_RequestSyntax) **   <a name="fms-ListThirdPartyFirewallFirewallPolicies-request-MaxResults"></a>
The maximum number of third-party firewall policies that you want Firewall Manager to return. If the specified third-party firewall vendor is associated with more than `MaxResults` firewall policies, the response includes a `NextToken` element. `NextToken` contains an encrypted token that identifies the first third-party firewall policies that Firewall Manager will return if you submit another request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: Yes

 ** [NextToken](#API_ListThirdPartyFirewallFirewallPolicies_RequestSyntax) **   <a name="fms-ListThirdPartyFirewallFirewallPolicies-request-NextToken"></a>
If the previous response included a `NextToken` element, the specified third-party firewall vendor is associated with more third-party firewall policies. To get more third-party firewall policies, submit another `ListThirdPartyFirewallFirewallPoliciesRequest` request.
 For the value of `NextToken`, specify the value of `NextToken` from the previous response. If the previous response didn't include a `NextToken` element, there are no more third-party firewall policies to get.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** [ThirdPartyFirewall](#API_ListThirdPartyFirewallFirewallPolicies_RequestSyntax) **   <a name="fms-ListThirdPartyFirewallFirewallPolicies-request-ThirdPartyFirewall"></a>
The name of the third-party firewall vendor.
Type: String
Valid Values: `PALO_ALTO_NETWORKS_CLOUD_NGFW | FORTIGATE_CLOUD_NATIVE_FIREWALL`
Required: Yes

## Response Syntax
<a name="API_ListThirdPartyFirewallFirewallPolicies_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ThirdPartyFirewallFirewallPolicies": [
      {
         "FirewallPolicyId": "string",
         "FirewallPolicyName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListThirdPartyFirewallFirewallPolicies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListThirdPartyFirewallFirewallPolicies_ResponseSyntax) **   <a name="fms-ListThirdPartyFirewallFirewallPolicies-response-NextToken"></a>
The value that you will use for `NextToken` in the next `ListThirdPartyFirewallFirewallPolicies` request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

 ** [ThirdPartyFirewallFirewallPolicies](#API_ListThirdPartyFirewallFirewallPolicies_ResponseSyntax) **   <a name="fms-ListThirdPartyFirewallFirewallPolicies-response-ThirdPartyFirewallFirewallPolicies"></a>
A list that contains one `ThirdPartyFirewallFirewallPolicies` element for each third-party firewall policies that the specified third-party firewall vendor is associated with. Each `ThirdPartyFirewallFirewallPolicies` element contains the firewall policy name and ID.
Type: Array of [ThirdPartyFirewallFirewallPolicy](API_ThirdPartyFirewallFirewallPolicy.md) objects

## Errors
<a name="API_ListThirdPartyFirewallFirewallPolicies_Errors"></a>

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
<a name="API_ListThirdPartyFirewallFirewallPolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fms-2018-01-01/ListThirdPartyFirewallFirewallPolicies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fms-2018-01-01/ListThirdPartyFirewallFirewallPolicies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/ListThirdPartyFirewallFirewallPolicies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fms-2018-01-01/ListThirdPartyFirewallFirewallPolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/ListThirdPartyFirewallFirewallPolicies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fms-2018-01-01/ListThirdPartyFirewallFirewallPolicies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fms-2018-01-01/ListThirdPartyFirewallFirewallPolicies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fms-2018-01-01/ListThirdPartyFirewallFirewallPolicies)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fms-2018-01-01/ListThirdPartyFirewallFirewallPolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/ListThirdPartyFirewallFirewallPolicies)
