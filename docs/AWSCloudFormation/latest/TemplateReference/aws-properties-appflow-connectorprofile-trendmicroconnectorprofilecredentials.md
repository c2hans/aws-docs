---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-appflow-connectorprofile-trendmicroconnectorprofilecredentials.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppFlow::ConnectorProfile TrendmicroConnectorProfileCredentials
<a name="aws-properties-appflow-connectorprofile-trendmicroconnectorprofilecredentials"></a>

 The connector-specific profile credentials required when using Trend Micro.

## Syntax
<a name="aws-properties-appflow-connectorprofile-trendmicroconnectorprofilecredentials-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-appflow-connectorprofile-trendmicroconnectorprofilecredentials-syntax.json"></a>

```
{
  "[ApiSecretKey](#cfn-appflow-connectorprofile-trendmicroconnectorprofilecredentials-apisecretkey)" : {{String}}
}
```

### YAML
<a name="aws-properties-appflow-connectorprofile-trendmicroconnectorprofilecredentials-syntax.yaml"></a>

```
  [ApiSecretKey](#cfn-appflow-connectorprofile-trendmicroconnectorprofilecredentials-apisecretkey): {{String}}
```

## Properties
<a name="aws-properties-appflow-connectorprofile-trendmicroconnectorprofilecredentials-properties"></a>

`ApiSecretKey`  <a name="cfn-appflow-connectorprofile-trendmicroconnectorprofilecredentials-apisecretkey"></a>
 The Secret Access Key portion of the credentials.
*Required*: Yes
*Type*: String
*Pattern*: `\S+`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-properties-appflow-connectorprofile-trendmicroconnectorprofilecredentials--seealso"></a>
+ [TrendmicroConnectorProfileCredentials](https://docs.aws.amazon.com/appflow/1.0/APIReference/API_TrendmicroConnectorProfileCredentials.html) in the *Amazon AppFlow API Reference*.
