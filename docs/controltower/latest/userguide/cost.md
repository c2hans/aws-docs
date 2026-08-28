---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/cost.html
---

# Cost
<a name="cost"></a>

The cost for running CfCT depends on the number of AWS CodePipeline runs, the duration of AWS CodeBuild runs, the number and duration of AWS Lambda functions, and the number of Amazon EventBridge events published. For example, if you run 100 builds in one month using **build.general1.small** where each build runs for five minutes, then the approximate cost for running CfCT is **$3.00 per month**. For full details, you can review the pricing webpage for each AWS service you are running.

The Amazon Simple Storage Service (Amazon S3) bucket and AWS CodeCommit Git-based repository resources are retained after you delete the template, to protect your configuration information. Depending on the option you select, you are charged based on the amount of data stored in the Amazon S3 bucket and the number of Git requests (not applicable to Amazon S3 resource). Refer to [Amazon S3](https://aws.amazon.com/s3/pricing/) and [AWS CodeCommit](https://aws.amazon.com/codecommit/pricing/) pricing for details.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
