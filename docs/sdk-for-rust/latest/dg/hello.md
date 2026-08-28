---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/hello.html
---

# Creating a simple application using the AWS SDK for Rust
<a name="hello"></a>

You can get started quickly with AWS SDK for Rust by following this tutorial for creating a simple application that calls an AWS service.

## Prerequisites
<a name="prerequisites"></a>

In order to use the AWS SDK for Rust, you must have Rust and Cargo installed.
+ Install the Rust toolchain: [https://www.rust-lang.org/tools/install](https://www.rust-lang.org/tools/install)
+ Install the `cargo-component` [tool](https://github.com/bytecodealliance/cargo-component) by running command: `cargo install cargo-component`

### Recommended tools:
<a name="recommended-tools"></a>

The following optional tools can be installed in your IDE to assist with code completion and troubleshooting.
+ The rust-analyzer extension, see [Rust in Visual Studio Code](https://code.visualstudio.com/docs/languages/rust).
+ Amazon Q Developer, see [Installing the Amazon Q Developer extension or plugin in your IDE](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-IDE-setup.html).

## Create your first SDK app
<a name="hello-world"></a>

This procedure creates your first SDK for Rust application that lists your DynamoDB tables.

1. In a terminal or console window, navigate to a location on your computer where you want to create the app.

1. Run the following command to create a `hello_world` directory and populate it with a skeleton Rust project:

   ```
   $ cargo new hello_world --bin
   ```

1. Navigate into the `hello_world` directory and use the following command to add the required dependencies to the app:

   ```
   $ cargo add aws-config aws-sdk-dynamodb tokio --features tokio/full,aws-config/credentials-login
   ```

   These dependencies include the SDK crates that provide configuration features and support for DynamoDB, including the [`tokio` crate](https://crates.io/crates/tokio), which is used to implement asynchronous I/O operations.
**Note**
Unless you use a feature like `tokio/full` Tokio will not provide an async runtime. The SDK for Rust requires an async runtime.
The `aws-config/credentials-login` feature enables support for AWS Management Console sign-in credentials, see [Authentication and access in the AWS SDKs and Tools Reference Guide](https://docs.aws.amazon.com/sdkref/latest/guide/access.html) for more information.

1. Update `main.rs` in the `src` directory to contain the following code.

   ```
   use aws_config::meta::region::RegionProviderChain;
   use aws_config::BehaviorVersion;
   use aws_sdk_dynamodb::{Client, Error};

   /// Lists your DynamoDB tables in the default Region or us-east-1 if a default Region isn't set.
   #[tokio::main]
   async fn main() -> Result<(), Error> {
       let region_provider = RegionProviderChain::default_provider().or_else("us-east-1");
       let config = aws_config::defaults(BehaviorVersion::latest())
           .region(region_provider)
           .load()
           .await;
       let client = Client::new(&config);

       let resp = client.list_tables().send().await?;

       println!("Tables:");

       let names = resp.table_names();

       for name in names {
           println!("  {}", name);
       }

       println!();
       println!("Found {} tables", names.len());

       Ok(())
   }
   ```
**Note**
This example only displays the first page of results. See [Using paginated results in the AWS SDK for Rust](paginating.md) to learn how to handle multiple pages of results.

1. Run the program:

   ```
   $ cargo run
   ```

   You should see a list of your table names.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Rust. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-rust` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
