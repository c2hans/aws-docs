---
source_url: https://docs.aws.amazon.com/glue/latest/dg/creating-azurecosmos-connection.html
---

# Creating a Azure Cosmos DB connection
<a name="creating-azurecosmos-connection"></a>

**Prerequisites**:
+ In Azure, you will need to identify or generate an Azure Cosmos DB Key for use by AWS Glue, `cosmosKey`. For more information, see [Secure access to data in Azure Cosmos DB](https://learn.microsoft.com/en-us/azure/cosmos-db/secure-access-to-data?tabs=using-primary-key) in the Azure documentation.

**To configure a connection to Azure Cosmos DB:**

1. In AWS Secrets Manager, create a secret using your Azure Cosmos DB Key. To create a secret in Secrets Manager, follow the tutorial available in [ Create an AWS Secrets Manager secret ](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html) in the AWS Secrets Manager documentation. After creating the secret, keep the Secret name, {{secretName}} for the next step.
   + When selecting **Key/value pairs**, create a pair for the key `spark.cosmos.accountKey` with the value {{cosmosKey}}.

1. In the AWS Glue console, create a connection by following the steps in [Adding an AWS Glue connection](console-connections.md). After creating the connection, keep the connection name, {{connectionName}}, for future use in AWS Glue.
   + When selecting a **Connection type**, select Azure Cosmos DB.
   + When selecting an **AWS Secret**, provide {{secretName}}.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
