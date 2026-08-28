---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-multiplexprogram-multiplexprogramsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::Multiplexprogram MultiplexProgramSettings
<a name="aws-properties-medialive-multiplexprogram-multiplexprogramsettings"></a>

Multiplex Program settings configuration.

## Syntax
<a name="aws-properties-medialive-multiplexprogram-multiplexprogramsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-multiplexprogram-multiplexprogramsettings-syntax.json"></a>

```
{
  "[PreferredChannelPipeline](#cfn-medialive-multiplexprogram-multiplexprogramsettings-preferredchannelpipeline)" : {{String}},
  "[ProgramNumber](#cfn-medialive-multiplexprogram-multiplexprogramsettings-programnumber)" : {{Integer}},
  "[ServiceDescriptor](#cfn-medialive-multiplexprogram-multiplexprogramsettings-servicedescriptor)" : {{MultiplexProgramServiceDescriptor}},
  "[VideoSettings](#cfn-medialive-multiplexprogram-multiplexprogramsettings-videosettings)" : {{MultiplexVideoSettings}}
}
```

### YAML
<a name="aws-properties-medialive-multiplexprogram-multiplexprogramsettings-syntax.yaml"></a>

```
  [PreferredChannelPipeline](#cfn-medialive-multiplexprogram-multiplexprogramsettings-preferredchannelpipeline): {{String}}
  [ProgramNumber](#cfn-medialive-multiplexprogram-multiplexprogramsettings-programnumber): {{Integer}}
  [ServiceDescriptor](#cfn-medialive-multiplexprogram-multiplexprogramsettings-servicedescriptor): {{
    MultiplexProgramServiceDescriptor}}
  [VideoSettings](#cfn-medialive-multiplexprogram-multiplexprogramsettings-videosettings): {{
    MultiplexVideoSettings}}
```

## Properties
<a name="aws-properties-medialive-multiplexprogram-multiplexprogramsettings-properties"></a>

`PreferredChannelPipeline`  <a name="cfn-medialive-multiplexprogram-multiplexprogramsettings-preferredchannelpipeline"></a>
Indicates which pipeline is preferred by the multiplex for program ingest.
*Required*: No
*Type*: String
*Allowed values*: `CURRENTLY_ACTIVE | PIPELINE_0 | PIPELINE_1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProgramNumber`  <a name="cfn-medialive-multiplexprogram-multiplexprogramsettings-programnumber"></a>
Unique program number.
*Required*: Yes
*Type*: Integer
*Minimum*: `0`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceDescriptor`  <a name="cfn-medialive-multiplexprogram-multiplexprogramsettings-servicedescriptor"></a>
Transport stream service descriptor configuration for the Multiplex program.
*Required*: No
*Type*: [MultiplexProgramServiceDescriptor](aws-properties-medialive-multiplexprogram-multiplexprogramservicedescriptor.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VideoSettings`  <a name="cfn-medialive-multiplexprogram-multiplexprogramsettings-videosettings"></a>
Program video settings configuration.
*Required*: No
*Type*: [MultiplexVideoSettings](aws-properties-medialive-multiplexprogram-multiplexvideosettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
