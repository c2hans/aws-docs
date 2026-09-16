---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_GetPolicy.html
---

# GetPolicy
<a name="API_GetPolicy"></a>

Returns information about the specified AWS Firewall Manager policy.

## Request Syntax
<a name="API_GetPolicy_RequestSyntax"></a>

```
{
   "PolicyId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [PolicyId](#API_GetPolicy_RequestSyntax) **   <a name="fms-GetPolicy-request-PolicyId"></a>
The ID of the AWS Firewall Manager policy that you want the details for.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-z0-9A-Z-]{36}$`
Required: Yes

## Response Syntax
<a name="API_GetPolicy_ResponseSyntax"></a>

```
{
   "Policy": {
      "DeleteUnusedFMManagedResources": boolean,
      "ExcludeMap": {
         "string" : [ "string" ]
      },
      "ExcludeResourceTags": boolean,
      "IncludeMap": {
         "string" : [ "string" ]
      },
      "PolicyDescription": "string",
      "PolicyId": "string",
      "PolicyName": "string",
      "PolicyStatus": "string",
      "PolicyUpdateToken": "string",
      "RemediationEnabled": boolean,
      "ResourceSetIds": [ "string" ],
      "ResourceTagLogicalOperator": "string",
      "ResourceTags": [
         {
            "Key": "string",
            "Value": "string"
         }
      ],
      "ResourceType": "string",
      "ResourceTypeList": [ "string" ],
      "SecurityServicePolicyData": {
         "ManagedServiceData": "string",
         "PolicyOption": {
            "NetworkAclCommonPolicy": {
               "NetworkAclEntrySet": {
                  "FirstEntries": [
                     {
                        "CidrBlock": "string",
                        "Egress": boolean,
                        "IcmpTypeCode": {
                           "Code": number,
                           "Type": number
                        },
                        "Ipv6CidrBlock": "string",
                        "PortRange": {
                           "From": number,
                           "To": number
                        },
                        "Protocol": "string",
                        "RuleAction": "string"
                     }
                  ],
                  "ForceRemediateForFirstEntries": boolean,
                  "ForceRemediateForLastEntries": boolean,
                  "LastEntries": [
                     {
                        "CidrBlock": "string",
                        "Egress": boolean,
                        "IcmpTypeCode": {
                           "Code": number,
                           "Type": number
                        },
                        "Ipv6CidrBlock": "string",
                        "PortRange": {
                           "From": number,
                           "To": number
                        },
                        "Protocol": "string",
                        "RuleAction": "string"
                     }
                  ]
               }
            },
            "NetworkFirewallPolicy": {
               "FirewallDeploymentModel": "string"
            },
            "ThirdPartyFirewallPolicy": {
               "FirewallDeploymentModel": "string"
            }
         },
         "Type": "string"
      }
   },
   "PolicyArn": "string"
}
```

## Response Elements
<a name="API_GetPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Policy](#API_GetPolicy_ResponseSyntax) **   <a name="fms-GetPolicy-response-Policy"></a>
Information about the specified AWS Firewall Manager policy.
Type: [Policy](API_Policy.md) object

 ** [PolicyArn](#API_GetPolicy_ResponseSyntax) **   <a name="fms-GetPolicy-response-PolicyArn"></a>
The Amazon Resource Name (ARN) of the specified policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

## Errors
<a name="API_GetPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **
The operation failed because of a system problem, even though the request was valid. Retry your request.
HTTP Status Code: 400

 ** InvalidOperationException **
The operation failed because there was nothing to do or the operation wasn't possible. For example, you might have submitted an `AssociateAdminAccount` request for an account ID that was already set as the AWS Firewall Manager administrator. Or you might have tried to access a Region that's disabled by default, and that you need to enable for the Firewall Manager administrator account and for AWS Organizations before you can access it.
HTTP Status Code: 400

 ** InvalidTypeException **
The value of the `Type` parameter is invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_GetPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fms-2018-01-01/GetPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fms-2018-01-01/GetPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/GetPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fms-2018-01-01/GetPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/GetPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fms-2018-01-01/GetPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fms-2018-01-01/GetPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fms-2018-01-01/GetPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/fms-2018-01-01/GetPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/GetPolicy)
