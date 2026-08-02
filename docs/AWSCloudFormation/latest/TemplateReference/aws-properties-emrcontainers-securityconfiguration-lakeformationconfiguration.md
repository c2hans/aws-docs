---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-securityconfiguration-lakeformationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::SecurityConfiguration LakeFormationConfiguration
<a name="aws-properties-emrcontainers-securityconfiguration-lakeformationconfiguration"></a>

AWS Lake Formation related configuration inputs for the security configuration.

## Syntax
<a name="aws-properties-emrcontainers-securityconfiguration-lakeformationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-securityconfiguration-lakeformationconfiguration-syntax.json"></a>

```
{
  "[AuthorizedSessionTagValue](#cfn-emrcontainers-securityconfiguration-lakeformationconfiguration-authorizedsessiontagvalue)" : {{String}},
  "[QueryAccessControlEnabled](#cfn-emrcontainers-securityconfiguration-lakeformationconfiguration-queryaccesscontrolenabled)" : {{Boolean}},
  "[QueryEngineRoleArn](#cfn-emrcontainers-securityconfiguration-lakeformationconfiguration-queryenginerolearn)" : {{String}},
  "[SecureNamespaceInfo](#cfn-emrcontainers-securityconfiguration-lakeformationconfiguration-securenamespaceinfo)" : {{SecureNamespaceInfo}}
}
```

### YAML
<a name="aws-properties-emrcontainers-securityconfiguration-lakeformationconfiguration-syntax.yaml"></a>

```
  [AuthorizedSessionTagValue](#cfn-emrcontainers-securityconfiguration-lakeformationconfiguration-authorizedsessiontagvalue): {{String}}
  [QueryAccessControlEnabled](#cfn-emrcontainers-securityconfiguration-lakeformationconfiguration-queryaccesscontrolenabled): {{Boolean}}
  [QueryEngineRoleArn](#cfn-emrcontainers-securityconfiguration-lakeformationconfiguration-queryenginerolearn): {{String}}
  [SecureNamespaceInfo](#cfn-emrcontainers-securityconfiguration-lakeformationconfiguration-securenamespaceinfo): {{
    SecureNamespaceInfo}}
```

## Properties
<a name="aws-properties-emrcontainers-securityconfiguration-lakeformationconfiguration-properties"></a>

`AuthorizedSessionTagValue`  <a name="cfn-emrcontainers-securityconfiguration-lakeformationconfiguration-authorizedsessiontagvalue"></a>
The session tag to authorize Amazon EMR on EKS for API calls to AWS Lake Formation.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`QueryAccessControlEnabled`  <a name="cfn-emrcontainers-securityconfiguration-lakeformationconfiguration-queryaccesscontrolenabled"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`QueryEngineRoleArn`  <a name="cfn-emrcontainers-securityconfiguration-lakeformationconfiguration-queryenginerolearn"></a>
The query engine IAM role ARN that is tied to the secure Spark job. The `QueryEngine` role assumes the `JobExecutionRole` to execute all the Lake Formation calls.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):iam::\d{12}:role/.+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SecureNamespaceInfo`  <a name="cfn-emrcontainers-securityconfiguration-lakeformationconfiguration-securenamespaceinfo"></a>
The namespace input of the system job.
*Required*: No
*Type*: [SecureNamespaceInfo](aws-properties-emrcontainers-securityconfiguration-securenamespaceinfo.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
