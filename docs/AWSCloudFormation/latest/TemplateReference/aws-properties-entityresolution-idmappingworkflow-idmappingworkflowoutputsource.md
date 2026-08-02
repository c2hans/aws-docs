---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-entityresolution-idmappingworkflow-idmappingworkflowoutputsource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EntityResolution::IdMappingWorkflow IdMappingWorkflowOutputSource
<a name="aws-properties-entityresolution-idmappingworkflow-idmappingworkflowoutputsource"></a>

A list of `IdMappingWorkflowOutputSource` objects, each of which contains fields `outputS3Path` and `KMSArn`.

## Syntax
<a name="aws-properties-entityresolution-idmappingworkflow-idmappingworkflowoutputsource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-entityresolution-idmappingworkflow-idmappingworkflowoutputsource-syntax.json"></a>

```
{
  "[KMSArn](#cfn-entityresolution-idmappingworkflow-idmappingworkflowoutputsource-kmsarn)" : {{String}},
  "[OutputS3Path](#cfn-entityresolution-idmappingworkflow-idmappingworkflowoutputsource-outputs3path)" : {{String}}
}
```

### YAML
<a name="aws-properties-entityresolution-idmappingworkflow-idmappingworkflowoutputsource-syntax.yaml"></a>

```
  [KMSArn](#cfn-entityresolution-idmappingworkflow-idmappingworkflowoutputsource-kmsarn): {{String}}
  [OutputS3Path](#cfn-entityresolution-idmappingworkflow-idmappingworkflowoutputsource-outputs3path): {{String}}
```

## Properties
<a name="aws-properties-entityresolution-idmappingworkflow-idmappingworkflowoutputsource-properties"></a>

`KMSArn`  <a name="cfn-entityresolution-idmappingworkflow-idmappingworkflowoutputsource-kmsarn"></a>
Customer AWS KMS ARN for encryption at rest. If not provided, system will use an AWS Entity Resolution managed KMS key.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-us-gov|aws-cn):kms:.*:[0-9]+:.*$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputS3Path`  <a name="cfn-entityresolution-idmappingworkflow-idmappingworkflowoutputsource-outputs3path"></a>
The S3 path to which AWS Entity Resolution will write the output table.
*Required*: Yes
*Type*: String
*Pattern*: `^s3://([^/]+)/?(.*?([^/]+)/?)$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
