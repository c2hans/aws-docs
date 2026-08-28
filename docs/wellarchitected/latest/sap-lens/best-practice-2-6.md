---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-2-6.html
---

# Best Practice 2.6 – Make frequent, small, and reversible changes
<a name="best-practice-2-6"></a>

Frequent, small, and reversible changes reduce the scope and impact of a change. Although many SAP NetWeaver solutions only support a “patch forward” approach, consider using feature toggles in custom development to allow rollback. This eases troubleshooting, enables faster remediation, and provides the option to roll back a change.

 **Suggestion 2.6.1 - Divide development and releases into frequent and smaller changes where possible**

 **Suggestion 2.6.2 - Because many SAP solutions only support a “patch forward” approach (and do not allow reversible transports), consider using feature toggles in custom development to allow disablement of features rather than rollback/withdraw**

 **Suggestion 2.6.3 - For non-reversible SAP changes, consider additional rollback options, such as whole system snapshots, database backup, and restore options**
+ AWS Blog: [Amazon EBS crash-consistent snapshots](https://aws.amazon.com/blogs/storage/taking-crash-consistent-snapshots-across-multiple-amazon-ebs-volumes-on-an-amazon-ec2-instance/)
+ AWS Documentation: [Restoring to a specified time using Point-In-Time Recovery (PITR)](https://docs.aws.amazon.com/aws-backup/latest/devguide/point-in-time-recovery.html)
+ AWS Documentation: [AWS Backint for SAP HANA](https://aws.amazon.com/backint-agent/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
