---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/evaluationform-audit-trail.html
---

# View an evaluation form audit trail in Connect Customer
<a name="evaluationform-audit-trail"></a>

1. Select the evaluation form that you want to research.
![The evaluation forms page, a box to the left of an evaluation form.](http://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-select.png)

1. At the bottom of the page, under **Example Evaluation**, use the dropdown menu to view previous versions, who accessed them, and when. The following image shows an example audit trail.
![An example audit trail for an evaluation.](http://docs.aws.amazon.com/connect/latest/adminguide/images/evaluationforms-version.png)

1. Optionally, choose one of the forms to open it.

## What do Active, Draft, and Locked mean?
<a name="evaluationform-active-draft-locked"></a>

An form is in one of the following states:
+ **Active**. A published version of the form that is available to evaluators.
+ **Draft**. An inactive, locked version of the form. A draft is unlocked only when you are working on it.
+ **Locked**. An evaluation form is locked when you activate or publish it. Even after you deactivate the form, it stays locked, and becomes a historical version of the form. However, you can activate the historical version to save it as new version.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
