---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/problem-configuration-file-not-found-issue.html
---

# Problem: Configuration file not found issue
<a name="problem-configuration-file-not-found-issue"></a>

## Resolution
<a name="resolution-config-file-not-found"></a>

When S3 buckets are used for configuration files, you might receive the following error:

 `error | accelerator | ENOENT: no such file or directory, open '/codebuild/output/src437/src/s3/01/accounts-config.yaml'`

Ensure that the configuration zip file uploaded to the S3 config bucket does not contain a top-level directory. Once the zip file has been unzipped, it should contain the solution configuration `yaml` files and other resource policy related folders at the root. Refer to the [Update the configuration files](step-3.-update-the-configuration-files.md) section for more information about the proper structure of the zip archive configuration files.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Landing Zone Accelerator on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
