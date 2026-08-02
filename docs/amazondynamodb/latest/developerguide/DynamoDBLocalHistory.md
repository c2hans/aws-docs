---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocalHistory.html
---

# Release history for DynamoDB local
<a name="DynamoDBLocalHistory"></a>

The following table describes the important changes in each release of *DynamoDB local*.

****

| Version | Change | Description | Date |
| --- | --- | --- | --- |
| 3.3.0 | Adding multi-attribute key support for Global Secondary Indexes |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocalHistory.html)  | January 19, 2026 |
| 3.2.0 | Fixed Compatibility Issues with multiple Kotlin Versions |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocalHistory.html)  | January 09, 2026 |
| 3.1.0 | Improving performance for PartiQL Queries, Including Joda-time dependency |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocalHistory.html)  | September 14, 2025 |
| 3.0.0 | Migrating from AWS SDK Java V1 to V2 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocalHistory.html)  | July 17, 2025 |
| 2.6.0 | Support table ARN as table name in DynamoDB APIs<br />Performance fix and security updates |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocalHistory.html)  | March 13, 2025 |
| 2.5.4 | Upgrading to Jetty Dependencies |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocalHistory.html)  | December 12, 2024 |
| 2.5.3 | Upgrading Jackson Dependencies to 2.17.x in Log4j Core (Resolves CVE-2022-1471) |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocalHistory.html)  | November 6, 2024 |
| 2.5.2 | Bug fix for Update table workflow | [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocalHistory.html)  | June 20, 2024 |
| 2.5.1 | Patch for bugs introduced in OndemandThroughPut feature  | [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocalHistory.html) | June 5, 2024 |
| 2.5.0 | Support for configurable maximum throughput for on-demand tables, `ReturnValuesOnConditionCheckFailure`, `BatchExecuteStatement`, and `ExecuteTransactionRequest` |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocalHistory.html)  | May 28, 2024 |
| 2.4.0 | Support for `ReturnValuesOnConditionCheckFailure` - Embedded Mode |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocalHistory.html)  | April 17, 2024 |
| 2.3.0 | Jetty and JDK Upgrade |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocalHistory.html)  | March 14, 2024 |
| 2.2.0 | Added support for table deletion protection and the `ReturnValuesOnConditionCheckFailure` parameter |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocalHistory.html)  | December 14, 2023 |
| 2.1.0 | Support for SQLLite Native Libraries for Maven projects and adding telemetry |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocalHistory.html)  | October 23, 2023 |
| 2.0.0 | Migrating from javax to jakarta namespace and JDK11 Support |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocalHistory.html)  | July 5, 2023 |
| 1.25.1 | Upgrading Jackson Dependencies to 2.17.x in Log4j Core (Resolves CVE-2022-1471) | Upgrading Jackson Dependencies to 2.17.x in Log4j Core (Resolves CVE-2022-1471) to address a critical security vulnerability in the SnakeYAML library, which is a transitive dependency | November 6, 2024 |
| 1.25.0 | Added support for table deletion protection and the `ReturnValuesOnConditionCheckFailure` parameter |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocalHistory.html)  | December 18, 2023 |
| 1.24.0 | Support for SQLLite Native Libraries for Maven projects and adding telemetry |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocalHistory.html)  | October 23, 2023 |
| 1.23.0 | Handle invalid access and secret key while server startup |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocalHistory.html)  | June 28, 2023 |
| 1.22.0 | Support of Limit Operation for PartiQL |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocalHistory.html)  | June 8, 2023 |
| 1.21.0 | Support for 100 actions per transaction |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocalHistory.html)  | January 26, 2023 |
| 1.20.0 | Added support for M1 Mac |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocalHistory.html)  | September 12, 2022 |
| 1.19.0 | Upgraded the PartiQL Parser | Upgraded the PartiQL Parser and other related libraries | July 27, 2022 |
| 1.18.0 | Upgraded log4j-core and Jackson-core | Upgraded log4j-core to 2.17.1 and Jackson-core 2.10.x to 2.12.0 | January 10, 2022 |
| 1.17.2 | Upgraded log4j-core | Upgraded log4j-core dependency to version 2.16 | January 16, 2021 |
| 1.17.1 | Upgraded log4j-core | Updated log4j-core dependency to patch zero-day exploit to prevent remote code execution - Log4Shel | January 10, 2021 |
| 1.17.0 | Deprecated Javascript Web Shell |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocalHistory.html)  | January 8, 2021 |
