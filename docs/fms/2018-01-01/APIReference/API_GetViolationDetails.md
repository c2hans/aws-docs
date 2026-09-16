---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_GetViolationDetails.html
---

# GetViolationDetails
<a name="API_GetViolationDetails"></a>

Retrieves violations for a resource based on the specified AWS Firewall Manager policy and AWS account.

## Request Syntax
<a name="API_GetViolationDetails_RequestSyntax"></a>

```
{
   "MemberAccount": "{{string}}",
   "PolicyId": "{{string}}",
   "ResourceId": "{{string}}",
   "ResourceType": "{{string}}"
}
```

## Request Parameters
<a name="API_GetViolationDetails_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MemberAccount](#API_GetViolationDetails_RequestSyntax) **   <a name="fms-GetViolationDetails-request-MemberAccount"></a>
The AWS account ID that you want the details for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^[0-9]+$`
Required: Yes

 ** [PolicyId](#API_GetViolationDetails_RequestSyntax) **   <a name="fms-GetViolationDetails-request-PolicyId"></a>
The ID of the AWS Firewall Manager policy that you want the details for. You can get violation details for the following policy types:
+  AWS WAF
+ DNS Firewall
+ Imported Network Firewall
+ Network Firewall
+ Security group content audit
+ Network ACL
+ Third-party firewall
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-z0-9A-Z-]{36}$`
Required: Yes

 ** [ResourceId](#API_GetViolationDetails_RequestSyntax) **   <a name="fms-GetViolationDetails-request-ResourceId"></a>
The ID of the resource that has violations.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

 ** [ResourceType](#API_GetViolationDetails_RequestSyntax) **   <a name="fms-GetViolationDetails-request-ResourceType"></a>
The resource type. This is in the format shown in the [AWS Resource Types Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html). Supported resource types are: `AWS::WAFv2::WebACL`, `AWS::EC2::Instance`, `AWS::EC2::NetworkInterface`, `AWS::EC2::SecurityGroup`, `AWS::NetworkFirewall::FirewallPolicy`, and `AWS::EC2::Subnet`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

## Response Syntax
<a name="API_GetViolationDetails_ResponseSyntax"></a>

```
{
   "ViolationDetail": {
      "MemberAccount": "string",
      "PolicyId": "string",
      "ResourceDescription": "string",
      "ResourceId": "string",
      "ResourceTags": [
         {
            "Key": "string",
            "Value": "string"
         }
      ],
      "ResourceType": "string",
      "ResourceViolations": [
         {
            "AwsEc2InstanceViolation": {
               "AwsEc2NetworkInterfaceViolations": [
                  {
                     "ViolatingSecurityGroups": [ "string" ],
                     "ViolationTarget": "string"
                  }
               ],
               "ViolationTarget": "string"
            },
            "AwsEc2NetworkInterfaceViolation": {
               "ViolatingSecurityGroups": [ "string" ],
               "ViolationTarget": "string"
            },
            "AwsVPCSecurityGroupViolation": {
               "PartialMatches": [
                  {
                     "Reference": "string",
                     "TargetViolationReasons": [ "string" ]
                  }
               ],
               "PossibleSecurityGroupRemediationActions": [
                  {
                     "Description": "string",
                     "IsDefaultAction": boolean,
                     "RemediationActionType": "string",
                     "RemediationResult": {
                        "FromPort": number,
                        "IPV4Range": "string",
                        "IPV6Range": "string",
                        "PrefixListId": "string",
                        "Protocol": "string",
                        "ToPort": number
                     }
                  }
               ],
               "ViolationTarget": "string",
               "ViolationTargetDescription": "string"
            },
            "DnsDuplicateRuleGroupViolation": {
               "ViolationTarget": "string",
               "ViolationTargetDescription": "string"
            },
            "DnsRuleGroupLimitExceededViolation": {
               "NumberOfRuleGroupsAlreadyAssociated": number,
               "ViolationTarget": "string",
               "ViolationTargetDescription": "string"
            },
            "DnsRuleGroupPriorityConflictViolation": {
               "ConflictingPolicyId": "string",
               "ConflictingPriority": number,
               "UnavailablePriorities": [ number ],
               "ViolationTarget": "string",
               "ViolationTargetDescription": "string"
            },
            "FirewallSubnetIsOutOfScopeViolation": {
               "FirewallSubnetId": "string",
               "SubnetAvailabilityZone": "string",
               "SubnetAvailabilityZoneId": "string",
               "VpcEndpointId": "string",
               "VpcId": "string"
            },
            "FirewallSubnetMissingVPCEndpointViolation": {
               "FirewallSubnetId": "string",
               "SubnetAvailabilityZone": "string",
               "SubnetAvailabilityZoneId": "string",
               "VpcId": "string"
            },
            "InvalidNetworkAclEntriesViolation": {
               "CurrentAssociatedNetworkAcl": "string",
               "EntryViolations": [
                  {
                     "ActualEvaluationOrder": "string",
                     "EntriesWithConflicts": [
                        {
                           "EntryDetail": {
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
                           },
                           "EntryRuleNumber": number,
                           "EntryType": "string"
                        }
                     ],
                     "EntryAtExpectedEvaluationOrder": {
                        "EntryDetail": {
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
                        },
                        "EntryRuleNumber": number,
                        "EntryType": "string"
                     },
                     "EntryViolationReasons": [ "string" ],
                     "ExpectedEntry": {
                        "EntryDetail": {
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
                        },
                        "EntryRuleNumber": number,
                        "EntryType": "string"
                     },
                     "ExpectedEvaluationOrder": "string"
                  }
               ],
               "Subnet": "string",
               "SubnetAvailabilityZone": "string",
               "Vpc": "string"
            },
            "NetworkFirewallBlackHoleRouteDetectedViolation": {
               "RouteTableId": "string",
               "ViolatingRoutes": [
                  {
                     "Destination": "string",
                     "DestinationType": "string",
                     "Target": "string",
                     "TargetType": "string"
                  }
               ],
               "ViolationTarget": "string",
               "VpcId": "string"
            },
            "NetworkFirewallInternetTrafficNotInspectedViolation": {
               "ActualFirewallSubnetRoutes": [
                  {
                     "Destination": "string",
                     "DestinationType": "string",
                     "Target": "string",
                     "TargetType": "string"
                  }
               ],
               "ActualInternetGatewayRoutes": [
                  {
                     "Destination": "string",
                     "DestinationType": "string",
                     "Target": "string",
                     "TargetType": "string"
                  }
               ],
               "CurrentFirewallSubnetRouteTable": "string",
               "CurrentInternetGatewayRouteTable": "string",
               "ExpectedFirewallEndpoint": "string",
               "ExpectedFirewallSubnetRoutes": [
                  {
                     "AllowedTargets": [ "string" ],
                     "ContributingSubnets": [ "string" ],
                     "IpV4Cidr": "string",
                     "IpV6Cidr": "string",
                     "PrefixListId": "string",
                     "RouteTableId": "string"
                  }
               ],
               "ExpectedInternetGatewayRoutes": [
                  {
                     "AllowedTargets": [ "string" ],
                     "ContributingSubnets": [ "string" ],
                     "IpV4Cidr": "string",
                     "IpV6Cidr": "string",
                     "PrefixListId": "string",
                     "RouteTableId": "string"
                  }
               ],
               "FirewallSubnetId": "string",
               "InternetGatewayId": "string",
               "IsRouteTableUsedInDifferentAZ": boolean,
               "RouteTableId": "string",
               "SubnetAvailabilityZone": "string",
               "SubnetId": "string",
               "ViolatingRoutes": [
                  {
                     "Destination": "string",
                     "DestinationType": "string",
                     "Target": "string",
                     "TargetType": "string"
                  }
               ],
               "VpcId": "string"
            },
            "NetworkFirewallInvalidRouteConfigurationViolation": {
               "ActualFirewallEndpoint": "string",
               "ActualFirewallSubnetId": "string",
               "ActualFirewallSubnetRoutes": [
                  {
                     "Destination": "string",
                     "DestinationType": "string",
                     "Target": "string",
                     "TargetType": "string"
                  }
               ],
               "ActualInternetGatewayRoutes": [
                  {
                     "Destination": "string",
                     "DestinationType": "string",
                     "Target": "string",
                     "TargetType": "string"
                  }
               ],
               "AffectedSubnets": [ "string" ],
               "CurrentFirewallSubnetRouteTable": "string",
               "CurrentInternetGatewayRouteTable": "string",
               "ExpectedFirewallEndpoint": "string",
               "ExpectedFirewallSubnetId": "string",
               "ExpectedFirewallSubnetRoutes": [
                  {
                     "AllowedTargets": [ "string" ],
                     "ContributingSubnets": [ "string" ],
                     "IpV4Cidr": "string",
                     "IpV6Cidr": "string",
                     "PrefixListId": "string",
                     "RouteTableId": "string"
                  }
               ],
               "ExpectedInternetGatewayRoutes": [
                  {
                     "AllowedTargets": [ "string" ],
                     "ContributingSubnets": [ "string" ],
                     "IpV4Cidr": "string",
                     "IpV6Cidr": "string",
                     "PrefixListId": "string",
                     "RouteTableId": "string"
                  }
               ],
               "InternetGatewayId": "string",
               "IsRouteTableUsedInDifferentAZ": boolean,
               "RouteTableId": "string",
               "ViolatingRoute": {
                  "Destination": "string",
                  "DestinationType": "string",
                  "Target": "string",
                  "TargetType": "string"
               },
               "VpcId": "string"
            },
            "NetworkFirewallMissingExpectedRoutesViolation": {
               "ExpectedRoutes": [
                  {
                     "AllowedTargets": [ "string" ],
                     "ContributingSubnets": [ "string" ],
                     "IpV4Cidr": "string",
                     "IpV6Cidr": "string",
                     "PrefixListId": "string",
                     "RouteTableId": "string"
                  }
               ],
               "ViolationTarget": "string",
               "VpcId": "string"
            },
            "NetworkFirewallMissingExpectedRTViolation": {
               "AvailabilityZone": "string",
               "CurrentRouteTable": "string",
               "ExpectedRouteTable": "string",
               "ViolationTarget": "string",
               "VPC": "string"
            },
            "NetworkFirewallMissingFirewallViolation": {
               "AvailabilityZone": "string",
               "TargetViolationReason": "string",
               "ViolationTarget": "string",
               "VPC": "string"
            },
            "NetworkFirewallMissingSubnetViolation": {
               "AvailabilityZone": "string",
               "TargetViolationReason": "string",
               "ViolationTarget": "string",
               "VPC": "string"
            },
            "NetworkFirewallPolicyModifiedViolation": {
               "CurrentPolicyDescription": {
                  "StatefulDefaultActions": [ "string" ],
                  "StatefulEngineOptions": {
                     "RuleOrder": "string",
                     "StreamExceptionPolicy": "string"
                  },
                  "StatefulRuleGroups": [
                     {
                        "Override": {
                           "Action": "string"
                        },
                        "Priority": number,
                        "ResourceId": "string",
                        "RuleGroupName": "string"
                     }
                  ],
                  "StatelessCustomActions": [ "string" ],
                  "StatelessDefaultActions": [ "string" ],
                  "StatelessFragmentDefaultActions": [ "string" ],
                  "StatelessRuleGroups": [
                     {
                        "Priority": number,
                        "ResourceId": "string",
                        "RuleGroupName": "string"
                     }
                  ]
               },
               "ExpectedPolicyDescription": {
                  "StatefulDefaultActions": [ "string" ],
                  "StatefulEngineOptions": {
                     "RuleOrder": "string",
                     "StreamExceptionPolicy": "string"
                  },
                  "StatefulRuleGroups": [
                     {
                        "Override": {
                           "Action": "string"
                        },
                        "Priority": number,
                        "ResourceId": "string",
                        "RuleGroupName": "string"
                     }
                  ],
                  "StatelessCustomActions": [ "string" ],
                  "StatelessDefaultActions": [ "string" ],
                  "StatelessFragmentDefaultActions": [ "string" ],
                  "StatelessRuleGroups": [
                     {
                        "Priority": number,
                        "ResourceId": "string",
                        "RuleGroupName": "string"
                     }
                  ]
               },
               "ViolationTarget": "string"
            },
            "NetworkFirewallUnexpectedFirewallRoutesViolation": {
               "FirewallEndpoint": "string",
               "FirewallSubnetId": "string",
               "RouteTableId": "string",
               "ViolatingRoutes": [
                  {
                     "Destination": "string",
                     "DestinationType": "string",
                     "Target": "string",
                     "TargetType": "string"
                  }
               ],
               "VpcId": "string"
            },
            "NetworkFirewallUnexpectedGatewayRoutesViolation": {
               "GatewayId": "string",
               "RouteTableId": "string",
               "ViolatingRoutes": [
                  {
                     "Destination": "string",
                     "DestinationType": "string",
                     "Target": "string",
                     "TargetType": "string"
                  }
               ],
               "VpcId": "string"
            },
            "PossibleRemediationActions": {
               "Actions": [
                  {
                     "Description": "string",
                     "IsDefaultAction": boolean,
                     "OrderedRemediationActions": [
                        {
                           "Order": number,
                           "RemediationAction": {
                              "CreateNetworkAclAction": {
                                 "Description": "string",
                                 "FMSCanRemediate": boolean,
                                 "Vpc": {
                                    "Description": "string",
                                    "ResourceId": "string"
                                 }
                              },
                              "CreateNetworkAclEntriesAction": {
                                 "Description": "string",
                                 "FMSCanRemediate": boolean,
                                 "NetworkAclEntriesToBeCreated": [
                                    {
                                       "EntryDetail": {
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
                                       },
                                       "EntryRuleNumber": number,
                                       "EntryType": "string"
                                    }
                                 ],
                                 "NetworkAclId": {
                                    "Description": "string",
                                    "ResourceId": "string"
                                 }
                              },
                              "DeleteNetworkAclEntriesAction": {
                                 "Description": "string",
                                 "FMSCanRemediate": boolean,
                                 "NetworkAclEntriesToBeDeleted": [
                                    {
                                       "EntryDetail": {
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
                                       },
                                       "EntryRuleNumber": number,
                                       "EntryType": "string"
                                    }
                                 ],
                                 "NetworkAclId": {
                                    "Description": "string",
                                    "ResourceId": "string"
                                 }
                              },
                              "Description": "string",
                              "EC2AssociateRouteTableAction": {
                                 "Description": "string",
                                 "GatewayId": {
                                    "Description": "string",
                                    "ResourceId": "string"
                                 },
                                 "RouteTableId": {
                                    "Description": "string",
                                    "ResourceId": "string"
                                 },
                                 "SubnetId": {
                                    "Description": "string",
                                    "ResourceId": "string"
                                 }
                              },
                              "EC2CopyRouteTableAction": {
                                 "Description": "string",
                                 "RouteTableId": {
                                    "Description": "string",
                                    "ResourceId": "string"
                                 },
                                 "VpcId": {
                                    "Description": "string",
                                    "ResourceId": "string"
                                 }
                              },
                              "EC2CreateRouteAction": {
                                 "Description": "string",
                                 "DestinationCidrBlock": "string",
                                 "DestinationIpv6CidrBlock": "string",
                                 "DestinationPrefixListId": "string",
                                 "GatewayId": {
                                    "Description": "string",
                                    "ResourceId": "string"
                                 },
                                 "RouteTableId": {
                                    "Description": "string",
                                    "ResourceId": "string"
                                 },
                                 "VpcEndpointId": {
                                    "Description": "string",
                                    "ResourceId": "string"
                                 }
                              },
                              "EC2CreateRouteTableAction": {
                                 "Description": "string",
                                 "VpcId": {
                                    "Description": "string",
                                    "ResourceId": "string"
                                 }
                              },
                              "EC2DeleteRouteAction": {
                                 "Description": "string",
                                 "DestinationCidrBlock": "string",
                                 "DestinationIpv6CidrBlock": "string",
                                 "DestinationPrefixListId": "string",
                                 "RouteTableId": {
                                    "Description": "string",
                                    "ResourceId": "string"
                                 }
                              },
                              "EC2ReplaceRouteAction": {
                                 "Description": "string",
                                 "DestinationCidrBlock": "string",
                                 "DestinationIpv6CidrBlock": "string",
                                 "DestinationPrefixListId": "string",
                                 "GatewayId": {
                                    "Description": "string",
                                    "ResourceId": "string"
                                 },
                                 "RouteTableId": {
                                    "Description": "string",
                                    "ResourceId": "string"
                                 }
                              },
                              "EC2ReplaceRouteTableAssociationAction": {
                                 "AssociationId": {
                                    "Description": "string",
                                    "ResourceId": "string"
                                 },
                                 "Description": "string",
                                 "RouteTableId": {
                                    "Description": "string",
                                    "ResourceId": "string"
                                 }
                              },
                              "FMSPolicyUpdateFirewallCreationConfigAction": {
                                 "Description": "string",
                                 "FirewallCreationConfig": "string"
                              },
                              "ReplaceNetworkAclAssociationAction": {
                                 "AssociationId": {
                                    "Description": "string",
                                    "ResourceId": "string"
                                 },
                                 "Description": "string",
                                 "FMSCanRemediate": boolean,
                                 "NetworkAclId": {
                                    "Description": "string",
                                    "ResourceId": "string"
                                 }
                              }
                           }
                        }
                     ]
                  }
               ],
               "Description": "string"
            },
            "RouteHasOutOfScopeEndpointViolation": {
               "CurrentFirewallSubnetRouteTable": "string",
               "CurrentInternetGatewayRouteTable": "string",
               "FirewallSubnetId": "string",
               "FirewallSubnetRoutes": [
                  {
                     "Destination": "string",
                     "DestinationType": "string",
                     "Target": "string",
                     "TargetType": "string"
                  }
               ],
               "InternetGatewayId": "string",
               "InternetGatewayRoutes": [
                  {
                     "Destination": "string",
                     "DestinationType": "string",
                     "Target": "string",
                     "TargetType": "string"
                  }
               ],
               "RouteTableId": "string",
               "SubnetAvailabilityZone": "string",
               "SubnetAvailabilityZoneId": "string",
               "SubnetId": "string",
               "ViolatingRoutes": [
                  {
                     "Destination": "string",
                     "DestinationType": "string",
                     "Target": "string",
                     "TargetType": "string"
                  }
               ],
               "VpcId": "string"
            },
            "ThirdPartyFirewallMissingExpectedRouteTableViolation": {
               "AvailabilityZone": "string",
               "CurrentRouteTable": "string",
               "ExpectedRouteTable": "string",
               "ViolationTarget": "string",
               "VPC": "string"
            },
            "ThirdPartyFirewallMissingFirewallViolation": {
               "AvailabilityZone": "string",
               "TargetViolationReason": "string",
               "ViolationTarget": "string",
               "VPC": "string"
            },
            "ThirdPartyFirewallMissingSubnetViolation": {
               "AvailabilityZone": "string",
               "TargetViolationReason": "string",
               "ViolationTarget": "string",
               "VPC": "string"
            },
            "WebACLHasIncompatibleConfigurationViolation": {
               "Description": "string",
               "WebACLArn": "string"
            },
            "WebACLHasOutOfScopeResourcesViolation": {
               "OutOfScopeResourceList": [ "string" ],
               "WebACLArn": "string"
            }
         }
      ]
   }
}
```

## Response Elements
<a name="API_GetViolationDetails_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ViolationDetail](#API_GetViolationDetails_ResponseSyntax) **   <a name="fms-GetViolationDetails-response-ViolationDetail"></a>
Violation detail for a resource.
Type: [ViolationDetail](API_ViolationDetail.md) object

## Errors
<a name="API_GetViolationDetails_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalErrorException **
The operation failed because of a system problem, even though the request was valid. Retry your request.
HTTP Status Code: 400

 ** InvalidInputException **
The parameters of the request were invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_GetViolationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/fms-2018-01-01/GetViolationDetails)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/fms-2018-01-01/GetViolationDetails)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/GetViolationDetails)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/fms-2018-01-01/GetViolationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/GetViolationDetails)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/fms-2018-01-01/GetViolationDetails)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/fms-2018-01-01/GetViolationDetails)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/fms-2018-01-01/GetViolationDetails)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/fms-2018-01-01/GetViolationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/GetViolationDetails)
