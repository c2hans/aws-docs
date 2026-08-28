---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws/customization.html
---

# Customization
<a name="customization"></a>

This solution leverages AWS Step Functions, which breaks the workflow into individual steps, making it easier to customize or extend the architecture for your specific video-on-demand needs. For example, you can modify or replace the encoding steps to produce different content sets. You can also add steps to extend support for more complex workflows, including image processing for poster artwork or additional custom data to the metadata file that will then be stored in DynamoDB. The solution originates MediaConvert output content directly from Amazon S3 through CloudFront. You can, however, customize the solution to leverage a dedicated origin server such as MediaPackage.

Each time the workflow is initiated, the solution creates a unique identifier. The unique identifier is used as the primary key in DynamoDB and the run ID in Step Functions. The unique identifier is passed to each step in the workflow, allowing information to be stored and retrieved in DynamoDB. This makes it easier to add and remove steps from the workflow.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Video on Demand on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
