---
source_url: https://docs.aws.amazon.com/guardduty/latest/ug/compromised-ec2-recoverypoint.html
---

# Remediating a potentially compromised EC2 Recovery Point
<a name="compromised-ec2-recoverypoint"></a>

When GuardDuty generates an Execution:EC2/MaliciousFile\!RecoveryPoint finding type, it indicates that malware has been detected in an EC2 Recovery Point Backup resource. Perform the following steps to remediate the potentially compromised recovery point:

1. **Identify the potentially compromised EC2 Recovery Point**

   1. A GuardDuty finding for EC2 Recovery Point will list its Amazon Resource Name (ARN), and associated malware scan details in the finding details:

      ```
      aws backup describe-recovery-point --backup-vault-name {{021345abcdef6789}} --recovery-point-arn "{{arn:aws:backup:us-east-1:111122223333:recovery-point:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}"
      ```

   1. Review recovery details to look for source image:

      ```
      aws backup get-recovery-point-restore-metadata --backup-vault-name {{021345abcdef6789}} --recovery-point-arn "{{arn:aws:backup:us-east-1:111122223333:recovery-point:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}"
      ```

1. **Restrict access to the compromised resources**
   + Review and modify backup vault access policies to restrict recovery point access and suspend any automated restore jobs that might use this recovery point. If your environment uses resource tagging, tag the recovery point appropriately to indicate it's under investigation and consider pausing scheduled backups if necessary.

     Example:

     {{aws backup tag-resource -—resource-arn arn:aws:backup:us-east-1:111122223333:recovery-point:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 -—tags Investigation=Malware,DoNotDelete=True}}

1. **Take remediation action**
   + Before proceeding with deletion, ensure you have identified all dependencies and have proper backups if needed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
