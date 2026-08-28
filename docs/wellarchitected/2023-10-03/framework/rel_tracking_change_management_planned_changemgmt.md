---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-10-03/framework/rel_tracking_change_management_planned_changemgmt.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL08-BP01 Use runbooks for standard activities such as deployment
<a name="rel_tracking_change_management_planned_changemgmt"></a>

 Runbooks are the predefined procedures to achieve specific outcomes. Use runbooks to perform standard activities, whether done manually or automatically. Examples include deploying a workload, patching a workload, or making DNS modifications.

 For example, put processes in place to [ensure rollback safety during deployments](https://aws.amazon.com/builders-library/ensuring-rollback-safety-during-deployments). Ensuring that you can roll back a deployment without any disruption for your customers is critical in making a service reliable.

 For runbook procedures, start with a valid effective manual process, implement it in code, and invoke it to automatically run where appropriate.

 Even for sophisticated workloads that are highly automated, runbooks are still useful for [running game days](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/test-reliability.html#GameDays) or meeting rigorous reporting and auditing requirements.

 Note that playbooks are used in response to specific incidents, and runbooks are used to achieve specific outcomes. Often, runbooks are for routine activities, while playbooks are used for responding to non-routine events.

 **Common anti-patterns:**
+  Performing unplanned changes to configuration in production.
+  Skipping steps in your plan to deploy faster, resulting in a failed deployment.
+  Making changes without testing the reversal of the change.

 **Benefits of establishing this best practice:** Effective change planning increases your ability to successfully run the change because you are aware of all the systems impacted. Validating your change in test environments increases your confidence.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Provide consistent and prompt responses to well-understood events by documenting procedures in runbooks.
  +  [AWS Well-Architected Framework: Concepts: Runbook](https://wa.aws.amazon.com/wat.concept.runbook.en.html)
+  Use the principle of infrastructure as code to define your infrastructure. By using AWS CloudFormation (or a trusted third party) to define your infrastructure, you can use version control software to version and track changes.
  +  Use AWS CloudFormation (or a trusted third-party provider) to define your infrastructure.
    +  [What is AWS CloudFormation?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
  +  Create templates that are singular and decoupled, using good software design principles.
    +  Determine the permissions, templates, and responsible parties for implementation.
      + [ Controlling access with AWS Identity and Access Management](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html)
    +  Use source control, like AWS CodeCommit or a trusted third-party tool, for version control.
      +  [What is AWS CodeCommit?](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [APN Partner: partners that can help you create automated deployment solutions](https://aws.amazon.com/partners/find/results/?keyword=devops)
+  [AWS Marketplace: products that can be used to automate your deployments](https://aws.amazon.com/marketplace/search/results?searchTerms=DevOps)
+  [AWS Well-Architected Framework: Concepts: Runbook](https://wa.aws.amazon.com/wat.concept.runbook.en.html)
+  [What is AWS CloudFormation?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
+  [What is AWS CodeCommit?](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html)

   **Related examples:**
+  [Automating operations with Playbooks and Runbooks](https://wellarchitectedlabs.com/operational-excellence/200_labs/200_automating_operations_with_playbooks_and_runbooks/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
