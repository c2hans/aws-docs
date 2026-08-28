---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/operations.html
---

# Operations
<a name="operations"></a>

 AWS enables visibility into your streaming workload at all layers through log collection and monitoring features. Data on use of services, resources, application programming interfaces (APIs), network flow logs, and system traces can be collected using **Amazon CloudWatch**, **AWS CloudTrail**, **VPC Flow Logs**, and **AWS X-Ray**. Equipped with this data, you can design automated failure and remediation systems at each stage in your video application – ingest, processing, origin, delivery, and client-side.

 For live streaming, expressing the component relationships and tracing the signal path is important for operators who need to identify and respond to issues that arise. Visual documentation or interactive dashboards that reflect the real-time status of the workflow will improve awareness and shorten time to issue resolution. Consider using or building your own tools like the [Media Services Application Mapper](https://aws.amazon.com/solutions/implementations/media-services-application-mapper/) to model your workload and better inform operations.

 One unique property of media streaming is that while every component in the workload can be operating as expected, the resulting audio or video might not be the intended content. Consider placing video decoder probes throughout your live stream signal path to emit thumbnail images or low bitrate proxy media to monitoring systems. This will ensure that the correct content is being transmitted and improve operational observability for troubleshooting.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
