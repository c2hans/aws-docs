---
source_url: https://docs.aws.amazon.com/whitepapers/latest/develop-deploy-dotnet-apps-on-aws/amazon-cloudwatch-application-insights-for-.net-and-sql-server.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Amazon CloudWatch Application Insights for .NET and SQL Server
<a name="amazon-cloudwatch-application-insights-for-.net-and-sql-server"></a>

Whereas CloudWatch gives you a rich set of tools to customize your approach to monitoring, [Amazon CloudWatch Application Insights for .NET and SQL Server](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.html) enables application owners to easily monitor their application stack. It automatically sets up and analyses important metrics and logs from across their application resources in real time, and uses machine learning techniques to discover anomalies and errors. CloudWatch Application Insights for .NET and SQL Server creates automated dashboards for detected problems, helping application owners troubleshoot faster and reduce the mean time to resolution (MTTR) for their application issues and improve Service Level Agreements (SLAs).
+  **Automatically recognized application metrics and logs** — CloudWatch Application Insights for .NET and SQL Server scans your application resources and provides a list of recommended metrics and logs to monitor, and sets them up automatically, reducing your effort spent in setting up monitoring for your applications.
+  **Intelligent problem detection** — CloudWatch Application Insights for .NET and SQL Server uses prebuilt rules and machine learning algorithms to dynamically monitor and analyze symptoms of a problem across your application stack and detect application problems. It helps you reduce the overhead of dealing with individual metric spikes, or events, or log exceptions, and instead get notified on real problems, along with contextual information about these problems.
+  **Faster troubleshooting** — CloudWatch Application Insights for .NET and SQL Server assesses the detected problems to give you insights on them, such as the possible root cause of the detected problem and list of metrics and logs impacted because of the problem. You can provide feedback on generated insights to make the problem detection engine specific to your use case.

For example, consider you have an ASP .NET application backed by a SQL Server database, and your database starts malfunctioning due to high memory pressure, leading to HTTP 500 errors in your application server. Previously, to identify the problem and triage, you would have to go through your metrics dashboards, sift through server, application error and database logs, and possibly use third-party tools.

With CloudWatch Application Insights for .NET and SQL Server and its intelligent analytics, you can find the layer (SQL database, in this case) in your application stack causing the problem just by looking at the dynamically created dashboard of the related metrics anomalies, and log file snippets. This significantly reduces alert fatigue and the time and effort required to troubleshoot and return your application to a healthy state.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
