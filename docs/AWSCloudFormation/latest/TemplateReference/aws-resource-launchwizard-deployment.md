---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-launchwizard-deployment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LaunchWizard::Deployment
<a name="aws-resource-launchwizard-deployment"></a>

Creates a deployment for the given workload. Deployments created by this operation are not available in the Launch Wizard console to use the `Clone deployment` action on.

## Syntax
<a name="aws-resource-launchwizard-deployment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-launchwizard-deployment-syntax.json"></a>

```
{
  "Type" : "AWS::LaunchWizard::Deployment",
  "Properties" : {
      "[DeploymentPatternName](#cfn-launchwizard-deployment-deploymentpatternname)" : {{String}},
      "[Name](#cfn-launchwizard-deployment-name)" : {{String}},
      "[Specifications](#cfn-launchwizard-deployment-specifications)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Tags](#cfn-launchwizard-deployment-tags)" : {{[ Tags, ... ]}},
      "[WorkloadName](#cfn-launchwizard-deployment-workloadname)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-launchwizard-deployment-syntax.yaml"></a>

```
Type: AWS::LaunchWizard::Deployment
Properties:
  [DeploymentPatternName](#cfn-launchwizard-deployment-deploymentpatternname): {{String}}
  [Name](#cfn-launchwizard-deployment-name): {{String}}
  [Specifications](#cfn-launchwizard-deployment-specifications): {{
    {{Key}}: {{Value}}}}
  [Tags](#cfn-launchwizard-deployment-tags): {{
    - Tags}}
  [WorkloadName](#cfn-launchwizard-deployment-workloadname): {{String}}
```

## Properties
<a name="aws-resource-launchwizard-deployment-properties"></a>

`DeploymentPatternName`  <a name="cfn-launchwizard-deployment-deploymentpatternname"></a>
The name of the deployment pattern.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9][a-zA-Z0-9-]*$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-launchwizard-deployment-name"></a>
The name of the deployment.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9_\s\.-]+$`
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Specifications`  <a name="cfn-launchwizard-deployment-specifications"></a>
The settings specified for the deployment. These settings define how to deploy and configure your resources created by the deployment. For more information about the specifications required for creating a deployment for a SAP workload, see [SAP deployment specifications](https://docs.aws.amazon.com/launchwizard/latest/APIReference/launch-wizard-specifications-sap.html). To retrieve the specifications required to create a deployment for other workloads, use the [https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_GetWorkloadDeploymentPattern.html](https://docs.aws.amazon.com/launchwizard/latest/APIReference/API_GetWorkloadDeploymentPattern.html) operation.
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z0-9-:]{3,256}$`
*Minimum*: `1`
*Maximum*: `1500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-launchwizard-deployment-tags"></a>
Information about the tags attached to a deployment.
*Required*: No
*Type*: [Array](aws-properties-launchwizard-deployment-tags.md) of [Tags](aws-properties-launchwizard-deployment-tags.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkloadName`  <a name="cfn-launchwizard-deployment-workloadname"></a>
The name of the workload.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z][a-zA-Z0-9-_]*$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-launchwizard-deployment-return-values"></a>

### Ref
<a name="aws-resource-launchwizard-deployment-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the deployment. For example:

 `{ "Ref": "myLaunchWizardDeployment" }`

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-launchwizard-deployment-return-values-fn--getatt"></a>

####
<a name="aws-resource-launchwizard-deployment-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the deployment.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The time the deployment was created.

`DeletedAt`  <a name="DeletedAt-fn::getatt"></a>
The time the deployment was deleted.

`DeploymentId`  <a name="DeploymentId-fn::getatt"></a>
The ID of the deployment.

`ResourceGroup`  <a name="ResourceGroup-fn::getatt"></a>
The resource group of the deployment.

`Status`  <a name="Status-fn::getatt"></a>
The status of the deployment.
