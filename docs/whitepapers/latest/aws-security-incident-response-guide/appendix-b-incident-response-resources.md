---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/appendix-b-incident-response-resources.html
---

# Appendix B: AWS incident response resources
<a name="appendix-b-incident-response-resources"></a>

 AWS publishes resources to assist customers with developing incident response capabilities. Most example code and procedures can be found at the AWS external GitHub public repository. Following are some resources that provide examples of how to perform incident response.

## Playbook resources
<a name="playbook-resources"></a>
+  [Framework for Incident Response Playbooks](https://github.com/aws-samples/aws-customer-playbook-framework) - An example framework for customers to create, develop, and integrate security playbooks in preparation for potential attack scenarios when using AWS services.
+  [Develop your own Incident Response Playbooks](https://github.com/aws-samples/aws-incident-response-playbooks-workshop) - This workshop is designed to help you get familiar with developing incident response playbooks for AWS.
+  [Incident Response Playbook Samples](https://github.com/aws-samples/aws-incident-response-playbooks) - Playbooks covering common scenarios faced by AWS customers.
+  [Building an AWS incident response runbook using Jupyter playbooks and CloudTrail Lake](https://catalog.workshops.aws/incident-response-jupyter/en-US) - This workshop guides you through building an incident response playbook for your AWS environment using Jupyter notebooks and CloudTrail Lake.

## Forensic resources
<a name="forensic-resources"></a>
+  [Automated Incident Response and Forensics Framework](https://github.com/awslabs/aws-automated-incident-response-and-forensics) – This framework and solution provides a standard digital forensic process, consisting of the following phases: containment, acquisition, examination, and analysis. It leverages AWS Lambda functions to trigger the incident response process in an automated repeatable way. It provides segregation of accounts to operate the automation steps, store artifacts and create forensic environments.
+  [Automated Forensics Orchestrator for Amazon EC2](https://aws.amazon.com/solutions/implementations/automated-forensics-orchestrator-for-amazon-ec2/) – This implementation guide provides a self-service solution to capture and examine data from EC2 instances and attached volumes for forensic analysis in the event of a potential security issue being detected. There is an AWS CloudFormation template to deploy the solution.
+  [How to automate forensic disk collection in AWS](https://aws.amazon.com/blogs/security/how-to-automate-forensic-disk-collection-in-aws/) – This AWS blog details how to set up an automation workflow to capture the disk evidence for analysis in order to determine the scope and the impact of potential security incidents. There is also an AWS CloudFormation template included to deploy the solution.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
