---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-redshiftprovisionedconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase RedshiftProvisionedConfiguration
<a name="aws-properties-bedrock-knowledgebase-redshiftprovisionedconfiguration"></a>

Contains configurations for a provisioned Amazon Redshift query engine.

## Syntax
<a name="aws-properties-bedrock-knowledgebase-redshiftprovisionedconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-redshiftprovisionedconfiguration-syntax.json"></a>

```
{
  "[AuthConfiguration](#cfn-bedrock-knowledgebase-redshiftprovisionedconfiguration-authconfiguration)" : {{RedshiftProvisionedAuthConfiguration}},
  "[ClusterIdentifier](#cfn-bedrock-knowledgebase-redshiftprovisionedconfiguration-clusteridentifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-redshiftprovisionedconfiguration-syntax.yaml"></a>

```
  [AuthConfiguration](#cfn-bedrock-knowledgebase-redshiftprovisionedconfiguration-authconfiguration): {{
    RedshiftProvisionedAuthConfiguration}}
  [ClusterIdentifier](#cfn-bedrock-knowledgebase-redshiftprovisionedconfiguration-clusteridentifier): {{String}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-redshiftprovisionedconfiguration-properties"></a>

`AuthConfiguration`  <a name="cfn-bedrock-knowledgebase-redshiftprovisionedconfiguration-authconfiguration"></a>
Specifies configurations for authentication to Amazon Redshift.
*Required*: Yes
*Type*: [RedshiftProvisionedAuthConfiguration](aws-properties-bedrock-knowledgebase-redshiftprovisionedauthconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ClusterIdentifier`  <a name="cfn-bedrock-knowledgebase-redshiftprovisionedconfiguration-clusteridentifier"></a>
The ID of the Amazon Redshift cluster.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
