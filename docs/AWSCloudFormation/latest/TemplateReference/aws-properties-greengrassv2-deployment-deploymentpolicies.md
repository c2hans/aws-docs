---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-greengrassv2-deployment-deploymentpolicies.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GreengrassV2::Deployment DeploymentPolicies
<a name="aws-properties-greengrassv2-deployment-deploymentpolicies"></a>

Contains information about policies that define how a deployment updates components and handles failure.

## Syntax
<a name="aws-properties-greengrassv2-deployment-deploymentpolicies-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-greengrassv2-deployment-deploymentpolicies-syntax.json"></a>

```
{
  "[ComponentUpdatePolicy](#cfn-greengrassv2-deployment-deploymentpolicies-componentupdatepolicy)" : {{DeploymentComponentUpdatePolicy}},
  "[ConfigurationValidationPolicy](#cfn-greengrassv2-deployment-deploymentpolicies-configurationvalidationpolicy)" : {{DeploymentConfigurationValidationPolicy}},
  "[FailureHandlingPolicy](#cfn-greengrassv2-deployment-deploymentpolicies-failurehandlingpolicy)" : {{String}}
}
```

### YAML
<a name="aws-properties-greengrassv2-deployment-deploymentpolicies-syntax.yaml"></a>

```
  [ComponentUpdatePolicy](#cfn-greengrassv2-deployment-deploymentpolicies-componentupdatepolicy): {{
    DeploymentComponentUpdatePolicy}}
  [ConfigurationValidationPolicy](#cfn-greengrassv2-deployment-deploymentpolicies-configurationvalidationpolicy): {{
    DeploymentConfigurationValidationPolicy}}
  [FailureHandlingPolicy](#cfn-greengrassv2-deployment-deploymentpolicies-failurehandlingpolicy): {{String}}
```

## Properties
<a name="aws-properties-greengrassv2-deployment-deploymentpolicies-properties"></a>

`ComponentUpdatePolicy`  <a name="cfn-greengrassv2-deployment-deploymentpolicies-componentupdatepolicy"></a>
The component update policy for the configuration deployment. This policy defines when it's safe to deploy the configuration to devices.
*Required*: No
*Type*: [DeploymentComponentUpdatePolicy](aws-properties-greengrassv2-deployment-deploymentcomponentupdatepolicy.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ConfigurationValidationPolicy`  <a name="cfn-greengrassv2-deployment-deploymentpolicies-configurationvalidationpolicy"></a>
The configuration validation policy for the configuration deployment. This policy defines how long each component has to validate its configure updates.
*Required*: No
*Type*: [DeploymentConfigurationValidationPolicy](aws-properties-greengrassv2-deployment-deploymentconfigurationvalidationpolicy.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FailureHandlingPolicy`  <a name="cfn-greengrassv2-deployment-deploymentpolicies-failurehandlingpolicy"></a>
The failure handling policy for the configuration deployment. This policy defines what to do if the deployment fails.
Default: `ROLLBACK`
*Required*: No
*Type*: String
*Allowed values*: `ROLLBACK | DO_NOTHING`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
