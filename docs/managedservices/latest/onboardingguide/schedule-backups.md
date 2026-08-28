---
source_url: https://docs.aws.amazon.com/managedservices/latest/onboardingguide/schedule-backups.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Scheduling AMS backups at the VPC level
<a name="schedule-backups"></a>

AWS Managed Services (AMS) backup scheduling in the VPC, where the target instances are allocated, is created during account onboarding with a default tag in the VPC creation schema. The backup system schedules the execution of the snapshots depending on that VPC Tag. Modification of the schedule can be made by creating a service request. For more information, see [VPC Tag and Defaults](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/vpc-tag-and-defaults.html).

For backup defaults, see [Understanding AMS Defaults](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/backup-defaults.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
