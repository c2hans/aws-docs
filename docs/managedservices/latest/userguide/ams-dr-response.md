---
source_url: https://docs.aws.amazon.com/managedservices/latest/userguide/ams-dr-response.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Disaster recovery response
<a name="ams-dr-response"></a>

In addition to the options described in the following sections, it is good for you to know what steps to take to initiate a disaster recovery (DR) with AMS.

If you experience a disaster and need to initiate a recovery, follow these general guidelines:

1. Open a **High** priority incident with the **Availability** category. AMS will open a conference bridge and invite your team to join.

1. Know the list of resources you need to recover.

1. Know the target landing zone (LZ) you need to recover to (for example, the same account, different AZ or different account and different region).

1. Submit recover requests for each resource in the target landing zone. Follow your existing DR plan or see the options in the following section (for example, [Disaster protection for EC2 with EBS snapshots on AMS](ams-disaster-recovery.md#ams-dr-ebs-snapshots), or [Disaster protection for EC2 with Elastic Disaster Recovery on AMS](ams-disaster-recovery.md#ams-dr-ebs-snapshots-ce)).

1. Restore the application functionality and use AMS assistance to troubleshoot infrastructure-related issues.

AMS can help you with preparing for this event and with creating a DR plan for your organization to cover these questions. For more details, contact your cloud service delivery manager (CSDM) or cloud architect (CA).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
