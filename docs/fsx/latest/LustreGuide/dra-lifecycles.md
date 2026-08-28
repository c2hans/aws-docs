---
source_url: https://docs.aws.amazon.com/fsx/latest/LustreGuide/dra-lifecycles.html
---

# Data repository association lifecycle state
<a name="dra-lifecycles"></a>

The data repository association lifecycle state provides status information about a specific DRA. A data repository association can have the following **Lifecycle states**:
+ **Creating** – Amazon FSx is creating the data repository association between the file system and the linked data repository. The data repository is unavailable.
+ **Available** – The data repository association is available for use.
+ **Updating** – The data repository association is undergoing a customer initiated update that might affect its availability.
+ **Deleting** – The data repository association is undergoing a customer initiated deletion.
+ **Misconfigured** – Amazon FSx cannot automatically import updates from the S3 bucket or automatically export updates to the S3 bucket until the data repository association configuration is corrected.

  A DRA can become **Misconfigured** due to the following:
  + Amazon FSx lacks necessary IAM permissions to access the S3 bucket.
  + The FSx event notification configuration on the S3 bucket is deleted or modified.
  + The S3 bucket has existing event notifications that overlap with FSx event types.

  After resolving the underlying issue, the DRA automatically returns to the **Available** state within 15 minutes, or you can immediately trigger the state change using the AWS CLI command [update-data-repository-association](https://docs.aws.amazon.com/cli/latest/reference/fsx/update-data-repository-association.html).
+ **Failed** – The data repository association is in a terminal state that cannot be recovered (for example, because its file system path is deleted or the S3 bucket is deleted).

 You can view a data repository association’s lifecycle state using the Amazon FSx console, the AWS Command Line Interface, and the Amazon FSx API. For more information, see [Viewing data repository association details](view-dra-details.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
