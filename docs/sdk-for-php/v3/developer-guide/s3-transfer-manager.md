---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/s3-transfer-manager.html
---

# S3 Transfer Manager
<a name="s3-transfer-manager"></a>

The S3 Transfer Manager provides an interface for uploading and downloading files to and from Amazon S3. You can use it for single file operations or directory operations.

The Transfer Manager handles multipart uploads and downloads automatically. It manages large files and tracks progress. The library implements best practices for S3 data transfers. You can use it to build file transfer capabilities in your PHP applications.

## Key features
<a name="key-features"></a>

The S3 Transfer Manager provides the following key features:
+ **Simple API:** Upload and download files and directories
+ **Custom download handlers:** Implement your own download logic
+ **Automatic multipart uploads and downloads:** Handle large files automatically
+ **Concurrent processing**: Maximize throughput
+ **Progress tracking:** Monitor transfer status
+ **Customizable behavior:** Configure extensive options
+ **Error handling:** Configure retry and failure policies
+ **Directory operations:** Transfer multiple files in batches
+ **Checksum validation:** Ensure data integrity

## Installation
<a name="installation"></a>

The S3 Transfer Manager is included in the AWS SDK for PHP Version 3. You don't need to install it separately.

To install using Composer, run the following command:

```
composer require aws/aws-sdk-php
```

This command installs the complete AWS SDK for PHP Version 3, including the S3 Transfer Manager.
