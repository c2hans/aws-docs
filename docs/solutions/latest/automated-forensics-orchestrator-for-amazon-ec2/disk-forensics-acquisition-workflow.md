---
source_url: https://docs.aws.amazon.com/solutions/latest/automated-forensics-orchestrator-for-amazon-ec2/disk-forensics-acquisition-workflow.html
---

# Disk forensics acquisition workflow
<a name="disk-forensics-acquisition-workflow"></a>

 **Disk forensics acquisition workflow**

![disk forensics acquisition workflow](http://docs.aws.amazon.com/solutions/latest/automated-forensics-orchestrator-for-amazon-ec2/images/disk-forensics-acquisition-workflow.png)

The *Forensic triage* Step Function initiates *disk acquisition flow*. . The *Perform Instance Snapshot* Lambda function performs an instance snapshot. . The *Perform Instance Snapshot* Lambda function assumes a role in the application account and initiates an instance snapshot API call. . *Check for Instance Snapshot* Lambda function assumes a role in the application account and checks for snapshot completion. . If the response is `Pending` or `In Progress` it waits for 120 seconds. . The disk acquisition flow [copies](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-copy-snapshot.html) the compromised instance snapshot using AWS KMS keys shared with the forensic account. . After the copy snapshot operation of the compromised instance, the disk acquisition flow [shares](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modifying-snapshot-permissions.html) the copied EBS snapshot with the forensic account. . To keep the copy of snapshot in the forensic account, copy the shared copy of compromised instance snapshot using Forensic KMS keys. This step allows protection of the shared snapshot with a local copy to perform forensics in case of the AWS account being compromised, or the shared snapshot being deleted by the security team. . Post copy flow the step functions initiates the investigation flow with forensic type as `DISK`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Automated Forensics Orchestrator for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
