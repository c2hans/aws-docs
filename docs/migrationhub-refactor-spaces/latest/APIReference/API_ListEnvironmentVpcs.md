---
source_url: https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_ListEnvironmentVpcs.html
---

# ListEnvironmentVpcs
<a name="API_ListEnvironmentVpcs"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

Lists all AWS Migration Hub Refactor Spaces service virtual private clouds (VPCs) that are part of the environment.

## Request Syntax
<a name="API_ListEnvironmentVpcs_RequestSyntax"></a>

```
GET /environments/{{EnvironmentIdentifier}}/vpcs?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListEnvironmentVpcs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EnvironmentIdentifier](#API_ListEnvironmentVpcs_RequestSyntax) **   <a name="migrationhubrefactorspaces-ListEnvironmentVpcs-request-uri-EnvironmentIdentifier"></a>
The ID of the environment.
Length Constraints: Fixed length of 14.
Pattern: `env-[0-9A-Za-z]{10}`
Required: Yes

 ** [MaxResults](#API_ListEnvironmentVpcs_RequestSyntax) **   <a name="migrationhubrefactorspaces-ListEnvironmentVpcs-request-uri-MaxResults"></a>
The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned `nextToken` value.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListEnvironmentVpcs_RequestSyntax) **   <a name="migrationhubrefactorspaces-ListEnvironmentVpcs-request-uri-NextToken"></a>
The token for the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[a-zA-Z0-9/\+\=]{0,2048}`

## Request Body
<a name="API_ListEnvironmentVpcs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListEnvironmentVpcs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "EnvironmentVpcList": [
      {
         "AccountId": "string",
         "CidrBlocks": [ "string" ],
         "CreatedTime": number,
         "EnvironmentId": "string",
         "LastUpdatedTime": number,
         "VpcId": "string",
         "VpcName": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListEnvironmentVpcs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EnvironmentVpcList](#API_ListEnvironmentVpcs_ResponseSyntax) **   <a name="migrationhubrefactorspaces-ListEnvironmentVpcs-response-EnvironmentVpcList"></a>
The list of `EnvironmentVpc` objects.
Type: Array of [EnvironmentVpc](API_EnvironmentVpc.md) objects

 ** [NextToken](#API_ListEnvironmentVpcs_ResponseSyntax) **   <a name="migrationhubrefactorspaces-ListEnvironmentVpcs-response-NextToken"></a>
The token for the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[a-zA-Z0-9/\+\=]{0,2048}`

## Errors
<a name="API_ListEnvironmentVpcs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that does not exist.
 ** ResourceId **
The ID of the resource.
 ** ResourceType **
The type of resource.
HTTP Status Code: 404

 ** ThrottlingException **
Request was denied because the request was throttled.
 ** QuotaCode **
Service quota requirement to identify originating quota. Reached throttling quota exception.
 ** RetryAfterSeconds **
The number of seconds to wait before retrying.
 ** ServiceCode **
Service quota requirement to identify originating service. Reached throttling quota exception service code.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListEnvironmentVpcs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migration-hub-refactor-spaces-2021-10-26/ListEnvironmentVpcs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migration-hub-refactor-spaces-2021-10-26/ListEnvironmentVpcs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migration-hub-refactor-spaces-2021-10-26/ListEnvironmentVpcs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migration-hub-refactor-spaces-2021-10-26/ListEnvironmentVpcs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migration-hub-refactor-spaces-2021-10-26/ListEnvironmentVpcs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migration-hub-refactor-spaces-2021-10-26/ListEnvironmentVpcs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migration-hub-refactor-spaces-2021-10-26/ListEnvironmentVpcs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migration-hub-refactor-spaces-2021-10-26/ListEnvironmentVpcs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migration-hub-refactor-spaces-2021-10-26/ListEnvironmentVpcs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migration-hub-refactor-spaces-2021-10-26/ListEnvironmentVpcs)
