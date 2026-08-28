---
source_url: https://docs.aws.amazon.com/agentworkspace/latest/devguide/getting-started-test-with-deployed-app.html
---

# Test a deployed version of your application for Connect Customer agent workspace
<a name="getting-started-test-with-deployed-app"></a>

When ready, deploy the app that you created for the Connect Customer agent workspace to a place that is internet accessible. Update your application configuration (or configure a new application) to point to the deployed version of your application. A simple way to deploy your app assuming it only has static assets is to [host them on S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html) and (optionally) [use CloudFront](https://aws.amazon.com/blogs/networking-and-content-delivery/amazon-s3-amazon-cloudfront-a-match-made-in-the-cloud/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer Agent Workspace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query agentworkspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
