---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/testing-smithy-mocks.html
---

# Unit testing with `aws-smithy-mocks` in the AWS SDK for Rust
<a name="testing-smithy-mocks"></a>

The AWS SDK for Rust provides multiple approaches for testing your code that interacts with AWS services. This topic describes how to use the [`aws-smithy-mocks`](https://docs.rs/aws-smithy-mocks/latest/aws_smithy_mocks/) crate, which offers a simple yet powerful way to mock AWS SDK client responses for testing purposes.

## Overview
<a name="overview-smithy-mock"></a>

When writing tests for code that uses AWS services, you often want to avoid making actual network calls. The `aws-smithy-mocks` crate provides a solution by allowing you to:
+ Create mock rules that define how the SDK should respond to specific requests.
+ Return different types of responses (success, error, HTTP responses).
+ Match requests based on their properties.
+ Define sequences of responses for testing retry behavior.
+ Verify that your rules were used as expected.

## Adding the dependency
<a name="dependency-smithy-mock"></a>

In a command prompt for your project directory, add the [`aws-smithy-mocks`](https://crates.io/crates/aws-smithy-mocks) crate as a dependency:

```
$ cargo add --dev aws-smithy-mocks
```

Using the `--dev` [option](https://doc.rust-lang.org/cargo/commands/cargo-add.html) adds the crate to the `[dev-dependencies]` section of your `Cargo.toml` file. As a [development dependency](https://doc.rust-lang.org/cargo/reference/specifying-dependencies.html#development-dependencies), it is not compiled and included into your final binary that is used for production code.

This example code also use Amazon Simple Storage Service as the example AWS service, and requires feature `test-util`.

```
$ cargo add aws-sdk-s3 --features test-util
```

This adds the crate to the `[dependencies]` section of your `Cargo.toml` file.

## Basic usage
<a name="basic-smithy-mocks"></a>

 Here's a simple example of how to use `aws-smithy-mocks` to test code that interacts with Amazon Simple Storage Service (Amazon S3):

```
use aws_sdk_s3::operation::get_object::GetObjectOutput;
use aws_sdk_s3::primitives::ByteStream;
use aws_smithy_mocks::{mock, mock_client};

#[tokio::test]
async fn test_s3_get_object() {
    // Create a rule that returns a successful response
    let get_object_rule = mock!(aws_sdk_s3::Client::get_object)
        .then_output(|| {
            GetObjectOutput::builder()
                .body(ByteStream::from_static(b"test-content"))
                .build()
        });

    // Create a mocked client with the rule
    let s3 = mock_client!(aws_sdk_s3, [&get_object_rule]);

    // Use the client as you would normally
    let result = s3
        .get_object()
        .bucket("test-bucket")
        .key("test-key")
        .send()
        .await
        .expect("success response");

    // Verify the response
    let data = result.body.collect().await.expect("successful read").to_vec();
    assert_eq!(data, b"test-content");

    // Verify the rule was used
    assert_eq!(get_object_rule.num_calls(), 1);
}
```

## Creating mock rules
<a name="creating-rules-smithy-mocks"></a>

Rules are created using the `mock!` macro, which takes a client operation as an argument. You can then configure how the rule should behave.

### Matching Requests
<a name="matching-requests-smithy-mocks"></a>

 You can make rules more specific by matching on request properties:

```
let rule = mock!(Client::get_object)
    .match_requests(|req| req.bucket() == Some("test-bucket") && req.key() == Some("test-key"))
    .then_output(|| {
        GetObjectOutput::builder()
            .body(ByteStream::from_static(b"test-content"))
            .build()
    });
```

### Different Response Types
<a name="diff-response-smithy-mocks"></a>

You can return different types of responses:

```
// Return a successful response
let success_rule = mock!(Client::get_object)
    .then_output(|| GetObjectOutput::builder().build());

// Return an error
let error_rule = mock!(Client::get_object)
    .then_error(|| GetObjectError::NoSuchKey(NoSuchKey::builder().build()));

// Return a specific HTTP response
let http_rule = mock!(Client::get_object)
    .then_http_response(|| {
        HttpResponse::new(
            StatusCode::try_from(503).unwrap(),
            SdkBody::from("service unavailable")
        )
    });
```

## Testing retry behavior
<a name="testing-retry-behavior-smithy-mocks"></a>

One of the most powerful features of `aws-smithy-mocks` is the ability to test retry behavior by defining sequences of responses:

```
// Create a rule that returns 503 twice, then succeeds
let retry_rule = mock!(aws_sdk_s3::Client::get_object)
    .sequence()
    .http_status(503, None)                          // First call returns 503
    .http_status(503, None)                          // Second call returns 503
    .output(|| GetObjectOutput::builder().build())   // Third call succeeds
    .build();

// With repetition using times()
let retry_rule = mock!(Client::get_object)
    .sequence()
    .http_status(503, None)
    .times(2)                                        // First two calls return 503
    .output(|| GetObjectOutput::builder().build())   // Third call succeeds
    .build();
```

## Rule modes
<a name="rule-modes-smithy-mocks"></a>

You can control how rules are matched and applied using rule modes:

```
// Sequential mode: Rules are tried in order, and when a rule is exhausted, the next rule is used
let client = mock_client!(aws_sdk_s3, RuleMode::Sequential, [&rule1, &rule2]);

// MatchAny mode: The first matching rule is used, regardless of order
let client = mock_client!(aws_sdk_s3, RuleMode::MatchAny, [&rule1, &rule2]);
```

## Example: Testing retry behavior
<a name="example-retry-smithy-mocks"></a>

Here's a more complete example showing how to test retry behavior:

```
use aws_sdk_s3::operation::get_object::GetObjectOutput;
use aws_sdk_s3::config::RetryConfig;
use aws_sdk_s3::primitives::ByteStream;
use aws_smithy_mocks::{mock, mock_client, RuleMode};

#[tokio::test]
async fn test_retry_behavior() {
    // Create a rule that returns 503 twice, then succeeds
    let retry_rule = mock!(aws_sdk_s3::Client::get_object)
        .sequence()
        .http_status(503, None)
        .times(2)
        .output(|| GetObjectOutput::builder()
            .body(ByteStream::from_static(b"success"))
            .build())
        .build();

    // Create a mocked client with the rule and custom retry configuration
    let s3 = mock_client!(
        aws_sdk_s3,
        RuleMode::Sequential,
        [&retry_rule],
        |client_builder| {
            client_builder.retry_config(RetryConfig::standard().with_max_attempts(3))
        }
    );

    // This should succeed after two retries
    let result = s3
        .get_object()
        .bucket("test-bucket")
        .key("test-key")
        .send()
        .await
        .expect("success after retries");

    // Verify the response
    let data = result.body.collect().await.expect("successful read").to_vec();
    assert_eq!(data, b"success");

    // Verify all responses were used
    assert_eq!(retry_rule.num_calls(), 3);
}
```

## Example: Different responses based on request parameters
<a name="example-request-param-smithy-mocks"></a>

You can also create rules that return different responses based on request parameters:

```
use aws_sdk_s3::operation::get_object::{GetObjectOutput, GetObjectError};
use aws_sdk_s3::types::error::NoSuchKey;
use aws_sdk_s3::Client;
use aws_sdk_s3::primitives::ByteStream;
use aws_smithy_mocks::{mock, mock_client, RuleMode};

#[tokio::test]
async fn test_different_responses() {
    // Create rules for different request parameters
    let exists_rule = mock!(Client::get_object)
        .match_requests(|req| req.bucket() == Some("test-bucket") && req.key() == Some("exists"))
        .sequence()
        .output(|| GetObjectOutput::builder()
            .body(ByteStream::from_static(b"found"))
            .build())
        .build();

    let not_exists_rule = mock!(Client::get_object)
        .match_requests(|req| req.bucket() == Some("test-bucket") && req.key() == Some("not-exists"))
        .sequence()
        .error(|| GetObjectError::NoSuchKey(NoSuchKey::builder().build()))
        .build();

    // Create a mocked client with the rules in MatchAny mode
    let s3 = mock_client!(aws_sdk_s3, RuleMode::MatchAny, [&exists_rule, &not_exists_rule]);

    // Test the "exists" case
    let result1 = s3
        .get_object()
        .bucket("test-bucket")
        .key("exists")
        .send()
        .await
        .expect("object exists");

    let data = result1.body.collect().await.expect("successful read").to_vec();
    assert_eq!(data, b"found");

    // Test the "not-exists" case
    let result2 = s3
        .get_object()
        .bucket("test-bucket")
        .key("not-exists")
        .send()
        .await;

    assert!(result2.is_err());
    assert!(matches!(result2.unwrap_err().into_service_error(),
                    GetObjectError::NoSuchKey(_)));
}
```

## Best practices
<a name="best-practices-smithy-mocks"></a>

When using `aws-smithy-mocks` for testing:

1.  Match specific requests: Use `match_requests()` to ensure your rules only apply to the intended requests, in particular with `RuleMode:::MatchAny`.

1.  Verify rule usage: Check `rule.num_calls()` to ensure your rules were actually used.

1.  Test error handling: Create rules that return errors to test how your code handles failures.

1.  Test retry logic: Use response sequences to verify that your code correctly handles any custom retry classifiers or other retry behavior.

1. Keep tests focused: Create separate tests for different scenarios rather than trying to cover everything in one test.
