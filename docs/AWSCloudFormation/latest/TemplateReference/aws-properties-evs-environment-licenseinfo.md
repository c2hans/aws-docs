---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-evs-environment-licenseinfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EVS::Environment LicenseInfo
<a name="aws-properties-evs-environment-licenseinfo"></a>

 The license information that Amazon EVS requires to create an environment. Amazon EVS requires two license keys: a VCF solution key and a vSAN license key.

## Syntax
<a name="aws-properties-evs-environment-licenseinfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-evs-environment-licenseinfo-syntax.json"></a>

```
{
  "[SolutionKey](#cfn-evs-environment-licenseinfo-solutionkey)" : {{String}},
  "[VsanKey](#cfn-evs-environment-licenseinfo-vsankey)" : {{String}}
}
```

### YAML
<a name="aws-properties-evs-environment-licenseinfo-syntax.yaml"></a>

```
  [SolutionKey](#cfn-evs-environment-licenseinfo-solutionkey): {{String}}
  [VsanKey](#cfn-evs-environment-licenseinfo-vsankey): {{String}}
```

## Properties
<a name="aws-properties-evs-environment-licenseinfo-properties"></a>

`SolutionKey`  <a name="cfn-evs-environment-licenseinfo-solutionkey"></a>
 The VCF solution key. This license unlocks VMware VCF product features, including vSphere, NSX, SDDC Manager, and vCenter Server. The VCF solution key must meet the instance-type-specific minimum core requirements.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]{5}-[a-zA-Z0-9]{5}-[a-zA-Z0-9]{5}-[a-zA-Z0-9]{5}-[a-zA-Z0-9]{5}$`
*Update requires*: Updates are not supported.

`VsanKey`  <a name="cfn-evs-environment-licenseinfo-vsankey"></a>
 The VSAN license key. This license unlocks vSAN features. The vSAN license key must meet the instance-type-specific minimum capacity requirements.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]{5}-[a-zA-Z0-9]{5}-[a-zA-Z0-9]{5}-[a-zA-Z0-9]{5}-[a-zA-Z0-9]{5}$`
*Update requires*: Updates are not supported.
