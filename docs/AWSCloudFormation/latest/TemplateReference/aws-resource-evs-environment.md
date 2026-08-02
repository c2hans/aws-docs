---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-evs-environment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EVS::Environment
<a name="aws-resource-evs-environment"></a>

Creates an Amazon EVS environment that runs VCF software, such as SDDC Manager, NSX Manager, and vCenter Server.

**Note**
When you specify `SELF_DEPLOYED` for `vcfVersion`, Amazon EVS provisions only the VLAN subnets; no hosts are added and no VCF installation is performed. After the environment is created, you can add hosts with `CreateEnvironmentHost` and install VCF yourself. The `licenseInfo`, `hosts`, `vcfHostnames`, `siteId`, and `connectivityInfo` parameters are not supported in this mode.

When you specify any other VCF version, Amazon EVS installs and configures VCF for you. For more information, see [Self-deployed mode](https://docs.aws.amazon.com/evs/latest/userguide/getting-started-self-deployed.html) in the *Amazon EVS User Guide*.

**Important**
When Amazon EVS installs VCF, the default ESX version for the selected VCF version will be used. After a host is added with a specific ESX version, it can only be upgraded using vCenter Lifecycle Manager.

**Note**
You cannot use the `dedicatedHostId` and `placementGroupId` parameters together in the same `CreateEnvironment` action. This results in a `ValidationException` response.

## Syntax
<a name="aws-resource-evs-environment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-evs-environment-syntax.json"></a>

```
{
  "Type" : "AWS::EVS::Environment",
  "Properties" : {
      "[ConnectivityInfo](#cfn-evs-environment-connectivityinfo)" : {{ConnectivityInfo}},
      "[EnvironmentName](#cfn-evs-environment-environmentname)" : {{String}},
      "[Hosts](#cfn-evs-environment-hosts)" : {{[ HostInfoForCreate, ... ]}},
      "[InitialVlans](#cfn-evs-environment-initialvlans)" : {{InitialVlans}},
      "[KmsKeyId](#cfn-evs-environment-kmskeyid)" : {{String}},
      "[LicenseInfo](#cfn-evs-environment-licenseinfo)" : {{LicenseInfo}},
      "[ServiceAccessSecurityGroups](#cfn-evs-environment-serviceaccesssecuritygroups)" : {{ServiceAccessSecurityGroups}},
      "[ServiceAccessSubnetId](#cfn-evs-environment-serviceaccesssubnetid)" : {{String}},
      "[SiteId](#cfn-evs-environment-siteid)" : {{String}},
      "[Tags](#cfn-evs-environment-tags)" : {{[ Tag, ... ]}},
      "[TermsAccepted](#cfn-evs-environment-termsaccepted)" : {{Boolean}},
      "[VcfHostnames](#cfn-evs-environment-vcfhostnames)" : {{VcfHostnames}},
      "[VcfVersion](#cfn-evs-environment-vcfversion)" : {{String}},
      "[VpcId](#cfn-evs-environment-vpcid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-evs-environment-syntax.yaml"></a>

```
Type: AWS::EVS::Environment
Properties:
  [ConnectivityInfo](#cfn-evs-environment-connectivityinfo): {{
    ConnectivityInfo}}
  [EnvironmentName](#cfn-evs-environment-environmentname): {{String}}
  [Hosts](#cfn-evs-environment-hosts): {{
    - HostInfoForCreate}}
  [InitialVlans](#cfn-evs-environment-initialvlans): {{
    InitialVlans}}
  [KmsKeyId](#cfn-evs-environment-kmskeyid): {{String}}
  [LicenseInfo](#cfn-evs-environment-licenseinfo): {{
    LicenseInfo}}
  [ServiceAccessSecurityGroups](#cfn-evs-environment-serviceaccesssecuritygroups): {{
    ServiceAccessSecurityGroups}}
  [ServiceAccessSubnetId](#cfn-evs-environment-serviceaccesssubnetid): {{String}}
  [SiteId](#cfn-evs-environment-siteid): {{String}}
  [Tags](#cfn-evs-environment-tags): {{
    - Tag}}
  [TermsAccepted](#cfn-evs-environment-termsaccepted): {{Boolean}}
  [VcfHostnames](#cfn-evs-environment-vcfhostnames): {{
    VcfHostnames}}
  [VcfVersion](#cfn-evs-environment-vcfversion): {{String}}
  [VpcId](#cfn-evs-environment-vpcid): {{String}}
```

## Properties
<a name="aws-resource-evs-environment-properties"></a>

`ConnectivityInfo`  <a name="cfn-evs-environment-connectivityinfo"></a>
The connectivity configuration for the environment. Amazon EVS requires that you specify two route server peer IDs. During environment creation, the route server endpoints peer with the NSX uplink VLAN for connectivity to the NSX overlay network.
*Required*: No
*Type*: [ConnectivityInfo](aws-properties-evs-environment-connectivityinfo.md)
*Update requires*: Updates are not supported.

`EnvironmentName`  <a name="cfn-evs-environment-environmentname"></a>
The name of the environment.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]{1,100}$`
*Update requires*: Updates are not supported.

`Hosts`  <a name="cfn-evs-environment-hosts"></a>
Required for environment resource creation.
Not supported when `vcfVersion` is `SELF_DEPLOYED`. In that case, you can add hosts using `CreateEnvironmentHost` after the environment is created.
*Required*: Conditional
*Type*: Array of [HostInfoForCreate](aws-properties-evs-environment-hostinfoforcreate.md)
*Minimum*: `4`
*Maximum*: `4`
*Update requires*: Updates are not supported.

`InitialVlans`  <a name="cfn-evs-environment-initialvlans"></a>
The initial VLAN subnets for the environment. Amazon EVS VLAN subnets have a minimum CIDR block size of /28 and a maximum size of /24. Amazon EVS VLAN subnet CIDR blocks must not overlap with other subnets in the VPC.
Required for environment resource creation.
*Required*: Conditional
*Type*: [InitialVlans](aws-properties-evs-environment-initialvlans.md)
*Update requires*: Updates are not supported.

`KmsKeyId`  <a name="cfn-evs-environment-kmskeyid"></a>
The AWS KMS key ID that AWS Secrets Manager uses to encrypt secrets that are associated with the environment. These secrets contain the VCF credentials that are needed to install vCenter Server, NSX, and SDDC Manager.
By default, Amazon EVS use the AWS Secrets Manager managed key `aws/secretsmanager`. You can also specify a customer managed key.
*Required*: No
*Type*: String
*Update requires*: Updates are not supported.

`LicenseInfo`  <a name="cfn-evs-environment-licenseinfo"></a>
 The license information that Amazon EVS requires to create an environment. Amazon EVS requires two license keys: a VCF solution key and a vSAN license key. The VCF solution key must meet minimum core requirements, and the vSAN license key must meet minimum capacity requirements for your selected instance type.
For information about minimum license requirements, see [the VCF subscriptions section](https://docs.aws.amazon.com/evs/latest/userguide/vcf-license-mgmt.html) in the *Amazon EVS User Guide*.
*Required*: No
*Type*: [LicenseInfo](aws-properties-evs-environment-licenseinfo.md)
*Update requires*: Updates are not supported.

`ServiceAccessSecurityGroups`  <a name="cfn-evs-environment-serviceaccesssecuritygroups"></a>
The security groups that allow traffic between the Amazon EVS control plane and your VPC for service access. If a security group is not specified, Amazon EVS uses the default security group in your account for service access.
*Required*: No
*Type*: [ServiceAccessSecurityGroups](aws-properties-evs-environment-serviceaccesssecuritygroups.md)
*Update requires*: Updates are not supported.

`ServiceAccessSubnetId`  <a name="cfn-evs-environment-serviceaccesssubnetid"></a>
 The subnet that is used to establish connectivity between the Amazon EVS control plane and VPC. Amazon EVS uses this subnet to perform validations and create the environment.
*Required*: Yes
*Type*: String
*Pattern*: `^subnet-[a-f0-9]{8}([a-f0-9]{9})?$`
*Minimum*: `15`
*Maximum*: `24`
*Update requires*: Updates are not supported.

`SiteId`  <a name="cfn-evs-environment-siteid"></a>
The Broadcom Site ID that is associated with your Amazon EVS environment. Amazon EVS uses the Broadcom Site ID that you provide to meet Broadcom VCF license usage reporting requirements for Amazon EVS.
*Required*: No
*Type*: String
*Update requires*: Updates are not supported.

`Tags`  <a name="cfn-evs-environment-tags"></a>
Metadata that assists with categorization and organization. Each tag consists of a key and an optional value. You define both. Tags don't propagate to any other cluster or AWS resources.
*Required*: No
*Type*: Array of [Tag](aws-properties-evs-environment-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TermsAccepted`  <a name="cfn-evs-environment-termsaccepted"></a>
Customer confirmation that the customer has purchased and will continue to maintain the required number of VCF software licenses to cover all physical processor cores in the Amazon EVS environment. Information about your VCF software in Amazon EVS will be shared with Broadcom to verify license compliance. Amazon EVS does not validate license keys. To validate license keys, visit the Broadcom support portal.
*Required*: Yes
*Type*: Boolean
*Update requires*: Updates are not supported.

`VcfHostnames`  <a name="cfn-evs-environment-vcfhostnames"></a>
The DNS hostnames to be used by the VCF management appliances in your environment.
For environment creation to be successful, each hostname entry must resolve to a domain name that you've registered in your DNS service of choice and configured in the DHCP option set of your VPC. DNS hostnames cannot be changed after environment creation has started.
*Required*: No
*Type*: [VcfHostnames](aws-properties-evs-environment-vcfhostnames.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VcfVersion`  <a name="cfn-evs-environment-vcfversion"></a>
The VCF version of the environment.
*Required*: Yes
*Type*: String
*Allowed values*: `VCF-5.2.1 | VCF-5.2.2 | SELF_DEPLOYED`
*Update requires*: Updates are not supported.

`VpcId`  <a name="cfn-evs-environment-vpcid"></a>
The VPC associated with the environment.
*Required*: Yes
*Type*: String
*Pattern*: `^vpc-[a-f0-9]{8}([a-f0-9]{9})?$`
*Minimum*: `12`
*Maximum*: `21`
*Update requires*: Updates are not supported.

## Return values
<a name="aws-resource-evs-environment-return-values"></a>

### Ref
<a name="aws-resource-evs-environment-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon EVS `EnvironmentId`. For example: `{ "Ref": "env-1234567890" }`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-evs-environment-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-evs-environment-return-values-fn--getatt-fn--getatt"></a>

`Checks`  <a name="Checks-fn::getatt"></a>
A check on the environment to identify instance health and VMware VCF licensing issues. For example:

```
            {
                "checks": [
                    {
                        "type": "KEY_REUSE",
                        "result": "PASSED"
                    },
                    {
                        "type": "KEY_COVERAGE",
                        "result": "PASSED"
                    },
                    {
                        "type": "REACHABILITY",
                        "result": "PASSED"
                    },
                    {
                        "type": "HOST_COUNT",
                        "result": "PASSED"
                    }
                ]
            }
```

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time that the environment was created. For example:`1749081600.000`.

`Credentials`  <a name="Credentials-fn::getatt"></a>
The VCF credentials that are stored as Amazon EVS managed secrets in AWS Secrets Manager. Amazon EVS stores credentials that are needed to install vCenter Server, NSX, and SDDC Manager. For example:

```
            {
                [
                    {
                        "secretArn": "arn:aws:secretsmanager:us-east-1:000000000000:secret:evs!env-1234567890_vCenterAdmin-MnTMEi"
                    },
                    {
                        "secretArn": "arn:aws:secretsmanager:us-east-1:000000000000:secret:evs!env-1234567890_vCenterRoot-87VyCF"
                    },
                    {
                        "secretArn": "arn:aws:secretsmanager:us-east-1:000000000000:secret:evs!env-1234567890_NSXRoot-SR3k43"
                    },
                    {
                        "secretArn": "arn:aws:secretsmanager:us-east-1:000000000000:secret:evs!env-1234567890_NSXAdmin-L5LUiD"
                    },
                    {
                        "secretArn": "arn:aws:secretsmanager:us-east-1:000000000000:secret:evs!env-1234567890_NSXAudit-Q2oW46"
                    },
                    {
                        "secretArn": "arn:aws:secretsmanager:us-east-1:000000000000:secret:evs!env-1234567890_SDDCManagerRoot-bFulOq"
                    },
                    {
                        "secretArn": "arn:aws:secretsmanager:us-east-1:000000000000:secret:evs!env-1234567890_SDDCManagerVCF-Ec3gES"
                    },
                    {
                        "secretArn": "arn:aws:secretsmanager:us-east-1:000000000000:secret:evs!env-1234567890_SDDCManagerAdmin-JMTAAb"
                    }
                ]
            }
```

`EnvironmentArn`  <a name="EnvironmentArn-fn::getatt"></a>
The Amazon Resource Name (ARN) that is associated with the environment. For example: `arn:aws:evs:us-east-1:000000000000:environment/env-1234567890`.

`EnvironmentId`  <a name="EnvironmentId-fn::getatt"></a>
The unique ID for the environment. For example: `env-1234567890`.

`EnvironmentState`  <a name="EnvironmentState-fn::getatt"></a>
The state of an environment. For example: `CREATED`.

`ModifiedAt`  <a name="ModifiedAt-fn::getatt"></a>
 The date and time that the environment was modified. For example:`1749081600.000`.

`StateDetails`  <a name="StateDetails-fn::getatt"></a>
A detailed description of the `environmentState` of an environment. For example: `Environment successfully created`.
