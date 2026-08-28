---
source_url: https://docs.aws.amazon.com/fsx/latest/LustreGuide/rename-directory-time.html
---

# Renaming directories takes a long time
<a name="rename-directory-time"></a>

**Question**

I renamed a directory on a file system linked to an Amazon S3 bucket and have automatic export enabled. Why are the files inside this directory taking a long time to get renamed on the S3 bucket?

**Answer**

When you rename a directory on the file system, FSx for Lustre creates new S3 objects for all of the files and directories inside the directory that was renamed. The amount of time it takes to propagate the directory rename to S3 is directly correlated to the quantity of files and directories that are descendants of the directory being renamed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
