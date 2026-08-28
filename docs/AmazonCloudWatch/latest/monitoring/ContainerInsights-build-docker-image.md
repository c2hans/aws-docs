---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights-build-docker-image.html
---

# Building your own CloudWatch agent Docker image
<a name="ContainerInsights-build-docker-image"></a>

You can build your own CloudWatch agent Docker image by referring to the Dockerfile located at [ https://github.com/aws-samples/amazon-cloudwatch-container-insights/blob/latest/cloudwatch-agent-dockerfile/Dockerfile](https://github.com/aws-samples/amazon-cloudwatch-container-insights/blob/latest/cloudwatch-agent-dockerfile/Dockerfile).

The Dockerfile supports building multi-architecture images directly using `docker buildx`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
