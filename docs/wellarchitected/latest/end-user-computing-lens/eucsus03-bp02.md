---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsus03-bp02.html
---

# EUCSUS03-BP02 Adapt the AutoStop timeout and idle disconnect timeout for Amazon DCV
<a name="eucsus03-bp02"></a>

 The AutoStop timeout in WorkSpaces is only available with AutoStop. This is not applicable to AlwaysOn WorkSpaces. In WorkSpaces, you can configure how long a user can be inactive while connected to a WorkSpace before they are disconnected. Amazon DCV (Desktop Cloud Virtualization) is the remote display protocol used by Amazon WorkSpaces to stream pixels, keystrokes and mouse movements.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance-97"></a>

 By default, AutoStop time (in hours**)** is set to one hour, which means that the WorkSpace stops automatically an hour after the WorkSpace is disconnected.  Keep the AutoStop time at the default value, as this is the lowest value offered.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
