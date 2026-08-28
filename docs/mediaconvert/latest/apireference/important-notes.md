---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/apireference/important-notes.html
---

# Important Notes
<a name="important-notes"></a>

## Using the AWS CLI
<a name="using-the-cli"></a>

When you send requests using the AWS CLI, use PascalCase for all properties. For example, if you used the properties `settings` and `timecodeConfig` in your API call, you must change those to `Settings` and `TimecodeConfig` for your CLI call. This is required because the CLI is built on Python, which uses PascalCase for properties.

## Schemas and Example Job Settings
<a name="about-the-resources-section"></a>

The schemas provided in this guide are not working examples. Instead, they provide information about how to structure your job settings specification. For example job settings in JSON format, see [example job settings](https://docs.aws.amazon.com/mediaconvert/latest/ug/example-job-settings.html) in the *AWS Elemental MediaConvert User Guide*. You pass in job settings as the payload when you create jobs, custom output presets, and custom job templates.

If you access AWS Elemental MediaConvert directly through the API, using theAWS CLI, or using the AWS SDK for Python (Boto), you submit your job settings as a JSON file. The simplest way to generate this file is to set up your job using the [MediaConvert console](https://console.aws.amazon.com/mediaconvert/) and then, on the **Create job** page, choose **Show job JSON**.

If you access AWS Elemental MediaConvert through one of the AWS SDKs other than Python, consult the documentation for those SDKs for information about the syntax to use to for your job settings specification. For more information about using the AWS SDKs to access MediaConvert, see [Getting Started with AWS Elemental MediaConvert Using the AWS SDKs or the AWS CLI](custom-endpoints.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
