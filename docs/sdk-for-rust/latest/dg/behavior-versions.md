---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/behavior-versions.html
---

# Using behavior versions in the AWS SDK for Rust
<a name="behavior-versions"></a>

AWS SDK for Rust developers expect and rely upon the robust and predictable behavior the language and its major libraries offer. To help developers using the SDK for Rust get the expected behavior, client configurations are required to include a `BehaviorVersion`. The `BehaviorVersion` specifies the version of the SDK whose defaults are expected. This lets the SDK evolve over time, changing best practices to match new standards and support new features without unexpected adverse impact on your application's behavior.

**Warning**
If you try to configure the SDK or create a client without explicitly specifying a `BehaviorVersion`, the constructor will panic.

For example, imagine that a new version of the SDK is released with a new default retry policy. If your application uses a `BehaviorVersion` matching a previous version of the SDK, then that prior configuration is used instead of the new default configuration.

Each time a new behavior version of the SDK for Rust is released, the previous `BehaviorVersion` is marked with the SDK for Rust `deprecated` attribute and the new version is added. This causes warnings to occur at compile time, but otherwise lets the build continue as usual. `BehaviorVersion::latest()` is also updated to indicate the new version's default behavior.

**Note**
If your code isn't reliant on extremely specific behavior characteristics, you should use `BehaviorVersion::latest()` in code or use the feature flag `behavior-version-latest` in the `Cargo.toml` file. If you're writing code that's latency sensitive, or that tunes Rust SDK behaviors, consider pinning `BehaviorVersion` to a specific major version.

## Set the behavior version in `Cargo.toml`
<a name="set-the-behavior-version-in-cargo-toml"></a>

You can specify the behavior version for the SDK and individual modules,such as `aws-sdk-s3` or `aws-sdk-iam`, by including an appropriate feature flag in the `Cargo.toml` file. At this time, only the `latest` version of the SDK is supported in `Cargo.toml`:

```
[dependencies]
aws-config = { version = "1", features = ["behavior-version-latest"] }
aws-sdk-s3 = { version = "1", features = ["behavior-version-latest"] }
```

## Set the behavior version in code
<a name="set-the-behavior-version-in-code"></a>

Your code can change the behavior version as needed by specifying it when configuring the SDK or a client:

```
let config = aws_config::load_defaults(BehaviorVersion::v2023_11_09()).await;
```

This example creates a configuration that uses the environment to configure the SDK but sets the `BehaviorVersion` to `v2023_11_09()`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Rust. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-rust` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
