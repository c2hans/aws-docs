---
source_url: https://docs.aws.amazon.com/managedservices/latest/userguide/auto-config-pre-reqs.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Prerequisites for automated instance configuration
<a name="auto-config-pre-reqs"></a>

For AMS Advanced customers who deploy instances with Change Management, the following prerequisites must be met:
+ The SSM Agent is installed, and in a managed state.
+ The instance is tagged as a managed instance. (The `aws:cloudformation:stack-name` tag has a value starting with `stack-` or `sc-`.)

If the SSM Agent is not already installed on your instance, you can install it using the AMS SSM Agent auto installation feature. For more information, see [SSM Agent automatic installation](ssm-agent-auto-install.md).

Or, you can install the SSM Agent manually. For more information, see the following:
+ Linux: [Manually install SSM Agent on EC2 instances for Linux - AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-manual-agent-install.html)
+ Windows: [Manually install SSM Agent on EC2 instances for Windows Server - AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-install-win.html)

For more information on SSM agent, see the AWS documentation [Working with SSM Agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
