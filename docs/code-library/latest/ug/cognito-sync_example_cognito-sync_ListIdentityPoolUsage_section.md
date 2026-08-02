---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cognito-sync_example_cognito-sync_ListIdentityPoolUsage_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListIdentityPoolUsage` with an AWS SDK
<a name="cognito-sync_example_cognito-sync_ListIdentityPoolUsage_section"></a>

The following code example shows how to use `ListIdentityPoolUsage`.

------
#### [ Rust ]

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

------
