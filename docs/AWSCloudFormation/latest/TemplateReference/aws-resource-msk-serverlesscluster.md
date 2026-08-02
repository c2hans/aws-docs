---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-msk-serverlesscluster.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::ServerlessCluster
<a name="aws-resource-msk-serverlesscluster"></a>

Specifies the properties required for creating a serverless cluster.

## Syntax
<a name="aws-resource-msk-serverlesscluster-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-msk-serverlesscluster-syntax.json"></a>

```
{
  "Type" : "AWS::MSK::ServerlessCluster",
  "Properties" : {
      "[ClientAuthentication](#cfn-msk-serverlesscluster-clientauthentication)" : {{ClientAuthentication}},
      "[ClusterName](#cfn-msk-serverlesscluster-clustername)" : {{String}},
      "[Tags](#cfn-msk-serverlesscluster-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[VpcConfigs](#cfn-msk-serverlesscluster-vpcconfigs)" : {{[ VpcConfig, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-msk-serverlesscluster-syntax.yaml"></a>

```
Type: AWS::MSK::ServerlessCluster
Properties:
  [ClientAuthentication](#cfn-msk-serverlesscluster-clientauthentication): {{
    ClientAuthentication}}
  [ClusterName](#cfn-msk-serverlesscluster-clustername): {{String}}
  [Tags](#cfn-msk-serverlesscluster-tags): {{
    {{Key}}: {{Value}}}}
  [VpcConfigs](#cfn-msk-serverlesscluster-vpcconfigs): {{
    - VpcConfig}}
```

## Properties
<a name="aws-resource-msk-serverlesscluster-properties"></a>

`ClientAuthentication`  <a name="cfn-msk-serverlesscluster-clientauthentication"></a>
Includes all client authentication related information.
*Required*: Yes
*Type*: [ClientAuthentication](aws-properties-msk-serverlesscluster-clientauthentication.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ClusterName`  <a name="cfn-msk-serverlesscluster-clustername"></a>
The name of the cluster.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-msk-serverlesscluster-tags"></a>
An arbitrary set of tags (key-value pairs) for the cluster.
*Required*: No
*Type*: Object of String
*Pattern*: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcConfigs`  <a name="cfn-msk-serverlesscluster-vpcconfigs"></a>
VPC configuration information for the serverless cluster.
*Required*: Yes
*Type*: Array of [VpcConfig](aws-properties-msk-serverlesscluster-vpcconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-msk-serverlesscluster-return-values"></a>

### Ref
<a name="aws-resource-msk-serverlesscluster-return-values-ref"></a>

When you provide the logical ID of this resource to the `Ref` intrinsic function, it returns the ARN of the created MSK cluster.

### Fn::GetAtt
<a name="aws-resource-msk-serverlesscluster-return-values-fn--getatt"></a>

`Fn::GetAtt` returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

####
<a name="aws-resource-msk-serverlesscluster-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the MSK cluster.
