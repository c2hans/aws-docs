---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-events-connection-apikeyauthparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Events::Connection ApiKeyAuthParameters
<a name="aws-properties-events-connection-apikeyauthparameters"></a>

The API key authorization parameters for the connection.

## Syntax
<a name="aws-properties-events-connection-apikeyauthparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-events-connection-apikeyauthparameters-syntax.json"></a>

```
{
  "[ApiKeyName](#cfn-events-connection-apikeyauthparameters-apikeyname)" : {{String}},
  "[ApiKeyValue](#cfn-events-connection-apikeyauthparameters-apikeyvalue)" : {{String}}
}
```

### YAML
<a name="aws-properties-events-connection-apikeyauthparameters-syntax.yaml"></a>

```
  [ApiKeyName](#cfn-events-connection-apikeyauthparameters-apikeyname): {{String}}
  [ApiKeyValue](#cfn-events-connection-apikeyauthparameters-apikeyvalue): {{String}}
```

## Properties
<a name="aws-properties-events-connection-apikeyauthparameters-properties"></a>

`ApiKeyName`  <a name="cfn-events-connection-apikeyauthparameters-apikeyname"></a>
The name of the API key to use for authorization.
*Required*: Yes
*Type*: String
*Pattern*: `^[ \t]*[^\x00-\x1F\x7F]+([ \t]+[^\x00-\x1F\x7F]+)*[ \t]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApiKeyValue`  <a name="cfn-events-connection-apikeyauthparameters-apikeyvalue"></a>
The value for the API key to use for authorization.
*Required*: Yes
*Type*: String
*Pattern*: `^[ \t]*[^\x00-\x1F\x7F]+([ \t]+[^\x00-\x1F\x7F]+)*[ \t]*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
