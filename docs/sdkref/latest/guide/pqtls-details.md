---
source_url: https://docs.aws.amazon.com/sdkref/latest/guide/pqtls-details.html
---

# Enabling hybrid post-quantum TLS
<a name="pqtls-details"></a>

AWS SDKs and tools have cryptographic capabilities and configuration that differ across language and runtime. There are three ways that an AWS SDK or tool currently provides PQ TLS support:

**Topics**
+ [SDKs with PQ TLS enabled by default](#pq-tls-default)
+ [Opt-in PQ TLS support](#pq-tls-opt-in)
+ [SDKs that rely on System OpenSSL](#pq-tls-open-ssl)
+ [AWS SDKs and tools not planning to support PQ TLS](#pq-tls-nosupport)

## SDKs with PQ TLS enabled by default
<a name="pq-tls-default"></a>

**Note**
As of 6-Nov-2025, AWS SDK and its underlying CRT libraries for MacOS and Windows uses system libraries for TLS, so PQ TLS capabilities on those platforms is generally determined by system-level support.

### AWS SDK for Go
<a name="pq-sdk-go"></a>

The AWS SDK for Go uses Golang’s own TLS implementation provided by its standard library. Golang supports and prefers PQ TLS as of v1.24, so AWS SDK for Go users can enable PQ TLS by simply upgrading Golang to v1.24.

### AWS SDK for JavaScript (browser)
<a name="pq-sdk-javascript"></a>

The AWS SDK for JavaScript (browser) uses the browser’s TLS stack, so the SDK will negotiate PQ TLS if the browser runtime supports and prefers it. Firefox launched support for PQ TLS in v132.0. Chrome announced support for PQ TLS in v131. Edge supports opt-in PQ TLS in v120 for desktop and 140 for Android.

### AWS SDK for Node.js
<a name="pq-sdk-nodejs"></a>

As of Node.js v22.20 (LTS) and v24.9.0, Node.js statically links and bundles OpenSSL 3.5. This means that PQ TLS is enabled and preferred by default for those and subsequent versions.

### AWS SDK for Kotlin
<a name="pq-sdk-kotlin"></a>

The Kotlin SDK supports and prefers PQ TLS on Linux as of v1.5.78. Because AWS SDK for Kotlin’s CRT-based client relies on system libraries for TLS on MacOS and Windows, support for PQ TLS will depend on those underlying system libraries.

### AWS SDK for Rust
<a name="pq-sdk-rust"></a>

The AWS SDK for Rust distributes distinct packages (known as “crates” in the Rust ecosystem) for each service client. These are all managed in a consolidated GitHub repository, but each service client follows its own version and release cadence. The consolidated SDK released PQ TLS preference on 8/29/25, so any individual service client version released after that date will support and prefer PQ TLS by default.

 You can determine the minimum version supporting PQ TLS for a particular service client by navigating to the relevant crates.io version URL (for example, AWS Promotional Credit's is [here](https://crates.io/crates/aws-sdk-paymentcryptography/versions)) and finding the first version published after 29-Aug-25. Any service client version published after 29-Aug-25 will have PQ TLS enabled and preferred by default.

## Opt-in PQ TLS support
<a name="pq-tls-opt-in"></a>

### AWS SDK for C\+\+
<a name="pq-sdk-cplusplus"></a>

By default, the C\+\+ SDK uses platform-native clients like libcurl and WinHttp. Libcurl generally relies on system OpenSSL for TLS, so PQ TLS is only enabled by default if system OpenSSL is ≥ v3.5. You can override this default in C\+\+ SDK v1.11.673 or later, and opt-in to the AwsCrtHttpClient which supports and enables PQ TLS by default.

Notes on Building for Opt-In PQ TLS You can fetch the SDK’s CRT dependencies with [this script](https://github.com/aws/aws-sdk-cpp/blob/main/prefetch_crt_dependency.sh). Building the SDK from source is described [here](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/sdk-from-source.html) and [here](https://github.com/aws/aws-sdk-cpp/tree/main?tab=readme-ov-file#building-from-source), but note that you may need a few additional CMake flags:

```
-DUSE_CRT_HTTP_CLIENT=ON \
-DUSE_TLS_V1_2=OFF \
-DUSE_TLS_V1_3=ON \
-DUSE_OPENSSL=OFF \
```

### AWS SDK for Java
<a name="pq-sdk-java"></a>

 As of v2, AWS SDK for Java provides an AWS Common Runtime (AWS CRT) HTTP Client that can be configured to perform PQ TLS. As of v2.35.11, the AwsCrtHttpClient enables and prefers PQ TLS by default wherever it’s used.

## SDKs that rely on System OpenSSL
<a name="pq-tls-open-ssl"></a>

Several AWS SDKs and tools depend on the system's libcrypto/libssl library for TLS. The system library most often used is OpenSSL. OpenSSL enabled PQ TLS support in version 3.5, so the easiest way to configure these SDKs and tools for PQ TLS is to use it on an operating system distribution that has at least OpenSSL 3.5 installed.

You can also configure a Docker container to use OpenSSL 3.5 to enable PQ TLS on any system that supports Docker. See [Post-quantum TLS in Python](https://aws.amazon.com/blogs/security/post-quantum-tls-in-python/) for an example of setting this up for Python.

### AWS CLI
<a name="pq-tls-cli"></a>

As of v2.34.54, the [AWS CLI installer](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) for Linux bundles OpenSSL 3.5.6, so PQ TLS is enabled and preferred by default for that and subsequent versions on Linux. AWS CLI users on Linux can enable PQ TLS by upgrading to AWS CLI v2.34.54 or later.

For MacOS, install the AWS CLI via [Homebrew](https://brew.sh/) and ensure that your Homebrew-vended OpenSSL is upgraded to version 3.5\+. You can do this with “brew install openssl@3.6” and validate with “brew list \| grep openssl”.

For step-by-step instructions to validate the installation, see [github repository](https://github.com/aws-samples/sample-post-quantum-tls-python/) and accompanying [blog post](https://aws.amazon.com/blogs/security/post-quantum-tls-in-python/).

### AWS SDK for PHP
<a name="pq-tls-php"></a>

The AWS SDK for PHP relies on system libssl/libcrypto. To use PQ TLS, use this SDK on an operating system distribution that has at least OpenSSL 3.5 installed.

### AWS SDK for Python (Boto3)
<a name="pq-tls-python"></a>

The AWS SDK for Python (Boto3) relies on the OpenSSL library linked by your Python installation for TLS. The behavior differs by platform:

------
#### [ Windows and macOS (python.org installer) ]

The official [python.org](https://www.python.org/) installers for Windows (.exe) and macOS (.pkg) bundle their own OpenSSL library. As of Python 3.14.6, the bundled OpenSSL 3.5.7 supports and prefers PQ TLS by default. No additional configuration is needed.

------
#### [ macOS (Homebrew) ]

Since Homebrew's [python@3.14](https://www.python.org/downloads/release/python-3140/) links against Homebrew's openssl@3 shared library, as of Homebrew OpenSSL 3.5\+, PQ TLS is supported and preferred by default. You can validate your OpenSSL version with:

`python3.14 -c "import ssl; print(ssl.OPENSSL_VERSION)"`

If your version is below 3.5, upgrade with brew upgrade openssl@3.

------
#### [ Linux ]

On Linux, Python dynamically links against the system's shared libssl. Having OpenSSL 3.5\+ installed is necessary but not sufficient, as the system's cryptographic policy must also include post-quantum groups in its default TLS configuration.

For Amazon Linux 2023 (AL2023.12 or higher), enable PQ TLS with:

`sudo update-crypto-policies --set DEFAULT:PQ`

For more information, see [Enable Post-Quantum Cryptography (PQC) on AL2023](https://docs.aws.amazon.com/linux/al2023/ug/crypto-policies-pq.html).

For other Linux distributions, consult your distribution's documentation on configuring default TLS groups.

You can verify that PQ TLS is working by checking for the X25519MLKEM768 key exchange in your TLS handshake.

------

### AWS SDK for Ruby
<a name="pq-tls-ruby"></a>

The AWS SDK for Ruby relies on system libssl/libcrypto. To use PQ TLS, use this SDK on an operating system distribution that has at least OpenSSL 3.5 installed.

### AWS SDK for .NET
<a name="pq-tls-dotnet"></a>

On Linux, AWS SDK for .NET relies on system libssl/libcrypto. To use PQ TLS, use this SDK on an operating system distribution that has at least OpenSSL 3.5 installed. On Windows and MacOS, PQ TLS is available starting in [.NET 10](https://devblogs.microsoft.com/dotnet/post-quantum-cryptography-in-dotnet/) and [Windows 11](https://techcommunity.microsoft.com/blog/microsoft-security-blog/post-quantum-cryptography-apis-now-generally-available-on-microsoft-platforms/4469093). On MacOS, TLS 1.3 support (a prerequisite for PQ TLS) can be enabled by opting-in to Apple's Network.framework as described [here](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-10/libraries#tls-13-for-macos-client). Assuming a minimum .NET version of 10, PQ TLS should then be enabled.

## AWS SDKs and tools not planning to support PQ TLS
<a name="pq-tls-nosupport"></a>

There are currently no plans to support the following language SDKs and tools:
+ AWS SDK for SAP
+ AWS SDK for Swift
+ AWS Tools for Windows PowerShell

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for none. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdkref` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
