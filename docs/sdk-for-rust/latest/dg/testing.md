---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/testing.html
---

# Adding unit testing to your AWS SDK for Rust application
<a name="testing"></a>

While there are many ways you can implement unit testing in your AWS SDK for Rust project, there are a few that we recommend:
+ [Unit testing using `mockall`](testing-automock.md) – Use `automock` from the `mockall` crate to automatically generate and execute your tests.
+ [Static replay](testing-replay.md) – Use the AWS Smithy runtime's `StaticReplayClient` to create a fake HTTP client that can be used instead of the standard HTTP client that is normally used by AWS services. This client returns the HTTP responses that you specify rather than communicating with the service over the network, so that tests get known data for testing purposes.
+ [Unit testing using `aws-smithy-mocks`](testing-smithy-mocks.md) – Use `mock` and `mock_client` from the `aws-smithy-mocks` crate to mock AWS SDK client responses and to create mock rules that define how the SDK should respond to specific requests.
