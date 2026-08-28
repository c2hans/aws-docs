---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws/processing-step-functions.html
---

# Processing Step Functions
<a name="processing-step-functions"></a>

The solution uses the height and width of the source video to determine which job template to use to submit encoding jobs to MediaConvert. If you allow frame capture, the frame capture parameters are added to the job template. Then, the encoding job is created in MediaConvert and the details are stored in DynamoDB.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Video on Demand on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
