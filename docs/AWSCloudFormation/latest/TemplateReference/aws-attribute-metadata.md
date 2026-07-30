---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-attribute-metadata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# `Metadata` attribute
<a name="aws-attribute-metadata"></a>

The `Metadata` attribute enables you to associate structured data with a resource. By adding a `Metadata` attribute to a resource, you can add data in JSON or YAML to the resource declaration. In addition, you can use intrinsic functions (such as [`Fn::GetAtt`](intrinsic-function-reference-getatt.md) and [`Ref`](intrinsic-function-reference-ref.md)), parameters, and pseudo parameters within the `Metadata` attribute to add those interpreted values.

**Note**
CloudFormation doesn't validate the syntax within the metadata attribute.

**Important**
CloudFormation doesn't redact or obfuscate any information you include in the metadata attribute. We strongly recommend you don't use this section to store sensitive information, such as passwords or secrets.

You can retrieve this data using the [describe-stack-resource](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/describe-stack-resource.html) CLI command or the [DescribeStackResource](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeStackResource.html) API operation.

## Example
<a name="aws-attribute-metadata-example"></a>

The following template contains an Amazon S3 bucket resource with a `Metadata` attribute.

### JSON
<a name="aws-attribute-metadata-example.json"></a>

```
{
   "AWSTemplateFormatVersion" : "2010-09-09",
   "Resources" : {
      "MyBucket" : {
         "Type" : "AWS::S3::Bucket",
         "Metadata" : {
            "Object1" : "Location1",
            "Object2" : "Location2"
         }
      }
   }
}
```

### YAML
<a name="aws-attribute-metadata-example.yaml"></a>

```
1. AWSTemplateFormatVersion: '2010-09-09'
2. Resources:
3.   MyBucket:
4.     Type: AWS::S3::Bucket
5.     Metadata:
6.       Object1: Location1
7.       Object2: Location2
```
