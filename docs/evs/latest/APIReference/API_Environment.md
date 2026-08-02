---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_Environment.html
---

# Environment
<a name="API_Environment"></a>

An object that represents an Amazon EVS environment.

## Contents
<a name="API_Environment_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** checks **   <a name="evs-Type-Environment-checks"></a>
A check on the environment to identify connector health.
Type: Array of [Check](API_Check.md) objects
Required: No

 ** connectivityInfo **   <a name="evs-Type-Environment-connectivityInfo"></a>
The connectivity configuration for the environment. Amazon EVS requires that you specify two route server peer IDs. During environment creation, the route server endpoints peer with the NSX uplink VLAN for connectivity to the NSX overlay network.
Type: [ConnectivityInfo](API_ConnectivityInfo.md) object
Required: No

 ** createdAt **   <a name="evs-Type-Environment-createdAt"></a>
The date and time that the environment was created.
Type: Timestamp
Required: No

 ** credentials **   <a name="evs-Type-Environment-credentials"></a>
The VCF credentials that are stored as Amazon EVS managed secrets in AWS Secrets Manager.
Amazon EVS stores credentials that are needed to install vCenter Server, NSX, and SDDC Manager.
Type: Array of [Secret](API_Secret.md) objects
Required: No

 ** environmentArn **   <a name="evs-Type-Environment-environmentArn"></a>
The Amazon Resource Name (ARN) that is associated with the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws:evs:[a-z]{2}-[a-z]+-[0-9]:[0-9]{12}:environment/[a-zA-Z0-9_-]+`
Required: No

 ** environmentId **   <a name="evs-Type-Environment-environmentId"></a>
The unique ID for the environment.
Type: String
Pattern: `(env-[a-zA-Z0-9]{10})`
Required: No

 ** environmentName **   <a name="evs-Type-Environment-environmentName"></a>
The name of the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** environmentState **   <a name="evs-Type-Environment-environmentState"></a>
The state of an environment.
Type: String
Valid Values: `CREATING | CREATED | DELETING | DELETED | CREATE_FAILED`
Required: No

 ** environmentStatus **   <a name="evs-Type-Environment-environmentStatus"></a>
Reports impaired functionality that stems from issues internal to the environment, such as impaired reachability.
Type: String
Valid Values: `PASSED | FAILED | UNKNOWN`
Required: No

 ** kmsKeyId **   <a name="evs-Type-Environment-kmsKeyId"></a>
The AWS KMS key ID that AWS Secrets Manager uses to encrypt secrets that are associated with the environment. These secrets contain the VCF credentials that are needed to install vCenter Server, NSX, and SDDC Manager.
By default, Amazon EVS use the AWS Secrets Manager managed key `aws/secretsmanager`. You can also specify a customer managed key.
Type: String
Required: No

 ** licenseInfo **   <a name="evs-Type-Environment-licenseInfo"></a>
 The license information that Amazon EVS requires to create an environment. Amazon EVS requires two license keys: a VCF solution key and a vSAN license key. The VCF solution key must meet minimum core requirements, and the vSAN license key must meet minimum capacity requirements for your selected instance type.
For information about minimum license requirements, see [the VCF subscriptions section](https://docs.aws.amazon.com/evs/latest/userguide/vcf-license-mgmt.html) in the *Amazon EVS User Guide*.
Type: Array of [LicenseInfo](API_LicenseInfo.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** modifiedAt **   <a name="evs-Type-Environment-modifiedAt"></a>
 The date and time that the environment was modified.
Type: Timestamp
Required: No

 ** serviceAccessSecurityGroups **   <a name="evs-Type-Environment-serviceAccessSecurityGroups"></a>
The security groups that allow traffic between the Amazon EVS control plane and your VPC for service access. If a security group is not specified, Amazon EVS uses the default security group in your account for service access.
Type: [ServiceAccessSecurityGroups](API_ServiceAccessSecurityGroups.md) object
Required: No

 ** serviceAccessSubnetId **   <a name="evs-Type-Environment-serviceAccessSubnetId"></a>
 The subnet that is used to establish connectivity between the Amazon EVS control plane and VPC. Amazon EVS uses this subnet to perform validations and create the environment.
Type: String
Length Constraints: Minimum length of 15. Maximum length of 24.
Pattern: `subnet-[a-f0-9]{8}([a-f0-9]{9})?`
Required: No

 ** siteId **   <a name="evs-Type-Environment-siteId"></a>
The Broadcom Site ID that is associated with your Amazon EVS environment. Amazon EVS uses the Broadcom Site ID that you provide to meet Broadcom VCF license usage reporting requirements for Amazon EVS.
Type: String
Required: No

 ** stateDetails **   <a name="evs-Type-Environment-stateDetails"></a>
A detailed description of the `environmentState` of an environment.
Type: String
Required: No

 ** termsAccepted **   <a name="evs-Type-Environment-termsAccepted"></a>
Customer confirmation that the customer has purchased and will continue to maintain the required number of VCF software licenses to cover all physical processor cores in the Amazon EVS environment. Information about your VCF software in Amazon EVS will be shared with Broadcom to verify license compliance. Amazon EVS does not validate license keys. To validate license keys, visit the Broadcom support portal.
Type: Boolean
Required: No

 ** vcfHostnames **   <a name="evs-Type-Environment-vcfHostnames"></a>
The DNS hostnames to be used by the VCF management appliances in your environment.
For environment creation to be successful, each hostname entry must resolve to a domain name that you've registered in your DNS service of choice and configured in the DHCP option set of your VPC. DNS hostnames cannot be changed after environment creation has started.
Type: [VcfHostnames](API_VcfHostnames.md) object
Required: No

 ** vcfVersion **   <a name="evs-Type-Environment-vcfVersion"></a>
The VCF version of the environment.
Type: String
Valid Values: `VCF-5.2.1 | VCF-5.2.2 | SELF_DEPLOYED`
Required: No

 ** vpcId **   <a name="evs-Type-Environment-vpcId"></a>
The VPC associated with the environment.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 21.
Pattern: `vpc-[a-f0-9]{8}([a-f0-9]{9})?`
Required: No

## See Also
<a name="API_Environment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/evs-2023-07-27/Environment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/evs-2023-07-27/Environment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/Environment)
