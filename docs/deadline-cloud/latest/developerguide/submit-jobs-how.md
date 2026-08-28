---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/submit-jobs-how.html
---

# How to submit a job to Deadline Cloud
<a name="submit-jobs-how"></a>

There are many different ways to submit jobs to AWS Deadline Cloud. This section describes some of the ways that you can submit jobs using the tools provided by Deadline Cloud or by creating your own custom tools for your workloads.
+ From a terminal – for when you're first developing a job bundle, or when users submitting a job are comfortable using the command line
+ From a script – for customizing and automating workloads
+ From an application – for when the user's work is in an application, or when an application's context is important.

 The following examples use the `deadline` Python library and the `deadline` command line tool. Both are available from [PyPi](https://pypi.org/project/deadline/) and [hosted on GitHub](https://github.com/aws-deadline/deadline-cloud).

**Topics**
+ [Submit a job to Deadline Cloud from a terminal](from-a-terminal.md)
+ [Submit a job to Deadline Cloud using a script](from-a-script.md)
+ [Submit a job within an application](from-within-applications.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
