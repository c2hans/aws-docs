---
source_url: https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_UpdateKeyspace.html
---

# UpdateKeyspace
<a name="API_UpdateKeyspace"></a>

 Adds a new AWS Region to the keyspace. You can add a new Region to a keyspace that is either a single or a multi-Region keyspace. Amazon Keyspaces is going to replicate all tables in the keyspace to the new Region. To successfully replicate all tables to the new Region, they must use client-side timestamps for conflict resolution. To enable client-side timestamps, specify `clientSideTimestamps.status = enabled` when invoking the API. For more information about client-side timestamps, see [Client-side timestamps in Amazon Keyspaces](https://docs.aws.amazon.com/keyspaces/latest/devguide/client-side-timestamps.html) in the *Amazon Keyspaces Developer Guide*.

To add a Region to a keyspace using the `UpdateKeyspace` API, the IAM principal needs permissions for the following IAM actions:
+  `cassandra:Alter`
+  `cassandra:AlterMultiRegionResource`
+  `cassandra:Create`
+  `cassandra:CreateMultiRegionResource`
+  `cassandra:Select`
+  `cassandra:SelectMultiRegionResource`
+  `cassandra:Modify`
+  `cassandra:ModifyMultiRegionResource`

If the keyspace contains a table that is configured in provisioned mode with auto scaling enabled, the following additional IAM actions need to be allowed.
+  `application-autoscaling:RegisterScalableTarget`
+  `application-autoscaling:DeregisterScalableTarget`
+  `application-autoscaling:DescribeScalableTargets`
+  `application-autoscaling:PutScalingPolicy`
+  `application-autoscaling:DescribeScalingPolicies`

To use the `UpdateKeyspace` API, the IAM principal also needs permissions to create a service-linked role with the following elements:
+  `iam:CreateServiceLinkedRole` - The **action** the principal can perform.
+  `arn:aws:iam::*:role/aws-service-role/replication.cassandra.amazonaws.com/AWSServiceRoleForKeyspacesReplication` - The **resource** that the action can be performed on.
+  `iam:AWSServiceName: replication.cassandra.amazonaws.com` - The only AWS service that this role can be attached to is Amazon Keyspaces.

For more information, see [Configure the IAM permissions required to add an AWS Region to a keyspace](https://docs.aws.amazon.com/keyspaces/latest/devguide/howitworks_replication_permissions_addReplica.html) in the *Amazon Keyspaces Developer Guide*.

## Request Syntax
<a name="API_UpdateKeyspace_RequestSyntax"></a>

```
{
   "clientSideTimestamps": {
      "status": "{{string}}"
   },
   "keyspaceName": "{{string}}",
   "replicationSpecification": {
      "regionList": [ "{{string}}" ],
      "replicationStrategy": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_UpdateKeyspace_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientSideTimestamps](#API_UpdateKeyspace_RequestSyntax) **   <a name="keyspaces-UpdateKeyspace-request-clientSideTimestamps"></a>
The client-side timestamp setting of the table.
For more information, see [How it works: Amazon Keyspaces client-side timestamps](https://docs.aws.amazon.com/keyspaces/latest/devguide/client-side-timestamps-how-it-works.html) in the *Amazon Keyspaces Developer Guide*.
Type: [ClientSideTimestamps](API_ClientSideTimestamps.md) object
Required: No

 ** [keyspaceName](#API_UpdateKeyspace_RequestSyntax) **   <a name="keyspaces-UpdateKeyspace-request-keyspaceName"></a>
 The name of the keyspace.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_]{0,47}`
Required: Yes

 ** [replicationSpecification](#API_UpdateKeyspace_RequestSyntax) **   <a name="keyspaces-UpdateKeyspace-request-replicationSpecification"></a>
 The replication specification of the keyspace includes:
+  `regionList` - the AWS Regions where the keyspace is replicated in.
+  `replicationStrategy` - the required value is `SINGLE_REGION` or `MULTI_REGION`.
Type: [ReplicationSpecification](API_ReplicationSpecification.md) object
Required: Yes

## Response Syntax
<a name="API_UpdateKeyspace_ResponseSyntax"></a>

```
{
   "resourceArn": "string"
}
```

## Response Elements
<a name="API_UpdateKeyspace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [resourceArn](#API_UpdateKeyspace_ResponseSyntax) **   <a name="keyspaces-UpdateKeyspace-response-resourceArn"></a>
 The unique identifier of the keyspace in the format of an Amazon Resource Name (ARN).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1000.
Pattern: `arn:(aws[a-zA-Z0-9-]*):cassandra:.+.*`

## Errors
<a name="API_UpdateKeyspace_Errors"></a>

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
<a name="API_UpdateKeyspace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/keyspaces-2022-02-10/UpdateKeyspace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/keyspaces-2022-02-10/UpdateKeyspace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspaces-2022-02-10/UpdateKeyspace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/keyspaces-2022-02-10/UpdateKeyspace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspaces-2022-02-10/UpdateKeyspace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/keyspaces-2022-02-10/UpdateKeyspace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/keyspaces-2022-02-10/UpdateKeyspace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/keyspaces-2022-02-10/UpdateKeyspace)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/keyspaces-2022-02-10/UpdateKeyspace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspaces-2022-02-10/UpdateKeyspace)
