---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_rds-data_code_examples.html
---

# Amazon RDS Data Service examples using SDK for Rust
<a name="rust_rds-data_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Rust with Amazon RDS Data Service.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `ExecuteStatement`
<a name="rds-data_ExecuteStatement_rust_topic"></a>

The following code example shows how to use `ExecuteStatement`.

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
