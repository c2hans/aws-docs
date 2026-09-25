---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-jobtemplate-jobtemplatedata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::JobTemplate JobTemplateData
<a name="aws-properties-emrcontainers-jobtemplate-jobtemplatedata"></a>

The values of StartJobRun API requests used in job runs started using the job template.

## Syntax
<a name="aws-properties-emrcontainers-jobtemplate-jobtemplatedata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-jobtemplate-jobtemplatedata-syntax.json"></a>

```
{
  "[ConfigurationOverrides](#cfn-emrcontainers-jobtemplate-jobtemplatedata-configurationoverrides)" : {{ParametricConfigurationOverrides}},
  "[ExecutionRoleArn](#cfn-emrcontainers-jobtemplate-jobtemplatedata-executionrolearn)" : {{String}},
  "[JobDriver](#cfn-emrcontainers-jobtemplate-jobtemplatedata-jobdriver)" : {{JobDriver}},
  "[JobTags](#cfn-emrcontainers-jobtemplate-jobtemplatedata-jobtags)" : {{{{{Key}}: {{Value}}, ...}}},
  "[ParameterConfiguration](#cfn-emrcontainers-jobtemplate-jobtemplatedata-parameterconfiguration)" : {{{{{Key}}: {{Value}}, ...}}},
  "[ReleaseLabel](#cfn-emrcontainers-jobtemplate-jobtemplatedata-releaselabel)" : {{String}}
}
```

### YAML
<a name="aws-properties-emrcontainers-jobtemplate-jobtemplatedata-syntax.yaml"></a>

```
  [ConfigurationOverrides](#cfn-emrcontainers-jobtemplate-jobtemplatedata-configurationoverrides): {{
    ParametricConfigurationOverrides}}
  [ExecutionRoleArn](#cfn-emrcontainers-jobtemplate-jobtemplatedata-executionrolearn): {{String}}
  [JobDriver](#cfn-emrcontainers-jobtemplate-jobtemplatedata-jobdriver): {{
    JobDriver}}
  [JobTags](#cfn-emrcontainers-jobtemplate-jobtemplatedata-jobtags): {{
    {{Key}}: {{Value}}}}
  [ParameterConfiguration](#cfn-emrcontainers-jobtemplate-jobtemplatedata-parameterconfiguration): {{
    {{Key}}: {{Value}}}}
  [ReleaseLabel](#cfn-emrcontainers-jobtemplate-jobtemplatedata-releaselabel): {{String}}
```

## Properties
<a name="aws-properties-emrcontainers-jobtemplate-jobtemplatedata-properties"></a>

`ConfigurationOverrides`  <a name="cfn-emrcontainers-jobtemplate-jobtemplatedata-configurationoverrides"></a>
 The configuration settings that are used to override defaults configuration.
*Required*: No
*Type*: [ParametricConfigurationOverrides](aws-properties-emrcontainers-jobtemplate-parametricconfigurationoverrides.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExecutionRoleArn`  <a name="cfn-emrcontainers-jobtemplate-jobtemplatedata-executionrolearn"></a>
The execution role ARN of the job run.
*Required*: Yes
*Type*: String
*Pattern*: `^(^arn:(aws[a-zA-Z0-9-]*):iam::(\d{12})?:(role((\u002F)|(\u002F[\u0021-\u007F]+\u002F))[\w+=,.@-]+)$)|([\.\-_\#A-Za-z0-9\$\{\}]+)$`
*Minimum*: `4`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`JobDriver`  <a name="cfn-emrcontainers-jobtemplate-jobtemplatedata-jobdriver"></a>
Property description not available.
*Required*: Yes
*Type*: [JobDriver](aws-properties-emrcontainers-jobtemplate-jobdriver.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`JobTags`  <a name="cfn-emrcontainers-jobtemplate-jobtemplatedata-jobtags"></a>
The tags assigned to jobs started using the job template.
*Required*: No
*Type*: Object of String
*Pattern*: `^.+$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ParameterConfiguration`  <a name="cfn-emrcontainers-jobtemplate-jobtemplatedata-parameterconfiguration"></a>
The configuration of parameters existing in the job template.
*Required*: No
*Type*: Object of [TemplateParameterConfiguration](aws-properties-emrcontainers-jobtemplate-templateparameterconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ReleaseLabel`  <a name="cfn-emrcontainers-jobtemplate-jobtemplatedata-releaselabel"></a>
 The release version of Amazon EMR.
*Required*: Yes
*Type*: String
*Pattern*: `^([\.\-_/A-Za-z0-9]+|\$\{[a-zA-Z]\w*\})$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
