---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-patchbaseline.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSM::PatchBaseline
<a name="aws-resource-ssm-patchbaseline"></a>

The `AWS::SSM::PatchBaseline` resource defines the basic information for an AWS Systems Manager patch baseline. A patch baseline defines which patches are approved for installation on your instances.

For more information, see [CreatePatchBaseline](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreatePatchBaseline.html) in the *AWS Systems Manager API Reference*.

## Syntax
<a name="aws-resource-ssm-patchbaseline-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ssm-patchbaseline-syntax.json"></a>

```
{
  "Type" : "AWS::SSM::PatchBaseline",
  "Properties" : {
      "[ApprovalRules](#cfn-ssm-patchbaseline-approvalrules)" : {{RuleGroup}},
      "[ApprovedPatches](#cfn-ssm-patchbaseline-approvedpatches)" : {{[ String, ... ]}},
      "[ApprovedPatchesComplianceLevel](#cfn-ssm-patchbaseline-approvedpatchescompliancelevel)" : {{String}},
      "[ApprovedPatchesEnableNonSecurity](#cfn-ssm-patchbaseline-approvedpatchesenablenonsecurity)" : {{Boolean}},
      "[AvailableSecurityUpdatesComplianceStatus](#cfn-ssm-patchbaseline-availablesecurityupdatescompliancestatus)" : {{String}},
      "[DefaultBaseline](#cfn-ssm-patchbaseline-defaultbaseline)" : {{Boolean}},
      "[Description](#cfn-ssm-patchbaseline-description)" : {{String}},
      "[GlobalFilters](#cfn-ssm-patchbaseline-globalfilters)" : {{PatchFilterGroup}},
      "[Name](#cfn-ssm-patchbaseline-name)" : {{String}},
      "[OperatingSystem](#cfn-ssm-patchbaseline-operatingsystem)" : {{String}},
      "[PatchGroups](#cfn-ssm-patchbaseline-patchgroups)" : {{[ String, ... ]}},
      "[RejectedPatches](#cfn-ssm-patchbaseline-rejectedpatches)" : {{[ String, ... ]}},
      "[RejectedPatchesAction](#cfn-ssm-patchbaseline-rejectedpatchesaction)" : {{String}},
      "[Sources](#cfn-ssm-patchbaseline-sources)" : {{[ PatchSource, ... ]}},
      "[Tags](#cfn-ssm-patchbaseline-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ssm-patchbaseline-syntax.yaml"></a>

```
Type: AWS::SSM::PatchBaseline
Properties:
  [ApprovalRules](#cfn-ssm-patchbaseline-approvalrules): {{
    RuleGroup}}
  [ApprovedPatches](#cfn-ssm-patchbaseline-approvedpatches): {{
    - String}}
  [ApprovedPatchesComplianceLevel](#cfn-ssm-patchbaseline-approvedpatchescompliancelevel): {{String}}
  [ApprovedPatchesEnableNonSecurity](#cfn-ssm-patchbaseline-approvedpatchesenablenonsecurity): {{Boolean}}
  [AvailableSecurityUpdatesComplianceStatus](#cfn-ssm-patchbaseline-availablesecurityupdatescompliancestatus): {{String}}
  [DefaultBaseline](#cfn-ssm-patchbaseline-defaultbaseline): {{Boolean}}
  [Description](#cfn-ssm-patchbaseline-description): {{String}}
  [GlobalFilters](#cfn-ssm-patchbaseline-globalfilters): {{
    PatchFilterGroup}}
  [Name](#cfn-ssm-patchbaseline-name): {{String}}
  [OperatingSystem](#cfn-ssm-patchbaseline-operatingsystem): {{String}}
  [PatchGroups](#cfn-ssm-patchbaseline-patchgroups): {{
    - String}}
  [RejectedPatches](#cfn-ssm-patchbaseline-rejectedpatches): {{
    - String}}
  [RejectedPatchesAction](#cfn-ssm-patchbaseline-rejectedpatchesaction): {{String}}
  [Sources](#cfn-ssm-patchbaseline-sources): {{
    - PatchSource}}
  [Tags](#cfn-ssm-patchbaseline-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ssm-patchbaseline-properties"></a>

`ApprovalRules`  <a name="cfn-ssm-patchbaseline-approvalrules"></a>
A set of rules used to include patches in the baseline.
*Required*: No
*Type*: [RuleGroup](aws-properties-ssm-patchbaseline-rulegroup.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApprovedPatches`  <a name="cfn-ssm-patchbaseline-approvedpatches"></a>
A list of explicitly approved patches for the baseline.
For information about accepted formats for lists of approved patches and rejected patches, see [Package name formats for approved and rejected patch lists](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html) in the *AWS Systems Manager User Guide*.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 0`
*Maximum*: `100 | 50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApprovedPatchesComplianceLevel`  <a name="cfn-ssm-patchbaseline-approvedpatchescompliancelevel"></a>
Defines the compliance level for approved patches. When an approved patch is reported as missing, this value describes the severity of the compliance violation. The default value is `UNSPECIFIED`.
*Required*: No
*Type*: String
*Allowed values*: `CRITICAL | HIGH | MEDIUM | LOW | INFORMATIONAL | UNSPECIFIED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApprovedPatchesEnableNonSecurity`  <a name="cfn-ssm-patchbaseline-approvedpatchesenablenonsecurity"></a>
Indicates whether the list of approved patches includes non-security updates that should be applied to the managed nodes. The default value is `false`. Applies to Linux managed nodes only.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AvailableSecurityUpdatesComplianceStatus`  <a name="cfn-ssm-patchbaseline-availablesecurityupdatescompliancestatus"></a>
Indicates the status you want to assign to security patches that are available but not approved because they don't meet the installation criteria specified in the patch baseline.
Example scenario: Security patches that you might want installed can be skipped if you have specified a long period to wait after a patch is released before installation. If an update to the patch is released during your specified waiting period, the waiting period for installing the patch starts over. If the waiting period is too long, multiple versions of the patch could be released but never installed.
Supported for Windows Server managed nodes only.
*Required*: No
*Type*: String
*Allowed values*: `NON_COMPLIANT | COMPLIANT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DefaultBaseline`  <a name="cfn-ssm-patchbaseline-defaultbaseline"></a>
Indicates whether this is the default baseline. AWS Systems Manager supports creating multiple default patch baselines. For example, you can create a default patch baseline for each operating system.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-ssm-patchbaseline-description"></a>
A description of the patch baseline.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GlobalFilters`  <a name="cfn-ssm-patchbaseline-globalfilters"></a>
A set of global filters used to include patches in the baseline.
The `GlobalFilters` parameter can be configured only by using the AWS CLI or an AWS SDK. It can't be configured from the Patch Manager console, and its value isn't displayed in the console.
*Required*: No
*Type*: [PatchFilterGroup](aws-properties-ssm-patchbaseline-patchfiltergroup.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-ssm-patchbaseline-name"></a>
The name of the patch baseline.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\-.]{3,128}$`
*Minimum*: `3`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OperatingSystem`  <a name="cfn-ssm-patchbaseline-operatingsystem"></a>
Defines the operating system the patch baseline applies to. The default value is `WINDOWS`.
*Required*: No
*Type*: String
*Allowed values*: `WINDOWS | AMAZON_LINUX | AMAZON_LINUX_2 | AMAZON_LINUX_2022 | AMAZON_LINUX_2023 | UBUNTU | REDHAT_ENTERPRISE_LINUX | SUSE | CENTOS | ORACLE_LINUX | DEBIAN | MACOS | RASPBIAN | ROCKY_LINUX | ALMA_LINUX`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PatchGroups`  <a name="cfn-ssm-patchbaseline-patchgroups"></a>
The name of the patch group to be registered with the patch baseline.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RejectedPatches`  <a name="cfn-ssm-patchbaseline-rejectedpatches"></a>
A list of explicitly rejected patches for the baseline.
For information about accepted formats for lists of approved patches and rejected patches, see [Package name formats for approved and rejected patch lists](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html) in the *AWS Systems Manager User Guide*.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 0`
*Maximum*: `100 | 50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RejectedPatchesAction`  <a name="cfn-ssm-patchbaseline-rejectedpatchesaction"></a>
The action for Patch Manager to take on patches included in the `RejectedPackages` list.
ALLOW\_AS\_DEPENDENCY
**Linux and macOS**: A package in the rejected patches list is installed only if it is a dependency of another package. It is considered compliant with the patch baseline, and its status is reported as `INSTALLED_OTHER`. This is the default action if no option is specified.
**Windows Server**: Windows Server doesn't support the concept of package dependencies. If a package in the rejected patches list and already installed on the node, its status is reported as `INSTALLED_OTHER`. Any package not already installed on the node is skipped. This is the default action if no option is specified.
BLOCK
**All OSs**: Packages in the rejected patches list, and packages that include them as dependencies, aren't installed by Patch Manager under any circumstances.
State value assignment for patch compliance:
+ If a package was installed before it was added to the rejected patches list, or is installed outside of Patch Manager afterward, it's considered noncompliant with the patch baseline and its status is reported as `INSTALLED_REJECTED`.
+ If an update attempts to install a dependency package that is now rejected by the baseline, when previous versions of the package were not rejected, the package being updated is reported as `MISSING` for `SCAN` operations and as `FAILED` for `INSTALL` operations.
*Required*: No
*Type*: String
*Allowed values*: `ALLOW_AS_DEPENDENCY | BLOCK`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Sources`  <a name="cfn-ssm-patchbaseline-sources"></a>
Information about the patches to use to update the managed nodes, including target operating systems and source repositories. Applies to Linux managed nodes only.
*Required*: No
*Type*: Array of [PatchSource](aws-properties-ssm-patchbaseline-patchsource.md)
*Minimum*: `0`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ssm-patchbaseline-tags"></a>
Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a patch baseline to identify the severity level of patches it specifies and the operating system family it applies to.
*Required*: No
*Type*: Array of [Tag](aws-properties-ssm-patchbaseline-tag.md)
*Minimum*: `0`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ssm-patchbaseline-return-values"></a>

### Ref
<a name="aws-resource-ssm-patchbaseline-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the patch baseline ID, such as `pb-abcde1234567890yz`.

**Note**
The ID of the default patch baseline provided by AWS is an Amazon Resource Name (ARN), for example `arn:aws:ssm:us-west-2:123456789012:patchbaseline/abcde1234567890yz`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ssm-patchbaseline-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

## Examples
<a name="aws-resource-ssm-patchbaseline--examples"></a>

### Create a patch baseline
<a name="aws-resource-ssm-patchbaseline--examples--Create_a_patch_baseline"></a>

The following example creates a Systems Manager patch baseline that approves patches for Windows Server 2019 instances seven days after they are released by Microsoft. The patch baseline also approves patches for Active Directory seven days after they are released by Microsoft.

####
<a name="aws-resource-ssm-patchbaseline--examples--Create_a_patch_baseline--language_owl_wvr_qlb"></a>

```
{
    "Resources": {
        "myPatchBaseline": {
            "Type": "AWS::SSM::PatchBaseline",
            "Properties": {
                "Name": "myPatchBaseline",
                "Description": "Baseline containing all updates approved for Windows instances",
                "OperatingSystem": "WINDOWS",
                "PatchGroups": [
                    "myPatchGroup"
                ],
                "ApprovalRules": {
                    "PatchRules": [
                        {
                            "PatchFilterGroup": {
                                "PatchFilters": [
                                    {
                                        "Values": [
                                            "Critical",
                                            "Important",
                                            "Moderate"
                                        ],
                                        "Key": "MSRC_SEVERITY"
                                    },
                                    {
                                        "Values": [
                                            "SecurityUpdates",
                                            "CriticalUpdates"
                                        ],
                                        "Key": "CLASSIFICATION"
                                    },
                                    {
                                        "Values": [
                                            "WindowsServer2019"
                                        ],
                                        "Key": "PRODUCT"
                                    }
                                ]
                            },
                            "ApproveAfterDays": 7,
                            "ComplianceLevel": "CRITICAL"
                        },
                        {
                            "PatchFilterGroup": {
                                "PatchFilters": [
                                    {
                                        "Values": [
                                            "Critical",
                                            "Important",
                                            "Moderate"
                                        ],
                                        "Key": "MSRC_SEVERITY"
                                    },
                                    {
                                        "Values": [
                                            "*"
                                        ],
                                        "Key": "CLASSIFICATION"
                                    },
                                    {
                                        "Values": [
                                            "APPLICATION"
                                        ],
                                        "Key": "PATCH_SET"
                                    },
                                    {
                                        "Values": [
                                            "Active Directory Rights Management Services Client 2.0"
                                        ],
                                        "Key": "PRODUCT"
                                    },
                                    {
                                        "Values": [
                                            "Active Directory"
                                        ],
                                        "Key": "PRODUCT_FAMILY"
                                    }
                                ]
                            },
                            "ApproveAfterDays": 7,
                            "ComplianceLevel": "CRITICAL"
                        }
                    ]
                }
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-ssm-patchbaseline--examples--Create_a_patch_baseline--yaml"></a>

```
---
Resources:
  myPatchBaseline:
    Type: AWS::SSM::PatchBaseline
    Properties:
      Name: myPatchBaseline
      Description: Baseline containing all updates approved for Windows instances
      OperatingSystem: WINDOWS
      PatchGroups:
      - myPatchGroup
      ApprovalRules:
        PatchRules:
        - PatchFilterGroup:
            PatchFilters:
            - Values:
              - Critical
              - Important
              - Moderate
              Key: MSRC_SEVERITY
            - Values:
              - SecurityUpdates
              - CriticalUpdates
              Key: CLASSIFICATION
            - Values:
              - WindowsServer2019
              Key: PRODUCT
          ApproveAfterDays: 7
          ComplianceLevel: CRITICAL
        - PatchFilterGroup:
            PatchFilters:
            - Values:
              - Critical
              - Important
              - Moderate
              Key: MSRC_SEVERITY
            - Values:
              - "*"
              Key: CLASSIFICATION
            - Values:
              - APPLICATION
              Key: PATCH_SET
            - Values:
              - Active Directory Rights Management Services Client 2.0
              Key: PRODUCT
            - Values:
              - Active Directory
              Key: PRODUCT_FAMILY
          ApproveAfterDays: 7
          ComplianceLevel: CRITICAL
```

## See also
<a name="aws-resource-ssm-patchbaseline--seealso"></a>
+ [CreatePatchBaseline](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreatePatchBaseline.html) in the *AWS Systems Manager API Reference*.
