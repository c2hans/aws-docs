---
source_url: https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_SuggesterStatus.html
---

# SuggesterStatus
<a name="API_SuggesterStatus"></a>

## Description
<a name="API_SuggesterStatus_Description"></a>

The value of a `Suggester` and its current status.

## Contents
<a name="API_SuggesterStatus_Contents"></a>

 **Options**
Configuration information for a search suggester. Each suggester has a unique name and specifies the text field you want to use for suggestions. The following options can be configured for a suggester: `FuzzyMatching`, `SortExpression`.
Type: [Suggester](API_Suggester.md)
 Required: Yes

 **Status**
The status of domain configuration option.
Type: [OptionStatus](API_OptionStatus.md)
 Required: Yes

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cloud Search. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudsearch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
