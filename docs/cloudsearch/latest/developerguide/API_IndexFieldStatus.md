---
source_url: https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_IndexFieldStatus.html
---

# IndexFieldStatus
<a name="API_IndexFieldStatus"></a>

## Description
<a name="API_IndexFieldStatus_Description"></a>

The value of an `IndexField` and its current status.

## Contents
<a name="API_IndexFieldStatus_Contents"></a>

 **Options**
Configuration information for a field in the index, including its name, type, and options. The supported options depend on the ` IndexFieldType `.
Type: [IndexField](API_IndexField.md)
 Required: Yes

 **Status**
The status of domain configuration option.
Type: [OptionStatus](API_OptionStatus.md)
 Required: Yes

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cloud Search. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudsearch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
