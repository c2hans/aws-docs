---
source_url: https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_CreateKeyspace.html
---

# CreateKeyspace
<a name="API_CreateKeyspace"></a>

The `CreateKeyspace` operation adds a new keyspace to your account. In an AWS account, keyspace names must be unique within each Region.

 `CreateKeyspace` is an asynchronous operation. You can monitor the creation status of the new keyspace by using the `GetKeyspace` operation.

For more information, see [Create a keyspace](https://docs.aws.amazon.com/keyspaces/latest/devguide/getting-started.keyspaces.html) in the *Amazon Keyspaces Developer Guide*.

## Request Syntax
<a name="API_CreateKeyspace_RequestSyntax"></a>

```
{
   "keyspaceName": "{{string}}",
   "replicationSpecification": {
      "regionList": [ "{{string}}" ],
      "replicationStrategy": "{{string}}"
   },
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateKeyspace_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [keyspaceName](#API_CreateKeyspace_RequestSyntax) **   <a name="keyspaces-CreateKeyspace-request-keyspaceName"></a>
The name of the keyspace to be created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_]{0,47}`
Required: Yes

 ** [replicationSpecification](#API_CreateKeyspace_RequestSyntax) **   <a name="keyspaces-CreateKeyspace-request-replicationSpecification"></a>
 The replication specification of the keyspace includes:
+  `replicationStrategy` - the required value is `SINGLE_REGION` or `MULTI_REGION`.
+  `regionList` - if the `replicationStrategy` is `MULTI_REGION`, the `regionList` requires the current Region and at least one additional AWS Region where the keyspace is going to be replicated in.
Type: [ReplicationSpecification](API_ReplicationSpecification.md) object
Required: No

 ** [tags](#API_CreateKeyspace_RequestSyntax) **   <a name="keyspaces-CreateKeyspace-request-tags"></a>
A list of key-value pair tags to be attached to the keyspace.
For more information, see [Adding tags and labels to Amazon Keyspaces resources](https://docs.aws.amazon.com/keyspaces/latest/devguide/tagging-keyspaces.html) in the *Amazon Keyspaces Developer Guide*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 60 items.
Required: No

## Response Syntax
<a name="API_CreateKeyspace_ResponseSyntax"></a>

```
{
   "resourceArn": "string"
}
```

## Response Elements
<a name="API_CreateKeyspace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [resourceArn](#API_CreateKeyspace_ResponseSyntax) **   <a name="keyspaces-CreateKeyspace-response-resourceArn"></a>
The unique identifier of the keyspace in the format of an Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1000.
Pattern: `arn:(aws[a-zA-Z0-9-]*):cassandra:.+.*`

## Errors
<a name="API_CreateKeyspace_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
You don't have sufficient access permissions to perform this action.
 ** message **
You don't have the required permissions to perform this operation. Verify your IAM permissions and try again.
HTTP Status Code: 400

 [ConflictException](API_ConflictException.md)
Amazon Keyspaces couldn't complete the requested action. This error may occur if you try to perform an action and the same or a different action is already in progress, or if you try to create a resource that already exists.
 ** message **
The requested operation conflicts with the current state of the resource or another concurrent operation.
HTTP Status Code: 400

 [InternalServerException](API_InternalServerException.md)
Amazon Keyspaces was unable to fully process this request because of an internal server error.
 ** message **
An internal service error occurred. Retry your request. If the problem persists, contact AWS Support.
HTTP Status Code: 500

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
<a name="API_CreateKeyspace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/keyspaces-2022-02-10/CreateKeyspace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/keyspaces-2022-02-10/CreateKeyspace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspaces-2022-02-10/CreateKeyspace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/keyspaces-2022-02-10/CreateKeyspace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspaces-2022-02-10/CreateKeyspace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/keyspaces-2022-02-10/CreateKeyspace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/keyspaces-2022-02-10/CreateKeyspace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/keyspaces-2022-02-10/CreateKeyspace)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/keyspaces-2022-02-10/CreateKeyspace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspaces-2022-02-10/CreateKeyspace)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces (for Apache Cassandra). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
