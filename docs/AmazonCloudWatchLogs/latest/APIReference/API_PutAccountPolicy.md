---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutAccountPolicy.html
---

# PutAccountPolicy
<a name="API_PutAccountPolicy"></a>

Creates an account-level data protection policy, subscription filter policy, field index policy, transformer policy, or metric extraction policy that applies to all log groups, a subset of log groups, or a data source name and type combination in the account.

**Important**
 `PutAccountPolicy` is an account-wide administrative operation intended for CloudWatch Logs administrators. Because it affects all log groups (or a broad subset) in the account, you should grant `logs:PutAccountPolicy` permissions only to administrators who manage logging configuration across the account, not to application teams or individual log group owners.

 **Conflict resolution between account-level and log-group-level policies**

When both an account-level policy and a log-group-level policy of the same type apply to a log group, the resolution depends on the policy type:
+  *Data protection* — The two policies are cumulative. Any sensitive term specified in either the account-level or the log-group-level policy is masked.
+  *Subscription filters* — Account-level and log-group-level subscription filters are additive. A log group can have up to 1 account-level and up to 2 log-group-level subscription filters.
+  *Transformers* — A log-group-level transformer overrides the account-level transformer. If a log group has its own transformer, it ignores the account-level transformer policy.
+  *Field index policies* — If a log group has its own field index policy (created with `PutIndexPolicy`), any account-level policy that uses `LogGroupNamePrefix` selection criteria or has no selection criteria is ignored for that log group. However, account-level policies that use `DataSourceName` and `DataSourceType` selection criteria still apply alongside the log-group-level policy.
+  *Metric extraction policies* — Metric extraction policies are account-level only and have no log-group-level equivalent, so no conflict resolution applies.

For field index policies, you can configure indexed fields as *facets* to enable interactive exploration of your logs. Facets provide value distributions and counts for indexed fields in the CloudWatch Logs Insights console without requiring query execution. For more information, see [Use facets to group and explore logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Facets.html).

To use this operation, you must be signed on with the correct permissions depending on the type of policy that you are creating.
+ To create a data protection policy, you must have the `logs:PutDataProtectionPolicy` and `logs:PutAccountPolicy` permissions.
+ To create a subscription filter policy, you must have the `logs:PutSubscriptionFilter` and `logs:PutAccountPolicy` permissions.
+ To create a transformer policy, you must have the `logs:PutTransformer` and `logs:PutAccountPolicy` permissions.
+ To create a field index policy, you must have the `logs:PutIndexPolicy` and `logs:PutAccountPolicy` permissions.
+ To configure facets for field index policies, you must have the `logs:PutIndexPolicy` and `logs:PutAccountPolicy` permissions.
+ To create a metric extraction policy, you must have the `logs:PutMetricExtractionPolicy` and `logs:PutAccountPolicy` permissions.

 **Data protection policy**

A data protection policy can help safeguard sensitive data that's ingested by your log groups by auditing and masking the sensitive log data. Each account can have only one account-level data protection policy.

**Important**
Sensitive data is detected and masked when it is ingested into a log group. When you set a data protection policy, log events ingested into the log groups before that time are not masked.

If you use `PutAccountPolicy` to create a data protection policy for your whole account, it applies to both existing log groups and all log groups that are created later in this account. The account-level policy is applied to existing log groups with eventual consistency. It might take up to 5 minutes before sensitive data in existing log groups begins to be masked.

By default, when a user views a log event that includes masked data, the sensitive data is replaced by asterisks. A user who has the `logs:Unmask` permission can use a [GetLogEvents](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLogEvents.html) or [FilterLogEvents](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_FilterLogEvents.html) operation with the `unmask` parameter set to `true` to view the unmasked log events. Users with the `logs:Unmask` can also view unmasked data in the CloudWatch Logs console by running a CloudWatch Logs Insights query with the `unmask` query command.

For more information, including a list of types of data that can be audited and masked, see [Protect sensitive log data with masking](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html).

To use the `PutAccountPolicy` operation for a data protection policy, you must be signed on with the `logs:PutDataProtectionPolicy` and `logs:PutAccountPolicy` permissions.

The `PutAccountPolicy` operation applies to all log groups in the account. You can use [PutDataProtectionPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDataProtectionPolicy.html) to create a data protection policy that applies to just one log group. If a log group has its own data protection policy and the account also has an account-level data protection policy, then the two policies are cumulative. Any sensitive term specified in either policy is masked.

 **Subscription filter policy**

