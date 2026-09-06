---
source_url: https://docs.aws.amazon.com/inspector/v1/userguide/inspector_agents.html
---

 End of support notice: On May 20, 2026, AWS will end support for Amazon Inspector Classic. After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. Amazon Inspector Classic no longer available to new accounts and accounts that have not completed an assessment in the last 6 months. For all other accounts, access will remain valid until May 20, 2026, after which you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

# Amazon Inspector Classic agents
<a name="inspector_agents"></a>

The Amazon Inspector Classic agent is an entity that collects installed package information and software configuration for an Amazon EC2 instance. Though not required in all cases, you should install the Amazon Inspector Classic agent on each of your target Amazon EC2 instances in order to fully assess their security.

For more information about how to install, uninstall, and reinstall the agent, how to verify whether the installed agent is running, and how to configure proxy support for the agent, see [Working with Amazon Inspector Classic agents on Linux-based operating systems](inspector_agents-on-linux.md) and [Working with Amazon Inspector Classic agents on Windows-based operating systems](inspector_agents-on-win.md).

**Note**
An Amazon Inspector Classic agent is not required to run the [Network Reachability](inspector_network-reachability.md) rules package.

**Important**
The Amazon Inspector Classic agent relies on Amazon EC2 instance metadata to function correctly. It accesses instance metadata using version 1 or version 2 of the Instance Metadata Service (IMDSv1 or IMDSv2). See [Instance Metadata and User Data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html) to learn more about EC2 instance metadata and access methods.

**Topics**
+ [Amazon Inspector Classic agent privileges](#agent-privileges)
+ [Network and Amazon Inspector Classic agent security](#agent-security)
+ [Amazon Inspector Classic agent updates](#agent-updates)
+ [Telemetry data lifecycle](#telemetry-data-lifecycle)
+ [Access control from Amazon Inspector Classic into AWS accounts](#access-control)
+ [Amazon Inspector Classic agent limits](#agent-limits)
+ [Installing Amazon Inspector Classic agents](inspector_installing-uninstalling-agents.md)
+ [Working with Amazon Inspector Classic agents on Linux-based operating systems](inspector_agents-on-linux.md)
+ [Working with Amazon Inspector Classic agents on Windows-based operating systems](inspector_agents-on-win.md)
+ [(Optional) Verify the signature of the Amazon Inspector Classic agent installation script on Linux-based operating systems](inspector_verify-sig-agent-download-linux.md)
+ [(Optional) Verify the signature of the Amazon Inspector Classic agent installation script on Windows-based operating systems](inspector_verify-sig-agent-download-win.md)

## Amazon Inspector Classic agent privileges
<a name="agent-privileges"></a>

You must have administrative or root permissions to install the Amazon Inspector Classic agent. On supported Linux-based operating systems, the agent consists of a user mode executable that runs with root access. On supported Windows-based operating systems, the agent consists of an updater service and an agent service, each running in user mode with `LocalSystem` privileges.

## Network and Amazon Inspector Classic agent security
<a name="agent-security"></a>

The Amazon Inspector Classic agent initiates all communication with the Amazon Inspector Classic service. This means that the agent must have an outbound network path to public endpoints so that it can send telemetry data. For example, the agent might connect to `arsenal.<region>.amazonaws.com`, or the endpoint might be an Amazon S3 bucket at `s3.dualstack.<region>.amazonaws.com`. Make sure to replace `<region>` with the actual AWS Region where you are running Amazon Inspector Classic. For more information, see [AWS IP Address Ranges](http://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html). Because all connections from the agent are established outbound, it is not necessary to open ports in your security groups to allow inbound communications to the agent from Amazon Inspector Classic.

The agent periodically communicates with Amazon Inspector Classic over a TLS-protected channel, which is authenticated using either the AWS identity associated with the role of the EC2 instance, or, if no role is assigned, with the instance's metadata document. When authenticated, the agent sends heartbeat messages to the service and receives instructions from the service in response. If an assessment has been scheduled, the agent receives the instructions for that assessment. These instructions are structured JSON files, and they tell the agent to enable or disable specific preconfigured sensors in the agent. Each instruction action is predefined within the agent. Arbitrary instructions can't be executed.

During an assessment, the agent gathers telemetry data from the system to send back to Amazon Inspector Classic over a TLS-protected channel. The agent doesn't make changes to the system that it collects data from. After the agent collects the telemetry data, it sends the data back to Amazon Inspector Classic for processing. Beyond the telemetry data that it generates, the agent is not capable of collecting or transmitting any other data about the system or assessment targets. Currently, there is no method exposed for intercepting and examining telemetry data at the agent.

## Amazon Inspector Classic agent updates
<a name="agent-updates"></a>

As updates for the Amazon Inspector Classic agent become available, they are automatically downloaded from Amazon S3 and applied. This also updates any required dependencies. The auto-update feature eliminates the need for you to track and manually maintain the versioning of the agents that you have installed on your EC2 instances. All updates are subject to audited Amazon change control processes to ensure compliance with applicable security standards.

To further ensure the security of the agent, all communication between the agent and the auto-update release site (S3) is performed over a TLS connection, and the server is authenticated. All binaries involved in the auto-update process are digitally signed, and the signatures are verified by the updater before installation. The auto-update process is executed only during non-assessment periods. If any errors are detected, the update process can rollback and retry the update. Finally, the agent update process serves to upgrade only the agent capabilities. None of your specific information is ever sent from the agent to Amazon Inspector Classic as part of the update workflow. The only information that is communicated as part of the update process is the basic installation success or fail telemetry and, if applicable, any update failure diagnostic information.

## Telemetry data lifecycle
<a name="telemetry-data-lifecycle"></a>

The telemetry data that is generated by the Amazon Inspector Classic agent during assessment runs is formatted in JSON files. The files are delivered in near-real-time over TLS to Amazon Inspector Classic, where they are encrypted with a per-assessment-run, ephemeral KMS-derived key. The files are securely stored in an Amazon S3 bucket this is dedicated for Amazon Inspector Classic. The rules engine of Amazon Inspector Classic accesses the encrypted telemetry data in the S3 bucket, decrypts it in memory, and processes the data against the configured assessment rules to generate findings. The telemetry data that is stored in S3 is retained only to allow for assistance with support requests. It isn't used or aggregated by Amazon for any other purpose. After 30 days, telemetry data is permanently deleted according to a standard S3 bucket lifecycle policy for Amazon Inspector Classic data. Currently, Amazon Inspector Classic does not provide an API or an S3 bucket access mechanism to collected telemetry.

## Access control from Amazon Inspector Classic into AWS accounts
<a name="access-control"></a>

As a security service, Amazon Inspector Classic accesses your AWS accounts and resources only when it needs to find EC2 instances to assess by querying for tags. It does this through standard IAM access through the role created during the initial setup of the Amazon Inspector Classic service. During an assessment, all communications with your environment are initiated by the Amazon Inspector Classic agent that is installed locally on EC2 instances. The Amazon Inspector Classic service objects that are created, such as assessment targets, assessment templates, and findings generated by the service, are stored in a database managed by and accessible only to Amazon Inspector Classic.

## Amazon Inspector Classic agent limits
<a name="agent-limits"></a>

For information about Amazon Inspector Classic agent limits, see [Amazon Inspector Classic service limits](inspector_limits.md).
