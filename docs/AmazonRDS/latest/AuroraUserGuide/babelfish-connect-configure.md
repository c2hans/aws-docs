---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-connect-configure.html
---

# Creating C\# or JDBC client connections to Babelfish
<a name="babelfish-connect-configure"></a>

In the following you can find some examples of using C\# and JDBC classes to connect to an Babelfish for Aurora PostgreSQL.

**Example : Using C\# code to connect to a DB cluster**

```
string dataSource = 'babelfishServer_11_24';

//Create connection
connectionString = @"Data Source=" + dataSource
    +";Initial Catalog={{your-DB-name}}"
    +";User ID={{user-id}};Password={{password}}";

// [optional] To validate server certificate during TLS/SSL connection
connectionString = connectionString + ";ServerCertificate=/path/to/certificate.pem";

SqlConnection cnn = new SqlConnection(connectionString);
cnn.Open();
```

**Example : Using generic JDBC API classes and interfaces to connect to a DB cluster**

```
String dbServer =
   "database-babelfish.cluster-123abc456def.us-east-1-rds.amazonaws.com";
String connectionUrl = "jdbc:sqlserver://" + dbServer + ":1433;" +
    "databaseName={{your-DB-name}};user={{user-id}};password={{password}}";

// [optional] To validate server certificate during TLS/SSL connection
connectionUrl = connectionUrl + ";serverCertificate=/path/to/certificate.pem";

// Load the SQL Server JDBC driver and establish the connection.
System.out.print("Connecting Babelfish Server ... ");
Connection cnn = DriverManager.getConnection(connectionUrl);
```

**Example : Using SQL Server-specific JDBC classes and interfaces to connect to a DB cluster**

```
// Create datasource.
SQLServerDataSource ds = new SQLServerDataSource();
ds.setUser("{{user-id}}");
ds.setPassword("{{password}}");
String babelfishServer =
   "database-babelfish.cluster-123abc456def.us-east-1-rds.amazonaws.com";

ds.setServerName(babelfishServer);
ds.setPortNumber(1433);
ds.setDatabaseName("{{your-DB-name}}");

// [optional] To validate server certificate during TLS/SSL connection
ds.setServerCertificate("/path/to/certificate.pem");

Connection con = ds.getConnection();
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