A subscription filter policy sets up a real-time feed of log events from CloudWatch Logs to other AWS services. Account-level subscription filter policies apply to both existing log groups and log groups that are created later in this account. Supported destinations are Kinesis Data Streams, Firehose, and Lambda. When log events are sent to the receiving service, they are Base64 encoded and compressed with the GZIP format.

The following destinations are supported for subscription filters:
+ An Kinesis Data Streams data stream in the same account as the subscription policy, for same-account delivery.
+ An Firehose data stream in the same account as the subscription policy, for same-account delivery.
+ A Lambda function in the same account as the subscription policy, for same-account delivery.
+ A logical destination in a different account created with [PutDestination](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDestination.html), for cross-account delivery. Kinesis Data Streams and Firehose are supported as logical destinations.

Each account can have one account-level subscription filter policy per Region. If you are updating an existing filter, you must specify the correct name in `PolicyName`. To perform a `PutAccountPolicy` subscription filter operation for any destination except a Lambda function, you must also have the `iam:PassRole` permission.

 **Transformer policy**

Creates or updates a *log transformer policy* for your account. You use log transformers to transform log events into a different format, making them easier for you to process and analyze. You can also transform logs from different sources into standardized formats that contain relevant, source-specific information. After you have created a transformer, CloudWatch Logs performs this transformation at the time of log ingestion. You can then refer to the transformed versions of the logs during operations such as querying with CloudWatch Logs Insights or creating metric filters or subscription filters.

You can also use a transformer to copy metadata from metadata keys into the log events themselves. This metadata can include log group name, log stream name, account ID and Region.

A transformer for a log group is a series of processors, where each processor applies one type of transformation to the log events ingested into this log group. For more information about the available processors to use in a transformer, see [ Processors that you can use](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-Processors).

Having log events in standardized format enables visibility across your applications for your log analysis, reporting, and alarming needs. CloudWatch Logs provides transformation for common log types with out-of-the-box transformation templates for major AWS log sources such as VPC flow logs, Lambda, and Amazon RDS. You can use pre-built transformation templates or create custom transformation policies.

You can create transformers only for the log groups in the Standard log class.

You can have one account-level transformer policy that applies to all log groups in the account. Or you can create as many as 20 account-level transformer policies that are each scoped to a subset of log groups with the `selectionCriteria` parameter. If you have multiple account-level transformer policies with selection criteria, no two of them can use the same or overlapping log group name prefixes. For example, if you have one policy filtered to log groups that start with `my-log`, you can't have another transformer policy filtered to `my-logpprod` or `my-logging`.

You can also set up a transformer at the log-group level. For more information, see [PutTransformer](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutTransformer.html). If there is both a log-group level transformer created with `PutTransformer` and an account-level transformer that could apply to the same log group, the log group uses only the log-group level transformer. It ignores the account-level transformer.

 **Field index policy**

You can use field index policies to create indexes on fields found in log events for a log group or data source name and type combination. Creating field indexes can help lower the scan volume for CloudWatch Logs Insights queries that reference those fields, because these queries attempt to skip the processing of log events that are known to not match the indexed field. Good fields to index are fields that you often need to query for and fields or values that match only a small fraction of the total log events. Common examples of indexes include request ID, session ID, user IDs, or instance IDs. For more information, see [Create field indexes to improve query performance and reduce costs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Field-Indexing.html)

To find the fields that are in your log group events, use the [GetLogGroupFields](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLogGroupFields.html) operation. To find the fields for a data source use the [GetLogFields](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLogFields.html) operation.

For example, suppose you have created a field index for `requestId`. Then, any CloudWatch Logs Insights query on that log group that includes `requestId = value ` or `requestId in [value, value, ...]` will attempt to process only the log events where the indexed field matches the specified value.

Matches of log events to the names of indexed fields are case-sensitive. For example, an indexed field of `RequestId` won't match a log event containing `requestId`.

You can have one account-level field index policy that applies to all log groups in the account. Or you can create as many as 20 account-level field index policies that are each scoped to a subset of log groups using `LogGroupNamePrefix` with the `selectionCriteria` parameter. You can have another 20 account-level field index policies using `DataSourceName` and `DataSourceType` for the `selectionCriteria` parameter. If you have multiple account-level index policies with `LogGroupNamePrefix` selection criteria, no two of them can use the same or overlapping log group name prefixes. For example, if you have one policy filtered to log groups that start with *my-log*, you can't have another field index policy filtered to *my-logpprod* or *my-logging*. Similarly, if you have multiple account-level index policies with `DataSourceName` and `DataSourceType` selection criteria, no two of them can use the same data source name and type combination. For example, if you have one policy filtered to the data source name `amazon_vpc` and data source type `flow` you cannot create another policy with this combination.

