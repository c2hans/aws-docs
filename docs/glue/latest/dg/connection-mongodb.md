---
source_url: https://docs.aws.amazon.com/glue/latest/dg/connection-mongodb.html
---

# Using a MongoDB or MongoDB Atlas connection
<a name="connection-mongodb"></a>

After you create a connection for MongoDB or MongoDB Atlas, you can use the connection in your ETL job. You create a table in the AWS Glue Data Catalog and specify the MongoDB or MongoDB Atlas connection for the `connection` attribute of the table.

AWS Glue stores your connection `url` and credentials in the MongoDB connection. The connection URI formats are as follows:
+ For MongoDB: mongodb://host:port/database. The host can be a hostname, IP address, or UNIX domain socket. If the connection string doesn't specify a port, it uses the default MongoDB port, 27017.
+ For MongoDB Atlas: mongodb\+srv://server.example.com/database. The host can be a hostname that follows corresponds to a DNS SRV record. The SRV format does not require a port and will use the default MongoDB port, 27017.

Additionally, you can specify options in your job script. For more information, see [MongoDB connection option reference](aws-glue-programming-etl-connect-mongodb-home.md#aws-glue-programming-etl-connect-mongodb).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
