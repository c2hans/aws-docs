---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/s3-transfers.html
---

# Transfer files and directories
<a name="s3-transfers"></a>

The AWS SDK for PHP Version 3 provides two approaches for transferring files and directories to and from Amazon S3. Both solutions handle the complexity of multipart uploads and downloads for large files, but they differ in their design philosophy, feature set, and usage patterns.

## Transfer options overview
<a name="transfer-options-overview"></a>

Choose the transfer approach that best fits your application's needs:

**[S3 Transfer Manager](s3-transfer-manager.md) (recommended)**
A modern, high-level library that provides a comprehensive solution for file transfers. It offers extensive configuration options, built-in progress tracking, custom download handlers, and robust error handling. The S3 Transfer Manager uses a promise-based API and supports both individual file operations and directory transfers with advanced filtering capabilities.

**[Transfer](s3-transfer.md)**
A directory transfer implementation that focuses specifically on bulk directory operations. It provides a simpler API for uploading and downloading entire directories with basic configuration options. This approach has fewer features compared to the S3 Transfer Manager.

## Key differences
<a name="key-differences"></a>

The following table highlights the main differences between the two transfer approaches:

| Feature | S3 Transfer Manager | Transfer |
| --- | --- | --- |
| Individual file operations | Yes (upload/download single files) | No (directory operations only) |
| Directory operations | Yes (with advanced filtering) | Yes (basic directory transfers) |
| Progress tracking | Built-in with custom listeners | Limited (debug output only) |
| Custom download handlers | Yes | No |
| Checksum validation | Automatic with configuration | Manual (add\_content\_md5 option) |
| Error handling | Comprehensive with failure policies | Basic promise-based handling |
| Configuration options | Extensive (8\+ options) | Basic (6 options) |
| API design | Request/response objects | Simple constructor parameters |

## Choosing the right approach
<a name="choosing-the-right-approach"></a>

Use the S3 Transfer Manager when you need:
+ Individual file upload or download operations
+ Advanced progress tracking and monitoring
+ Custom download handlers for specialized processing
+ Comprehensive error handling and retry policies
+ Fine-grained control over multipart operations
+ Directory operations with complex filtering logic

Use Transfer when you need:
+ Simple directory-to/from-S3 transfers
+ Minimal configuration and setup
+ Compatibility with existing code that uses Transfer
+ Basic multipart upload functionality

**Note**
For new applications, we recommend using the S3 Transfer Manager as it provides a more comprehensive and flexible solution for file transfers.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for PHP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-php` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
