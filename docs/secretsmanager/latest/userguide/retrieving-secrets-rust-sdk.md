---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets-rust-sdk.html
---

# Get a Secrets Manager secret value using the Rust AWS SDK
<a name="retrieving-secrets-rust-sdk"></a>

In applications, you can retrieve your secrets by calling `GetSecretValue` or `BatchGetSecretValue`in any of the AWS SDKs. However, we recommend that you cache your secret values by using client-side caching. Caching secrets improves speed and reduces your costs.

For Rust applications, use the [Secrets Manager Rust-based caching component](retrieving-secrets_cache-rust.md) or call the [SDK directly](https://docs.rs/releases/search?query=aws-sdk-secretsmanager) with GetSecretValue or BatchGetSecretValue.

The following code example shows how to get a Secrets Manager secret value.

**Required permissions: **`secretsmanager:GetSecretValue`

```
async fn show_secret(client: &Client, name: &str) -> Result<(), Error> {
    let resp = client.get_secret_value().secret_id(name).send().await?;

    println!("Value: {}", resp.secret_string().unwrap_or("No value!"));

    Ok(())
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
