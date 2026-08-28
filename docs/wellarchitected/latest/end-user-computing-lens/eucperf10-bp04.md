---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf10-bp04.html
---

# EUCPERF10-BP04 Remove caches, temporary data, log files, and unneeded files such as tutorials and sample data before creating an image
<a name="eucperf10-bp04"></a>

 Remove non-required files that are installed, downloaded, or created by applications to optimize storage consumption.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance-26"></a>

 Remove unneeded files from images to optimize storage consumption.

 Unnecessary files included in an Amazon WorkSpaces golden image use space for each WorkSpace provisioned using that image. Similarly, for Amazon WorkSpaces Applications where the image builder volume size is limited, removing unneeded files can provide additional storage space for other applications.

 Consider data access patterns and whether data not included in an image can be downloaded when needed. For example, if 10% of users access an application library that can be downloaded when needed, omit the library from images.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
