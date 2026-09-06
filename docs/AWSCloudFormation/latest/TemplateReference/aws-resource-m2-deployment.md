---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-m2-deployment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::M2::Deployment
<a name="aws-resource-m2-deployment"></a>

**Important**
AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

Creates and starts a deployment to deploy an application into a runtime environment.

## Syntax
<a name="aws-resource-m2-deployment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-m2-deployment-syntax.json"></a>

```
{
  "Type" : "AWS::M2::Deployment",
  "Properties" : {
      "[ApplicationId](#cfn-m2-deployment-applicationid)" : {{String}},
      "[ApplicationVersion](#cfn-m2-deployment-applicationversion)" : {{Integer}},
      "[EnvironmentId](#cfn-m2-deployment-environmentid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-m2-deployment-syntax.yaml"></a>

```
Type: AWS::M2::Deployment
Properties:
  [ApplicationId](#cfn-m2-deployment-applicationid): {{String}}
  [ApplicationVersion](#cfn-m2-deployment-applicationversion): {{Integer}}
  [EnvironmentId](#cfn-m2-deployment-environmentid): {{String}}
```

## Properties
<a name="aws-resource-m2-deployment-properties"></a>

`ApplicationId`  <a name="cfn-m2-deployment-applicationid"></a>
The unique identifier of the application.
*Required*: Yes
*Type*: String
*Pattern*: `^\S{1,80}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ApplicationVersion`  <a name="cfn-m2-deployment-applicationversion"></a>
The version of the application.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnvironmentId`  <a name="cfn-m2-deployment-environmentid"></a>
The unique identifier of the runtime environment.
*Required*: Yes
*Type*: String
*Pattern*: `^\S{1,80}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-m2-deployment-return-values"></a>

### Ref
<a name="aws-resource-m2-deployment-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-m2-deployment-return-values-fn--getatt"></a>

####
<a name="aws-resource-m2-deployment-return-values-fn--getatt-fn--getatt"></a>

`DeploymentId`  <a name="DeploymentId-fn::getatt"></a>
The unique identifier of the deployment.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the deployment.
