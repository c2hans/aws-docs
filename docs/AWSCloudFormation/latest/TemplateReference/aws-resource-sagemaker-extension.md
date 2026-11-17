---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-extension.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::Extension
<a name="aws-resource-sagemaker-extension"></a>

Installs an extension, such as `sagemaker-observability`, on a SageMaker HyperPod cluster orchestrated by Slurm. The cluster must have `NodeProvisioningMode` set to `Continuous` and can have only one extension with a given name. To track the installation, call `DescribeClusterExtension`.

## Syntax
<a name="aws-resource-sagemaker-extension-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-extension-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::Extension",
  "Properties" : {
      "[ClusterArn](#cfn-sagemaker-extension-clusterarn)" : {{String}},
      "[ConfigurationValues](#cfn-sagemaker-extension-configurationvalues)" : {{String}},
      "[ExtensionName](#cfn-sagemaker-extension-extensionname)" : {{String}},
      "[ExtensionVersion](#cfn-sagemaker-extension-extensionversion)" : {{String}},
      "[Tags](#cfn-sagemaker-extension-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-extension-syntax.yaml"></a>

```
Type: AWS::SageMaker::Extension
Properties:
  [ClusterArn](#cfn-sagemaker-extension-clusterarn): {{String}}
  [ConfigurationValues](#cfn-sagemaker-extension-configurationvalues): {{String}}
  [ExtensionName](#cfn-sagemaker-extension-extensionname): {{String}}
  [ExtensionVersion](#cfn-sagemaker-extension-extensionversion): {{String}}
  [Tags](#cfn-sagemaker-extension-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-sagemaker-extension-properties"></a>

`ClusterArn`  <a name="cfn-sagemaker-extension-clusterarn"></a>
The Amazon Resource Name (ARN) of the SageMaker HyperPod cluster on which the extension is installed.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:cluster/[a-z0-9]{12}$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ConfigurationValues`  <a name="cfn-sagemaker-extension-configurationvalues"></a>
The configuration of the extension, as a JSON object serialized as a string. The configuration includes the default value of every setting that you didn't specify.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `10240`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExtensionName`  <a name="cfn-sagemaker-extension-extensionname"></a>
The name of the extension.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z][a-z0-9-]*$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExtensionVersion`  <a name="cfn-sagemaker-extension-extensionversion"></a>
The version of the extension. While SageMaker HyperPod creates or updates the extension, some nodes might still run a different version. To see how many nodes run this version, see `NodeSummary`.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]+\.[0-9]+\.[0-9]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-sagemaker-extension-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-sagemaker-extension-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-sagemaker-extension-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-extension-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-sagemaker-extension-return-values-fn--getatt"></a>

####
<a name="aws-resource-sagemaker-extension-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The time when the extension was created.

`ExtensionArn`  <a name="ExtensionArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the extension.

`LastModifiedTime`  <a name="LastModifiedTime-fn::getatt"></a>
The time when the extension was last updated.

`Status`  <a name="Status-fn::getatt"></a>
The status of the extension can be one of the following values:
Creating
SageMaker HyperPod is installing the extension on the cluster's nodes.
Active
The extension runs its current version and configuration on all of the cluster's nodes.
Updating
SageMaker HyperPod is applying a configuration change or version update to the cluster's nodes.
Degraded
The extension runs its current version and configuration on some of the cluster's nodes but not all of them. Or, at least one node recently reported that the extension is unhealthy.
CreateFailed
SageMaker HyperPod couldn't install the extension on any of the cluster's nodes.
UpdateFailed
SageMaker HyperPod couldn't apply the update on any of the cluster's nodes.
Deleting
SageMaker HyperPod is removing the extension from the cluster's nodes.
DeleteFailed
SageMaker HyperPod couldn't remove the extension from any of the cluster's nodes.
