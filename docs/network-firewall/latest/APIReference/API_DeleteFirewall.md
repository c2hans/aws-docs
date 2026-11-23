---
source_url: https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_DeleteFirewall.html
---

# DeleteFirewall

Deletes the specified [Firewall](API_Firewall.md) and its [FirewallStatus](API_FirewallStatus.md). This operation requires the firewall's `DeleteProtection` flag to be `FALSE`. You can't revert this operation.

You can check whether a firewall is in use by reviewing the route tables for the Availability Zones where you have firewall subnet mappings. Retrieve the subnet mappings by calling [DescribeFirewall](API_DescribeFirewall.md). You define and update the route tables through Amazon VPC. As needed, update the route tables for the zones to remove the firewall endpoints. When the route tables no longer use the firewall endpoints, you can remove the firewall safely.

To delete a firewall, remove the delete protection if you need to using [UpdateFirewallDeleteProtection](API_UpdateFirewallDeleteProtection.md), then delete the firewall by calling [DeleteFirewall](API_DeleteFirewall.md).

Deleting a proxy mode firewall detaches its NAT gateways. To also delete the NAT gateways that Network Firewall created for the firewall, specify `DeleteAssociatedNatGateways`.

## Request Syntax
<a name="API_DeleteFirewall_RequestSyntax"></a>

```
{
   "DeleteAssociatedNatGateways": {{boolean}},
   "FirewallArn": "{{string}}",
   "FirewallName": "{{string}}",
   "FirewallType": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteFirewall_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DeleteAssociatedNatGateways](#API_DeleteFirewall_RequestSyntax) **   <a name="networkfirewall-DeleteFirewall-request-DeleteAssociatedNatGateways"></a>
Specifies whether to delete the NAT gateways that Network Firewall created for a proxy mode firewall when you delete the firewall. You can choose from the following values:
+  `FALSE` - Network Firewall detaches the NAT gateways from the firewall and keeps them. This is the default.
+  `TRUE` - Network Firewall also deletes the NAT gateways. The firewall status stays `DELETING` until they're deleted. You need permission to call the Amazon EC2 `DeleteNatGateway` action.
You can't specify `TRUE` for a firewall that isn't a proxy mode firewall.
Type: Boolean
Required: No

 ** [FirewallArn](#API_DeleteFirewall_RequestSyntax) **   <a name="networkfirewall-DeleteFirewall-request-FirewallArn"></a>
The Amazon Resource Name (ARN) of the firewall.
You must specify the ARN or the name, and you can specify both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn:aws.*`
Required: No

 ** [FirewallName](#API_DeleteFirewall_RequestSyntax) **   <a name="networkfirewall-DeleteFirewall-request-FirewallName"></a>
The descriptive name of the firewall. You can't change the name of a firewall after you create it.
You must specify the ARN or the name, and you can specify both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-]+$`
Required: No

 ** [FirewallType](#API_DeleteFirewall_RequestSyntax) **   <a name="networkfirewall-DeleteFirewall-request-FirewallType"></a>
The type of firewall that the request targets. Network Firewall supports the following firewall types:
+  `IGW_FIREWALL` - An internet gateway firewall, which AWS Network Security Manager creates and manages for a VPC.
+  `FIREWALL` - A standard Network Firewall firewall.
If you specify the firewall ARN, the type must match the resource type in the ARN. If you specify only the firewall name, Network Firewall uses this value to identify the firewall. If you don't specify a type, the default is `FIREWALL`.
Type: String
Valid Values: `FIREWALL | IGW_FIREWALL`
Required: No

## Response Syntax
<a name="API_DeleteFirewall_ResponseSyntax"></a>

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
      "IgwFirewallConfiguration": {
         "EnforcementMode": "string"
      },
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
            "AddressTranslations": {
               "PublicIPv4Addresses": [ "string" ],
               "PublicIPv6Addresses": [ "string" ]
            },
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
<a name="API_DeleteFirewall_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Firewall](#API_DeleteFirewall_ResponseSyntax) **   <a name="networkfirewall-DeleteFirewall-response-Firewall"></a>
A firewall defines the behavior of a firewall, the main VPC where the firewall is used, the Availability Zones where the firewall can be used, and one subnet to use for a firewall endpoint within each of the Availability Zones. The Availability Zones are defined implicitly in the subnet specifications.
In addition to the firewall endpoints that you define in this `Firewall` specification, you can create firewall endpoints in `VpcEndpointAssociation` resources for any VPC, in any Availability Zone where the firewall is already in use.
The status of the firewall, for example whether it's ready to filter network traffic, is provided in the corresponding [FirewallStatus](API_FirewallStatus.md). You can retrieve both the firewall and firewall status by calling [DescribeFirewall](API_DescribeFirewall.md).
Type: [Firewall](API_Firewall.md) object

 ** [FirewallStatus](#API_DeleteFirewall_ResponseSyntax) **   <a name="networkfirewall-DeleteFirewall-response-FirewallStatus"></a>
Detailed information about the current status of a [Firewall](API_Firewall.md). You can retrieve this for a firewall by calling [DescribeFirewall](API_DescribeFirewall.md) and providing the firewall name and ARN.
The firewall status indicates a combined status. It indicates whether all subnets are up-to-date with the latest firewall configurations, which is based on the sync states config values, and also whether all subnets have their endpoints fully enabled, based on their sync states attachment values.
Type: [FirewallStatus](API_FirewallStatus.md) object

## Errors
<a name="API_DeleteFirewall_Errors"></a>

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

 ** ResourceNotFoundException **
Unable to locate a resource using the parameters that you provided.
HTTP Status Code: 400

 ** ThrottlingException **
Unable to process the request due to throttling limitations.
HTTP Status Code: 400

 ** UnsupportedOperationException **
The operation you requested isn't supported by Network Firewall.
HTTP Status Code: 400

## See Also
<a name="API_DeleteFirewall_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/network-firewall-2020-11-12/DeleteFirewall)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/network-firewall-2020-11-12/DeleteFirewall)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-firewall-2020-11-12/DeleteFirewall)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/network-firewall-2020-11-12/DeleteFirewall)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-firewall-2020-11-12/DeleteFirewall)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/network-firewall-2020-11-12/DeleteFirewall)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/network-firewall-2020-11-12/DeleteFirewall)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/network-firewall-2020-11-12/DeleteFirewall)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/network-firewall-2020-11-12/DeleteFirewall)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-firewall-2020-11-12/DeleteFirewall)
