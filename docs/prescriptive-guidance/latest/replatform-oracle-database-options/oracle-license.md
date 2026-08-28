---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/replatform-oracle-database-options/oracle-license.html
---

# Oracle license
<a name="oracle-license"></a>

On AWS, there are two licensing models for running Oracle databases:
+ Bring Your Own License (BYOL)
+ License Included

Under the BYOL model, you can use your existing on-premises Oracle Database licenses on AWS. To run a DB instance under the BYOL model, you must have the appropriate licenses for software and support. Under this model, you continue to use your active Oracle Support account, and you contact Oracle Support directly for Oracle database-specific service requests. If you have an active AWS Support account, you can contact AWS Support for issues with infrastructure, such as operating system, storage, network, and hardware.

In the License Included model, you don't need to purchase Oracle licenses separately. The Oracle database software has been licensed by AWS. In this model, AWS Support, if purchased and active, can be contacted for both Amazon RDS service requests and Oracle Database‒specific service requests.

Another advantage of the License Included model is that cost is incurred only for the hours that the database is running. This is especially cost-effective for non-production environments where databases don't need to run all day, every day.

The License Included model is supported only on Amazon RDS for Oracle Database SE2. It isn't available on Amazon RDS Custom for Oracle.

|
|
| License model | Amazon RDS for Oracle | Amazon RDS Custom for Oracle |
| --- |--- |--- |
| Bring Your Own License | Yes | Yes |
| License Included (SE2 only) | Yes | No |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
