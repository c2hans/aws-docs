---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/operational-dashboard.html
---

# Operational Dashboard
<a name="operational-dashboard"></a>

The solution will deploy a Cloudwatch Dashboard for Solution Observability by default. This dashboard allows you to see the following information about your Dynamic Image Transformation for Amazon CloudFront deployment:

1. Lambda Errors

1. Lambda Duration

1. Lambda Invocations

1. CloudFront Requests

1. CloudFront Bytes Downloaded

1. Cache Hit Rate (% of requests to CloudFront which were returned from the cache)

1. Average Image Size

1. Estimated Cost (Based on us-east-1 pricing with a default deployment, doesn’t include cost of observability)

Unless the dashboard is included in your AWS Free Tier, it will add a cost of $3 per month to your Dynamic Image Transformation for Amazon CloudFront deployment. To prevent the inclusion of the dashboard in your deployment, in combination with the instructions in , change the value under `DeployCloudWatchDashboard` from "Yes", to "No".

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
