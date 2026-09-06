---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/document-history.html
---

# Document history
<a name="document-history"></a>

This topic describes important changes to the AWS SDK for Java Developer Guide over the course of its history.

| Change | Description | Date |
| --- | --- | --- |
| [Migrating Amazon S3 pre-signed URL downloads from v1 to v2](migration-s3-presign-download.html) | Add migration guide for pre-signed URL downloads from v1 to v2 | July 15, 2026 |
| [Pre-signed URL download examples for Amazon S3](examples-s3-presign.html) | Add pre-signed URL download examples using S3AsyncClient pre-signed URL extension and S3 Transfer Manager | July 15, 2026 |
| [Current key](openpgp.md#pgp-current-keys) | Add new PGP key that expires on 2026-09-27. | October 1, 2025 |
| [Unsupported code patterns](migration-tool-unsupported-patterns.md) | Document the unsupported code patterns of the migration tool. | September 23, 2025 |
| [Migration tool](migration-tool.md) | Updates for GA release. | September 19, 2025 |
| [Metrics reference](metrics-list.md) | Add more details about metrics collected by the SDK. | September 3, 2025 |
| [Implement optimistic locking with the `VersionedRecordExtension`](ddb-en-client-extensions.md#ddb-en-client-extensions-VRE) | Add details about DynamoDB Enhanced Client's VersionRecordExtension. | September 2, 2025 |
| [Find applications using 1.x clients](migration-find-apps-using-v1.md) | Add instructions to help identify applications using AWS SDK for Java 1.x clients by querying AWS CloudTrail events before migrating to version 2. | August 20, 2025 |
| [Transfer Manager](migration-s3-transfer-manager.md) | Add comprehensive migration tables for client constructors, methods, model objects, and behavior changes. Included detailed code examples for unsupported methods requiring manual migration. | July 1, 2025 |
| [Metrics](metrics.md) | Add comprehensive [documentation for `LoggingMetricPublisher`](metric-pub-impl-logging.md). Restructured the metrics topic with improved getting-started guidance. | June 20, 2025 |
| [High-level changes in mapping libraries from version 1 to version 2 of the SDK for Java](dynamodb-mapping-high-level.md) | Add information about empty string handling differences between DynamoDBMapper (v1) and DynamoDB Enhanced Client (v2) in the migration guide. | June 18, 2025 |
| Table of contents reorganization | Add [Configuring service clients in the AWS SDK for Java 2.x](configuring-service-clients.md) chapter assembled from other sections of the guide. | June 16, 2025 |
| [Use the `LegacyMd5Plugin` for simplified MD5 compatibility](s3-checksums.md#S3-checksum-legacy-md5) | Add information about using the LegacyMd5Plugin for backward compatibility with systems that require MD5 checksums. | May 19, 2025 |
| [S3 client differences between version 1 and version 2 of the AWS SDK for Java](migration-s3-client.md) | Add S3 client differences between v1 and v2 of the AWS SDK for Java and provide migration examples if the migration tool cannot automatically migrate the V1 code. | April 24, 2025 |
| [Deserialization differences](migration-deserialization-changes.md) | Add deserialization difference between v1 and v2 of the SDK for Java. | April 10, 2025 |
| [Changes in automatic Amazon SQS request batching from version 1 to version 2](migration-sqs-auto-batching.md) | Add migration content for SQS automatic request batching from v1 to v2 of the SDK for Java. | April 8, 2025 |
| [Other checksum calculation options](s3-checksums.md#S3-checsum-calculation-options) | Update information about automatic checksum calculations | April 3, 2025 |
| [Configure ALPN protocol negotiation](http-configuration-netty.md#http-netty-config-alpn) | Show configuration of ALPN protocol negotiation with the Netty-based HTTP client. | February 21, 2025 |
| [Publish SDK metrics for AWS Lambda functions using the AWS SDK for Java 2.x](metric-pub-impl-emf.md) | Add information about using the EMF logging metric publisher with AWS Lambda to capture SDK metrics. | February 6, 2025 |
| [Implement `ContentStreamProvider`](content-stream-provider.md) | Add topic on how to implement a ContentStreamProvider. | January 29, 2025 |
| [Data integrity protection with checksums](s3-checksums.md) | Content updated with details about automatic checksum calculation. | January 16, 2025 |
| [Changes in working with Amazon S3 from version 1 to version 2 of the AWS SDK for Java](migration-s3.md) | Add migration content for working with Amazon S3. | January 8, 2025 |
| [Access the AWS CRT-based HTTP clients](http-configuration-crt.md#http-config-crt-access) | Add information about how to used a platform-specific jar with AWS CRT-based components. | November 14, 2024 |
| [Use IAM Roles Anywhere for authentication](credentials-process.md#credentials-iam-roles-anywhere) | Add information about how to use IAM Roles Anywhere for authentication. | November 6, 2024 |
| [Caching credentials configuration example](credential-caching.md#example-optimized-sts-config) | Add an example that configures a credentials provider by using the asyncCredentialUpdateEnabled property. | November 4, 2024 |
| [Use automatic request batching for Amazon SQS with the AWS SDK for Java 2.x](sqs-auto-batch.md) | Add a new topic that documents the Automatic Request Batching API for Amazon SQS. | October 23, 2024 |
| [OpenPGP key for the AWS SDK for Java](openpgp.md) | Update current OpenPGP key information. | October 10, 2024 |
| [Use complex types in expressions](ddb-en-client-adv-features-nested.md#ddb-en-client-adv-features-nested-expressions) and [Update items that contain complex types](ddb-en-client-adv-features-nested.md#ddb-en-client-adv-features-nested-updates) | Add content for how to work with complex types in expressions and updates. | October 10, 2024 |
| Update Amazon S3 bucket names | Update Amazon S3 bucket names. | September 30, 2024 |
| [Optimize performance with account-based endpoints](examples-dynamodb.md#ddb-account-based-endpoints-v2) | Add information about AWS account-based endpoints for DynamoDB. | September 24, 2024 |
| [Work with attributes that are beans, maps, lists and sets](ddb-en-client-adv-features-nested.md) | Update section for DynamoDB Enhance Client that discusses working with attributes that are complex types. | September 6, 2024 |
| [Configure service clients to shortcut lookups](lambda-optimize-starttime.md#lambda-quick-clients) | Clarify use of the EnvironmentVariableCredentialsProvider when Lambda SnapStart for Java is used. | August 19, 2024 |
| [Configure the Java-based S3 async client to use parallel transfers](s3-async-client-multipart.md) | Add page with information on how to enable parallel transfer support | August 15, 2024 |
| [Generate a UUID with the AutoGeneratedUuidExtension](ddb-en-client-extensions.md#ddb-en-client-extensions-AGUE) | Add information about the DynamoDB Enhanced Client AutoGeneratedUuidExtension | August 14, 2024 |
| [AWS SDK for Java migration tool](migration-tool.md) | Add a section about the migration tool (preview release) | August 9, 2024 |
| [Work with S3 Event Notifications](examples-s3-event-notifications.md) | Add section that discusses how to work with the S3 Event Notifications API | July 21, 2024 |
| [Changes in working with DynamoDB from version 1 to version 2 of the AWS SDK for Java](migration-ddb-mapper.md) | Add v1 to v2 migration information for the DynamoDB mapping/document APIs | July 21, 2024 |
| [Changes in the S3 Event Notifications API from version 1 to version 2](migration-s3-event-notification.md) | Add v1 to b2 migration information for the S3 Event Notifications API | July 21, 2024 |
| [Configure retry behavior in the AWS SDK for Java 2.x](retry-strategy.md) | Add retry strategy topic | June 18, 2024 |
| [How to set the JVM TTL](jvm-ttl-dns.md#how-to-set-the-jvm-ttl) | Remove instructions to set networkaddress.cache.ttl security property by using a java command-line system property. | May 21, 2024 |
| [Reduce SDK startup time for AWS Lambda](lambda-optimize-starttime.md) | Update HTTP client recommendation to reduce startup time for AWS Lambda | May 14, 2024 |
| [AWS SDK for Java 2.x: Comprehensive Metrics Reference](metrics-list.md) | Reorganize metrics table items | May 1, 2024 |
| [Troubleshooting FAQs](troubleshooting.md) | Add troubleshooting topic. | April 26, 2024 |
| [Metrics collected with each request](metrics-list.md#metrics-perrequest) | Add new metrics reported by the SDK. | April 26, 2024 |
| [Set the JVM TTL for DNS name lookups](jvm-ttl-dns.md) | Change recommended DNS lookup TTL to 5 seconds. | April 23, 2024 |
| [Package name to Maven artifactId mappings](migration-steps.md#migration-serviceid-artifactid-mapping) | Add package name to Maven artifactId mapping topic. | April 17, 2024 |
| [Publish SDK metrics from the AWS SDK for Java 2.x](metrics.md) | Add configuration details to the metrics section. | April 12, 2024 |
| [Changes in the IAM Policy Builder API from version 1 to version 2](migration-iam-policy-builder.md) | Add IAM Policy Builder API migration information. | April 11, 2024 |
| [Configure HTTP proxies](http-config-proxy-support.md) | Update HTTP proxy information. | April 3, 2024 |
| [Securely acquire IAM role credentials](ec2-iam-roles.md#securely-read-IAM-role_credentials) | Add instructions to disable IMDSv1. | March 14, 2024 |
| [Migration step-by-step instructions with example](migration-steps.md) | Add step-by-step migration instructions. | March 8, 2024 |
| [Migrate from version 1.x to 2.x of the AWS SDK for Java](migration.md) | Update migration topic. | February, 14, 2024 |
| [Configure AWS CRT-based HTTP clients](http-configuration-crt.md) | Add information about the synchronous AWS CRT-based HTTP client. | January 5, 2024 |
| [Amazon Cognito Identity examples using SDK for Java 2.x](java_cognito-identity_code_examples.md) and [Amazon Cognito Identity Provider examples using SDK for Java 2.x](java_cognito-identity-provider_code_examples.md) | Amazon Cognito examples moved to Code Examples section. | December 28, 2023 |
| [OpenPGP key for the AWS SDK for Java](openpgp.md) | Provide current OpenPGP key. | December 6, 2023 |
| [Serialization differences between 1.x and 2.x of the AWS SDK for Java](migration-serialization-changes.md) | Describe serialization differences between v1 and v2 of the SDK for Java. | December 5, 2023 |
| [Migrate the Transfer Manager from version 1 to version 2 of the AWS SDK for Java](migration-s3-transfer-manager.md) | Add a section that details the changes in the S3 Transfer Manager from version 1 to version 2. | November 13, 2023 |
| [Data class annotations](ddb-en-client-anno-index.md) | Add a listing of data class annotations that can be used with the DynamoDB Enhanced Client.  | October 30, 2023 |
| [Migration status of libraries and utilities](migration-whats-different.md#migration-libraries-utilities) | Add information on the migration status of libraries and utilities from SDK for Java v1.x to v2.x | October 17, 2023 |
| [Set up a Gradle project that uses the AWS SDK for Java 2.x](setup-project-gradle.md) | Update the Gradle setup topic | October 17, 2023 |
| [Avoid saving null attributes of nested objects](ddb-en-client-adv-features-ignore-null.md) | Add information about the DynamoDB Enhanced Client @DynamoDbIgnoreNulls annotation. | September 22, 2023 |
| [Cross-Region access for Amazon S3](s3-cross-region.md) | Add information about cross-Region access to Amazon S3 buckets. | August 31, 2023 |
| [Preserve empty objects with `@DynamoDbPreserveEmptyObject`](ddb-en-client-adv-features-empty.md) | Add section that discusses the @DynamoDbPreserveEmptyObject annotation. | August 25, 2023 |
| [Making AWS service requests using the AWS SDK for Java 2.x](work-witih-clients.md) | Update service client section. | August 15, 2023 |
| [HTTP client recommendations](http-configuration.md#http-clients-recommend) | Since version 0.23, AWS CRT supports musl-based OS such as Alpine Linux. HTTP client recommendations now reflect the musl support. | August 11, 2023 |
| [Create IAM policies with the AWS SDK for Java 2.x](feature-iam-policy-builder.md) | Add IAM Policy Builder API section | July 31, 2023 |
| [Get Started using the DynamoDB Enhanced Client API](ddb-en-client-getting-started.md) | Correct several snippets in the Get Started section of the DynamoDB Enhanced Client topic. | July 24, 2023 |
| [Configure HTTP proxies](http-config-proxy-support.md) | Add HTTP proxy support information and examples for each HTTP client. | June 2, 2023 |
| Reorganize the table of contents | Promote [SDK for Java 2.x code examples](java_code_examples.md) section and [Calling AWS services from the AWS SDK for Java 2.x](work-with-services.md) to top-level TOC entries. | May 24, 2023 |
| [Add logging dependency](logging-slf4j.md#sdk-java-logging-classpath) | Show Gradle dependencies in logging section. | May 23, 2023 |
| [Using paginated results in the AWS SDK for Java 2.x](pagination.md) | Update pagination topic. | May 18, 2023 |
| [Set up a Gradle project that uses the AWS SDK for Java 2.x](setup-project-gradle.md) | Update Gradle project setup. | May 3, 2023 |
| [DynamoDB Enhanced Client API](dynamodb-enhanced-client.md) | Rewritten DynamoDB Enhanced Client API topic released. | April 28, 2023 |
| [Update get started tutorial instructions](get-started-tutorial.md#get-started-projectsetup) | Maven archetype modified to include option for credentialsProvider; instructions modified accordingly. | April 11, 2023 |
| [HTTP client recommendations](http-configuration.md#http-clients-recommend) | Add HTTP client decision guidance | March 30, 2023 |
| IAM best practices updates | Updated guide to align with the IAM best practices. For more information, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html). | March 14, 2023 |
| [Reload profile credentials](credentials-profiles.md#profile-reloading) | Add section on reloading profile credentials. | February 9, 2023 |
| [Configure AWS CRT-based HTTP clients](http-configuration-crt.md) | Update topic for GA release. | February 8, 2023 |
| [Work with Amazon EC2 instance metadata](examples-ec2-IMDS.md) | Add guided example for Java SDK client for Amazon S3 instance metadata service. | February 1, 2023 |
| [Use a performant S3 client: AWS CRT-based S3 client](crt-based-s3-client.md) | Add section for the AWS CRT-based S3 Client. | December 19, 2022 |
| [Transfer files and directories with the Amazon S3 Transfer Manager](transfer-manager.md) | Update Amazon S3 Transfer Manager examples for GA release. | December 19, 2022 |
| [Best practices for using the AWS SDK for Java 2.x](best-practices.md) | Added best practices section. | November 18, 2022 |
| [Load credentials from an external process using the AWS SDK for Java 2.x](credentials-process.md) | Added section on loading credentials from an external process. | November 15, 2022 |
| [AWS SDK for Java 2.x: Comprehensive Metrics Reference](metrics-list.md) | Updated metric listing with HTTP client usage requirement. | November 9, 2022 |
| [Transfer files and directories with the Amazon S3 Transfer Manager](transfer-manager.md) | Example code corrected. | November 2, 2022 |
| [Reduce SDK startup time for AWS Lambda](lambda-optimize-starttime.md) | Updated section with additional options to reduce Lambda startup time. | November 1, 2022 |
| [Configure HTTP clients in the AWS SDK for Java 2.x](http-configuration.md) | Added configuration information to cover all HTTP clients in the SDK. | October 26, 2022 |
| [Logging with the SDK for Java 2.x](logging-slf4j.md) | Updated logging topic to include wire logging details for all HTTP clients. | October 4, 2022 |
|  [AWS database services and AWS SDK for Java 2.x](examples-databases.md)  | Added overview section of AWS database services and the SDK for Java 2.x. | September 13, 2022 |
| [EC2-Classic Networking is Retiring](https://aws.amazon.com/blogs/aws/ec2-classic-is-retiring-heres-how-to-prepare)  | EC2-Classic is retiring on August 15, 2022. | July 28, 2022 |
|  [Additional authentication options](get-started-auth.md#setup-additional)  | Update to dependency required for single sign-on authentication. | July 18, 2022 |
|  [Working with TLS in the SDK for Java](security-java-tls.md)  | Update TLS security information. | April 8, 2022 |
|  [Additional authentication options](get-started-auth.md#setup-additional)  | Added more information about setting up and using credentials. | February 22, 2021 |
|  [Set up a GraalVM Native Image project that uses the AWS SDK for Java 2.x](setup-project-graalvm.md)  | New topic for setting up a GraalVM Native Image project. | February 18, 2021 |
|  [Using waiters in the AWS SDK for Java 2.x](waiters.md)  | Waiters released; added topic for the new feature. | September 30, 2020 |
|  [Publish SDK metrics from the AWS SDK for Java 2.x](metrics.md)  | Metrics released; added topic for the new feature. | August 17, 2020 |
| [Work with Amazon Simple Notification Service](examples-simple-notification-service.md)  | Added example topics for Amazon SNS. | May 30, 2020 |
|  [Reduce SDK startup time for AWS Lambda](lambda-optimize-starttime.md)  | Added AWS Lambda function performance topic. | May 29, 2020 |
|  [Set the JVM TTL for DNS name lookups](jvm-ttl-dns.md)  | Added JVM TTL DNS caching topic. | April 27, 2020 |
|  [Set up an Apache Maven project that uses the AWS SDK for Java 2.x](setup-project-maven.md), [Set up a Gradle project that uses the AWS SDK for Java 2.x](setup-project-gradle.md)  | New Maven and Gradle set up topics. | April 21, 2020 |
|  [Working with TLS in the SDK for Java](security-java-tls.md)  | Added TLS 1.2 to security section. | March 19, 2020 |
|  [Subscribe to Amazon Kinesis Data Streams](examples-kinesis-stream.md)  | Added Kinesis stream examples. | August 2, 2018 |
|  [Using paginated results in the AWS SDK for Java 2.x](pagination.md)  | Added auto pagination topic. | April 5, 2018 |
|  [Calling AWS services from the AWS SDK for Java 2.x](work-with-services.md) | Added example topics for IAM, Amazon EC2, CloudWatch and DynamoDB. | December 29, 2017 |
|  [Work with Amazon S3](examples-s3.md)  | Added getobjects example for Amazon S3. | August 7, 2017 |
|  [Programming asynchronously using the AWS SDK for Java 2.x](asynchronous.md)  | Added async topic. | August 4, 2017 |
| GA release of the [AWS SDK for Java 2.x](https://aws.amazon.com/sdk-for-java/)  |  AWS SDK for Java version 2 (v2) released. | June 28, 2017 |
