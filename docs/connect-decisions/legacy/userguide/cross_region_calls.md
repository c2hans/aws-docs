---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/cross_region_calls.html
---

# Cross-Region calls with Amazon Q in AWS Supply Chain
<a name="cross_region_calls"></a>

Amazon Q in AWS Supply Chain has a dependency on Amazon Kendra for retrieving relevant search results from public documentation that may be used to answer your questions. Amazon Kendra is available in a subset of AWS Regions that Amazon Q in AWS Supply Chain supports. Amazon Q in AWS Supply Chain calls Amazon Kendra local endpoints when Amazon Kendra is available locally in an AWS Region. When Amazon Kendra is not available locally, Amazon Q in AWS Supply Chain calls Amazon Kendra’s endpoints in a different AWS Region. In these cross-region calls, Amazon Q in AWS Supply Chain may send your prompts to Amazon Kendra.

<table>
<thead>
  <tr><th colspan="2">Amazon Q in AWS Supply Chain Region</th><th colspan="2">Amazon Kendra Region</th></tr>
  <tr><th>Region Code</th><th>Region Name</th><th>Region Code</th><th>Region Name</th></tr>
</thead>
<tbody>
  <tr><td>eu-central-1</td><td>Europe (Frankfurt)</td><td>eu-west-1</td><td>Europe (Ireland)</td></tr>
</tbody>
</table>

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
