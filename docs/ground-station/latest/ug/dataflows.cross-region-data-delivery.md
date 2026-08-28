---
source_url: https://docs.aws.amazon.com/ground-station/latest/ug/dataflows.cross-region-data-delivery.html
---

# Use cross-region data delivery
<a name="dataflows.cross-region-data-delivery"></a>

 The AWS Ground Station cross-region data delivery feature gives you the flexibility to send your data from an antenna to any AWS Ground Station supported AWS Region. This means you can maintain your infrastructure in a single AWS Region and schedule contacts on any [AWS Ground Station Locations](aws-ground-station-antenna-locations.md) you are onboarded to.

 When receiving your contact data in an Amazon S3 Bucket, AWS Ground Station will manage all delivery aspects for you.

 To use cross-region data delivery to an Amazon EC2 instance (using either the AWS Ground Station Agent or a dataflow endpoint), the *dataflow-endpoint* must be created in your current AWS Region and your *dataflow-endpoint-config* must specify the same region. AWS Ground Station will manage delivering the data cross-region for you.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Ground Station. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ground-station` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
