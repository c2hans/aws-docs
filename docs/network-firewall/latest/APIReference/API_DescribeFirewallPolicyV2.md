---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DescribeFirewallPolicyV2.html
---

# DescribeFirewallPolicyV2
<a name="API_DescribeFirewallPolicyV2"></a>

Returns the data objects for the specified Next Generation policy.

## Request Syntax
<a name="API_DescribeFirewallPolicyV2_RequestSyntax"></a>

```
{
   "FirewallPolicyV2Arn": "{{string}}",
   "FirewallPolicyV2Name": "{{string}}",
   "RuleOutputFormat": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeFirewallPolicyV2_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [FirewallPolicyV2Arn](#API_DescribeFirewallPolicyV2_RequestSyntax) **   <a name="networkfirewall-DescribeFirewallPolicyV2-request-FirewallPolicyV2Arn"></a>
The Amazon Resource Name (ARN) of the Next Generation policy.
You must specify the ARN or the name, and you can specify both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:aws.*`
Required: No

 ** [FirewallPolicyV2Name](#API_DescribeFirewallPolicyV2_RequestSyntax) **   <a name="networkfirewall-DescribeFirewallPolicyV2-request-FirewallPolicyV2Name"></a>
The descriptive name of the Next Generation policy. You can't change the name of a firewall policy after you create it.
You must specify the ARN or the name, and you can specify both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-]+$`
Required: No

 ** [RuleOutputFormat](#API_DescribeFirewallPolicyV2_RequestSyntax) **   <a name="networkfirewall-DescribeFirewallPolicyV2-request-RuleOutputFormat"></a>
The format in which to return the rules of any firewall engine rule groups that are embedded in the policy. Specify `FIREWALL_RULES` for structured `FirewallRule` objects or `RULES_STRING` for a Suricata-compatible firewall-mode rule string. If you don't specify a format, Network Firewall returns each embedded rule group in the format you provided it in. Referenced rule groups aren't affected.
Type: String
Valid Values: `FIREWALL_RULES | RULES_STRING`
Required: No

## Response Syntax
<a name="API_DescribeFirewallPolicyV2_ResponseSyntax"></a>

```
{
   "FirewallPolicyV2": {
      "FirewallDefaultAction": "string",
      "FirewallRuleGroupEntries": [
         {
            "InlineRuleGroup": {
               "ReferenceSets": {
                  "IPSetReferences": {
                     "string" : {
                        "ReferenceArn": "string"
                     }
                  }
               },
               "RulesSource": {
                  "FirewallRules": [
                     {
                        "AcceptPriorHooks": boolean,
                        "Action": "string",
                        "ActionScope": "string",
                        "AlertEnabled": boolean,
                        "BypassIPSEnabled": boolean,
                        "DestIPs": "string",
                        "DestPorts": "string",
                        "Hook": "string",
                        "Protocol": "string",
                        "RuleMetadata": {
                           "RuleDescription": "string",
                           "RuleEnabled": boolean
                        },
                        "RuleOptions": [
                           {
                              "Keyword": "string",
                              "Settings": [ "string" ]
                           }
                        ],
                        "SourceIPs": "string",
                        "SourcePorts": "string"
                     }
                  ],
                  "RulesSourceList": {
                     "GeneratedRulesType": "string",
                     "Targets": [ "string" ],
                     "TargetTypes": [ "string" ]
                  },
                  "RulesString": "string"
               },
               "RuleVariables": {
                  "IPSets": {
                     "string" : {
                        "Definition": [ "string" ]
                     }
                  },
                  "PortSets": {
                     "string" : {
                        "Definition": [ "string" ]
                     }
                  }
               }
            },
            "Priority": number,
            "ResourceArn": "string"
         }
      ],
      "IpsRuleGroupEntries": [
         {
            "InlineRuleGroup": {
               "ReferenceSets": {
                  "IPSetReferences": {
                     "string" : {
                        "ReferenceArn": "string"
                     }
                  }
               },
               "RulesSource": {
                  "RulesString": "string"
               },
               "RuleVariables": {
                  "IPSets": {
                     "string" : {
                        "Definition": [ "string" ]
                     }
                  },
                  "PortSets": {
                     "string" : {
                        "Definition": [ "string" ]
                     }
                  }
               }
            },
            "Override": {
               "Action": "string"
            },
            "ResourceArn": "string"
         }
      ],
      "PolicyMode": "string",
      "PolicyVariables": {
         "RuleVariables": {
            "string" : {
               "Definition": [ "string" ]
            }
         }
      },
      "Route53ResolvedIPValidation": {
         "Action": "string",
         "BypassDestinationValidationIPRanges": [
            {
               "AddressDefinition": "string"
            }
         ],
         "DNSExpiryExceptionPolicy": "string",
         "DNSFirewallRuleGroupId": "string",
         "SourceIPRanges": [
            {
               "AddressDefinition": "string"
            }
         ]
      },
      "StatefulEngineOptions": {
         "FlowTimeouts": {
            "TcpIdleTimeoutSeconds": number
         },
         "StreamExceptionPolicy": "string"
      },
      "TLSInspectionConfigurationArn": "string"
   },
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
<a name="API_DescribeFirewallPolicyV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FirewallPolicyV2](#API_DescribeFirewallPolicyV2_ResponseSyntax) **   <a name="networkfirewall-DescribeFirewallPolicyV2-response-FirewallPolicyV2"></a>
The rule groups and other settings that define the specified Next Generation policy.
Type: [FirewallPolicyV2](API_FirewallPolicyV2.md) object

 ** [FirewallPolicyV2Response](#API_DescribeFirewallPolicyV2_ResponseSyntax) **   <a name="networkfirewall-DescribeFirewallPolicyV2-response-FirewallPolicyV2Response"></a>
The high-level properties of the Next Generation policy. This, along with the [FirewallPolicyV2](API_FirewallPolicyV2.md), define the policy.
Type: [FirewallPolicyV2Response](API_FirewallPolicyV2Response.md) object

 ** [UpdateToken](#API_DescribeFirewallPolicyV2_ResponseSyntax) **   <a name="networkfirewall-DescribeFirewallPolicyV2-response-UpdateToken"></a>
A token used for optimistic locking. Network Firewall returns a token to your requests that access the firewall policy. The token marks the state of the policy resource at the time of the request.
To make changes to the policy, you provide the token in your request. Network Firewall uses the token to ensure that the policy hasn't changed since you last retrieved it. If it has changed, the operation fails with an `InvalidTokenException`. If this happens, retrieve the firewall policy again to get a current copy of it with current token. Reapply your changes as needed, then try the operation again using the new token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([0-9a-f]{8})-([0-9a-f]{4}-){3}([0-9a-f]{12})$`

## Errors
<a name="API_DescribeFirewallPolicyV2_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
Your request is valid, but Network Firewall couldn't perform the operation because of a system problem. Retry your request.
HTTP Status Code: 500

 ** InvalidRequestException **
The operation failed because of a problem with your request. Examples include:
+ You specified an unsupported parameter name or value.
+ You tried to update a property with a value that isn't among the available types.
+ Your request references an ARN that is malformed, or corresponds to a resource that isn't valid in the context of the request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Unable to locate a resource using the parameters that you provided.
HTTP Status Code: 400

 ** ThrottlingException **
Unable to process the request due to throttling limitations.
HTTP Status Code: 400

## See Also
<a name="API_DescribeFirewallPolicyV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/DescribeFirewallPolicyV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/DescribeFirewallPolicyV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/DescribeFirewallPolicyV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/DescribeFirewallPolicyV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/DescribeFirewallPolicyV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/DescribeFirewallPolicyV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/DescribeFirewallPolicyV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/DescribeFirewallPolicyV2)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/DescribeFirewallPolicyV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/DescribeFirewallPolicyV2)
