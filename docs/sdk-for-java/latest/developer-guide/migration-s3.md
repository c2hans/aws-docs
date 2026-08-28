---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-s3.html
---

# Changes in working with Amazon S3 from version 1 to version 2 of the AWS SDK for Java
<a name="migration-s3"></a>

The AWS SDK for Java 2.x introduces significant changes to the S3 client, including a new package structure, updated class names, and revised method signatures. While many methods can be automatically migrated from V1 to V2 using the [migration tool](migration-tool.md), some require manual migration, such as `listNextBatchOfObjects` and `selectObjectContent`. Additionally, V2 replaces certain V1 classes like `AccessControlList` and `CannedAccessControlList` with new implementations.

**Topics**
+ [S3 client differences between version 1 and version 2 of the AWS SDK for Java](migration-s3-client.md)
+ [Migrate the Transfer Manager from version 1 to version 2 of the AWS SDK for Java](migration-s3-transfer-manager.md)
+ [Migrate pre-signed URL downloads from AWS SDK for Java v1 to v2](migration-s3-presign-download.md)
+ [Changes in parsing Amazon S3 URIs from version 1 to version 2](migration-s3-uri-parser.md)
+ [Changes in the S3 Event Notifications API from version 1 to version 2](migration-s3-event-notification.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Java. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-java` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
