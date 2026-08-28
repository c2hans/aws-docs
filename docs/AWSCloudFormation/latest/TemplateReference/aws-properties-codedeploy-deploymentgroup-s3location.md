---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codedeploy-deploymentgroup-s3location.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeDeploy::DeploymentGroup S3Location
<a name="aws-properties-codedeploy-deploymentgroup-s3location"></a>

`S3Location` is a property of the [CodeDeploy DeploymentGroup Revision ](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision.html) property that specifies the location of an application revision that is stored in Amazon Simple Storage Service (Amazon S3).

## Syntax
<a name="aws-properties-codedeploy-deploymentgroup-s3location-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codedeploy-deploymentgroup-s3location-syntax.json"></a>

```
{
  "[Bucket](#cfn-codedeploy-deploymentgroup-s3location-bucket)" : {{String}},
  "[BundleType](#cfn-codedeploy-deploymentgroup-s3location-bundletype)" : {{String}},
  "[ETag](#cfn-codedeploy-deploymentgroup-s3location-etag)" : {{String}},
  "[Key](#cfn-codedeploy-deploymentgroup-s3location-key)" : {{String}},
  "[Version](#cfn-codedeploy-deploymentgroup-s3location-version)" : {{String}}
}
```

### YAML
<a name="aws-properties-codedeploy-deploymentgroup-s3location-syntax.yaml"></a>

```
  [Bucket](#cfn-codedeploy-deploymentgroup-s3location-bucket): {{String}}
  [BundleType](#cfn-codedeploy-deploymentgroup-s3location-bundletype): {{String}}
  [ETag](#cfn-codedeploy-deploymentgroup-s3location-etag): {{String}}
  [Key](#cfn-codedeploy-deploymentgroup-s3location-key): {{String}}
  [Version](#cfn-codedeploy-deploymentgroup-s3location-version): {{String}}
```

## Properties
<a name="aws-properties-codedeploy-deploymentgroup-s3location-properties"></a>

`Bucket`  <a name="cfn-codedeploy-deploymentgroup-s3location-bucket"></a>
The name of the Amazon S3 bucket where the application revision is stored.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BundleType`  <a name="cfn-codedeploy-deploymentgroup-s3location-bundletype"></a>
The file type of the application revision. Must be one of the following:
+ JSON
+ tar: A tar archive file.
+ tgz: A compressed tar archive file.
+ YAML
+ zip: A zip archive file.
*Required*: No
*Type*: String
*Allowed values*: `tar | tgz | zip | YAML | JSON`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ETag`  <a name="cfn-codedeploy-deploymentgroup-s3location-etag"></a>
The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.
If the ETag is not specified as an input parameter, ETag validation of the object is skipped.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Key`  <a name="cfn-codedeploy-deploymentgroup-s3location-key"></a>
The name of the Amazon S3 object that represents the bundled artifacts for the application revision.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Version`  <a name="cfn-codedeploy-deploymentgroup-s3location-version"></a>
A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.
If the version is not specified, the system uses the most recent version by default.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
