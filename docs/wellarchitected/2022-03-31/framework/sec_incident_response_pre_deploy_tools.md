---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sec_incident_response_pre_deploy_tools.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC10-BP06 Pre-deploy tools
<a name="sec_incident_response_pre_deploy_tools"></a>

 Ensure that security personnel have the right tools pre-deployed into AWS to reduce the time for investigation through to recovery.

To automate security engineering and operations functions, you can use a comprehensive set of APIs and tools from AWS. You can fully automate identity management, network security, data protection, and monitoring capabilities and deliver them using popular software development methods that you already have in place. When you build security automation, your system can monitor, review, and initiate a response, rather than having people monitor your security position and manually react to events. An effective way to automatically provide searchable and relevant log data across AWS services to your incident responders is to enable [Amazon Detective](https://aws.amazon.com/detective/).

If your incident response teams continue to respond to alerts in the same way, they risk alert fatigue. Over time, the team can become desensitized to alerts and can either make mistakes handling ordinary situations or miss unusual alerts. Automation helps avoid alert fatigue by using functions that process the repetitive and ordinary alerts, leaving humans to handle the sensitive and unique incidents. Integrating anomaly detection systems, such as Amazon GuardDuty, AWS CloudTrail Insights, and Amazon CloudWatch Anomaly Detection, can reduce the burden of common threshold-based alerts.

You can improve manual processes by programmatically automating steps in the process. After you define the remediation pattern to an event, you can decompose that pattern into actionable logic, and write the code to perform that logic. Responders can then execute that code to remediate the issue. Over time, you can automate more and more steps, and ultimately automatically handle whole classes of common incidents.

For tools that execute within the operating system of your Amazon Elastic Compute Cloud (Amazon EC2) instance, you should evaluate using the AWS Systems Manager Run Command, which enables you to remotely and securely administrate instances using an agent that you install on your Amazon EC2 instance operating system. It requires the Systems Manager Agent (SSM Agent), which is installed by default on many Amazon Machine Images (AMIs). Be aware, though, that once an instance has been compromised, no responses from tools or agents running on it should be considered trustworthy.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Pre-deploy tools: Ensure that security personnel have the right tools pre-deployed in AWS so that an appropriate response can be made to an incident.
  +  [Lab: Incident response with AWS Management Console and CLI ](https://wellarchitectedlabs.com/Security/300_Incident_Response_with_AWS_Console_and_CLI/README.html)
  + [ Incident Response Playbook with Jupyter - AWS IAM ](https://wellarchitectedlabs.com/Security/300_Incident_Response_Playbook_with_Jupyter-AWS_IAM/README.html)
  +  [AWS Security Automation ](https://github.com/awslabs/aws-security-automation)
+  Implement resource tagging: Tag resources with information, such as a code for the resource under investigation, so that you can identify resources during an incident.
  + [AWS Tagging Strategies ](https://aws.amazon.com/answers/account-management/aws-tagging-strategies/)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Incident Response Guide ](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/welcome.html)

 **Related videos:**
+  [ DIY guide to runbooks, incident reports, and incident response ](https://youtu.be/E1NaYN_fJUo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
