---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-emrcontainers-jobtemplate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::JobTemplate
<a name="aws-resource-emrcontainers-jobtemplate"></a>

This entity describes a job template. Job template stores values of StartJobRun API request in a template and can be used to start a job run. Job template allows two use cases: avoid repeating recurring StartJobRun API request values, enforcing certain values in StartJobRun API request.

## Syntax
<a name="aws-resource-emrcontainers-jobtemplate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-emrcontainers-jobtemplate-syntax.json"></a>

```
{
  "Type" : "AWS::EMRContainers::JobTemplate",
  "Properties" : {
      "[JobTemplateData](#cfn-emrcontainers-jobtemplate-jobtemplatedata)" : {{JobTemplateData}},
      "[Name](#cfn-emrcontainers-jobtemplate-name)" : {{String}},
      "[Tags](#cfn-emrcontainers-jobtemplate-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-emrcontainers-jobtemplate-syntax.yaml"></a>

```
Type: AWS::EMRContainers::JobTemplate
Properties:
  [JobTemplateData](#cfn-emrcontainers-jobtemplate-jobtemplatedata): {{
    JobTemplateData}}
  [Name](#cfn-emrcontainers-jobtemplate-name): {{String}}
  [Tags](#cfn-emrcontainers-jobtemplate-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-emrcontainers-jobtemplate-properties"></a>

`JobTemplateData`  <a name="cfn-emrcontainers-jobtemplate-jobtemplatedata"></a>
The job template data which holds values of StartJobRun API request.
*Required*: Yes
*Type*: [JobTemplateData](aws-properties-emrcontainers-jobtemplate-jobtemplatedata.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-emrcontainers-jobtemplate-name"></a>
The name of the job template.
*Required*: Yes
*Type*: String
*Pattern*: `^[\.\-_/#A-Za-z0-9]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-emrcontainers-jobtemplate-tags"></a>
The tags assigned to the job template.
*Required*: No
*Type*: Array of [Tag](aws-properties-emrcontainers-jobtemplate-tag.md)
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-emrcontainers-jobtemplate-return-values"></a>

### Ref
<a name="aws-resource-emrcontainers-jobtemplate-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-emrcontainers-jobtemplate-return-values-fn--getatt"></a>

####
<a name="aws-resource-emrcontainers-jobtemplate-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the job template.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
 The date and time when the job template was created.

`CreatedBy`  <a name="CreatedBy-fn::getatt"></a>
 The user who created the job template.

`Id`  <a name="Id-fn::getatt"></a>
The ID of the job template.
