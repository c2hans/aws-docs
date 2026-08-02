---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resiliencehubv2-service-crossaccountroleconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResilienceHubV2::Service CrossAccountRoleConfiguration
<a name="aws-properties-resiliencehubv2-service-crossaccountroleconfiguration"></a>

<a name="aws-properties-resiliencehubv2-service-crossaccountroleconfiguration-description"></a>The `CrossAccountRoleConfiguration` property type specifies Property description not available. for an [AWS::ResilienceHubV2::Service](aws-resource-resiliencehubv2-service.md).

## Syntax
<a name="aws-properties-resiliencehubv2-service-crossaccountroleconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-resiliencehubv2-service-crossaccountroleconfiguration-syntax.json"></a>

```
{
  "[CrossAccountRoleArn](#cfn-resiliencehubv2-service-crossaccountroleconfiguration-crossaccountrolearn)" : {{String}},
  "[ExternalId](#cfn-resiliencehubv2-service-crossaccountroleconfiguration-externalid)" : {{String}}
}
```

### YAML
<a name="aws-properties-resiliencehubv2-service-crossaccountroleconfiguration-syntax.yaml"></a>

```
  [CrossAccountRoleArn](#cfn-resiliencehubv2-service-crossaccountroleconfiguration-crossaccountrolearn): {{String}}
  [ExternalId](#cfn-resiliencehubv2-service-crossaccountroleconfiguration-externalid): {{String}}
```

## Properties
<a name="aws-properties-resiliencehubv2-service-crossaccountroleconfiguration-properties"></a>

`CrossAccountRoleArn`  <a name="cfn-resiliencehubv2-service-crossaccountroleconfiguration-crossaccountrolearn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):iam::[0-9]{12}:role\/(([^\/][\x21-\x7E]+\/){1,511})?[A-Za-z0-9_+=,.@-]{1,64}$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExternalId`  <a name="cfn-resiliencehubv2-service-crossaccountroleconfiguration-externalid"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
