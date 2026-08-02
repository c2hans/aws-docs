---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/presigned-urls.html
---

# Creating presigned URLs using the AWS SDK for Rust
<a name="presigned-urls"></a>

 You can presign requests for some AWS API operations so that another caller can use the request later without presenting their own credentials.

 For example, assume that Jane has access to an Amazon Simple Storage Service (Amazon S3) object and she wants to temporarily share object access with Alejandro. Jane can generate a presigned `GetObject` request to share with Alejandro so that he can download the object without requiring access to Jane's credentials or having any of his own. The credentials used by the presigned URL are Jane's because she is the AWS user who generated the URL.

To learn more about presigned URLs in Amazon S3, see [Working with presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html) in the *Amazon Simple Storage Service User Guide*.

## Presigning basics
<a name="presign-basics"></a>

 The AWS SDK for Rust provides a `presigned()` method on operation fluent-builders that can be used to get a presigned request.

 The following example creates a presigned `GetObject` request for Amazon S3. The request is valid for 5 minutes after creation.

```
use std::time::Duration;
use aws_config::BehaviorVersion;
use aws_sdk_s3::presigning::PresigningConfig;

let config = aws_config::defaults(BehaviorVersion::latest())
    .load()
    .await;

let s3 = aws_sdk_s3::Client::new(&config);

let presigned = s3.get_object()
    .presigned(
        PresigningConfig::builder()
            .expires_in(Duration::from_secs(60 * 5))
            .build()
            .expect("less than one week")
    )
    .await?;
```

 The `presigned()` method returns a `Result<PresignedRequest, SdkError<E, R>>`.

The returned `PresignedRequest` contains methods to get at the components of an HTTP request including the method, URI, and any headers. All of these need to be sent to the service, if present, for the request to be valid. Many presigned requests can be represented by the URI alone though.

## Presigning `POST` and `PUT` requests
<a name="presign-post-put"></a>

 Many operations that are presignable require only a URL and must be sent as HTTP `GET` requests. Some operations, however, take a body and must be sent as an HTTP `POST` or HTTP `PUT` request along with headers in some cases. Presigning these requests is identical to presigning `GET` requests, but invoking the presigned request is more complicated.

 The following is an example of presigning an Amazon S3 `PutObject` request and converting it into an [https://docs.rs/http/latest/http/request/struct.Request.html](https://docs.rs/http/latest/http/request/struct.Request.html) which can be sent using an HTTP client of your choosing.

To use the `into_http_1x_request()` method, add the `http-1x` feature to your `aws-sdk-s3` crate in your `Cargo.toml` file:

```
aws-sdk-s3 = { version = "1", features = ["http-1x"] }
```

Source file:

```
let presigned = s3.put_object()
    .presigned(
        PresigningConfig::builder()
            .expires_in(Duration::from_secs(60 * 5))
            .build()
            .expect("less than one week")
    )
    .await?;

let body = "Hello AWS SDK for Rust";
let http_req = presigned.into_http_1x_request(body);
```

## Standalone Signer
<a name="standalone-signer"></a>

**Note**
This is an advanced use case. It isn't needed or recommended for most users.

There are a few use cases where it is necessary to create a signed request outside of the SDK for Rust context. For that you can use the [https://docs.rs/aws-sigv4/latest/aws_sigv4/index.html](https://docs.rs/aws-sigv4/latest/aws_sigv4/index.html) crate independently from the SDK.

 The following is an example to demonstrate the basic elements, see the crate documentation for more details.

Add the `aws-sigv4` and `http` crates to your `Cargo.toml` file:

```
[dependencies]
aws-sigv4 = "1"
http = "1"
```

Source file:

```
use aws_smithy_runtime_api::client::identity::Identity;
use aws_sigv4::http_request::{sign, SigningSettings, SigningParams, SignableRequest};
use aws_sigv4::sign::v4;
use std::time::SystemTime;

// Set up information and settings for the signing.
// You can obtain credentials from `SdkConfig`.
let identity = Credentials::new(
    "AKIDEXAMPLE",
    "wJalrXUtnFEMI/K7MDENG+bPxRfiCYEXAMPLEKEY",
    None,
    None,
    "hardcoded-credentials").into();

let settings = SigningSettings::default();

let params = v4::SigningParams::builder()
    .identity(&identity)
    .region("us-east-1")
    .name("service")
    .time(SystemTime::now())
    .settings(settings)
    .build()?
    .into();

// Convert the HTTP request into a signable request.
let signable = SignableRequest::new(
    "GET",
    "https://some-endpoint.some-region.amazonaws.com",
    std::iter::empty(),
    SignableBody::UnsignedPayload
)?;

// Sign and then apply the signature to the request.
let (signing_instructions, _signature) = sign(signable, &params)?.into_parts();

let mut my_req = http::Request::new("...");
signing_instructions.apply_to_request_http1x(&mut my_req);
```
