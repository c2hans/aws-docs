---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-mediatailor-program-transition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaTailor::Program Transition
<a name="aws-properties-mediatailor-program-transition"></a>

Program transition configuration.

## Syntax
<a name="aws-properties-mediatailor-program-transition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-mediatailor-program-transition-syntax.json"></a>

```
{
  "[DurationMillis](#cfn-mediatailor-program-transition-durationmillis)" : {{Integer}},
  "[RelativePosition](#cfn-mediatailor-program-transition-relativeposition)" : {{String}},
  "[RelativeProgram](#cfn-mediatailor-program-transition-relativeprogram)" : {{String}},
  "[ScheduledStartTimeMillis](#cfn-mediatailor-program-transition-scheduledstarttimemillis)" : {{Integer}},
  "[Type](#cfn-mediatailor-program-transition-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-mediatailor-program-transition-syntax.yaml"></a>

```
  [DurationMillis](#cfn-mediatailor-program-transition-durationmillis): {{Integer}}
  [RelativePosition](#cfn-mediatailor-program-transition-relativeposition): {{String}}
  [RelativeProgram](#cfn-mediatailor-program-transition-relativeprogram): {{String}}
  [ScheduledStartTimeMillis](#cfn-mediatailor-program-transition-scheduledstarttimemillis): {{Integer}}
  [Type](#cfn-mediatailor-program-transition-type): {{String}}
```

## Properties
<a name="aws-properties-mediatailor-program-transition-properties"></a>

`DurationMillis`  <a name="cfn-mediatailor-program-transition-durationmillis"></a>
The duration of the live program in seconds.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RelativePosition`  <a name="cfn-mediatailor-program-transition-relativeposition"></a>
The position where this program will be inserted relative to the `RelativePosition`.
*Required*: Yes
*Type*: String
*Allowed values*: `BEFORE_PROGRAM | AFTER_PROGRAM`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RelativeProgram`  <a name="cfn-mediatailor-program-transition-relativeprogram"></a>
The name of the program that this program will be inserted next to, as defined by `RelativePosition`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ScheduledStartTimeMillis`  <a name="cfn-mediatailor-program-transition-scheduledstarttimemillis"></a>
The date and time that the program is scheduled to start, in epoch milliseconds.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-mediatailor-program-transition-type"></a>
Defines when the program plays in the schedule. You can set the value to `ABSOLUTE` or `RELATIVE`.
`ABSOLUTE` - The program plays at a specific wall clock time. This setting can only be used for channels using the `LINEAR``PlaybackMode`.
Note the following considerations when using `ABSOLUTE` transitions:
If the preceding program in the schedule has a duration that extends past the wall clock time, MediaTailor truncates the preceding program on a common segment boundary.
If there are gaps in playback, MediaTailor plays the `FillerSlate` you configured for your linear channel.
`RELATIVE` - The program is inserted into the schedule either before or after a program that you specify via `RelativePosition`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
