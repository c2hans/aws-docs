---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-securityconfiguration-securenamespaceinfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::SecurityConfiguration SecureNamespaceInfo
<a name="aws-properties-emrcontainers-securityconfiguration-securenamespaceinfo"></a>

Namespace inputs for the system job.

## Syntax
<a name="aws-properties-emrcontainers-securityconfiguration-securenamespaceinfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-securityconfiguration-securenamespaceinfo-syntax.json"></a>

```
{
  "[ClusterId](#cfn-emrcontainers-securityconfiguration-securenamespaceinfo-clusterid)" : {{String}},
  "[Namespace](#cfn-emrcontainers-securityconfiguration-securenamespaceinfo-namespace)" : {{String}}
}
```

### YAML
<a name="aws-properties-emrcontainers-securityconfiguration-securenamespaceinfo-syntax.yaml"></a>

```
  [ClusterId](#cfn-emrcontainers-securityconfiguration-securenamespaceinfo-clusterid): {{String}}
  [Namespace](#cfn-emrcontainers-securityconfiguration-securenamespaceinfo-namespace): {{String}}
```

## Properties
<a name="aws-properties-emrcontainers-securityconfiguration-securenamespaceinfo-properties"></a>

`ClusterId`  <a name="cfn-emrcontainers-securityconfiguration-securenamespaceinfo-clusterid"></a>
The ID of the Amazon EKS cluster where Amazon EMR on EKS jobs run.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Namespace`  <a name="cfn-emrcontainers-securityconfiguration-securenamespaceinfo-namespace"></a>
The namespace of the Amazon EKS cluster where the system jobs run.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
