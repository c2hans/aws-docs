---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_crt.html
---

# Use the AWS Common Runtime (AWS CRT) extension in the SDK for PHP
<a name="guide_crt"></a>

The [AWS CRT libraries](https://docs.aws.amazon.com//sdkref/latest/guide/common-runtime.html) provide basic functionality with good performance and minimal footprint for several AWS SDKs. This topic discusses when the AWS CRT is used by the SDK for PHP and how to install the AWS CRT extension.

## When you need the AWS CRT extension installed
<a name="php-crt-uses"></a>

The SDK for PHP uses the authorization and checksum functionality of the AWS CRT libraries. The AWS CRT extension is required when you work with:
+ [Amazon S3 Multi-Region Access Points](s3-multi-region-access-points.md)
+ [Amazon EventBridge global endpoints](eventbridge-examples.md)
+ [A CRC-32C checksum algorithm in Amazon Simple Storage Service (Amazon S3)](s3-checksums.md)

If you use a feature listed above and the AWS CRT extention is not installed in your PHP environment, the SDK for PHP will report an error message and remind you to install the extension.

## Install the AWS Common Runtime (AWS CRT) extension
<a name="php-crt-install"></a>

Instructions on how to install the AWS CRT extension are available on the main page of the [GitHub repository for the aws-crt-php](https://github.com/awslabs/aws-crt-php#aws-common-runtime-php-bindings).
