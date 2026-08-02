---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/logging.html
---

# Configuring and using logging in the AWS SDK for Rust
<a name="logging"></a>

The AWS SDK for Rust uses the [tracing](http://tracing.rs/) framework for logging. To enable logging, add the `tracing-subscriber` crate and initialize it in your Rust application. Logs include timestamps, log levels, and module paths, helping debug API requests and SDK behavior. Use the `RUST_LOG` environment variable to control log verbosity, filtering by module if needed.

## How to enable logging in the AWS SDK for Rust
<a name="enableLogging"></a>

1. In a command prompt for your project directory, add the [tracing-subscriber](https://crates.io/crates/tracing-subscriber) crate as a dependency:

   ```
   $ cargo add tracing-subscriber --features tracing-subscriber/env-filter
   ```

   This adds the crate to the `[dependencies]` section of your `Cargo.toml` file.

1. Initialize the subscriber. Usually this is done early in the `main` function before calling any SDK for Rust operation:

   ```
   use aws_config::BehaviorVersion;

   type BoxError = Box<dyn Error + Send + Sync>;

   #[tokio::main]
   async fn main() -> Result<(), BoxError> {
       tracing_subscriber::fmt::init();  // Initialize the subscriber.

       let config = aws_config::defaults(BehaviorVersion::latest())
           .load()
           .await;

       let s3 = aws_sdk_s3::Client::new(&config);

       let _resp = s3.list_buckets()
           .send()
           .await?;

       Ok(())
   }
   ```

1. Turn on logging using `RUST_LOG` environment variable. To enable the display of logging information, in a command prompt, set the `RUST_LOG` environment variable to the level you want to log at. The following example sets logging to the `debug` level:

------
#### [ Linux/macOS ]

   ```
   $ RUST_LOG={{debug}}
   ```

------
#### [ Windows ]

   If you're using VSCode, the terminal window often defaults to PowerShell. Verify the type of prompt you are using.

   ```
   C:\> set RUST_LOG={{debug}}
   ```

------
#### [ PowerShell ]

   ```
   PS C:\> $ENV:RUST_LOG="debug"
   ```

------

1. Run the program:

   ```
   $ cargo run
   ```

   You should see additional output in the console or terminal window.

For more information see [filtering events with environment variables](https://docs.rs/tracing-subscriber/0.3.18/tracing_subscriber/fmt/index.html#filtering-events-with-environment-variables) from the `tracing-subscriber` documentation.

## Interpret the log output
<a name="logging-understanding"></a>

Once you have turned on logging by following the steps in the previous section, additional log information will be printed to standard out by default.

If you're using the default log output format (called "full" by the tracing module), the information that you see in the log output looks similar to this:

```
2024-06-25T16:10:12.367482Z DEBUG invoke{service=s3 operation=ListBuckets sdk_invocation_id=3434933}:try_op:try_attempt:lazy_load_identity: aws_smithy_runtime::client::identity::cache::lazy: identity cache miss occurred; added new identity (took 480.892ms) new_expiration=2024-06-25T23:07:59Z valid_for=25066.632521s partition=IdentityCachePartition(7)
2024-06-25T16:10:12.367602Z DEBUG invoke{service=s3 operation=ListBuckets sdk_invocation_id=3434933}:try_op:try_attempt: aws_smithy_runtime::client::identity::cache::lazy: loaded identity
2024-06-25T16:10:12.367643Z TRACE invoke{service=s3 operation=ListBuckets sdk_invocation_id=3434933}:try_op:try_attempt: aws_smithy_runtime::client::orchestrator::auth: resolved identity identity=Identity { data: Credentials {... }, expiration: Some(SystemTime { tv_sec: 1719356879, tv_nsec: 0 }) }
2024-06-25T16:10:12.367695Z TRACE invoke{service=s3 operation=ListBuckets sdk_invocation_id=3434933}:try_op:try_attempt: aws_smithy_runtime::client::orchestrator::auth: signing request
```

Each entry includes the following:
+ The log entry's timestamp.
+ The log level of the entry. This is a word such as `INFO`, `DEBUG`, or `TRACE`.
+ The nested set of [spans](https://docs.rs/tracing/latest/tracing/span/index.html) from which the log entry was generated, separated by colons (":"). This helps you identify the source of the log entry.
+ The Rust module path containing the code that generated the log entry.
+ The log message text.

The tracing module's standard output formats use ANSI escape codes to colorize the output. Keep these escape sequences in mind when filtering or searching the output.

**Note**
The `sdk_invocation_id` that appears within the nested set of spans is a unique ID generated client side by the SDK to help correlate log messages. It is unrelated to the request ID found in the response from an AWS service.

## Fine-tune your logging levels
<a name="logging-control"></a>

If you use a crate that supports an environment filtering, such as `tracing_subscriber`, you can control the verbosity of logs by module.

You can turn on the same logging level for every module. The following sets the logging level to `trace` for every module:

```
$ RUST_LOG={{trace}} cargo run
```

You can turn on trace-level logging for a specific module. In the following example, only logs coming from `aws_smithy_runtime` will come in at `trace` level.

```
$ RUST_LOG={{aws_smithy_runtime}}={{trace}}
```

You can specify a different log level for multiple modules by separating them with commas. The following example sets the `aws_config` module to `trace` level logging, and the `aws_smithy_runtime` module to `debug` level logging.

```
$ RUST_LOG={{aws_config}}={{trace}},{{aws_smithy_runtime}}={{debug}} cargo run
```

The following table describes some of the modules that you can use to filter log messages:

| Prefix | Description |
| --- | --- |
| `aws_smithy_runtime` | Request and response wire logging |
| `aws_config` | Credentials loading |
| `aws_sigv4` | Request signing and canonical requests |

One way to figure out which modules you need to include in your log output is to first log everything, then find the crate name in the log output for the information you need. Then you can set the environment variable accordingly and run your program again.
