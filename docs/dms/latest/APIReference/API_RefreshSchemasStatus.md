---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_RefreshSchemasStatus.html
---

# RefreshSchemasStatus
<a name="API_RefreshSchemasStatus"></a>

Provides information that describes status of a schema at an endpoint specified by the `DescribeRefreshSchemaStatus` operation.

## Contents
<a name="API_RefreshSchemasStatus_Contents"></a>

 ** EndpointArn **   <a name="DMS-Type-RefreshSchemasStatus-EndpointArn"></a>
The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.
Type: String
Required: No

 ** LastFailureMessage **   <a name="DMS-Type-RefreshSchemasStatus-LastFailureMessage"></a>
The last failure message for the schema.
Type: String
Required: No

 ** LastRefreshDate **   <a name="DMS-Type-RefreshSchemasStatus-LastRefreshDate"></a>
The date the schema was last refreshed.
Type: Timestamp
Required: No

 ** ReplicationInstanceArn **   <a name="DMS-Type-RefreshSchemasStatus-ReplicationInstanceArn"></a>
The Amazon Resource Name (ARN) of the replication instance.
Type: String
Required: No

 ** Status **   <a name="DMS-Type-RefreshSchemasStatus-Status"></a>
The status of the schema.
Type: String
Valid Values: `successful | failed | refreshing`
Required: No

## See Also
<a name="API_RefreshSchemasStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/RefreshSchemasStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/RefreshSchemasStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/RefreshSchemasStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
