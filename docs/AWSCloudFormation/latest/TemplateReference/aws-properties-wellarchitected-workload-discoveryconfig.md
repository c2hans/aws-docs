---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-wellarchitected-workload-discoveryconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WellArchitected::Workload DiscoveryConfig
<a name="aws-properties-wellarchitected-workload-discoveryconfig"></a>

<a name="aws-properties-wellarchitected-workload-discoveryconfig-description"></a>The `DiscoveryConfig` property type specifies Property description not available. for an [AWS::WellArchitected::Workload](aws-resource-wellarchitected-workload.md).

## Syntax
<a name="aws-properties-wellarchitected-workload-discoveryconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-wellarchitected-workload-discoveryconfig-syntax.json"></a>

```
{
  "[TrustedAdvisorIntegrationStatus](#cfn-wellarchitected-workload-discoveryconfig-trustedadvisorintegrationstatus)" : {{String}},
  "[WorkloadResourceDefinition](#cfn-wellarchitected-workload-discoveryconfig-workloadresourcedefinition)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-wellarchitected-workload-discoveryconfig-syntax.yaml"></a>

```
  [TrustedAdvisorIntegrationStatus](#cfn-wellarchitected-workload-discoveryconfig-trustedadvisorintegrationstatus): {{String}}
  [WorkloadResourceDefinition](#cfn-wellarchitected-workload-discoveryconfig-workloadresourcedefinition): {{
    - String}}
```

## Properties
<a name="aws-properties-wellarchitected-workload-discoveryconfig-properties"></a>

`TrustedAdvisorIntegrationStatus`  <a name="cfn-wellarchitected-workload-discoveryconfig-trustedadvisorintegrationstatus"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkloadResourceDefinition`  <a name="cfn-wellarchitected-workload-discoveryconfig-workloadresourcedefinition"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Allowed values*: `WORKLOAD_METADATA | APP_REGISTRY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
