---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-f5-big-ip/migrate-partial-configuration.html
---

# Migrating a partial configuration
<a name="migrate-partial-configuration"></a>

When you choose to migrate a partial configuration, you will use either a TMSH or SCF file as your starting point. You will also need to look up the objects that you want to move and compile them in the correct order. The following table outlines the advantages and disadvantages of migrating a partial configuration.

|
|
| Advantages | Disadvantages |
| --- |--- |
| Configurations can be parsed and corrections made as the work progresses. | Knowledge is required of F5 objects and file structures. You must also be able to read iRules. |
| Configuration changes can be batched. | The migration takes time. |
| Easier to troubleshoot configuration load issues. | It can be time-consuming to edit the files or extract the information. |
| Reduced risk of being locked out of the device. |
| Easier to move the configuration to an appropriate topology. |
| Easier to address administrator partitions and route domains because it is a flat file. |
| The flat file structure allows the use of Linux text tools if you want to programmatically find and replace IP addresses. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
