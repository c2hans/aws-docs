---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-multiplexprogram-multiplexprogramservicedescriptor.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Multiplexprogram MultiplexProgramServiceDescriptor
<a name="aws-properties-medialive-multiplexprogram-multiplexprogramservicedescriptor"></a>

Transport stream service descriptor configuration for the Multiplex program.

## Syntax
<a name="aws-properties-medialive-multiplexprogram-multiplexprogramservicedescriptor-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-multiplexprogram-multiplexprogramservicedescriptor-syntax.json"></a>

```
{
  "[ProviderName](#cfn-medialive-multiplexprogram-multiplexprogramservicedescriptor-providername)" : {{String}},
  "[ServiceName](#cfn-medialive-multiplexprogram-multiplexprogramservicedescriptor-servicename)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-multiplexprogram-multiplexprogramservicedescriptor-syntax.yaml"></a>

```
  [ProviderName](#cfn-medialive-multiplexprogram-multiplexprogramservicedescriptor-providername): {{String}}
  [ServiceName](#cfn-medialive-multiplexprogram-multiplexprogramservicedescriptor-servicename): {{String}}
```

## Properties
<a name="aws-properties-medialive-multiplexprogram-multiplexprogramservicedescriptor-properties"></a>

`ProviderName`  <a name="cfn-medialive-multiplexprogram-multiplexprogramservicedescriptor-providername"></a>
Name of the provider.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceName`  <a name="cfn-medialive-multiplexprogram-multiplexprogramservicedescriptor-servicename"></a>
Name of the service.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
