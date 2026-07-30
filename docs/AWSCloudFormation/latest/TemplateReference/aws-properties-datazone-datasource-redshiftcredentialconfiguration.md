---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-datasource-redshiftcredentialconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::DataSource RedshiftCredentialConfiguration
<a name="aws-properties-datazone-datasource-redshiftcredentialconfiguration"></a>

The details of the credentials required to access an Amazon Redshift cluster.

## Syntax
<a name="aws-properties-datazone-datasource-redshiftcredentialconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-datasource-redshiftcredentialconfiguration-syntax.json"></a>

```
{
  "[SecretManagerArn](#cfn-datazone-datasource-redshiftcredentialconfiguration-secretmanagerarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-datazone-datasource-redshiftcredentialconfiguration-syntax.yaml"></a>

```
  [SecretManagerArn](#cfn-datazone-datasource-redshiftcredentialconfiguration-secretmanagerarn): {{String}}
```

## Properties
<a name="aws-properties-datazone-datasource-redshiftcredentialconfiguration-properties"></a>

`SecretManagerArn`  <a name="cfn-datazone-datasource-redshiftcredentialconfiguration-secretmanagerarn"></a>
The ARN of a secret manager for an Amazon Redshift cluster.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[^:]*:secretsmanager:[a-z]{2}-?(iso|gov)?-{1}[a-z]*-{1}[0-9]:\d{12}:secret:.*$`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
