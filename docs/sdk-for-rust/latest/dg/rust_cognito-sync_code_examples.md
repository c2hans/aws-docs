---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/rust_cognito-sync_code_examples.html
---

# Amazon Cognito Sync examples using SDK for Rust
<a name="rust_cognito-sync_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Rust with Amazon Cognito Sync.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `ListIdentityPoolUsage`
<a name="cognito-sync_ListIdentityPoolUsage_rust_topic"></a>

The following code example shows how to use `ListIdentityPoolUsage`.

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/cognitosync#code-examples).

```
async fn show_pools(client: &Client) -> Result<(), Error> {
    let response = client
        .list_identity_pool_usage()
        .max_results(10)
        .send()
        .await?;

    let pools = response.identity_pool_usages();
    println!("Identity pools:");

    for pool in pools {
        println!(
            "  Identity pool ID:    {}",
            pool.identity_pool_id().unwrap_or_default()
        );
        println!(
            "  Data storage:        {}",
            pool.data_storage().unwrap_or_default()
        );
        println!(
            "  Sync sessions count: {}",
            pool.sync_sessions_count().unwrap_or_default()
        );
        println!(
            "  Last modified:       {}",
            pool.last_modified_date().unwrap().to_chrono_utc()?
        );
        println!();
    }

    println!("Next token: {}", response.next_token().unwrap_or_default());

    Ok(())
}
```
+  For API details, see [ListIdentityPoolUsage](https://docs.rs/aws-sdk-cognitosync/latest/aws_sdk_cognitosync/client/struct.Client.html#method.list_identity_pool_usage) in *AWS SDK for Rust API reference*.
