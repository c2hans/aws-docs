---
source_url: https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/configuring-s3-storage.html
---

# Default S3 storage
<a name="configuring-s3-storage"></a>

Every project in Amazon SageMaker Unified Studio includes S3 shared storage by default. No additional configuration is required to use this storage option.

## Access model
<a name="s3-access-model"></a>

All project members have read, write, update, and delete access to the S3 shared storage area. This storage operates on a last-write-wins principle. When multiple team members modify the same file, the most recent save overwrites previous versions.

## Enabling S3 bucket versioning
<a name="s3-versioning"></a>

Administrators can turn on S3 bucket versioning from the Amazon S3 console under Account settings. Enabling versioning allows you to preserve, retrieve, and restore previous versions of files stored in the shared storage area.

## Next steps
<a name="s3-next-steps"></a>

To make repositories available to project members, configure a Git connection. For more information, see [Git connections](git-connections.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker Unified Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker-unified-studio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
