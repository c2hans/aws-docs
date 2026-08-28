---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/RequesterUI/ManagingQualificationTypes.html
---

# Managing qualification types
<a name="ManagingQualificationTypes"></a>

**Topics**
+ [Create a qualification type](CreatingaQualificationType.md)
+ [View existing qualification types](ViewingExistingQualificationTypes.md)
+ [Delete qualification types](DeleteQualification.md)

You can create your own qualification types, or use the ones supplied by Mechanical Turk.

Mechanical Turk provides system qualification types that keep track of a Worker's account statistics and attributes. You can use system qualification types to control who can and cannot work on your Human Intelligence Tasks (HITs). For example, you can require that Workers have a 95% approval rating or greater to work on your HITs.

You can create new custom qualification types to select Workers based on any criteria you want. You can assign a custom qualification type and a score to Workers who work for you. Then, when you create a HIT, you can specify the custom qualification type and the minimum score a Worker must have to be eligible to work on your HITs.

The Requester User Interface (RUI) does not support Qualification Tests that a Worker must take to achieve a qualification. Use the Mechanical Turk APIs or the command line tools for testing. For more information, see [https://docs.aws.amazon.com/mturk/](https://docs.aws.amazon.com/mturk/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
