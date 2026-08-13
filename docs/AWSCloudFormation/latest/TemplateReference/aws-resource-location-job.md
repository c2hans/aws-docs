---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-location-job.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Location::Job
<a name="aws-resource-location-job"></a>

<a name="aws-resource-location-job-description"></a>The `AWS::Location::Job` resource Property description not available. for Location.

## Syntax
<a name="aws-resource-location-job-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-location-job-syntax.json"></a>

```
{
  "Type" : "AWS::Location::Job",
  "Properties" : {
      "[Action](#cfn-location-job-action)" : {{String}},
      "[ActionOptions](#cfn-location-job-actionoptions)" : {{JobActionOptions}},
      "[ExecutionRoleArn](#cfn-location-job-executionrolearn)" : {{String}},
      "[InputOptions](#cfn-location-job-inputoptions)" : {{JobInputOptions}},
      "[Name](#cfn-location-job-name)" : {{String}},
      "[OutputOptions](#cfn-location-job-outputoptions)" : {{JobOutputOptions}},
      "[Tags](#cfn-location-job-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-location-job-syntax.yaml"></a>

```
Type: AWS::Location::Job
Properties:
  [Action](#cfn-location-job-action): {{String}}
  [ActionOptions](#cfn-location-job-actionoptions): {{
    JobActionOptions}}
  [ExecutionRoleArn](#cfn-location-job-executionrolearn): {{String}}
  [InputOptions](#cfn-location-job-inputoptions): {{
    JobInputOptions}}
  [Name](#cfn-location-job-name): {{String}}
  [OutputOptions](#cfn-location-job-outputoptions): {{
    JobOutputOptions}}
  [Tags](#cfn-location-job-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-location-job-properties"></a>

`Action`  <a name="cfn-location-job-action"></a>
Action performed by the job.
*Required*: Yes
*Type*: String
*Allowed values*: `ValidateAddress`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ActionOptions`  <a name="cfn-location-job-actionoptions"></a>
Additional options for configuring job action parameters.
*Required*: No
*Type*: [JobActionOptions](aws-properties-location-job-jobactionoptions.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExecutionRoleArn`  <a name="cfn-location-job-executionrolearn"></a>
IAM role used for job execution.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InputOptions`  <a name="cfn-location-job-inputoptions"></a>
Input configuration.
*Required*: Yes
*Type*: [JobInputOptions](aws-properties-location-job-jobinputoptions.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-location-job-name"></a>
Job name (if provided during creation).
*Required*: No
*Type*: String
*Pattern*: `^[-._\w]+$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OutputOptions`  <a name="cfn-location-job-outputoptions"></a>
Output configuration.
*Required*: Yes
*Type*: [JobOutputOptions](aws-properties-location-job-joboutputoptions.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-location-job-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-location-job-tag.md)
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-location-job-return-values"></a>

### Ref
<a name="aws-resource-location-job-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-location-job-return-values-fn--getatt"></a>

####
<a name="aws-resource-location-job-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
Job creation time in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sss`.

`JobArn`  <a name="JobArn-fn::getatt"></a>
Amazon Resource Name (ARN) of the job.

`JobId`  <a name="JobId-fn::getatt"></a>
Unique job identifier.

`Status`  <a name="Status-fn::getatt"></a>
Current job status.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
Last update time in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) format: `YYYY-MM-DDThh:mm:ss.sss`.
