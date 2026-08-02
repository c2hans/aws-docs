---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/testing-replay.html
---

# Simulate HTTP traffic using static replay in the AWS SDK for Rust
<a name="testing-replay"></a>

The AWS SDK for Rust provides multiple approaches for testing your code that interacts with AWS services. This topic describes how to use the `StaticReplayClient` to create a fake HTTP client that can be used instead of the standard HTTP client that is normally used by AWS services. This client returns the HTTP responses that you specify rather than communicating with the service over the network, so that tests get known data for testing purposes.

The `aws-smithy-http-client` crate includes a test utility class called [https://docs.rs/aws-smithy-http-client/latest/aws_smithy_http_client/test_util/struct.StaticReplayClient.html](https://docs.rs/aws-smithy-http-client/latest/aws_smithy_http_client/test_util/struct.StaticReplayClient.html). This HTTP client class can be specified instead of the default HTTP client when creating an AWS service object.

When initializing the `StaticReplayClient`, you provide a list of HTTP request and response pairs as `ReplayEvent` objects. While the test is running, each HTTP request is recorded and the client returns the next HTTP response found in the next `ReplayEvent` in the event list as the HTTP client's response. This lets the test run using known data and without a network connection.

## Using static replay
<a name="testing-replay-steps"></a>

To use static replay, you don't need to use a wrapper. Instead, determine what the actual network traffic should look like for the data your test will use, and provide that traffic data to the `StaticReplayClient` to use each time the SDK issues a request from the AWS service client.

**Note**
There are several ways to collect the expected network traffic, including the AWS CLI and many network traffic analyzers and packet sniffer tools.
+ Create a list of `ReplayEvent` objects that specify the expected HTTP requests and the responses that should be returned for them.
+ Create a `StaticReplayClient` using the HTTP transaction list created in the previous step.
+ Create a configuration object for the AWS client, specifying the `StaticReplayClient` as the `Config` object's `http_client`.
+ Create the AWS service client object, using the configuration created in the previous step.
+ Perform the operations that you want to test, using the service object that's configured to use the `StaticReplayClient`. Each time the SDK sends an API request to AWS, the next response in the list is used.
**Note**
The next response in the list is always returned, even if the sent request doesn't match the one in the vector of `ReplayEvent` objects.
+ When all the desired requests have been made, call the `StaticReplayClient.assert_requests_match()` function to verify that the requests sent by the SDK match the ones in the list of `ReplayEvent` objects.

## Example
<a name="testing-replay-example"></a>

Let's look at the tests for the same `determine_prefix_file_size()` function in the previous example, but using static replay instead of mocking.

1. In a command prompt for your project directory, add the [https://crates.io/crates/aws-smithy-http-client](https://crates.io/crates/aws-smithy-http-client) crate as a dependency:

   ```
   $ cargo add --dev aws-smithy-http-client --features test-util
   ```

   Using the `--dev` [option](https://doc.rust-lang.org/cargo/commands/cargo-add.html) adds the crate to the `[dev-dependencies]` section of your `Cargo.toml` file. As a [development dependency](https://doc.rust-lang.org/cargo/reference/specifying-dependencies.html#development-dependencies), it is not compiled and included into your final binary that is used for production code.

   This example code also use Amazon Simple Storage Service as the example AWS service.

   ```
   $ cargo add aws-sdk-s3
   ```

   This adds the crate to the `[dependencies]` section of your `Cargo.toml` file.

1. In your test code module, include both of the types that you'll need.

   ```
   use aws_smithy_http_client::test_util::{ReplayEvent, StaticReplayClient};
   use aws_sdk_s3::primitives::SdkBody;
   ```

1. The test begins by creating the `ReplayEvent` structures representing each of the HTTP transactions that should take place during the test. Each event contains an HTTP request object and an HTTP response object representing the information that the AWS service would normally reply with. These events are passed into a call to `StaticReplayClient::new()`:

   ```
           let page_1 = ReplayEvent::new(
                   http::Request::builder()
                       .method("GET")
                       .uri("https://test-bucket.s3.us-east-1.amazonaws.com/?list-type=2&prefix=test-prefix")
                       .body(SdkBody::empty())
                       .unwrap(),
                   http::Response::builder()
                       .status(200)
                       .body(SdkBody::from(include_str!("./testing/response_multi_1.xml")))
                       .unwrap(),
               );
           let page_2 = ReplayEvent::new(
                   http::Request::builder()
                       .method("GET")
                       .uri("https://test-bucket.s3.us-east-1.amazonaws.com/?list-type=2&prefix=test-prefix&continuation-token=next")
                       .body(SdkBody::empty())
                       .unwrap(),
                   http::Response::builder()
                       .status(200)
                       .body(SdkBody::from(include_str!("./testing/response_multi_2.xml")))
                       .unwrap(),
               );
           let replay_client = StaticReplayClient::new(vec![page_1, page_2]);
   ```

   The result is stored in `replay_client`. This represents an HTTP client that can then be used by the SDK for Rust by specifying it in the client's configuration.

1. To create the Amazon S3 client, call the client class's `from_conf()` function to create the client using a configuration object:

   ```
           let client: s3::Client = s3::Client::from_conf(
               s3::Config::builder()
                   .behavior_version(BehaviorVersion::latest())
                   .credentials_provider(make_s3_test_credentials())
                   .region(s3::config::Region::new("us-east-1"))
                   .http_client(replay_client.clone())
                   .build(),
           );
   ```

   The configuration object is specified using the builder's `http_client()` method, and the credentials are specified using the `credentials_provider()` method. The credentials are created using a function called `make_s3_test_credentials()`, which returns a fake credentials structure:

   ```
   fn make_s3_test_credentials() -> s3::config::Credentials {
       s3::config::Credentials::new(
           "ATESTCLIENT",
           "astestsecretkey",
           Some("atestsessiontoken".to_string()),
           None,
           "",
       )
   }
   ```

   These credentials don't need to be valid because they won't actually be sent to AWS.

1. Run the test by calling the function that needs testing. In this example, that function's name is `determine_prefix_file_size()`. Its first parameter is the Amazon S3 client object to use for its requests. Therefore, specify the client created using the `StaticReplayClient` so requests are handled by that rather than going out over the network:

   ```
           let size = determine_prefix_file_size(client, "test-bucket", "test-prefix")
               .await
               .unwrap();

           assert_eq!(19, size);

           replay_client.assert_requests_match(&[]);
   ```

   When the call to `determine_prefix_file_size()` is finished, an assert is used to confirm that the returned value matches the expected value. Then, the `StaticReplayClient` method `assert_requests_match()` function is called. This function scans the recorded HTTP requests and confirms that they all match the ones specified in the array of `ReplayEvent` objects provided when creating the replay client.

You can [view the complete code for these examples](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/testing) on GitHub.
