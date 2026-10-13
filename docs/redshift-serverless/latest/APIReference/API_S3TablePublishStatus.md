---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_S3TablePublishStatus.html
---

# S3TablePublishStatus
<a name="API_S3TablePublishStatus"></a>

Describes the state of Amazon S3 Tables system-table log publishing for a namespace.

## Contents
<a name="API_S3TablePublishStatus_Contents"></a>

 ** enabledAll **   <a name="redshiftserverless-Type-S3TablePublishStatus-enabledAll"></a>
 `true` when the namespace is enrolled in every current and future system table rather than an explicit list of tables.
Type: Boolean
Required: No

 ** lastIngestionTimes **   <a name="redshiftserverless-Type-S3TablePublishStatus-lastIngestionTimes"></a>
A map of system table name to the time that table last received data, as an ISO-8601 timestamp. A table that has not yet been ingested is absent from the map. Use it to judge data freshness.
Type: String to string map
Required: No

 ** s3TableGranularity **   <a name="redshiftserverless-Type-S3TablePublishStatus-s3TableGranularity"></a>
The scope currently in effect. Values are `namespace` or `account`.
Type: String
Valid Values: `namespace | account`
Required: No

 ** s3TableNamespace **   <a name="redshiftserverless-Type-S3TablePublishStatus-s3TableNamespace"></a>
The identifier of the namespace in the S3 table bucket that holds the published tables.
Type: String
Required: No

 ** s3Tables **   <a name="redshiftserverless-Type-S3TablePublishStatus-s3Tables"></a>
The system tables currently being published.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 256 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(all|sys_[a-z0-9_]+)`
Required: No

## See Also
<a name="API_S3TablePublishStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/S3TablePublishStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/S3TablePublishStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/S3TablePublishStatus)
