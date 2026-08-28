---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.html
---

# Setting up DynamoDB local (downloadable version)
<a name="DynamoDBLocal"></a>

 With the downloadable version of Amazon DynamoDB, you can develop and test applications without accessing the DynamoDB web service. Instead, the database is self-contained on your computer. When you're ready to deploy your application in production, you remove the local endpoint in the code, and then it points to the DynamoDB web service.

 Having this local version helps you save on throughput, data storage, and data transfer fees. In addition, you don't need an internet connection while you develop your application.

 DynamoDB local is available as a [download](DynamoDBLocal.DownloadingAndRunning.md#DynamoDBLocal.DownloadingAndRunning.title) (requires JRE), as an [ Apache Maven dependency](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html#apache-maven), or as a [Docker image](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html#docker).

 If you prefer to use the Amazon DynamoDB web service instead, see [Setting up DynamoDB (web service)](SettingUp.DynamoWebService.md).

**Topics**
+ [Deploying DynamoDB locally on your computer](DynamoDBLocal.DownloadingAndRunning.md)
+ [DynamoDB local usage notes](DynamoDBLocal.UsageNotes.md)
+ [Release history for DynamoDB local](DynamoDBLocalHistory.md)
+ [Telemetry in DynamoDB local](DynamoDBLocalTelemetry.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
