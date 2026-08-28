---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws/solution-updates.html
---

# Solution updates
<a name="solution-updates"></a>

To continue using this solution with the latest features and improvements, you must deploy the latest version of this stack. For information about updating your stack, refer to [Update the solution](update-the-solution.md).

Installing version 6.1.4 creates three new MediaConvert job templates that only output HLS renditions to reduce cost, without the use of presets. For more information, refer to [MediaConvert templates](mediaconvert-templates.md). Updating an existing solution deployment to version 6.1.4 creates these new templates without deleting the presets or templates created by the older versions. To use an older template with the latest version of the solution, specify the template using the **JobTemplate** field in your metadata file. For more information, refer to [Metadata file](metadata-file.md). Or, you can replace the default templates in the `Input Validate` AWS Lambda function by modifying the `MediaConvert_Template_` {{<resolution>}} environment variables.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Video on Demand on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
