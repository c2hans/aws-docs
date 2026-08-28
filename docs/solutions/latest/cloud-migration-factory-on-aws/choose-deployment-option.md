---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/choose-deployment-option.html
---

# Step 1: Choose your deployment option
<a name="choose-deployment-option"></a>

There are three options for deployment of the initial stack and choosing the correct one depends on the security policies for the target environment.

These options are:
+ Public (default): All Cloud Migration Factory on AWS endpoints are publicly addressable with user authentication. This option deploys the following entry points: CloudFront, Public API Gateway Endpoints, and Cognito.
+ Public with AWS WAF: Access to Cloud Migration Factory endpoints is restricted to customizable CIDR ranges. This option deploys the following entry points: CloudFront, Public API Gateway Endpoints, Cognito, and AWS WAF restricting access to specific CIDR ranges.
+ Private: All Cloud Migration Factory endpoints are accessible only from your VPC networks and the Cloud Migration Factory on AWS web console must be hosted on a private web server deployed separately. This option deploys the following entry points: [Private API Gateway Endpoints](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-apis.html) (accessible within a VPC only) and Cognito.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Cloud Migration Factory on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
