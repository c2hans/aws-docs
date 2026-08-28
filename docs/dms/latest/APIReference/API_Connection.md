---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_Connection.html
---

# Connection
<a name="API_Connection"></a>

Status of the connection between an endpoint and a replication instance, including Amazon Resource Names (ARNs) and the last error message issued.

## Contents
<a name="API_Connection_Contents"></a>

 ** EndpointArn **   <a name="DMS-Type-Connection-EndpointArn"></a>
The ARN string that uniquely identifies the endpoint.
Type: String
Required: No

 ** EndpointIdentifier **   <a name="DMS-Type-Connection-EndpointIdentifier"></a>
The identifier of the endpoint. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen or contain two consecutive hyphens.
Type: String
Required: No

 ** LastFailureMessage **   <a name="DMS-Type-Connection-LastFailureMessage"></a>
The error message when the connection last failed.
Type: String
Required: No

 ** ReplicationInstanceArn **   <a name="DMS-Type-Connection-ReplicationInstanceArn"></a>
The ARN of the replication instance.
Type: String
Required: No

 ** ReplicationInstanceIdentifier **   <a name="DMS-Type-Connection-ReplicationInstanceIdentifier"></a>
The replication instance identifier. This parameter is stored as a lowercase string.
Type: String
Required: No

 ** Status **   <a name="DMS-Type-Connection-Status"></a>
The connection status. This parameter can return one of the following values:
+  `"successful"`
+  `"testing"`
+  `"failed"`
+  `"deleting"`
Type: String
Required: No

## See Also
<a name="API_Connection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/Connection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/Connection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/Connection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
