---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/format-version-structure.html
---

# CloudFormation template format version syntax
<a name="format-version-structure"></a>

The `AWSTemplateFormatVersion` section (optional) identifies the template format version that the template conforms to. The latest template format version is `2010-09-09` and is currently the only valid value.

The template format version isn't the same as the API version. The template format version can change independently of the API versions.

The value for the template format version declaration must be a literal string. You can't use a parameter or function to specify the template format version. If you don't specify a value, CloudFormation assumes the latest template format version. The following snippet is an example of a valid template format version declaration:

## JSON
<a name="format-version-structure-example.json"></a>

```
"AWSTemplateFormatVersion" : "2010-09-09"
```

## YAML
<a name="format-version-structure-example.yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
