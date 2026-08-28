---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-databrew-job-outputlocation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataBrew::Job OutputLocation
<a name="aws-properties-databrew-job-outputlocation"></a>

The location in Amazon S3 or AWS Glue Data Catalog where the job writes its output.

## Syntax
<a name="aws-properties-databrew-job-outputlocation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-databrew-job-outputlocation-syntax.json"></a>

```
{
  "[Bucket](#cfn-databrew-job-outputlocation-bucket)" : {{String}},
  "[BucketOwner](#cfn-databrew-job-outputlocation-bucketowner)" : {{String}},
  "[Key](#cfn-databrew-job-outputlocation-key)" : {{String}}
}
```

### YAML
<a name="aws-properties-databrew-job-outputlocation-syntax.yaml"></a>

```
  [Bucket](#cfn-databrew-job-outputlocation-bucket): {{String}}
  [BucketOwner](#cfn-databrew-job-outputlocation-bucketowner): {{String}}
  [Key](#cfn-databrew-job-outputlocation-key): {{String}}
```

## Properties
<a name="aws-properties-databrew-job-outputlocation-properties"></a>

`Bucket`  <a name="cfn-databrew-job-outputlocation-bucket"></a>
The Amazon S3 bucket name.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BucketOwner`  <a name="cfn-databrew-job-outputlocation-bucketowner"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Key`  <a name="cfn-databrew-job-outputlocation-key"></a>
The unique name of the object in the bucket.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
