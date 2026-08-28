---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-description-structure.html
---

# CloudFormation template Description syntax
<a name="template-description-structure"></a>

The `Description` section (optional) enables you to include a text string that describes the template. This section must always follow the template format version section.

The value for the description declaration must be a literal string that is between 0 and 1024 bytes in length. You cannot use a parameter or function to specify the description. The following snippet is an example of a description declaration:

**Important**
During a stack update, you cannot update the `Description` section by itself. You can update it only when you include changes that add, modify, or delete resources.

## JSON
<a name="template-description-structure-example.json"></a>

```
"Description" : "Here are some details about the template."
```

## YAML
<a name="template-description-structure-example.yaml"></a>

```
Description: > Here are some details about the template.
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
