---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_CreateEnvironment.html
---

# CreateEnvironment
<a name="API_CreateEnvironment"></a>

Creates an Amazon EVS environment that runs VCF software, such as SDDC Manager, NSX Manager, and vCenter Server.

**Note**
When you specify `SELF_DEPLOYED` for `vcfVersion`, Amazon EVS provisions only the VLAN subnets; no hosts are added and no VCF installation is performed. After the environment is created, you can add hosts with `CreateEnvironmentHost` and install VCF yourself. The `licenseInfo`, `hosts`, `vcfHostnames`, `siteId`, and `connectivityInfo` parameters are not supported in this mode.

When you specify any other VCF version, Amazon EVS installs and configures VCF for you. For more information, see [Self-deployed mode](https://docs.aws.amazon.com/evs/latest/userguide/getting-started-self-deployed.html) in the *Amazon EVS User Guide*.

**Important**
When Amazon EVS installs VCF, the default ESX version for the selected VCF version will be used. After a host is added with a specific ESX version, it can only be upgraded using vCenter Lifecycle Manager.

**Note**
You cannot use the `dedicatedHostId` and `placementGroupId` parameters together in the same `CreateEnvironment` action. This results in a `ValidationException` response.

## Request Syntax
<a name="API_CreateEnvironment_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "connectivityInfo": {
      "privateRouteServerPeerings": [ "{{string}}" ]
   },
   "environmentName": "{{string}}",
   "hosts": [
      {
         "dedicatedHostId": "{{string}}",
         "hostName": "{{string}}",
         "instanceType": "{{string}}",
         "keyName": "{{string}}",
         "placementGroupId": "{{string}}"
      }
   ],
   "initialVlans": {
      "edgeVTep": {
         "cidr": "{{string}}"
      },
      "expansionVlan1": {
         "cidr": "{{string}}"
      },
      "expansionVlan2": {
         "cidr": "{{string}}"
      },
      "hcx": {
         "cidr": "{{string}}"
      },
      "hcxNetworkAclId": "{{string}}",
      "isHcxPublic": {{boolean}},
      "nsxUplink": {
         "cidr": "{{string}}"
      },
      "vmkManagement": {
         "cidr": "{{string}}"
      },
      "vmManagement": {
         "cidr": "{{string}}"
      },
      "vMotion": {
         "cidr": "{{string}}"
      },
      "vSan": {
         "cidr": "{{string}}"
      },
      "vTep": {
         "cidr": "{{string}}"
      }
   },
   "kmsKeyId": "{{string}}",
   "licenseInfo": [
      {
         "solutionKey": "{{string}}",
         "vsanKey": "{{string}}"
      }
   ],
   "serviceAccessSecurityGroups": {
      "securityGroups": [ "{{string}}" ]
   },
   "serviceAccessSubnetId": "{{string}}",
   "siteId": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "termsAccepted": {{boolean}},
   "vcfHostnames": {
      "cloudBuilder": "{{string}}",
      "nsx": "{{string}}",
      "nsxEdge1": "{{string}}",
      "nsxEdge2": "{{string}}",
      "nsxManager1": "{{string}}",
      "nsxManager2": "{{string}}",
      "nsxManager3": "{{string}}",
      "sddcManager": "{{string}}",
      "vCenter": "{{string}}"
   },
   "vcfVersion": "{{string}}",
   "vpcId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateEnvironment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [initialVlans](#API_CreateEnvironment_RequestSyntax) **   <a name="evs-CreateEnvironment-request-initialVlans"></a>
