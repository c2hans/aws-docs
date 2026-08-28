---
source_url: https://docs.aws.amazon.com/wellarchitected/2024-06-27/framework/rel-08.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL 8. How do you implement change?
<a name="rel-08"></a>

Controlled changes are necessary to deploy new functionality, and to verify that the workloads and the operating environment are running known software and can be patched or replaced in a predictable manner. If these changes are uncontrolled, then it makes it difficult to predict the effect of these changes, or to address issues that arise because of them.

**Topics**
+ [REL08-BP01 Use runbooks for standard activities such as deployment](rel_tracking_change_management_planned_changemgmt.md)
+ [REL08-BP02 Integrate functional testing as part of your deployment](rel_tracking_change_management_functional_testing.md)
+ [REL08-BP03 Integrate resiliency testing as part of your deployment](rel_tracking_change_management_resiliency_testing.md)
+ [REL08-BP04 Deploy using immutable infrastructure](rel_tracking_change_management_immutable_infrastructure.md)
+ [REL08-BP05 Deploy changes with automation](rel_tracking_change_management_automated_changemgmt.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
