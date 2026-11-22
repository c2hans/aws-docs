---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ssm-cloudconnector-gcpconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSM::CloudConnector GcpConfiguration

<a name="aws-properties-ssm-cloudconnector-gcpconfiguration-description"></a>The `GcpConfiguration` property type specifies Property description not available. for an [AWS::SSM::CloudConnector](aws-resource-ssm-cloudconnector.md).

## Syntax
<a name="aws-properties-ssm-cloudconnector-gcpconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ssm-cloudconnector-gcpconfiguration-syntax.json"></a>

```json
{
  "[OrganizationId](#cfn-ssm-cloudconnector-gcpconfiguration-organizationid)" : {{String}},
  "[ServiceAccountEmail](#cfn-ssm-cloudconnector-gcpconfiguration-serviceaccountemail)" : {{String}},
  "[Targets](#cfn-ssm-cloudconnector-gcpconfiguration-targets)" : {{GcpConfigurationTargets}},
  "[WorkloadIdentityPoolProvider](#cfn-ssm-cloudconnector-gcpconfiguration-workloadidentitypoolprovider)" : {{String}}
}
```

### YAML
<a name="aws-properties-ssm-cloudconnector-gcpconfiguration-syntax.yaml"></a>

```yaml
  [OrganizationId](#cfn-ssm-cloudconnector-gcpconfiguration-organizationid): {{String}}
  [ServiceAccountEmail](#cfn-ssm-cloudconnector-gcpconfiguration-serviceaccountemail): {{String}}
  [Targets](#cfn-ssm-cloudconnector-gcpconfiguration-targets): {{
    GcpConfigurationTargets}}
  [WorkloadIdentityPoolProvider](#cfn-ssm-cloudconnector-gcpconfiguration-workloadidentitypoolprovider): {{String}}
```

## Properties
<a name="aws-properties-ssm-cloudconnector-gcpconfiguration-properties"></a>

`OrganizationId`  <a name="cfn-ssm-cloudconnector-gcpconfiguration-organizationid"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[1-9][0-9]{0,18}$`
*Minimum*: `1`
*Maximum*: `19`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ServiceAccountEmail`  <a name="cfn-ssm-cloudconnector-gcpconfiguration-serviceaccountemail"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z][a-z0-9\-]*[a-z0-9]@[a-z][a-z0-9\-]*[a-z0-9]\.iam\.gserviceaccount\.com$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Targets`  <a name="cfn-ssm-cloudconnector-gcpconfiguration-targets"></a>
Property description not available.
*Required*: No
*Type*: [GcpConfigurationTargets](aws-properties-ssm-cloudconnector-gcpconfigurationtargets.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkloadIdentityPoolProvider`  <a name="cfn-ssm-cloudconnector-gcpconfiguration-workloadidentitypoolprovider"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^projects/[1-9][0-9]{0,18}/locations/global/workloadIdentityPools/[a-z0-9-]{4,32}/providers/[a-z0-9-]{4,32}$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
