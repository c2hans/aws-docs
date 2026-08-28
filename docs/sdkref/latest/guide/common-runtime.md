---
source_url: https://docs.aws.amazon.com/sdkref/latest/guide/common-runtime.html
---

# AWS Common Runtime (CRT) libraries
<a name="common-runtime"></a>

The AWS Common Runtime (CRT) libraries are a base library of the SDKs. The CRT is a modular family of independent packages, written in C. Each package provides good performance and minimal footprint for different required functionalities. These functionalities are common and shared across all SDKs providing better code reuse, optimization, and accuracy. The packages are:
+ [`awslabs/aws-c-auth`](https://github.com/awslabs/aws-c-auth): AWS client-side authentication (standard credential providers and signing (sigv4))
+ [`awslabs/aws-c-cal`](https://github.com/awslabs/aws-c-cal): Cryptographic primitive types, hashes (MD5, SHA256, SHA256 HMAC), signers, AES
+ [`awslabs/aws-c-common`](https://github.com/awslabs/aws-c-common): Basic data structures, threading/synchronization primitive types, buffer management, stdlib-related functions
+ [`awslabs/aws-c-compression`](https://github.com/awslabs/aws-c-compression): Compression algorithms (Huffman encoding/decoding)
+ [`awslabs/aws-c-event-stream`](https://github.com/awslabs/aws-c-event-stream): Event stream message processing (headers, prelude, payload, crc/trailer), remote procedure call (RPC) implementation over event streams
+ [`awslabs/aws-c-http`](https://github.com/awslabs/aws-c-http): C99 implementation of the HTTP/1.1 and HTTP/2 specifications
+ [`awslabs/aws-c-io`](https://github.com/awslabs/aws-c-io): Sockets (TCP, UDP), DNS, pipes, event loops, channels, SSL/TLS
+ [`awslabs/aws-c-iot`](https://github.com/awslabs/aws-c-iot): C99 implementation of AWS IoT cloud services integration with devices
+ [`awslabs/aws-c-mqtt`](https://github.com/awslabs/aws-c-mqtt): Standard, lightweight messaging protocol for the Internet of Things (IoT)
+ [`awslabs/aws-c-s3`](https://github.com/awslabs/aws-c-s3): C99 library implementation for communicating with the Amazon S3 service, designed for maximizing throughput on high bandwidth Amazon EC2 instances
+ [`awslabs/aws-c-sdkutils`](https://github.com/awslabs/aws-c-sdkutils): A utilities library for parsing and managing AWS profiles
+ [`awslabs/aws-checksums`](https://github.com/awslabs/aws-checksums): Cross-platform hardware-accelerated CRC32c and CRC32 with fallback to efficient software implementations
+ [`awslabs/aws-lc`](https://github.com/awslabs/aws-lc): General-purpose cryptographic library maintained by the AWS Cryptography team for AWS and their customers, based on code from the Google BoringSSL project and the OpenSSL project
+ [`awslabs/s2n`](https://github.com/awslabs/s2n): C99 implementation of the TLS/SSL protocols, designed to be small and fast with security as a priority

The CRT is available through all SDKs except Go and Rust.

## CRT dependencies
<a name="crt-dep"></a>

The CRT libraries form a complex net of relationships and dependencies. Knowing these relationships is helpful if you need to build the CRT directly from source. However, most users access CRT functionality through their language SDK (such as AWS SDK for C\+\+ or AWS SDK for Java) or their language IoT device SDK (such as AWS IoT SDK for C\+\+ or AWS IoT SDK for Java). In the following diagram, the Language CRT Bindings box refers to the package wrapping the CRT libraries for a specific language SDK. This is a collection of packages of the form `aws-crt-*`, where '\*' is an SDK language (such as [`aws-crt-cpp`](https://github.com/awslabs/aws-crt-cpp) or [`aws-crt-java`](https://github.com/awslabs/aws-crt-java)).

*The following is an illustration of the hierarchical dependencies of the CRT libraries.*

![CRT dependency diagram showing how the individual CRT libraries interrelate with each other.](http://docs.aws.amazon.com/sdkref/latest/guide/images/crt-dependency-graph.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for none. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdkref` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
