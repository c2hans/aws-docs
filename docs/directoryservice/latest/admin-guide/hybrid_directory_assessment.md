---
source_url: https://docs.aws.amazon.com/directoryservice/latest/admin-guide/hybrid_directory_assessment.html
---

# Directory assessments for hybrid directories
<a name="hybrid_directory_assessment"></a>

A directory assessment examines your self-managed Active Directory environment to make sure it meets the requirements for creating a hybrid directory. This assessment verifies network connectivity, domain controller configuration, and required services to help identify and resolve potential issues before establishing a connection between your self-managed AD and Directory Service.

There are two types of directory assessments:
+ *`CUSTOMER` assessments* – Initiated by you in the console when you begin setting up a hybrid directory. You can delete customer directory assessments, even while they're in progress. You can have up to 100 customer assessments.
+ *`SYSTEM` assessments* – Automatically created by AWS and run periodically after successful creation. You can't delete `SYSTEM` assessments.

Directory assessments provide valuable information about your environment's readiness, including:
+ Connectivity between your self-managed AD and AWS
+ Availability of required services on your domain controllers
+ Configuration compatibility with AWS Directory Service requirements
+ Potential issues that might prevent successful hybrid directory creation

A successful (passed) directory assessment is required before you can create a hybrid directory. If an assessment fails, you can view the detailed report to identify and address the issues before trying again. AWS deletes `SYSTEM` assessments after 30 days.

**Topics**
+ [Creating directory assessments](create_directory_assessment.md)
+ [Viewing directory assessments](viewing_hybrid_dir_assessment.md)
+ [Deleting directory assessments](deleting_hybrid_dir_assessment.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Directory Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query directoryservice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
