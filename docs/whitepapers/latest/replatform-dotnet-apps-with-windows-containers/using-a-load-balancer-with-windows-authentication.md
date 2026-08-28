---
source_url: https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/using-a-load-balancer-with-windows-authentication.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Using a load balancer with Windows Authentication
<a name="using-a-load-balancer-with-windows-authentication"></a>

 A typical architecture for a containerized ASP.NET application would involve ELB. A load balancer automatically distributes incoming traffic across multiple targets such as EC2 instances, containers, and IP addresses, in one or more Availability Zones. Windows Authentication requires that the source port be preserved in the connection from the client to the server. A Network Load Balancer with a TCP listener will preserve the source port for a load balanced connection. For that reason, use a Network Load Balancer when using Windows Authentication.

 This section covered how to enable users to sign in using their Active Directory domain credentials, and how your applications can also utilize Active Directory service accounts to connect to network resources, such as SQL Server databases. When running containers, you also must consider access control to AWS resources that may occur during container related lifecycle activities. IAM helps you securely control access granted to Amazon ECS, Amazon ECS container agent, and your application during these events.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
