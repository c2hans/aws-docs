---
source_url: https://docs.aws.amazon.com/guardduty/latest/ug/compromised-ami.html
---

# Remediating a potentially compromised EC2 AMI
<a name="compromised-ami"></a>

When GuardDuty generates an Execution:EC2/MaliciousFile\!AMI finding type, it indicates that malware has been detected in an Amazon Machine Image (AMI). Perform the following steps to remediate the potentially compromised AMI:

1. **Identify the potentially compromised AMI**

   1. A GuardDuty finding for AMIs will list the affected AMI ID, its Amazon Resource Name (ARN), and associated malware scan details in the finding details.

   1. Review AMI source image:

      ```
      aws ec2 describe-images --image-ids {{ami-021345abcdef6789}}
      ```

1. **Restrict access to the compromised resources**

   1. Review and modify backup vault access policies to restrict recovery point access and suspend any automated restore jobs that might use this recovery point.

   1. Remove Permissions from source AMI permissions

      First view existing permissions:

      ```
      aws ec2 describe-image-attribute --image-id {{ami-abcdef01234567890}} --attribute launchPermission
      ```

      Then remove individual permissions:

      ```
      aws ec2 modify-image-attribute --image-id {{ami-abcdef01234567890}} --launch-permission '{"Remove":[{"UserId":"{{111122223333}}"}]}'
      ```

      For additional CLI options, see [Share an AMI with specific accounts - Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharingamis-explicit.html#unsharing-an-ami)

   1. If source is an EC2 Instance see: [Remediating a potentially compromised Amazon EC2 instance](https://docs.aws.amazon.com/guardduty/latest/ug/compromised-ec2.html).

1. **Take remediation action**
   + Before proceeding with deletion, ensure you have identified all dependencies and have proper backups if needed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
