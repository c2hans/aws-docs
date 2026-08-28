---
source_url: https://docs.aws.amazon.com/glue/latest/dg/creating-azurecosmos-source-node.html
---

# Creating a Azure Cosmos DB source node
<a name="creating-azurecosmos-source-node"></a>

## Prerequisites needed
<a name="creating-azurecosmos-source-node-prerequisites"></a>
+ A AWS Glue Azure Cosmos DB connection, configured with an AWS Secrets Manager secret, as described in the previous section, [Creating a Azure Cosmos DB connection](creating-azurecosmos-connection.md).
+ Appropriate permissions on your job to read the secret used by the connection.
+ A Azure Cosmos DB for NoSQL container you would like to read from. You will need identification information for the container.

  An Azure Cosmos for NoSQL container is identified by its database and container. You must provide the database, {{cosmosDBName}}, and container, {{cosmosContainerName}}, names when connecting to the Azure Cosmos for NoSQL API.

## Adding a Azure Cosmos DB data source
<a name="creating-azurecosmos-source-node-add"></a>

**To add a **Data source – Azure Cosmos DB** node:**

1.  Choose the connection for your Azure Cosmos DB data source. Since you have created it, it should be available in the dropdown. If you need to create a connection, choose **Create Azure Cosmos DB connection**. For more information see the previous section, [Creating a Azure Cosmos DB connection](creating-azurecosmos-connection.md).

    Once you have chosen a connection, you can view the connection properties by clicking **View properties**.

1. Choose **Cosmos DB Database Name** – provide the name of the database you want to read from, {{cosmosDBName}}.

1. Choose **Azure Cosmos DB Container** – provide the name of the container you want to read from, {{cosmosContainerName}}.

1. Optionally, choose **Azure Cosmos DB Custom Query** – provide a SQL SELECT query to retrieve specific information from Azure Cosmos DB.

1.  In **Custom Azure Cosmos properties**, enter parameters and values as needed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
