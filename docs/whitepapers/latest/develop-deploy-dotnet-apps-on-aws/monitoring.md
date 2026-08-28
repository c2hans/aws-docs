---
source_url: https://docs.aws.amazon.com/whitepapers/latest/develop-deploy-dotnet-apps-on-aws/monitoring.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Monitoring
<a name="monitoring"></a>

Successful DevOps requires excellent communication between the development of new application capabilities and their subsequent operation. One of the key benefits over other approaches is that it shortens the feedback loop between development and operations.

Although structuring teams to include development and operations improves human communication, running modern and distributed systems is complicated, and it is critical that the team has a good understanding of the current state and the performance of the system components, the interactivity between components, as well as the historic view of the system’s behavior.

Designing a suitable approach to monitor .NET application behavior is relatively simple but requires a combination of approaches. Approaches include logging events and errors from your application and AWS resources, recording metrics, showing current status dashboards, sending and automating responses to alerts, and providing tracing to help isolate problems.

While the traditional .NET monitoring approaches and third-party libraries still work in AWS, implementing a modern, approach generally requires introducing one or more additional AWS services or third-party tools. Although it’s not necessary to use all these tools, mature DevOps teams invariably use a multi-layered approach to monitor the system, track performance, and provide alerts when notable or exceptional events occur.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
