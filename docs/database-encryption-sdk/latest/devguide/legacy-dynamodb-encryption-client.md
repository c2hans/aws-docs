---
source_url: https://docs.aws.amazon.com/database-encryption-sdk/latest/devguide/legacy-dynamodb-encryption-client.html
---

# Legacy DynamoDB Encryption Client
<a name="legacy-dynamodb-encryption-client"></a>

On June 9, 2023, our client-side encryption library was renamed to AWS Database Encryption SDK. The AWS Database Encryption SDK continues to support legacy DynamoDB Encryption Client versions. For more information on the different parts of the client-side encryption library that changed with the rename, see [Amazon DynamoDB Encryption Client rename](DDBEC-rename.md).

To migrate to the latest version of the Java client-side encryption library for DynamoDB, see [Migrate to version 4.x](ddb-java-migrate.md).

**Topics**
+ [AWS Database Encryption SDK for DynamoDB version support](#legacy-support)
+ [How the DynamoDB Encryption Client works](DDBEC-legacy-how-it-works.md)
+ [Amazon DynamoDB Encryption Client concepts](DDBEC-legacy-concepts.md)
+ [Cryptographic materials provider](crypto-materials-providers.md)
+ [Amazon DynamoDB Encryption Client available programming languages](programming-languages.md)
+ [Changing your data model](data-model.md)
+ [Troubleshooting issues in your DynamoDB Encryption Client application](troubleshooting.md)

## AWS Database Encryption SDK for DynamoDB version support
<a name="legacy-support"></a>

The topics in the Legacy chapter provide information on versions 1.*x*—2.*x* of the DynamoDB Encryption Client for Java and versions 1.*x*—3.*x* of the DynamoDB Encryption Client for Python.

The following table lists the languages and versions that support client-side encryption in Amazon DynamoDB.

| Programming language | Version | SDK major version life-cycle phase |
| --- | --- | --- |
| Java | Versions 1.*x* | [End-of-Support phase](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html#version-life-cycle), effective July 2022 |
| Java | Versions 2.*x* | [Maintenance phase](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html#version-life-cycle), until August 2026 |
| Python | Versions 1.*x* | [End-of-Support phase](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html#version-life-cycle), effective July 2022 |
| Python | Versions 2.*x* | [End-of-Support phase](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html#version-life-cycle), effective July 2022 |
| Python | Versions 3.*x* | [General Availability](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html#version-life-cycle) (GA) |
