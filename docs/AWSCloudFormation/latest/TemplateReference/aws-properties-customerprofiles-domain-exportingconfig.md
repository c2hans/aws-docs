---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-domain-exportingconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::Domain ExportingConfig
<a name="aws-properties-customerprofiles-domain-exportingconfig"></a>

Configuration information for exporting Identity Resolution results, for example, to an S3 bucket.

## Syntax
<a name="aws-properties-customerprofiles-domain-exportingconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-domain-exportingconfig-syntax.json"></a>

```
{
  "[S3Exporting](#cfn-customerprofiles-domain-exportingconfig-s3exporting)" : {{S3ExportingConfig}}
}
```

### YAML
<a name="aws-properties-customerprofiles-domain-exportingconfig-syntax.yaml"></a>

```
  [S3Exporting](#cfn-customerprofiles-domain-exportingconfig-s3exporting): {{
    S3ExportingConfig}}
```

## Properties
<a name="aws-properties-customerprofiles-domain-exportingconfig-properties"></a>

`S3Exporting`  <a name="cfn-customerprofiles-domain-exportingconfig-s3exporting"></a>
Property description not available.
*Required*: No
*Type*: [S3ExportingConfig](aws-properties-customerprofiles-domain-s3exportingconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
