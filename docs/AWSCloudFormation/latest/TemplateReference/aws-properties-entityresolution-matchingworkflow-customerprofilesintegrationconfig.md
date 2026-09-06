---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-entityresolution-matchingworkflow-customerprofilesintegrationconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EntityResolution::MatchingWorkflow CustomerProfilesIntegrationConfig
<a name="aws-properties-entityresolution-matchingworkflow-customerprofilesintegrationconfig"></a>

Specifies the configuration for integrating with Customer Profiles. This configuration enables AWS Entity Resolution to send matched output directly to Customer Profiles instead of Amazon S3, creating a unified customer view by automatically updating customer profiles based on match clusters.

## Syntax
<a name="aws-properties-entityresolution-matchingworkflow-customerprofilesintegrationconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-entityresolution-matchingworkflow-customerprofilesintegrationconfig-syntax.json"></a>

```
{
  "[DomainArn](#cfn-entityresolution-matchingworkflow-customerprofilesintegrationconfig-domainarn)" : {{String}},
  "[ObjectTypeArn](#cfn-entityresolution-matchingworkflow-customerprofilesintegrationconfig-objecttypearn)" : {{String}}
}
```

### YAML
<a name="aws-properties-entityresolution-matchingworkflow-customerprofilesintegrationconfig-syntax.yaml"></a>

```
  [DomainArn](#cfn-entityresolution-matchingworkflow-customerprofilesintegrationconfig-domainarn): {{String}}
  [ObjectTypeArn](#cfn-entityresolution-matchingworkflow-customerprofilesintegrationconfig-objecttypearn): {{String}}
```

## Properties
<a name="aws-properties-entityresolution-matchingworkflow-customerprofilesintegrationconfig-properties"></a>

`DomainArn`  <a name="cfn-entityresolution-matchingworkflow-customerprofilesintegrationconfig-domainarn"></a>
The Amazon Resource Name (ARN) of the Customer Profiles domain where the matched output will be sent.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-us-gov|aws-cn):profile:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(domains/[a-zA-Z_0-9-]{1,255})$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ObjectTypeArn`  <a name="cfn-entityresolution-matchingworkflow-customerprofilesintegrationconfig-objecttypearn"></a>
The Amazon Resource Name (ARN) of the Customer Profiles object type that defines the structure for the matched customer data.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-us-gov|aws-cn):profile:[a-z]{2}-[a-z]{1,10}-[0-9]:[0-9]{12}:(domains/[a-zA-Z_0-9-]{1,255}/object-types/[a-zA-Z_0-9-]{1,255})$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
