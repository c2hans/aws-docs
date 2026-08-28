---
source_url: https://docs.aws.amazon.com/managedservices/latest/userguide/auto-instance-config.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Automated instance configuration in AMS Advanced
<a name="auto-instance-config"></a>

The AMS Advanced automated instance configuration service runs daily and automatically scans and updates the SSM and CloudWatch agents and configuration files on your managed EC2 instances. The updates apply, as needed to:
+ SSM and CloudWatch agents
+ CloudWatch configuration files

 These updates allow AMS to access your AMS-managed EC2 instances, and to configure your instances to emit appropriate [logs](https://docs.aws.amazon.com/managedservices/latest/userguide/auto-config-logs-cw.html) and metrics.

**Topics**
+ [Prerequisites for automated instance configuration](auto-config-pre-reqs.md)
+ [SSM Agent automatic installation](ssm-agent-auto-install.md)
+ [Automated changes](auto-config-changes-made.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