If you create an account-level field index policy in a monitoring account in cross-account observability, the policy is applied only to the monitoring account and not to any source accounts.

CloudWatch Logs provides default field indexes for all log groups in the Standard log class. Default field indexes are automatically available for the following fields:
+  `@logStream`
+  `@aws.region`
+  `@aws.account`
+  `@source.log`
+  `@data_source_name`
+  `@data_source_type`
+  `@data_format`
+  `traceId`
+  `severityText`
+  `attributes.session.id`

CloudWatch Logs provides default field indexes for certain data source name and type combinations as well. Default field indexes are automatically available for the following data source name and type combinations as identified in the following list:

 `amazon_vpc.flow`
+  `action`
+  `logStatus`
+  `region`
+  `flowDirection`
+  `type`

 `amazon_route53.resolver_query`
+  `transport`
+  `rcode`

 `aws_waf.access`
+  `action`
+  `httpRequest.country`

 `aws_cloudtrail.data`, `aws_cloudtrail.management`
+  `eventSource`
+  `eventName`
+  `awsRegion`
+  `userAgent`
+  `errorCode`
+  `eventType`
+  `managementEvent`
+  `readOnly`
+  `eventCategory`
+  `requestId`

Default field indexes are in addition to any custom field indexes you define within your policy. Default field indexes are not counted towards your [field index quota](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Field-Indexing-Syntax).

If you want to create a field index policy for a single log group, you can use [PutIndexPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutIndexPolicy.html) instead of `PutAccountPolicy`. If you do so, that log group will use that log-group level policy and any account-level policies that match at the data source level; any account-level policy that matches at the log group level (for example, no selection criteria or log group name prefix selection criteria) will be ignored.

 **Metric extraction policy**

A metric extraction policy controls whether CloudWatch Metrics can be created through the Embedded Metrics Format (EMF) for log groups in your account. By default, EMF metric creation is enabled for all log groups. You can use metric extraction policies to disable EMF metric creation for your entire account or specific log groups.

When a policy disables EMF metric creation for a log group, log events in the EMF format are still ingested, but no CloudWatch Metrics are created from them.

**Important**
Creating a policy disables metrics for AWS features that use EMF to create metrics, such as CloudWatch Container Insights and CloudWatch Application Signals. To prevent turning off those features by accident, we recommend that you exclude the underlying log-groups through a selection-criteria such as `LogGroupNamePrefix NOT IN ["/aws/containerinsights", "/aws/ecs/containerinsights", "/aws/application-signals/data"]`.

Each account can have either one account-level metric extraction policy that applies to all log groups, or up to 5 policies that are each scoped to a subset of log groups with the `selectionCriteria` parameter. The selection criteria supports filtering by `LogGroupName` and `LogGroupNamePrefix` using the operators `IN` and `NOT IN`. You can specify up to 50 values in each `IN` or `NOT IN` list.

The selection criteria can be specified in these formats:

 `LogGroupName IN ["log-group-1", "log-group-2"]`

 `LogGroupNamePrefix NOT IN ["/aws/prefix1", "/aws/prefix2"]`

If you have multiple account-level metric extraction policies with selection criteria, no two of them can have overlapping criteria. For example, if you have one policy with selection criteria `LogGroupNamePrefix IN ["my-log"]`, you can't have another metric extraction policy with selection criteria `LogGroupNamePrefix IN ["/my-log-prod"]` or `LogGroupNamePrefix IN ["/my-logging"]`, as the set of log groups matching these prefixes would be a subset of the log groups matching the first policy's prefix, creating an overlap.

When using `NOT IN`, only one policy with this operator is allowed per account.

When combining policies with `IN` and `NOT IN` operators, the overlap check ensures that policies don't have conflicting effects. Two policies with `IN` and `NOT IN` operators do not overlap if and only if every value in the `IN `policy is completely contained within some value in the `NOT IN` policy. For example:
+ If you have a `NOT IN` policy for prefix `"/aws/lambda"`, you can create an `IN` policy for the exact log group name `"/aws/lambda/function1"` because the set of log groups matching `"/aws/lambda/function1"` is a subset of the log groups matching `"/aws/lambda"`.
+ If you have a `NOT IN` policy for prefix `"/aws/lambda"`, you cannot create an `IN` policy for prefix `"/aws"` because the set of log groups matching `"/aws"` is not a subset of the log groups matching `"/aws/lambda"`.

