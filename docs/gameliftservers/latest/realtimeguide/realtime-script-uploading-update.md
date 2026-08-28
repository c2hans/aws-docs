---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/realtimeguide/realtime-script-uploading-update.html
---

# Update an Amazon GameLift Servers Realtime script
<a name="realtime-script-uploading-update"></a>

You can update the metadata for a script resource using either the Amazon GameLift Servers console or the [`update-script`](https://docs.aws.amazon.com/cli/latest/reference/gamelift/update-script.html) AWS CLI command.

You can also update the script content for a script resource. Amazon GameLift Servers deploys script content to all fleet instances that use the updated script resource. When the updated script is deployed, instances use it when starting new game sessions. Game sessions that are already running at the time of the update don't use the updated script.

**To update script files**
+ For script files stored locally, to upload the updated script .zip file, use either the Amazon GameLift Servers console or the **update-script** command.
+ For script files stored in an Amazon S3 bucket, upload the updated script files to the S3 bucket. Amazon GameLift Servers periodically checks for updated script files and retrieves them directly from the S3 bucket.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
