---
source_url: https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_GetKeyspace.html
---

# GetKeyspace
<a name="API_GetKeyspace"></a>

Returns the name of the specified keyspace, the Amazon Resource Name (ARN), the replication strategy, the AWS Regions of a multi-Region keyspace, and the status of newly added Regions after an `UpdateKeyspace` operation.

## Request Syntax
<a name="API_GetKeyspace_RequestSyntax"></a>

```
{
   "keyspaceName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetKeyspace_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [keyspaceName](#API_GetKeyspace_RequestSyntax) **   <a name="keyspaces-GetKeyspace-request-keyspaceName"></a>
The name of the keyspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_]{0,47}`
Required: Yes

## Response Syntax
<a name="API_GetKeyspace_ResponseSyntax"></a>

```
{
   "keyspaceName": "string",
   "replicationGroupStatuses": [
      {
         "keyspaceStatus": "string",
         "region": "string",
         "tablesReplicationProgress": "string"
      }
   ],
   "replicationRegions": [ "string" ],
   "replicationStrategy": "string",
   "resourceArn": "string"
}
```

## Response Elements
<a name="API_GetKeyspace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [keyspaceName](#API_GetKeyspace_ResponseSyntax) **   <a name="keyspaces-GetKeyspace-response-keyspaceName"></a>
The name of the keyspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_]{0,47}`

 ** [replicationGroupStatuses](#API_GetKeyspace_ResponseSyntax) **   <a name="keyspaces-GetKeyspace-response-replicationGroupStatuses"></a>
 A list of all Regions the keyspace is replicated in after the update keyspace operation and their status.
Type: Array of [ReplicationGroupStatus](API_ReplicationGroupStatus.md) objects
Array Members: Minimum number of 2 items.

 ** [replicationRegions](#API_GetKeyspace_ResponseSyntax) **   <a name="keyspaces-GetKeyspace-response-replicationRegions"></a>
 If the `replicationStrategy` of the keyspace is `MULTI_REGION`, a list of replication Regions is returned.
Type: Array of strings
Array Members: Minimum number of 2 items.
Length Constraints: Minimum length of 2. Maximum length of 25.

 ** [replicationStrategy](#API_GetKeyspace_ResponseSyntax) **   <a name="keyspaces-GetKeyspace-response-replicationStrategy"></a>
 Returns the replication strategy of the keyspace. The options are `SINGLE_REGION` or `MULTI_REGION`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Valid Values: `SINGLE_REGION | MULTI_REGION`

 ** [resourceArn](#API_GetKeyspace_ResponseSyntax) **   <a name="keyspaces-GetKeyspace-response-resourceArn"></a>
Returns the ARN of the keyspace.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1000.
Pattern: `arn:(aws[a-zA-Z0-9-]*):cassandra:.+.*`

## Errors
<a name="API_GetKeyspace_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
You don't have sufficient access permissions to perform this action.
 ** message **
You don't have the required permissions to perform this operation. Verify your IAM permissions and try again.
HTTP Status Code: 400

 [InternalServerException](API_InternalServerException.md)
Amazon Keyspaces was unable to fully process this request because of an internal server error.
 ** message **
An internal service error occurred. Retry your request. If the problem persists, contact AWS Support.
HTTP Status Code: 500

 [ResourceNotFoundException](API_ResourceNotFoundException.md)
The operation tried to access a keyspace, table, or type that doesn't exist. The resource might not be specified correctly, or its status might not be `ACTIVE`.
 ** message **
The specified resource was not found. Verify the resource identifier and ensure the resource exists and is in an ACTIVE state.
 ** resourceArn **
The unique identifier in the format of Amazon Resource Name (ARN) for the resource couldn't be found.
HTTP Status Code: 400

 [ServiceQuotaExceededException](API_ServiceQuotaExceededException.md)
The operation exceeded the service quota for this resource. For more information on service quotas, see [Quotas](https://docs.aws.amazon.com/keyspaces/latest/devguide/quotas.html) in the *Amazon Keyspaces Developer Guide*.
 ** message **
The requested operation would exceed the service quota for this resource. Review the service quotas and adjust your request accordingly.
HTTP Status Code: 400

 [ValidationException](API_ValidationException.md)
The operation failed due to an invalid or malformed request.
 ** message **
The request parameters are invalid or malformed. Review the API documentation and correct the request format.
HTTP Status Code: 400

## See Also
<a name="API_GetKeyspace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/keyspaces-2022-02-10/GetKeyspace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/keyspaces-2022-02-10/GetKeyspace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspaces-2022-02-10/GetKeyspace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/keyspaces-2022-02-10/GetKeyspace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspaces-2022-02-10/GetKeyspace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/keyspaces-2022-02-10/GetKeyspace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/keyspaces-2022-02-10/GetKeyspace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/keyspaces-2022-02-10/GetKeyspace)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/keyspaces-2022-02-10/GetKeyspace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspaces-2022-02-10/GetKeyspace)
