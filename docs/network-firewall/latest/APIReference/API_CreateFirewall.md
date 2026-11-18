---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_CreateFirewall.html
---

# CreateFirewall
<a name="API_CreateFirewall"></a>

Creates an AWS Network Firewall [Firewall](API_Firewall.md) and accompanying [FirewallStatus](API_FirewallStatus.md) for a VPC.

The firewall defines the configuration settings for an AWS Network Firewall firewall. The settings that you can define at creation include the firewall policy, the subnets in your VPC to use for the firewall endpoints, and any tags that are attached to the firewall AWS resource.

After you create a firewall, you can provide additional settings, like the logging configuration.

To update the settings for a firewall, you use the operations that apply to the settings themselves, for example [UpdateLoggingConfiguration](API_UpdateLoggingConfiguration.md), [AssociateSubnets](API_AssociateSubnets.md), and [UpdateFirewallDeleteProtection](API_UpdateFirewallDeleteProtection.md).

To manage a firewall's tags, use the standard AWS resource tagging operations, [ListTagsForResource](API_ListTagsForResource.md), [TagResource](API_TagResource.md), and [UntagResource](API_UntagResource.md).

To retrieve information about firewalls, use [ListFirewalls](API_ListFirewalls.md) and [DescribeFirewall](API_DescribeFirewall.md).

To generate a report on the last 30 days of traffic monitored by a firewall, use [StartAnalysisReport](API_StartAnalysisReport.md).

To create a proxy mode firewall, specify `VpcEndpoint` and `NatGatewayCreateMappings` instead of `VpcId` and `SubnetMappings`. A proxy mode firewall is an explicit forward proxy. Your clients send HTTP and HTTPS proxy requests to the firewall's proxy DNS name, which `DescribeFirewall` returns in each Availability Zone's `Attachment`. The firewall evaluates proxy traffic with the stateful rules in its firewall policy, and sends allowed traffic out through the NAT gateway in the same Availability Zone. Your clients don't need route table changes. In each Availability Zone, the firewall has one endpoint and one NAT gateway, which Network Firewall creates for you.

## Request Syntax
<a name="API_CreateFirewall_RequestSyntax"></a>

