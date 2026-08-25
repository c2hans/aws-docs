---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/document-history.html
---

# Document history
<a name="document-history"></a>

The following tables describe the important changes since the last release of the AWS SDK for PHP Developer Guide.

Most recent changes:

| Change | Description | Date |
| --- |--- |--- |
| [Table of contents updates](#document-history) | Table of contents revised to be more consistent with other SDK guides. | July 28, 2025 |
| [Data integrity protection with checksums](s3-checksums.md) | Content updated with details about automatic checksum calculation. | January 16, 2025 |
| [Credentials topic revisions](guide_credentials.md) | Topic reorganized. More details provided for the [default credentials provider chain](https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/guide_credentials_default_chain.html). | January 10, 2025 |
| [Amazon S3 encryption client V3 migration](s3-encryption-migration-v2-v3.md) | Added topic on Amazon S3 encryption client migration from V2 to V3 | December 4, 2024 |
| [Amazon S3 multipart uploads](s3-multipart-upload.md) | Document the 'params' array that can be used to configure subcommands of the `ObjectUploader` and `MultipartUploader` | November 6, 2024 |
| [Object uploader](s3-multipart-upload.md#object-uploader) | Clarify use of callbacks available on the `ObjectUploader` for S3 uploads | October 11, 2024 |
| [Update Amazon S3 bucket names](#document-history) | Updated S3 bucket names throughout the guide. | September 30, 2024 |
| [Amazon EventBridge global endpoints](eventbridge-examples.md) | Add code example that shows how to use Amazon EventBridge global endpoints | December 22, 2023 |
| [AWS Common Runtime (AWS CRT)](guide_crt.md) | Add a topic that discusses the use of the AWS Common Runtime (AWS CRT) by the SDK for PHP. | November 17, 2023 |
| [StreamWrapper mkdir() updates](s3-stream-wrapper.md#working-with-buckets) | Add information about working with buckets and folder objects by using `mkdir()`. | November 2, 2023 |
| [Service client creation](configuring-service-clients-code.md#conf-service-client-code-basic) | Update code snippets by removing 'version' parameter since the 'latest' is the default. | August 31, 2023 |
| [Basic client creation](making-service-requests.md#creating-a-client) | Update code snippets by removing 'version' parameter since the 'latest' is the default. | August 31, 2023 |
| [Table of contents](#document-history) | Updated table of contents to make code examples more accessible. | June 1, 2023 |
| [IAM best practices updates](#document-history) | Updated guide to align with the IAM best practices. For more information, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html). Updates to Getting started. | May 20, 2023 |
| [Amazon S3 multipart uploads](s3-multipart-upload.md) | Included configuration information for synchronous uploads. Added the `add_content_md5` upload option for asynchronous uploads. | April 13, 2023 |
| [Amazon S3 directory transfers](s3-transfer.md) | Added the `add_content_md5` transfer option.  | April 13, 2023 |
| [Reference information](#document-history) | Added multiple links to relevant detail content in the AWS SDKs and Tools Reference Guide. Updated guide formatting. | September 14, 2022 |
| [General cleanup](#document-history) | Added references to the AWS SDKs and Tools Reference Guide. Updated AWS Key Management Service sections to reflect terminology updates.  | August 23, 2022 |
| [Working with AWS services](working-with-aws-services.md) | Included lists of the code examples that are available on GitHub. | April 1, 2022 |
| [Enabling SDK metrics](#document-history) | Removed information about enabling SDK metrics, which was deprecated on December 20, 2021. | January 27, 2022 |
| [Amazon S3 encryption client migration](s3-encryption-migration-v1-v2.md) | Added topic on Amazon S3 encryption client migration | August 7, 2020 |

Older changes:

| Change | Description | Release date |
| --- | --- | --- |
| Secrets Manager examples | Add more service examples | Mar 27th, 2019 |
| Endpoint discovery | Configuration of endpoint discovery | Feb 15th, 2019 |
| Amazon CloudFront | Add more service examples | Jan 25th, 2019 |
| Service features | SDK metrics | Jan 11th, 2018 |
| Amazon Kinesis, Amazon SNS | Add more service examples | Dec 14th, 2018 |
| Amazon SES examples | Add more service examples | Oct 5th, 2018 |
| AWS KMS examples | Add more service examples | Aug 8th, 2018 |
| Credentials | Clarify and simplify credentials guide | June 30th, 2018 |
| MediaConvert examples | Add more service examples | June 15th, 2018 |
| New web layout | Documentation switched to AWS style | May 9th, 2018 |
| Amazon S3 encryption | Client side encryption | Nov 17th, 2017 |
| Amazon S3, Amazon SQS | Add more service examples | Mar 26th, 2017 |
| Amazon S3, IAM, Amazon EC2 | Add more service examples | Mar 17th, 2017 |
| Add credentials | Adds support for AssumeRole and ini | Jan 17th, 2017 |
| S3 Examples | S3 Multi-Region and presigned posts | Mar 18th, 2016 |
| OpenSearch Service and Amazon CloudSearch | Add more service examples | Dec 28th, 2015 |
| Command line | Add command parameters | Aug 13th, 2015 |
| Service features | Adds service features for S3 and AWS | Apr 30th, 2015 |
| New SDK version | Version 3 of the AWS SDK for PHP released. | May 26th, 2015 |
