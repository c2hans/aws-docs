---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-guardduty-detector-cfnkubernetesauditlogsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GuardDuty::Detector CFNKubernetesAuditLogsConfiguration
<a name="aws-properties-guardduty-detector-cfnkubernetesauditlogsconfiguration"></a>

Describes which optional data sources are enabled for a detector.

## Syntax
<a name="aws-properties-guardduty-detector-cfnkubernetesauditlogsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-guardduty-detector-cfnkubernetesauditlogsconfiguration-syntax.json"></a>

```
{
  "[Enable](#cfn-guardduty-detector-cfnkubernetesauditlogsconfiguration-enable)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-guardduty-detector-cfnkubernetesauditlogsconfiguration-syntax.yaml"></a>

```
  [Enable](#cfn-guardduty-detector-cfnkubernetesauditlogsconfiguration-enable): {{Boolean}}
```

## Properties
<a name="aws-properties-guardduty-detector-cfnkubernetesauditlogsconfiguration-properties"></a>

`Enable`  <a name="cfn-guardduty-detector-cfnkubernetesauditlogsconfiguration-enable"></a>
Describes whether Kubernetes audit logs are enabled as a data source for the detector.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
