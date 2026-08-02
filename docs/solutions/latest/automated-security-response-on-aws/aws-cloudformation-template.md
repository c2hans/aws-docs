---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-security-response-on-aws/aws-cloudformation-template.html
---

# AWS CloudFormation templates
<a name="aws-cloudformation-template"></a>

 [https://solutions-reference.s3.amazonaws.com/automated-security-response-on-aws/latest/automated-security-response-admin.template](https://solutions-reference.s3.amazonaws.com/automated-security-response-on-aws/latest/automated-security-response-admin.template) **automated-security-response-admin.template** - Use this template to launch the Automated Security Response on AWS solution. The template installs the core components of the solution, a nested stack for the AWS Step Functions logs, and one nested stack for each security standard you choose to activate.

Services used include Amazon Simple Notification Service, AWS Key Management Service, AWS Identity and Access Management, AWS Lambda, AWS Step Functions, Amazon CloudWatch Logs, Amazon S3, and AWS Systems Manager.

## Admin account support
<a name="admin-account-support"></a>

The following templates are installed in the AWS Security Hub admin account to turn on the security standards that you want to support. You can choose which of the following templates to install when installing the `automated-security-response-admin.template`.

 **automated-security-response-orchestrator-log.template** - Creates a CloudWatch logs group for the Orchestrator Step Function.

 **automated-security-response-webui-nested-stack.template** - Creates the resources to support the solution’s Web UI.

 **AFSBPStack.template** - AWS Foundational Security Best Practices v1.0.0 rules.

 **CIS120Stack.template** - CIS Amazon Web Services Foundations benchmarks, v1.2.0 rules.

 **CIS140Stack.template** - CIS Amazon Web Services Foundations benchmarks, v1.4.0 rules.

 **CIS300Stack.template** - CIS Amazon Web Services Foundations benchmarks, v3.0.0 rules.

 **PCI321Stack.template** - PCI-DSS v3.2.1 rules.

 **NISTStack.template** - National Institute of Standards and Technology (NIST), v5.0.0 rules.

 **SCStack.template** - Security Controls v2.0.0 rules.

## Member roles
<a name="member-roles"></a>

 [https://solutions-reference.s3.amazonaws.com/automated-security-response-on-aws/latest/automated-security-response-member-roles.template](https://solutions-reference.s3.amazonaws.com/automated-security-response-on-aws/latest/automated-security-response-member-roles.template) **automated-security-response-member-roles.template** - Defines the remediation roles needed in each AWS Security Hub member account.

## Member accounts
<a name="member-accounts"></a>

 [https://solutions-reference.s3.amazonaws.com/automated-security-response-on-aws/latest/automated-security-response-member.template](https://solutions-reference.s3.amazonaws.com/automated-security-response-on-aws/latest/automated-security-response-member.template) **automated-security-response-member.template** - Use this template after you set up the core solution to install AWS Systems Manager automation runbooks and permissions in each of your AWS Security Hub member accounts (including the admin account). This template allows you to choose which security standard playbooks to install.

The `automated-security-response-member.template` installs the following templates based on your selections:

 **automated-security-response-remediation-runbooks.template** - Common remediation code used by one or more of the security standards.

 **AFSBPMemberStack.template** - AWS Foundational Security Best Practices v1.0.0 settings, permissions, and remediation runbooks.

 **CIS120MemberStack.template** - CIS Amazon Web Services Foundations benchmarks, version 1.2.0 settings, permissions, and remediation runbooks.

 **CIS140MemberStack.template** - CIS Amazon Web Services Foundations benchmarks, version 1.4.0 settings, permissions, and remediation runbooks.

 **CIS300MemberStack.template** - CIS Amazon Web Services Foundations benchmarks, version 3.0.0 settings, permissions, and remediation runbooks.

 **PCI321MemberStack.template** - PCI-DSS v3.2.1 settings, permissions, and remediation runbooks.

 **NISTMemberStack.template** - National Institute of Standards and Technology (NIST), v5.0.0 settings, permissions, and remediation runbooks.

 **SCMemberStack.template** - Security Control settings, permissions, and remediation runbooks.

 **automated-security-response-member-cloudtrail.template** - Used in the Action Log feature to track and audit and service activity.

## Ticket system integration
<a name="ticket-system-integration"></a>

Use one of the following templates to integrate with your ticketing system.

 [https://solutions-reference.s3.amazonaws.com/automated-security-response-on-aws/latest/blueprints/JiraBlueprintStack.template](https://solutions-reference.s3.amazonaws.com/automated-security-response-on-aws/latest/blueprints/JiraBlueprintStack.template) **JiraBlueprintStack.template** - Deploy if you use Jira as your ticketing system.

 [https://solutions-reference.s3.amazonaws.com/automated-security-response-on-aws/latest/blueprints/ServiceNowBlueprintStack.template](https://solutions-reference.s3.amazonaws.com/automated-security-response-on-aws/latest/blueprints/ServiceNowBlueprintStack.template) **ServiceNowBlueprintStack.template** - Deploy if you use ServiceNow as your ticketing system.

If you want to integrate a different external ticketing system, you can use either of these stacks as blueprint to understand how to implement your own custom integration.