The initial VLAN subnets for the Amazon EVS environment.
For each Amazon EVS VLAN subnet, you must specify a non-overlapping CIDR block. Amazon EVS VLAN subnets have a minimum CIDR block size of /28 and a maximum size of /24.
Type: [InitialVlans](API_InitialVlans.md) object
Required: Yes

 ** [serviceAccessSubnetId](#API_CreateEnvironment_RequestSyntax) **   <a name="evs-CreateEnvironment-request-serviceAccessSubnetId"></a>
The subnet that is used to establish connectivity between the Amazon EVS control plane and VPC. The Amazon EVS control plane uses this subnet to interface with your environment. This includes validating DNS records and enabling Amazon EVS Connectors.
Type: String
Length Constraints: Minimum length of 15. Maximum length of 24.
Pattern: `subnet-[a-f0-9]{8}([a-f0-9]{9})?`
Required: Yes

 ** [termsAccepted](#API_CreateEnvironment_RequestSyntax) **   <a name="evs-CreateEnvironment-request-termsAccepted"></a>
Confirmation that the customer has purchased and will continue to maintain the required number of VCF software licenses to cover all physical processor cores in the Amazon EVS environment. Information about your VCF software in Amazon EVS will be shared with Broadcom to verify license compliance. Amazon EVS does not validate license keys. To validate license keys, visit the Broadcom support portal.
Type: Boolean
Required: Yes

 ** [vcfVersion](#API_CreateEnvironment_RequestSyntax) **   <a name="evs-CreateEnvironment-request-vcfVersion"></a>
The VCF version to use for the environment.
+  `SELF_DEPLOYED`: You install VCF yourself. The `licenseInfo`, `hosts`, `vcfHostnames`, `siteId`, and `connectivityInfo` parameters are not supported.
+ Any other valid value: Amazon EVS installs and configures VCF for you in the version you specify.
Type: String
Valid Values: `VCF-5.2.1 | VCF-5.2.2 | SELF_DEPLOYED`
Required: Yes

 ** [vpcId](#API_CreateEnvironment_RequestSyntax) **   <a name="evs-CreateEnvironment-request-vpcId"></a>
A unique ID for the VPC that the environment is deployed inside.
Amazon EVS requires that all VPC subnets exist in a single Availability Zone in a Region where the service is available.
The VPC that you specify must have a valid DHCP option set with domain name, at least two DNS servers, and an NTP server. These settings are used to configure your VCF appliances and hosts. The VPC cannot be used with any other deployed Amazon EVS environment. Amazon EVS does not provide multi-VPC support for environments at this time.
Amazon EVS does not support the following AWS networking options for NSX overlay connectivity: cross-Region VPC peering, Amazon S3 gateway endpoints, or AWS Direct Connect virtual private gateway associations.
Ensure that you specify a VPC that is adequately sized to accommodate the Amazon EVS subnets.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 21.
Pattern: `vpc-[a-f0-9]{8}([a-f0-9]{9})?`
Required: Yes

 ** [clientToken](#API_CreateEnvironment_RequestSyntax) **   <a name="evs-CreateEnvironment-request-clientToken"></a>
This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.
A unique, case-sensitive identifier that you provide to ensure the idempotency of the environment creation request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[!-~]+`
Required: No

 ** [connectivityInfo](#API_CreateEnvironment_RequestSyntax) **   <a name="evs-CreateEnvironment-request-connectivityInfo"></a>
The connectivity configuration for the environment. Amazon EVS requires that you specify two route server peer IDs. During environment creation, the route server endpoints peer with the NSX edges over the NSX uplink subnet, providing BGP-based dynamic routing for overlay networks.
Not supported when `vcfVersion` is `SELF_DEPLOYED`.
Type: [ConnectivityInfo](API_ConnectivityInfo.md) object
Required: No

 ** [environmentName](#API_CreateEnvironment_RequestSyntax) **   <a name="evs-CreateEnvironment-request-environmentName"></a>
The name to give to your environment. The name can contain only alphanumeric characters (case-sensitive), hyphens, and underscores. It must start with an alphanumeric character, and can't be longer than 100 characters. The name must be unique within the AWS Region and AWS account that you're creating the environment in.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** [hosts](#API_CreateEnvironment_RequestSyntax) **   <a name="evs-CreateEnvironment-request-hosts"></a>
The ESX hosts to add to the environment. For each host, provide the desired hostname, EC2 SSH keypair name, and EC2 instance type. Optionally, provide a partition or cluster placement group, or use Amazon EC2 Dedicated Hosts.
Not supported when `vcfVersion` is `SELF_DEPLOYED`. In that case, you can add hosts using `CreateEnvironmentHost` after the environment is created.
Type: Array of [HostInfoForCreate](API_HostInfoForCreate.md) objects
Array Members: Fixed number of 4 items.
Required: No

 ** [kmsKeyId](#API_CreateEnvironment_RequestSyntax) **   <a name="evs-CreateEnvironment-request-kmsKeyId"></a>
A unique ID for the customer-managed KMS key that is used to encrypt the VCF credential pairs for SDDC Manager, NSX Manager, and vCenter appliances. These credentials are stored in AWS Secrets Manager.
Type: String
Required: No

 ** [licenseInfo](#API_CreateEnvironment_RequestSyntax) **   <a name="evs-CreateEnvironment-request-licenseInfo"></a>
The license information that Amazon EVS requires to create an environment. Amazon EVS requires two license keys: a VCF solution key and a vSAN license key. The VCF solution key must meet minimum core requirements, and the vSAN license key must meet minimum capacity requirements for your selected instance type.
For information about minimum license requirements, see [the VCF subscriptions section](https://docs.aws.amazon.com/evs/latest/userguide/vcf-license-mgmt.html) in the *Amazon EVS User Guide*.
VCF licenses can be used for only one Amazon EVS environment. Amazon EVS does not support reuse of VCF licenses for multiple environments.
VCF license information can be retrieved from the Broadcom portal.
Not supported when `vcfVersion` is `SELF_DEPLOYED`.
Type: Array of [LicenseInfo](API_LicenseInfo.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** [serviceAccessSecurityGroups](#API_CreateEnvironment_RequestSyntax) **   <a name="evs-CreateEnvironment-request-serviceAccessSecurityGroups"></a>
The security group that controls communication between the Amazon EVS control plane and VPC. The default security group is used if a custom security group isn't specified.
The security group should allow access to the following.
+ TCP/UDP access to the DNS servers
+ HTTPS/SSH access to the host management VLAN subnet
+ HTTPS/SSH access to the Management VM VLAN subnet
You should avoid modifying the security group rules after deployment, as this can break the persistent connection between the Amazon EVS control plane and VPC. This can cause future environment actions like adding or removing hosts to fail.
Type: [ServiceAccessSecurityGroups](API_ServiceAccessSecurityGroups.md) object
Required: No

 ** [siteId](#API_CreateEnvironment_RequestSyntax) **   <a name="evs-CreateEnvironment-request-siteId"></a>
The Broadcom Site ID that is allocated to you as part of your electronic software delivery. This ID allows customer access to the Broadcom portal, and is provided to you by Broadcom at the close of your software contract or contract renewal. Amazon EVS uses the Broadcom Site ID that you provide to meet Broadcom VCF license usage reporting requirements for Amazon EVS.
Not supported when `vcfVersion` is `SELF_DEPLOYED`.
Type: String
Required: No

 ** [tags](#API_CreateEnvironment_RequestSyntax) **   <a name="evs-CreateEnvironment-request-tags"></a>
Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or AWS resources.
Type: String to string map
Map Entries: Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\w.:/=+-@]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[\w.:/=+-@]+|`
Required: No

 ** [vcfHostnames](#API_CreateEnvironment_RequestSyntax) **   <a name="evs-CreateEnvironment-request-vcfHostnames"></a>
The DNS hostnames for the virtual machines that host the VCF management appliances. Provide hostnames for vCenter, NSX Manager, SDDC Manager, and Cloud Builder.
Not supported when `vcfVersion` is `SELF_DEPLOYED`.
Type: [VcfHostnames](API_VcfHostnames.md) object
Required: No

## Response Syntax
<a name="API_CreateEnvironment_ResponseSyntax"></a>

```
{
   "environment": {
      "checks": [
         {
            "id": "string",
            "impairedSince": number,
            "result": "string",
            "type": "string"
         }
      ],
      "connectivityInfo": {
         "privateRouteServerPeerings": [ "string" ]
      },
      "createdAt": number,
      "credentials": [
         {
            "secretArn": "string"
         }
      ],
      "environmentArn": "string",
      "environmentId": "string",
      "environmentName": "string",
      "environmentState": "string",
      "environmentStatus": "string",
      "kmsKeyId": "string",
      "licenseInfo": [
         {
            "solutionKey": "string",
            "vsanKey": "string"
         }
      ],
      "modifiedAt": number,
      "serviceAccessSecurityGroups": {
         "securityGroups": [ "string" ]
      },
      "serviceAccessSubnetId": "string",
      "siteId": "string",
      "stateDetails": "string",
      "termsAccepted": boolean,
      "vcfHostnames": {
         "cloudBuilder": "string",
         "nsx": "string",
         "nsxEdge1": "string",
         "nsxEdge2": "string",
         "nsxManager1": "string",
         "nsxManager2": "string",
         "nsxManager3": "string",
         "sddcManager": "string",
         "vCenter": "string"
      },
      "vcfVersion": "string",
      "vpcId": "string"
   }
}
```

## Response Elements
<a name="API_CreateEnvironment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [environment](#API_CreateEnvironment_ResponseSyntax) **   <a name="evs-CreateEnvironment-response-environment"></a>
A description of the created environment.
Type: [Environment](API_Environment.md) object

## Errors
<a name="API_CreateEnvironment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [ValidationException](API_ValidationException.md)
The input fails to satisfy the specified constraints. You will see this exception if invalid inputs are provided for any of the Amazon EVS environment operations, or if a list operation is performed on an environment resource that is still initializing.
 ** fieldList **
A list of fields that didn't validate.
 ** message **
Describes the error encountered.
 ** reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/evs-2023-07-27/CreateEnvironment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/evs-2023-07-27/CreateEnvironment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/evs-2023-07-27/CreateEnvironment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/evs-2023-07-27/CreateEnvironment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/evs-2023-07-27/CreateEnvironment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/evs-2023-07-27/CreateEnvironment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/evs-2023-07-27/CreateEnvironment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/evs-2023-07-27/CreateEnvironment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/evs-2023-07-27/CreateEnvironment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/CreateEnvironment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic VMware Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query evs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
