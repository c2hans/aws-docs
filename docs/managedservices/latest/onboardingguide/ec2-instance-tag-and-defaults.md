---
source_url: https://docs.aws.amazon.com/managedservices/latest/onboardingguide/ec2-instance-tag-and-defaults.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# EC2 instance tag and defaults
<a name="ec2-instance-tag-and-defaults"></a>

The **EC2 stack backup tag** specifies whether the stack requires a snapshot of the attached EBS volumes or not.

Tag` Key: Backup`

Tag` Value: True, False`

By default, the value is `False` the backup tag is not present, and the stack does not have scheduled backups.

Change the tag `Key: Backup` to `Value: True` to enable backups, which are then done on the schedule set with the VPC backup tag.

**Note**
The casing for the tag value (Value only) is insensitive, so True/true or False/false are all acceptable.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
