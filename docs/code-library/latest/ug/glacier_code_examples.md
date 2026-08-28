---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/glacier_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Code examples for Amazon Glacier using AWS SDKs
<a name="glacier_code_examples"></a>

The following code examples show you how to use Amazon Glacier with an AWS software development kit (SDK).

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

**More resources**
+  **[ Amazon Glacier Developer Guide](https://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html)** – More information about Amazon Glacier.
+ **[Amazon Glacier API Reference](https://docs.aws.amazon.com/amazonglacier/latest/dev/amazon-glacier-api.html)** – Details about all available Amazon Glacier actions.
+ **[AWS Developer Center](https://aws.amazon.com/developer/code-examples/?awsf.sdk-code-examples-product=product%23glacier)** – Code examples that you can filter by category or full-text search.
+ **[AWS SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples)** – GitHub repo with complete code in preferred languages. Includes instructions for setting up and running the code.

**Contents**
+ [Basics](glacier_code_examples_basics.md)
  + [Hello Amazon Glacier](glacier_example_glacier_Hello_section.md)
  + [Actions](glacier_code_examples_actions.md)
    + [`AddTagsToVault`](glacier_example_glacier_AddTagsToVault_section.md)
    + [`CreateVault`](glacier_example_glacier_CreateVault_section.md)
    + [`DeleteArchive`](glacier_example_glacier_DeleteArchive_section.md)
    + [`DeleteVault`](glacier_example_glacier_DeleteVault_section.md)
    + [`DeleteVaultNotifications`](glacier_example_glacier_DeleteVaultNotifications_section.md)
    + [`DescribeJob`](glacier_example_glacier_DescribeJob_section.md)
    + [`DescribeVault`](glacier_example_glacier_DescribeVault_section.md)
    + [`GetJobOutput`](glacier_example_glacier_GetJobOutput_section.md)
    + [`GetVaultNotifications`](glacier_example_glacier_GetVaultNotifications_section.md)
    + [`InitiateJob`](glacier_example_glacier_InitiateJob_section.md)
    + [`ListJobs`](glacier_example_glacier_ListJobs_section.md)
    + [`ListTagsForVault`](glacier_example_glacier_ListTagsForVault_section.md)
    + [`ListVaults`](glacier_example_glacier_ListVaults_section.md)
    + [`SetVaultNotifications`](glacier_example_glacier_SetVaultNotifications_section.md)
    + [`UploadArchive`](glacier_example_glacier_UploadArchive_section.md)
    + [`UploadMultipartPart`](glacier_example_glacier_UploadMultipartPart_section.md)
+ [Scenarios](glacier_code_examples_scenarios.md)
  + [Archive a file, get notifications, and initiate a job](glacier_example_glacier_Usage_UploadNotifyInitiate_section.md)
  + [Get archive content and delete the archive](glacier_example_glacier_Usage_RetrieveDelete_section.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
