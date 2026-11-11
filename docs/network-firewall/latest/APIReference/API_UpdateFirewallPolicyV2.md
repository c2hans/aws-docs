---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_UpdateFirewallPolicyV2.html
---

# UpdateFirewallPolicyV2
<a name="API_UpdateFirewallPolicyV2"></a>

Updates the properties of the specified Next Generation policy.

## Request Syntax
<a name="API_UpdateFirewallPolicyV2_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "DryRun": {{boolean}},
   "EncryptionConfiguration": {
      "KeyId": "{{string}}",
      "Type": "{{string}}"
   },
   "FirewallPolicyV2": {
      "FirewallDefaultAction": "{{string}}",
      "FirewallRuleGroupEntries": [
         {
            "InlineRuleGroup": {
               "ReferenceSets": {
                  "IPSetReferences": {
                     "{{string}}" : {
                        "ReferenceArn": "{{string}}"
                     }
                  }
               },
               "RulesSource": {
                  "FirewallRules": [
                     {
                        "AcceptPriorHooks": {{boolean}},
                        "Action": "{{string}}",
                        "ActionScope": "{{string}}",
                        "AlertEnabled": {{boolean}},
                        "BypassIPSEnabled": {{boolean}},
                        "DestIPs": "{{string}}",
                        "DestPorts": "{{string}}",
                        "Hook": "{{string}}",
                        "Protocol": "{{string}}",
                        "RuleMetadata": {
                           "RuleDescription": "{{string}}",
                           "RuleEnabled": {{boolean}}
                        },
                        "RuleOptions": [
                           {
                              "Keyword": "{{string}}",
                              "Settings": [ "{{string}}" ]
                           }
                        ],
                        "SourceIPs": "{{string}}",
                        "SourcePorts": "{{string}}"
                     }
                  ],
                  "RulesSourceList": {
                     "GeneratedRulesType": "{{string}}",
                     "Targets": [ "{{string}}" ],
                     "TargetTypes": [ "{{string}}" ]
                  },
                  "RulesString": "{{string}}"
               },
               "RuleVariables": {
                  "IPSets": {
                     "{{string}}" : {
                        "Definition": [ "{{string}}" ]
                     }
                  },
                  "PortSets": {
                     "{{string}}" : {
                        "Definition": [ "{{string}}" ]
                     }
                  }
               }
            },
            "Priority": {{number}},
            "ResourceArn": "{{string}}"
         }
      ],
      "IpsRuleGroupEntries": [
         {
            "InlineRuleGroup": {
               "ReferenceSets": {
                  "IPSetReferences": {
                     "{{string}}" : {
                        "ReferenceArn": "{{string}}"
                     }
                  }
               },
               "RulesSource": {
                  "RulesString": "{{string}}"
               },
               "RuleVariables": {
                  "IPSets": {
                     "{{string}}" : {
                        "Definition": [ "{{string}}" ]
                     }
                  },
                  "PortSets": {
                     "{{string}}" : {
                        "Definition": [ "{{string}}" ]
                     }
                  }
               }
            },
            "Override": {
               "Action": "{{string}}"
            },
            "ResourceArn": "{{string}}"
         }
      ],
      "PolicyMode": "{{string}}",
      "PolicyVariables": {
         "RuleVariables": {
            "{{string}}" : {
               "Definition": [ "{{string}}" ]
            }
         }
      },
      "Route53ResolvedIPValidation": {
         "Action": "{{string}}",
         "BypassDestinationValidationIPRanges": [
            {
               "AddressDefinition": "{{string}}"
            }
         ],
         "DNSExpiryExceptionPolicy": "{{string}}",
         "DNSFirewallRuleGroupId": "{{string}}",
         "SourceIPRanges": [
            {
               "AddressDefinition": "{{string}}"
            }
         ]
      },
      "StatefulEngineOptions": {
         "FlowTimeouts": {
            "TcpIdleTimeoutSeconds": {{number}}
         },
         "StreamExceptionPolicy": "{{string}}"
      },
      "TLSInspectionConfigurationArn": "{{string}}"
   },
   "FirewallPolicyV2Arn": "{{string}}",
   "FirewallPolicyV2Name": "{{string}}",
   "UpdateToken": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateFirewallPolicyV2_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateFirewallPolicyV2_RequestSyntax) **   <a name="networkfirewall-UpdateFirewallPolicyV2-request-Description"></a>