## Request Syntax
<a name="API_PutAccountPolicy_RequestSyntax"></a>

```
{
   "policyDocument": "{{string}}",
   "policyName": "{{string}}",
   "policyType": "{{string}}",
   "scope": "{{string}}",
   "selectionCriteria": "{{string}}"
}
```

## Request Parameters
<a name="API_PutAccountPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [policyDocument](#API_PutAccountPolicy_RequestSyntax) **   <a name="CWL-PutAccountPolicy-request-policyDocument"></a>
Specify the policy, in JSON.
 **Data protection policy**
A data protection policy must include two JSON blocks:
+ The first block must include both a `DataIdentifer` array and an `Operation` property with an `Audit` action. The `DataIdentifer` array lists the types of sensitive data that you want to mask. For more information about the available options, see [Types of data that you can mask](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data-types.html).

  The `Operation` property with an `Audit` action is required to find the sensitive data terms. This `Audit` action must contain a `FindingsDestination` object. You can optionally use that `FindingsDestination` object to list one or more destinations to send audit findings to. If you specify destinations such as log groups, Firehose streams, and S3 buckets, they must already exist.
+ The second block must include both a `DataIdentifer` array and an `Operation` property with an `Deidentify` action. The `DataIdentifer` array must exactly match the `DataIdentifer` array in the first block of the policy.

  The `Operation` property with the `Deidentify` action is what actually masks the data, and it must contain the ` "MaskConfig": {}` object. The ` "MaskConfig": {}` object must be empty.
For an example data protection policy, see the **Examples** section on this page.
The contents of the two `DataIdentifer` arrays must match exactly.
In addition to the two JSON blocks, the `policyDocument` can also include `Name`, `Description`, and `Version` fields. The `Name` is different than the operation's `policyName` parameter, and is used as a dimension when CloudWatch Logs reports audit findings metrics to CloudWatch.
The JSON specified in `policyDocument` can be up to 30,720 characters long.
 **Subscription filter policy**
A subscription filter policy can include the following attributes in a JSON block:
+  **DestinationArn** The ARN of the destination to deliver log events to. Supported destinations are:
  + An Kinesis Data Streams data stream in the same account as the subscription policy, for same-account delivery.
  + An Firehose data stream in the same account as the subscription policy, for same-account delivery.
  + A Lambda function in the same account as the subscription policy, for same-account delivery.
  + A logical destination in a different account created with [PutDestination](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDestination.html), for cross-account delivery. Kinesis Data Streams and Firehose are supported as logical destinations.
+  **RoleArn** The ARN of an IAM role that grants CloudWatch Logs permissions to deliver ingested log events to the destination stream. You don't need to provide the ARN when you are working with a logical destination for cross-account delivery.
+  **FilterPattern** A filter pattern for subscribing to a filtered stream of log events.
+  **Distribution** The method used to distribute log data to the destination. By default, log data is grouped by log stream, but the grouping can be set to `Random` for a more even distribution. This property is only applicable when the destination is an Kinesis Data Streams data stream.
 **Transformer policy**
A transformer policy must include one JSON block with the array of processors and their configurations. For more information about available processors, see [ Processors that you can use](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-Processors).
 **Field index policy**
A field index filter policy can include the following attribute in a JSON block:
+  **Fields** The array of field indexes to create.
+  **FieldsV2** The object of field indexes to create along with it's type.
It must contain at least one field index.
The following is an example of an index policy document that creates indexes with different types.
 `"policyDocument": "{ \"Fields\": [ \"TransactionId\" ], \"FieldsV2\": {\"RequestId\": {\"type\": \"FIELD_INDEX\"}, \"APIName\": {\"type\": \"FACET\"}, \"StatusCode\": {\"type\": \"FACET\"}}}"`
