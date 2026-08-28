---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/security-access-control.html
---

# Access control for notebooks
<a name="security-access-control"></a>

You must use different procedures to control access to Amazon SageMaker Studio Classic notebooks and SageMaker notebook instances because they have different runtime environments. Studio Classic uses file system permissions and containers to control access to Studio Classic notebooks and isolation of users. A SageMaker notebook instance gives users that login to the notebook instance default root access. The following topics describe how to change permissions for both kinds of notebooks.

**Topics**
+ [Access control and setting permissions for SageMaker Studio notebooks](security-access-control-studio-nb.md)
+ [Control root access to a SageMaker notebook instance](nbi-root-access.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
