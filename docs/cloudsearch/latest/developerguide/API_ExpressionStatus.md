---
source_url: https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_ExpressionStatus.html
---

# ExpressionStatus
<a name="API_ExpressionStatus"></a>

## Description
<a name="API_ExpressionStatus_Description"></a>

The value of an `Expression` and its current status.

## Contents
<a name="API_ExpressionStatus_Contents"></a>

 **Options**
The expression that is evaluated for sorting while processing a search request.
Type: [Expression](API_Expression.md)
 Required: Yes

 **Status**
The status of domain configuration option.
Type: [OptionStatus](API_OptionStatus.md)
 Required: Yes

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cloud Search. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudsearch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