You can use `FieldsV2` to specify the type for each field. Supported types are `FIELD_INDEX` and `FACET`. Field names within `Fields` and `FieldsV2` must be mutually exclusive.
Type: String
Required: Yes

 ** [policyName](#API_PutAccountPolicy_RequestSyntax) **   <a name="CWL-PutAccountPolicy-request-policyName"></a>
A name for the policy. This must be unique within the account and cannot start with `aws/`.
Type: String
Required: Yes

 ** [policyType](#API_PutAccountPolicy_RequestSyntax) **   <a name="CWL-PutAccountPolicy-request-policyType"></a>
The type of policy that you're creating or updating.
Type: String
Valid Values: `DATA_PROTECTION_POLICY | SUBSCRIPTION_FILTER_POLICY | FIELD_INDEX_POLICY | TRANSFORMER_POLICY | METRIC_EXTRACTION_POLICY`
Required: Yes

 ** [scope](#API_PutAccountPolicy_RequestSyntax) **   <a name="CWL-PutAccountPolicy-request-scope"></a>
Currently the only valid value for this parameter is `ALL`, which specifies that the data protection policy applies to all log groups in the account. If you omit this parameter, the default of `ALL` is used.
Type: String
Valid Values: `ALL`
Required: No

 ** [selectionCriteria](#API_PutAccountPolicy_RequestSyntax) **   <a name="CWL-PutAccountPolicy-request-selectionCriteria"></a>
Use this parameter to apply the new policy to a subset of log groups in the account or a data source name and type combination.
Specifying `selectionCriteria` is valid only when you specify `SUBSCRIPTION_FILTER_POLICY`, `FIELD_INDEX_POLICY` or `TRANSFORMER_POLICY`for `policyType`.
+ If `policyType` is `SUBSCRIPTION_FILTER_POLICY`, the only supported `selectionCriteria` filter is `LogGroupName NOT IN []`
+ If `policyType` is `TRANSFORMER_POLICY`, the only supported `selectionCriteria` filter is `LogGroupNamePrefix`
+ If `policyType` is `FIELD_INDEX_POLICY`, the supported `selectionCriteria` filters are:
  +  `LogGroupNamePrefix`
  +  `DataSourceName` AND `DataSourceType`

  When you specify `selectionCriteria` for a field index policy you can use either `LogGroupNamePrefix` by itself or `DataSourceName` and `DataSourceType` together.
The `selectionCriteria` string can be up to 25KB in length. The length is determined by using its UTF-8 bytes.
Using the `selectionCriteria` parameter with `SUBSCRIPTION_FILTER_POLICY` is useful to help prevent infinite loops. For more information, see [Log recursion prevention](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Subscriptions-recursion-prevention.html).
Type: String
Required: No

## Response Syntax
<a name="API_PutAccountPolicy_ResponseSyntax"></a>

```
{
   "accountPolicy": {
      "accountId": "string",
      "lastUpdatedTime": number,
      "policyDocument": "string",
      "policyName": "string",
      "policyType": "string",
      "scope": "string",
      "selectionCriteria": "string"
   }
}
```

## Response Elements
<a name="API_PutAccountPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accountPolicy](#API_PutAccountPolicy_ResponseSyntax) **   <a name="CWL-PutAccountPolicy-response-accountPolicy"></a>
The account policy that you created.
Type: [AccountPolicy](API_AccountPolicy.md) object

## Errors
<a name="API_PutAccountPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
A parameter is specified incorrectly.
HTTP Status Code: 400

 ** LimitExceededException **
You have reached the maximum number of resources that can be created.
HTTP Status Code: 400

 ** OperationAbortedException **
Multiple concurrent requests to update the same resource were in conflict.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

## Examples
<a name="API_PutAccountPolicy_Examples"></a>

### To create a log transformer policy
<a name="API_PutAccountPolicy_Example_1"></a>

The following example creates a log transformer that applies to log groups have names that start with `test-`

#### Sample Request
<a name="API_PutAccountPolicy_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: logs.<region>.<domain>
X-Amz-Date: <DATE>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Accept: application/json
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: Logs_20140328.PutAccountPolicy
{
    "policyName": "ExamplePolicy",
    "policyType": "TRANSFORMER_POLICY",
    "policyDocument": [
        {
            "parseJSON": {}
        },
        {
            "addKeys": {
                "entries": [
                    {
                        "key": "metadata.transformed_in",
                        "value": "CloudWatchLogs"
                    }
                ]
            }
        },
        {
            "trimString": {
                "withKeys": [
                    "status"
                ]
            }
        },
        {
            "lowerCaseString": {
                "withKeys": [
                    "status"
                ]
            }
        }
    ],
	"selectionCriteria": 'LogGroupNamePrefix= "test-"'
}
```

### To create a metric extraction policy
<a name="API_PutAccountPolicy_Example_2"></a>

The following example creates a metric extraction policy that disables EMF metric creation for all log groups except Container Insights log groups.

#### Sample Request
<a name="API_PutAccountPolicy_Example_2_Request"></a>

```
POST / HTTP/1.1
Host: logs.<region>.<domain>
X-Amz-Date: <DATE>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Accept: application/json
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: Logs_20140328.PutAccountPolicy
{
    "policyName": "DisableEMFMetrics",
    "policyType": "METRIC_EXTRACTION_POLICY",
    "policyDocument": {
        "EmbeddedMetricFormat": {
            "Status": "Disabled"
        }
    },
    "selectionCriteria": 'LogGroupNamePrefix NOT IN ["/aws/containerinsights", "/aws/ecs/containerinsights"]'
}
```

### To create an account-wide data protection policy
<a name="API_PutAccountPolicy_Example_3"></a>

The following example creates an account-wide log group data protection policy.

#### Sample Request
<a name="API_PutAccountPolicy_Example_3_Request"></a>

```
POST / HTTP/1.1
Host: logs.<region>.<domain>
X-Amz-Date: <DATE>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Accept: application/json
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: Logs_20140328.PutAccountPolicy
{
    "policyName": "my_global_data_protection_policy",
    "policyType": "GLOBAL",
    "policyDocument": {
        "Description": "test description",
        "Version": "2021-06-01",
        "Statement": [
            {
                "Sid": "audit-policy test",
                "DataIdentifier": [
                    "arn:aws:dataprotection::aws:data-identifier/EmailAddress",
                    "arn:aws:dataprotection::aws:data-identifier/DriversLicense-US"
                ],
                "Operation": {
                    "Audit": {
                        "FindingsDestination": {
                            "CloudWatchLogs": {
                                "LogGroup": "EXISTING_LOG_GROUP_IN_YOUR_ACCOUNT"
                            },
                            "Firehose": {
                                "DeliveryStream": "EXISTING_STREAM_IN_YOUR_ACCOUNT"
                            },
                            "S3": {
                                "Bucket": "EXISTING_BUCKET"
                            }
                        }
                    }
                }
            },
            {
            {
                "Sid": "redact-policy",
                "DataIdentifier": [
                    "arn:aws:dataprotection::aws:data-identifier/EmailAddress",
                    "arn:aws:dataprotection::aws:data-identifier/DriversLicense-US"
                ],
                "Operation": {
                    "Deidentify": {
                        "MaskConfig": {}
                    }
                }
            }
        ]
    }
}
```

### To create an account-wide subscription filter policy
<a name="API_PutAccountPolicy_Example_4"></a>

The following example creates an account-wide subscription filter policy that forwards log events containing the string `ERROR` to a Kinesis Data Streams stream. The policy applies to all log groups in the account except for `LogGroupToExclude1` and `LogGroupToExclude12`.

#### Sample Request
<a name="API_PutAccountPolicy_Example_4_Request"></a>

```
POST / HTTP/1.1
Host: logs.<region>.<domain>
X-Amz-Date: <DATE>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Accept: application/json
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: Logs_20140328.PutAccountPolicy
{
    "policyName": "ExamplePolicy",
    "policyType": "SUBSCRIPTION_FILTER_POLICY",
    "policyDocument": {
        "DestinationArn":"arn:aws:kinesis:region:111111111111:stream/TestStream",
        "RoleArn":"arn:aws:iam::111111111111:role/CWLtoKinesisRole",
        "FilterPattern": "ERROR",
        "Distribution": "Random"
    },
    "selectionCriteria": 'LogGroupName NOT IN ["LogGroupToExclude1", "LogGroupToExclude2"]'
}
```

### To create an account-wide field index policy
<a name="API_PutAccountPolicy_Example_5"></a>

The following example creates an account-wide field index policy for log groups with names that start with `lambda`.

#### Sample Request
<a name="API_PutAccountPolicy_Example_5_Request"></a>

```
POST / HTTP/1.1
Host: logs.<region>.<domain>
X-Amz-Date: <DATE>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Accept: application/json
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: Logs_20140328.PutAccountPolicy
{
    "policyDocument": {
        "Fields": ["RequestId", "TransactionId"]
     },
    "policyName": "LambdaIndexPolicy",
    "policyType" : "FIELD_INDEX_POLICY",
    "scope" : "ALL",
    "selectionCriteria": 'LogGroupNamePrefix="lambda"'
}
```

## See Also
<a name="API_PutAccountPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/PutAccountPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/PutAccountPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/PutAccountPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/PutAccountPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/PutAccountPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/PutAccountPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/PutAccountPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/PutAccountPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/PutAccountPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/PutAccountPolicy)
