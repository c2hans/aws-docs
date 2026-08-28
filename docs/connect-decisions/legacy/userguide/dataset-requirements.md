---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/dataset-requirements.html
---

# Dataset requirements
<a name="dataset-requirements"></a>

The following are important dataset requirements:
+ Default roles automatically include access to all required datasets.
+ Custom roles must be granted access to seven essential datasets: asc\_adp\_dp\_segmentation, asc\_adp\_forecast, asc\_adp\_planning\_cycle\_accuracy, outbound\_order\_line, product, product\_alternate, and supplementary\_time\_series.
+ Access to "asc\_adp\_dp\_segmentation" is specifically required for demand pattern and recommendation functionality.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
