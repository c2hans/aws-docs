---
source_url: https://docs.aws.amazon.com/mediapackage/latest/ug/harvest-jobs.html
---

# Working with harvest jobs
<a name="harvest-jobs"></a>

A harvest job represents a request to extract a live-to-VOD (video on demand) asset from an endpoint for a specific timeframe in the past. AWS Elemental MediaPackage uses information from the harvest job to determine the start and end times of the asset, and where to store it after the harvest job is complete.

A harvest job runs only once after it's been created. MediaPackage keeps a record of the job on your account for reference only. You can't modify or delete a record once you've created the harvest job.

**Topics**
+ [Creating a harvest job](hj-create.md)
+ [Viewing harvest job details](hj-view.md)
+ [Editing a harvest job](hj-edit.md)
+ [Deleting a harvest job](hj-delete.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V1. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
