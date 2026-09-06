---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-entityresolution-idnamespace-namespaceproviderproperties.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EntityResolution::IdNamespace NamespaceProviderProperties
<a name="aws-properties-entityresolution-idnamespace-namespaceproviderproperties"></a>

An object containing `providerConfiguration` and `providerServiceArn`.

## Syntax
<a name="aws-properties-entityresolution-idnamespace-namespaceproviderproperties-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-entityresolution-idnamespace-namespaceproviderproperties-syntax.json"></a>

```
{
  "[ProviderConfiguration](#cfn-entityresolution-idnamespace-namespaceproviderproperties-providerconfiguration)" : {{{{{Key}}: {{Value}}, ...}}},
  "[ProviderServiceArn](#cfn-entityresolution-idnamespace-namespaceproviderproperties-providerservicearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-entityresolution-idnamespace-namespaceproviderproperties-syntax.yaml"></a>

```
  [ProviderConfiguration](#cfn-entityresolution-idnamespace-namespaceproviderproperties-providerconfiguration): {{
    {{Key}}: {{Value}}}}
  [ProviderServiceArn](#cfn-entityresolution-idnamespace-namespaceproviderproperties-providerservicearn): {{String}}
```

## Properties
<a name="aws-properties-entityresolution-idnamespace-namespaceproviderproperties-properties"></a>

`ProviderConfiguration`  <a name="cfn-entityresolution-idnamespace-namespaceproviderproperties-providerconfiguration"></a>
An object which defines any additional configurations required by the provider service.
*Required*: No
*Type*: Object of String
*Pattern*: `^.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProviderServiceArn`  <a name="cfn-entityresolution-idnamespace-namespaceproviderproperties-providerservicearn"></a>
The Amazon Resource Name (ARN) of the provider service.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-us-gov|aws-cn):(entityresolution):([a-z]{2}-[a-z]{1,10}-[0-9])::providerservice/([a-zA-Z0-9_-]{1,255})/([a-zA-Z0-9_-]{1,255})$`
*Minimum*: `20`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
