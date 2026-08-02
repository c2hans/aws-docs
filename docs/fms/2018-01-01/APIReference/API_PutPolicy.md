---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_PutPolicy.html
---

# PutPolicy
<a name="API_PutPolicy"></a>

Creates an AWS Firewall Manager policy.

A Firewall Manager policy is specific to the individual policy type. If you want to enforce multiple policy types across accounts, you can create multiple policies. You can create more than one policy for each type.

If you add a new account to an organization that you created with AWS Organizations, Firewall Manager automatically applies the policy to the resources in that account that are within scope of the policy.

Firewall Manager provides the following types of policies:
+  ** AWS WAF policy** - This policy applies AWS WAF web ACL protections to specified accounts and resources.
+  **Shield Advanced policy** - This policy applies Shield Advanced protection to specified accounts and resources.
+  **Security Groups policy** - This type of policy gives you control over security groups that are in use throughout your organization in AWS Organizations and lets you enforce a baseline set of rules across your organization.
+  **Network ACL policy** - This type of policy gives you control over the network ACLs that are in use throughout your organization in AWS Organizations and lets you enforce a baseline set of first and last network ACL rules across your organization.
+  **Network Firewall policy** - This policy applies Network Firewall protection to your organization's VPCs.
+  **DNS Firewall policy** - This policy applies Amazon Route 53 Resolver DNS Firewall protections to your organization's VPCs.
+  **Third-party firewall policy** - This policy applies third-party firewall protections. Third-party firewalls are available by subscription through the AWS Marketplace console at [AWS Marketplace](http://aws.amazon.com/marketplace).
  +  **Palo Alto Networks Cloud NGFW policy** - This policy applies Palo Alto Networks Cloud Next Generation Firewall (NGFW) protections and Palo Alto Networks Cloud NGFW rulestacks to your organization's VPCs.
  +  **Fortigate CNF policy** - This policy applies Fortigate Cloud Native Firewall (CNF) protections. Fortigate CNF is a cloud-centered solution that blocks Zero-Day threats and secures cloud infrastructures with industry-leading advanced threat prevention, smart web application firewalls (WAF), and API protection.

## Request Syntax
<a name="API_PutPolicy_RequestSyntax"></a>

```
{
   "Policy": {
      "DeleteUnusedFMManagedResources": {{boolean}},
      "ExcludeMap": {
         "{{string}}" : [ "{{string}}" ]
      },
      "ExcludeResourceTags": {{boolean}},
      "IncludeMap": {
         "{{string}}" : [ "{{string}}" ]
      },
      "PolicyDescription": "{{string}}",
      "PolicyId": "{{string}}",
      "PolicyName": "{{string}}",
      "PolicyStatus": "{{string}}",
      "PolicyUpdateToken": "{{string}}",
      "RemediationEnabled": {{boolean}},
      "ResourceSetIds": [ "{{string}}" ],
      "ResourceTagLogicalOperator": "{{string}}",
      "ResourceTags": [
         {
            "Key": "{{string}}",
            "Value": "{{string}}"
         }
      ],
      "ResourceType": "{{string}}",
      "ResourceTypeList": [ "{{string}}" ],
      "SecurityServicePolicyData": {
         "ManagedServiceData": "{{string}}",
         "PolicyOption": {
            "NetworkAclCommonPolicy": {
               "NetworkAclEntrySet": {
                  "FirstEntries": [
                     {
                        "CidrBlock": "{{string}}",
                        "Egress": {{boolean}},
                        "IcmpTypeCode": {
                           "Code": {{number}},
                           "Type": {{number}}
                        },
                        "Ipv6CidrBlock": "{{string}}",
                        "PortRange": {
                           "From": {{number}},
                           "To": {{number}}
                        },
                        "Protocol": "{{string}}",
                        "RuleAction": "{{string}}"
                     }
                  ],
                  "ForceRemediateForFirstEntries": {{boolean}},
                  "ForceRemediateForLastEntries": {{boolean}},
                  "LastEntries": [
                     {
                        "CidrBlock": "{{string}}",
                        "Egress": {{boolean}},
                        "IcmpTypeCode": {
                           "Code": {{number}},
                           "Type": {{number}}
                        },
                        "Ipv6CidrBlock": "{{string}}",
                        "PortRange": {
                           "From": {{number}},
                           "To": {{number}}
                        },
                        "Protocol": "{{string}}",
                        "RuleAction": "{{string}}"
                     }
                  ]
               }
            },
            "NetworkFirewallPolicy": {
               "FirewallDeploymentModel": "{{string}}"
            },
            "ThirdPartyFirewallPolicy": {
               "FirewallDeploymentModel": "{{string}}"
            }
         },
         "Type": "{{string}}"
      }
   },
   "TagList": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_PutPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Policy](#API_PutPolicy_RequestSyntax) **   <a name="fms-PutPolicy-request-Policy"></a>
The details of the AWS Firewall Manager policy to be created.
Type: [Policy](API_Policy.md) object
Required: Yes

 ** [TagList](#API_PutPolicy_RequestSyntax) **   <a name="fms-PutPolicy-request-TagList"></a>
The tags to add to the AWS resource.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_PutPolicy_ResponseSyntax"></a>

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
<a name="API_PutPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Policy](#API_PutPolicy_ResponseSyntax) **   <a name="fms-PutPolicy-response-Policy"></a>
The details of the AWS Firewall Manager policy.
Type: [Policy](API_Policy.md) object

 ** [PolicyArn](#API_PutPolicy_ResponseSyntax) **   <a name="fms-PutPolicy-response-PolicyArn"></a>
The Amazon Resource Name (ARN) of the policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

## Errors
<a name="API_PutPolicy_Errors"></a>

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

 ** InvalidTypeException **
The value of the `Type` parameter is invalid.
HTTP Status Code: 400

 ** LimitExceededException **
The operation exceeds a resource limit, for example, the maximum number of `policy` objects that you can create for an AWS account. For more information, see [Firewall Manager Limits](https://docs.aws.amazon.com/waf/latest/developerguide/fms-limits.html) in the * AWS WAF Developer Guide*.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_PutPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fms-2018-01-01/PutPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fms-2018-01-01/PutPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/PutPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fms-2018-01-01/PutPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/PutPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fms-2018-01-01/PutPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fms-2018-01-01/PutPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fms-2018-01-01/PutPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/fms-2018-01-01/PutPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/PutPolicy)
