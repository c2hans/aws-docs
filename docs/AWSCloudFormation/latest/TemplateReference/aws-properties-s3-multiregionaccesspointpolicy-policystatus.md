---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3-multiregionaccesspointpolicy-policystatus.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3::MultiRegionAccessPointPolicy PolicyStatus
<a name="aws-properties-s3-multiregionaccesspointpolicy-policystatus"></a>

The container element for a bucket's policy status.

## Syntax
<a name="aws-properties-s3-multiregionaccesspointpolicy-policystatus-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3-multiregionaccesspointpolicy-policystatus-syntax.json"></a>

```
{
  "[IsPublic](#cfn-s3-multiregionaccesspointpolicy-policystatus-ispublic)" : {{String}}
}
```

### YAML
<a name="aws-properties-s3-multiregionaccesspointpolicy-policystatus-syntax.yaml"></a>

```
  [IsPublic](#cfn-s3-multiregionaccesspointpolicy-policystatus-ispublic): {{String}}
```

## Properties
<a name="aws-properties-s3-multiregionaccesspointpolicy-policystatus-properties"></a>

`IsPublic`  <a name="cfn-s3-multiregionaccesspointpolicy-policystatus-ispublic"></a>
The policy status for this bucket. `TRUE` indicates that this bucket is public. `FALSE` indicates that the bucket is not public.
*Required*: Yes
*Type*: String
*Allowed values*: `true | false`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