```
{
   "AvailabilityZoneChangeProtection": {{boolean}},
   "AvailabilityZoneMappings": [
      {
         "AvailabilityZone": "{{string}}"
      }
   ],
   "DeleteProtection": {{boolean}},
   "Description": "{{string}}",
   "EnabledAnalysisTypes": [ "{{string}}" ],
   "EncryptionConfiguration": {
      "KeyId": "{{string}}",
      "Type": "{{string}}"
   },
   "FirewallName": "{{string}}",
   "FirewallPolicyArn": "{{string}}",
   "FirewallPolicyChangeProtection": {{boolean}},
   "NatGatewayCreateMappings": [
      {
         "AllocationIds": [ "{{string}}" ],
         "PrivateIps": [ "{{string}}" ],
         "SubnetId": "{{string}}"
      }
   ],
   "ProxySettings": {
      "CertificateArn": "{{string}}",
      "DomainName": "{{string}}",
      "ListenerProperties": [
         {
            "Port": {{number}},
            "Type": "{{string}}"
         }
      ]
   },
   "SubnetChangeProtection": {{boolean}},
   "SubnetMappings": [
      {
         "IPAddressType": "{{string}}",
         "SubnetId": "{{string}}"
      }
   ],
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "TransitGatewayId": "{{string}}",
   "TransparentFilteringNatScope": "{{string}}",
   "VpcEndpoint": {
      "SubnetMappings": [
         {
            "IPAddressType": "{{string}}",
            "SubnetId": "{{string}}"
         }
      ],
      "VpcId": "{{string}}"
   },
   "VpcId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateFirewall_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AvailabilityZoneChangeProtection](#API_CreateFirewall_RequestSyntax) **   <a name="networkfirewall-CreateFirewall-request-AvailabilityZoneChangeProtection"></a>
Optional. A setting indicating whether the firewall is protected against changes to its Availability Zone configuration. When set to `TRUE`, you cannot add or remove Availability Zones without first disabling this protection using [UpdateAvailabilityZoneChangeProtection](API_UpdateAvailabilityZoneChangeProtection.md).
Default value: `FALSE`
Type: Boolean
Required: No

 ** [AvailabilityZoneMappings](#API_CreateFirewall_RequestSyntax) **   <a name="networkfirewall-CreateFirewall-request-AvailabilityZoneMappings"></a>
Required. The Availability Zones where you want to create firewall endpoints for a transit gateway-attached firewall. You must specify at least one Availability Zone. Consider enabling the firewall in every Availability Zone where you have workloads to maintain Availability Zone isolation.
You can modify Availability Zones later using [AssociateAvailabilityZones](API_AssociateAvailabilityZones.md) or [DisassociateAvailabilityZones](API_DisassociateAvailabilityZones.md), but this may briefly disrupt traffic. The `AvailabilityZoneChangeProtection` setting controls whether you can make these modifications.
Type: Array of [AvailabilityZoneMapping](API_AvailabilityZoneMapping.md) objects
Required: No

 ** [DeleteProtection](#API_CreateFirewall_RequestSyntax) **   <a name="networkfirewall-CreateFirewall-request-DeleteProtection"></a>
A flag indicating whether it is possible to delete the firewall. A setting of `TRUE` indicates that the firewall is protected against deletion. Use this setting to protect against accidentally deleting a firewall that is in use. When you create a firewall, the operation initializes this flag to `TRUE`.
Type: Boolean
Required: No

 ** [Description](#API_CreateFirewall_RequestSyntax) **   <a name="networkfirewall-CreateFirewall-request-Description"></a>
A description of the firewall.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `^.*$`
Required: No

 ** [EnabledAnalysisTypes](#API_CreateFirewall_RequestSyntax) **   <a name="networkfirewall-CreateFirewall-request-EnabledAnalysisTypes"></a>
An optional setting indicating the specific traffic analysis types to enable on the firewall.
Type: Array of strings
Valid Values: `TLS_SNI | HTTP_HOST`
Required: No

 ** [EncryptionConfiguration](#API_CreateFirewall_RequestSyntax) **   <a name="networkfirewall-CreateFirewall-request-EncryptionConfiguration"></a>
A complex type that contains settings for encryption of your firewall resources.
Type: [EncryptionConfiguration](API_EncryptionConfiguration.md) object
Required: No

 ** [FirewallName](#API_CreateFirewall_RequestSyntax) **   <a name="networkfirewall-CreateFirewall-request-FirewallName"></a>
The descriptive name of the firewall. You can't change the name of a firewall after you create it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-]+$`
Required: Yes

 ** [FirewallPolicyArn](#API_CreateFirewall_RequestSyntax) **   <a name="networkfirewall-CreateFirewall-request-FirewallPolicyArn"></a>
The Amazon Resource Name (ARN) of the [FirewallPolicy](API_FirewallPolicy.md) that you want to use for the firewall.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:aws.*`
Required: Yes

 ** [FirewallPolicyChangeProtection](#API_CreateFirewall_RequestSyntax) **   <a name="networkfirewall-CreateFirewall-request-FirewallPolicyChangeProtection"></a>
A setting indicating whether the firewall is protected against a change to the firewall policy association. Use this setting to protect against accidentally modifying the firewall policy for a firewall that is in use. When you create a firewall, the operation initializes this setting to `TRUE`.
Type: Boolean
Required: No

 ** [NatGatewayCreateMappings](#API_CreateFirewall_RequestSyntax) **   <a name="networkfirewall-CreateFirewall-request-NatGatewayCreateMappings"></a>
The NAT gateways that Network Firewall creates for a proxy mode firewall, one for each Availability Zone. When you specify this, you create a proxy mode firewall. Destinations see the IP address of the NAT gateway in the client's Availability Zone as the source of the traffic.
Specify one mapping for each Availability Zone in `VpcEndpoint`, and no other Availability Zones. Each NAT gateway subnet must be in the `VpcEndpoint` VPC and can't be one of the firewall endpoint subnets.
You need permission to call the Amazon EC2 `CreateNatGateway` action.
If Network Firewall can't set up an Availability Zone, for example because Amazon EC2 rejects the NAT gateway, it removes the Availability Zone from the firewall. It also deletes the NAT gateway that it created there. The Availability Zone's `Attachment` status is `FAILED`, and its status message explains why. You can add the Availability Zone again with `AssociateSubnets`. If no Availability Zone can be set up, the firewall status is `FAILED`.
Type: Array of [NatGatewayCreateMapping](API_NatGatewayCreateMapping.md) objects
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Required: No

 ** [ProxySettings](#API_CreateFirewall_RequestSyntax) **   <a name="networkfirewall-CreateFirewall-request-ProxySettings"></a>
The proxy settings for a proxy mode firewall: the ports and protocols on which the firewall's proxy listens for traffic, and optionally your own domain name and certificate. If you don't specify listeners, the firewall listens for HTTP on port 3128 and HTTPS on port 8443.
To change the listeners later, use `UpdateProxySettings`.
Type: [ProxySettings](API_ProxySettings.md) object
Required: No

 ** [SubnetChangeProtection](#API_CreateFirewall_RequestSyntax) **   <a name="networkfirewall-CreateFirewall-request-SubnetChangeProtection"></a>
A setting indicating whether the firewall is protected against changes to the subnet associations. Use this setting to protect against accidentally modifying the subnet associations for a firewall that is in use. When you create a firewall, the operation initializes this setting to `TRUE`.
Type: Boolean
Required: No

 ** [SubnetMappings](#API_CreateFirewall_RequestSyntax) **   <a name="networkfirewall-CreateFirewall-request-SubnetMappings"></a>
The public subnets to use for your Network Firewall firewalls. Each subnet must belong to a different Availability Zone in the VPC. Network Firewall creates a firewall endpoint in each subnet.
Type: Array of [SubnetMapping](API_SubnetMapping.md) objects
Required: No

 ** [Tags](#API_CreateFirewall_RequestSyntax) **   <a name="networkfirewall-CreateFirewall-request-Tags"></a>
The key:value pairs to associate with the resource.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 200 items.
Required: No

 ** [TransitGatewayId](#API_CreateFirewall_RequestSyntax) **   <a name="networkfirewall-CreateFirewall-request-TransitGatewayId"></a>
Required when creating a transit gateway-attached firewall. The unique identifier of the transit gateway to attach to this firewall. You can provide either a transit gateway from your account or one that has been shared with you through AWS Resource Access Manager.
After creating the firewall, you cannot change the transit gateway association. To use a different transit gateway, you must create a new firewall.
For information about creating firewalls, see [CreateFirewall](#API_CreateFirewall). For specific guidance about transit gateway-attached firewalls, see [Considerations for transit gateway-attached firewalls](https://docs.aws.amazon.com/network-firewall/latest/developerguide/tgw-firewall-considerations.html) in the * AWS Network Firewall Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^tgw-[0-9a-z]+$`
Required: No

 ** [TransparentFilteringNatScope](#API_CreateFirewall_RequestSyntax) **   <a name="networkfirewall-CreateFirewall-request-TransparentFilteringNatScope"></a>
How a proxy mode firewall handles traffic that isn't sent to its proxy listener. If you don't specify a value, the firewall uses `NAT_ALL`. You can choose from the following values:
+  `NAT_ALL` - After inspection, the firewall sends this traffic out through its NAT gateway, which translates the source address.
+  `NAT_NONE` - After inspection, the firewall returns this traffic to the firewall endpoint without address translation.
You can specify this only for a proxy mode firewall, and you can't change it after you create the firewall.
Type: String
Valid Values: `NAT_ALL | NAT_NONE`
Required: No

 ** [VpcEndpoint](#API_CreateFirewall_RequestSyntax) **   <a name="networkfirewall-CreateFirewall-request-VpcEndpoint"></a>
The VPC and subnets for the endpoints of a proxy mode firewall. Network Firewall creates a firewall endpoint in each subnet that you specify. It also creates the firewall's NAT gateways in this VPC, in the subnets that you specify in `NatGatewayCreateMappings`.
To create a proxy mode firewall, you must specify `VpcEndpoint` and `NatGatewayCreateMappings`, and you must not specify the top-level `VpcId` and `SubnetMappings`. Specify one subnet for each Availability Zone where you want to use the firewall.
Type: [VpcEndpoint](API_VpcEndpoint.md) object
Required: No

 ** [VpcId](#API_CreateFirewall_RequestSyntax) **   <a name="networkfirewall-CreateFirewall-request-VpcId"></a>
The unique identifier of the VPC where Network Firewall should create the firewall.
You can't change this setting after you create the firewall.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^vpc-[0-9a-f]+$`
Required: No

## Response Syntax
<a name="API_CreateFirewall_ResponseSyntax"></a>

```
{
   "Firewall": {
      "AvailabilityZoneChangeProtection": boolean,
      "AvailabilityZoneMappings": [
         {
            "AvailabilityZone": "string"
         }
      ],
      "ContextStoreId": "string",
      "ContextStoreOwnerAccountId": "string",
      "DeleteProtection": boolean,
      "Description": "string",
      "EnabledAnalysisTypes": [ "string" ],
      "EncryptionConfiguration": {
         "KeyId": "string",
         "Type": "string"
      },
      "FirewallArn": "string",
      "FirewallId": "string",
      "FirewallName": "string",
      "FirewallPolicyArn": "string",
      "FirewallPolicyChangeProtection": boolean,
      "NatGatewayCreateMappings": [
         {
            "AllocationIds": [ "string" ],
            "PrivateIps": [ "string" ],
            "SubnetId": "string"
         }
      ],
      "NumberOfAssociations": number,
      "ProxySettings": {
         "CertificateArn": "string",
         "DomainName": "string",
         "ListenerProperties": [
            {
               "Port": number,
               "Type": "string"
            }
         ]
      },
      "SubnetChangeProtection": boolean,
      "SubnetMappings": [
         {
            "IPAddressType": "string",
            "SubnetId": "string"
         }
      ],
      "Tags": [
         {
            "Key": "string",
            "Value": "string"
         }
      ],
      "TransitGatewayId": "string",
      "TransitGatewayOwnerAccountId": "string",
      "TransparentFilteringNatScope": "string",
      "VpcEndpoint": {
         "SubnetMappings": [
            {
               "IPAddressType": "string",
               "SubnetId": "string"
            }
         ],
         "VpcId": "string"
      },
      "VpcId": "string"
   },
   "FirewallStatus": {
      "CapacityUsageSummary": {
         "CIDRs": {
            "AvailableCIDRCount": number,
            "IPSetReferences": {
               "string" : {
                  "ResolvedCIDRCount": number
               }
            },
            "UtilizedCIDRCount": number
         }
      },
      "ConfigurationSyncStateSummary": "string",
      "ContextStoreSyncState": {
         "StatusMessage": "string",
         "SyncStatus": "string"
      },
      "Status": "string",
      "SyncStates": {
         "string" : {
            "Attachment": {
               "DnsName": "string",
               "EndpointId": "string",
               "Status": "string",
               "StatusMessage": "string",
               "SubnetId": "string"
            },
            "Config": {
               "string" : {
                  "SyncStatus": "string",
                  "UpdateToken": "string"
               }
            },
            "NatGatewayAttachments": [
               {
                  "DnsName": "string",
                  "NatGatewayId": "string",
                  "Status": "string",
                  "StatusMessage": "string"
               }
            ]
         }
      },
      "TransitGatewayAttachmentSyncState": {
         "AttachmentId": "string",
         "StatusMessage": "string",
         "TransitGatewayAttachmentStatus": "string"
      }
   }
}
```

## Response Elements
<a name="API_CreateFirewall_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Firewall](#API_CreateFirewall_ResponseSyntax) **   <a name="networkfirewall-CreateFirewall-response-Firewall"></a>
The configuration settings for the firewall. These settings include the firewall policy and the subnets in your VPC to use for the firewall endpoints.
Type: [Firewall](API_Firewall.md) object

 ** [FirewallStatus](#API_CreateFirewall_ResponseSyntax) **   <a name="networkfirewall-CreateFirewall-response-FirewallStatus"></a>
Detailed information about the current status of a [Firewall](API_Firewall.md). You can retrieve this for a firewall by calling [DescribeFirewall](API_DescribeFirewall.md) and providing the firewall name and ARN.
The firewall status indicates a combined status. It indicates whether all subnets are up-to-date with the latest firewall configurations, which is based on the sync states config values, and also whether all subnets have their endpoints fully enabled, based on their sync states attachment values.
Type: [FirewallStatus](API_FirewallStatus.md) object

## Errors
<a name="API_CreateFirewall_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InsufficientCapacityException **
 AWS doesn't currently have enough available capacity to fulfill your request. Try your request later.
HTTP Status Code: 500

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

 ** LimitExceededException **
Unable to perform the operation because doing so would violate a limit setting.
HTTP Status Code: 400

 ** ThrottlingException **
Unable to process the request due to throttling limitations.
HTTP Status Code: 400

## See Also
<a name="API_CreateFirewall_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/CreateFirewall)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/CreateFirewall)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/CreateFirewall)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/CreateFirewall)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/CreateFirewall)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/CreateFirewall)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/CreateFirewall)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/CreateFirewall)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/CreateFirewall)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/CreateFirewall)
