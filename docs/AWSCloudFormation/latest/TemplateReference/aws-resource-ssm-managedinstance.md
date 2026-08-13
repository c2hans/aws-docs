---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-managedinstance.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSM::ManagedInstance
<a name="aws-resource-ssm-managedinstance"></a>

<a name="aws-resource-ssm-managedinstance-description"></a>The `AWS::SSM::ManagedInstance` resource Property description not available. for SSM.

## Syntax
<a name="aws-resource-ssm-managedinstance-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ssm-managedinstance-syntax.json"></a>

```
{
  "Type" : "AWS::SSM::ManagedInstance",
  "Properties" : {
      "[Tags](#cfn-ssm-managedinstance-tags)" : {{[ TagsItems, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ssm-managedinstance-syntax.yaml"></a>

```
Type: AWS::SSM::ManagedInstance
Properties:
  [Tags](#cfn-ssm-managedinstance-tags): {{
    - TagsItems}}
```

## Properties
<a name="aws-resource-ssm-managedinstance-properties"></a>

`Tags`  <a name="cfn-ssm-managedinstance-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [TagsItems](aws-properties-ssm-managedinstance-tagsitems.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ssm-managedinstance-return-values"></a>

### Ref
<a name="aws-resource-ssm-managedinstance-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ssm-managedinstance-return-values-fn--getatt"></a>

####
<a name="aws-resource-ssm-managedinstance-return-values-fn--getatt-fn--getatt"></a>

`AgentVersion`  <a name="AgentVersion-fn::getatt"></a>
Property description not available.

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`ComputerName`  <a name="ComputerName-fn::getatt"></a>
Property description not available.

`InstanceId`  <a name="InstanceId-fn::getatt"></a>
Property description not available.

`IPAddress`  <a name="IPAddress-fn::getatt"></a>
Property description not available.

`IsLatestVersion`  <a name="IsLatestVersion-fn::getatt"></a>
Property description not available.

`PingStatus`  <a name="PingStatus-fn::getatt"></a>
Property description not available.

`PlatformName`  <a name="PlatformName-fn::getatt"></a>
Property description not available.

`PlatformType`  <a name="PlatformType-fn::getatt"></a>
Property description not available.

`PlatformVersion`  <a name="PlatformVersion-fn::getatt"></a>
Property description not available.

`ResourceType`  <a name="ResourceType-fn::getatt"></a>
Property description not available.
