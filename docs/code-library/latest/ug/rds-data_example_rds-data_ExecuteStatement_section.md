---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/rds-data_example_rds-data_ExecuteStatement_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ExecuteStatement` with an AWS SDK or CLI
<a name="rds-data_example_rds-data_ExecuteStatement_section"></a>

The following code examples show how to use `ExecuteStatement`.

------
#### [ CLI ]

**AWS CLI**
**Example 1: To execute a SQL statement that is part of a transaction**
The following `execute-statement` example runs a SQL statement that is part of a transaction.

```
aws rds-data execute-statement \
    --resource-arn {{"arn:aws:rds:us-west-2:123456789012:cluster:mydbcluster"}} \
    --database {{"mydb"}} \
    --secret-arn {{"arn:aws:secretsmanager:us-west-2:123456789012:secret:mysecret"}} \
    --sql {{"update mytable set quantity=5 where id=201"}} \
    --transaction-id {{"ABC1234567890xyz"}}
```
Output:

```
{
    "numberOfRecordsUpdated": 1
}
```
**Example 2: To execute a SQL statement with parameters**
The following `execute-statement` example runs a SQL statement with parameters.

```
aws rds-data execute-statement \
    --resource-arn {{"arn:aws:rds:us-east-1:123456789012:cluster:mydbcluster"}} \
    --database {{"mydb"}} \
    --secret-arn {{"arn:aws:secretsmanager:us-east-1:123456789012:secret:mysecret"}} \
    --sql {{"insert into mytable values (:id, :val)"}} \
    --parameters "[{\"name\": \"id\", \"value\": {\"longValue\": 1}},{\"name\": \"val\", \"value\": {\"stringValue\": \"value1\"}}]"
```
Output:

```
{
    "numberOfRecordsUpdated": 1
}
```
For more information, see [Using the Data API for Aurora Serverless](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html) in the *Amazon RDS User Guide*.
+  For API details, see [ExecuteStatement](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds-data/execute-statement.html) in *AWS CLI Command Reference*.

------
#### [ Rust ]

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/rdsdata#code-examples).

```
async fn query_cluster(
    client: &Client,
    cluster_arn: &str,
    query: &str,
    secret_arn: &str,
) -> Result<(), Error> {
    let st = client
        .execute_statement()
        .resource_arn(cluster_arn)
        .database("postgres") // Do not confuse this with db instance name
        .sql(query)
        .secret_arn(secret_arn);

    let result = st.send().await?;

    println!("{:?}", result);
    println!();

    Ok(())
}
```
+  For API details, see [ExecuteStatement](https://docs.rs/aws-sdk-rdsdata/latest/aws_sdk_rdsdata/client/struct.Client.html#method.execute_statement) in *AWS SDK for Rust API reference*.

------