A description of the firewall policy.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `^.*$`
Required: No

 ** [DryRun](#API_UpdateFirewallPolicyV2_RequestSyntax) **   <a name="networkfirewall-UpdateFirewallPolicyV2-request-DryRun"></a>
Indicates whether you want Network Firewall to just check the validity of the request, rather than run the request.
If set to `TRUE`, Network Firewall checks whether the request can run successfully, but doesn't actually make the requested changes. The call returns the value that the request would return if you ran it with dry run set to `FALSE`, but doesn't make additions or changes to your resources. This option allows you to make sure that you have the required permissions to run the request and that your request parameters are valid.
If set to `FALSE`, Network Firewall makes the requested changes to your resources.
Type: Boolean
Required: No

 ** [EncryptionConfiguration](#API_UpdateFirewallPolicyV2_RequestSyntax) **   <a name="networkfirewall-UpdateFirewallPolicyV2-request-EncryptionConfiguration"></a>
A complex type that contains settings for encryption of your firewall policy resources.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object
Required: No

 ** [FirewallPolicyV2](#API_UpdateFirewallPolicyV2_RequestSyntax) **   <a name="networkfirewall-UpdateFirewallPolicyV2-request-FirewallPolicyV2"></a>
The updated rule groups and other settings that define the Next Generation policy.
Type: [FirewallPolicyV2](API_FirewallPolicyV2.md) object
Required: Yes

 ** [FirewallPolicyV2Arn](#API_UpdateFirewallPolicyV2_RequestSyntax) **   <a name="networkfirewall-UpdateFirewallPolicyV2-request-FirewallPolicyV2Arn"></a>
The Amazon Resource Name (ARN) of the Next Generation policy.
You must specify the ARN or the name, and you can specify both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:aws.*`
Required: No

 ** [FirewallPolicyV2Name](#API_UpdateFirewallPolicyV2_RequestSyntax) **   <a name="networkfirewall-UpdateFirewallPolicyV2-request-FirewallPolicyV2Name"></a>
The descriptive name of the Next Generation policy. You can't change the name of a firewall policy after you create it.
You must specify the ARN or the name, and you can specify both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-]+$`
Required: No

 ** [UpdateToken](#API_UpdateFirewallPolicyV2_RequestSyntax) **   <a name="networkfirewall-UpdateFirewallPolicyV2-request-UpdateToken"></a>
A token used for optimistic locking. Network Firewall returns a token to your requests that access the firewall policy. The token marks the state of the policy resource at the time of the request.
To make changes to the policy, you provide the token in your request. Network Firewall uses the token to ensure that the policy hasn't changed since you last retrieved it. If it has changed, the operation fails with an `InvalidTokenException`. If this happens, retrieve the firewall policy again to get a current copy of it with current token. Reapply your changes as needed, then try the operation again using the new token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$`
Required: Yes

## Response Syntax
<a name="API_UpdateFirewallPolicyV2_ResponseSyntax"></a>

```
{
   "FirewallPolicyV2Response": {
      "ConsumedFirewallRuleCapacity": number,
      "ConsumedIpsDomainCapacity": number,
      "ConsumedIpsRuleCapacity": number,
      "Description": "string",
      "EncryptionConfiguration": {
         "KeyId": "string",
         "Type": "string"
      },
      "Errors": [
         {
            "Code": "string",
            "Message": "string",
            "ResourceId": "string"
         }
      ],
      "FirewallPolicyV2Arn": "string",
      "FirewallPolicyV2Id": "string",
      "FirewallPolicyV2Name": "string",
      "FirewallPolicyV2Status": "string",
      "LastModifiedTime": number,
      "NumberOfAssociations": number,
      "StatusMessage": "string",
      "Tags": [
         {
            "Key": "string",
            "Value": "string"
         }
      ]
   },
   "UpdateToken": "string"
}
```

## Response Elements
<a name="API_UpdateFirewallPolicyV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FirewallPolicyV2Response](#API_UpdateFirewallPolicyV2_ResponseSyntax) **   <a name="networkfirewall-UpdateFirewallPolicyV2-response-FirewallPolicyV2Response"></a>
The high-level properties of the Next Generation policy. This, along with the [FirewallPolicyV2](API_FirewallPolicyV2.md), define the policy. You can retrieve all objects for a Next Generation policy by calling [DescribeFirewallPolicyV2](API_DescribeFirewallPolicyV2.md).
Type: [FirewallPolicyV2Response](API_FirewallPolicyV2Response.md) object

 ** [UpdateToken](#API_UpdateFirewallPolicyV2_ResponseSyntax) **   <a name="networkfirewall-UpdateFirewallPolicyV2-response-UpdateToken"></a>
A token used for optimistic locking. Network Firewall returns a token to your requests that access the firewall policy. The token marks the state of the policy resource at the time of the request.
To make changes to the policy, you provide the token in your request. Network Firewall uses the token to ensure that the policy hasn't changed since you last retrieved it. If it has changed, the operation fails with an `InvalidTokenException`. If this happens, retrieve the firewall policy again to get a current copy of it with current token. Reapply your changes as needed, then try the operation again using the new token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$`

## Errors
<a name="API_UpdateFirewallPolicyV2_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request.
HTTP Status Code: 500

 ** InvalidOperationException **
The operation failed because it's not valid. For example, you might have tried to delete a rule group or firewall policy that's in use.
HTTP Status Code: 400

 ** InvalidRequestException **
The operation failed because of a problem with your request. Examples include:
+ You specified an unsupported parameter name or value.
+ You tried to update a property with a value that isn't among the available types.
+ Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.
HTTP Status Code: 400

 ** InvalidTokenException **
The token you provided is stale or isn't valid for the operation.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Unable to locate a resource using the parameters that you provided.
HTTP Status Code: 400

 ** ThrottlingException **
Unable to process the request due to throttling limitations.
HTTP Status Code: 400

## See Also
<a name="API_UpdateFirewallPolicyV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/UpdateFirewallPolicyV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/UpdateFirewallPolicyV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/UpdateFirewallPolicyV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/UpdateFirewallPolicyV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/UpdateFirewallPolicyV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/UpdateFirewallPolicyV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/UpdateFirewallPolicyV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/UpdateFirewallPolicyV2)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/UpdateFirewallPolicyV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/UpdateFirewallPolicyV2)
