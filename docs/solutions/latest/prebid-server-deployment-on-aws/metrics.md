---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/metrics.html
---

# Metrics
<a name="metrics"></a>

This solution currently writes Prebid Server metrics log data to the mounted EFS, which is shared across containers, and ingests and archives the data using a variety of data management tools continuously or as a batch process. The patch file registers a new logger stream to periodically write metrics data from Prebid Server to files using the standard Java logging mechanism.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Deploying a Prebid Server on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
