---
source_url: https://docs.aws.amazon.com/drs/latest/userguide/reinstalling-agent.html
---

# Reinstalling the agent
<a name="reinstalling-agent"></a>

To reinstall the AWS Replication Agent, download the latest version of the agent and follow the installation instructions. You do not need to remove any previous versions prior to reinstalling the agent.
+ [Linux](linux-agent.md)
+ [Windows](windows-agent.md)

**Note**
You must reinstall the agent to benefit from new features.

## Reinstalling the agent on a recovery instance
<a name="reinstalling-agent-recovery-instance"></a>

If you are reinstalling an agent on a recovery instance:

1. Select your recovery instance and choose **Disconnect from AWS** from the **Actions** drop-down menu.

1. When reinstalling the agent, include the **--install-as-recovery-instance** parameter.

Example:

```
chmod +x aws-replication-installer-init; sudo ./aws-replication-installer-init --install-as-recovery-instance s-abcd01234567890
```

**Note**
In order to reinstall the agent on a recovery instance, you need to provide the temporary credentials for a role that has the [AWSElasticDisasterRecoveryAgentInstallationPolicy](security-iam-awsmanpol-AWSElasticDisasterRecoveryAgentInstallationPolicy.md) policy.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
