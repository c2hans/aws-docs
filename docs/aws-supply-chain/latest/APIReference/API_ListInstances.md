---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_ListInstances.html
---

# ListInstances
<a name="API_ListInstances"></a>

List all AWS Supply Chain instances for a specific account. Enables you to programmatically list all AWS Supply Chain instances based on their account ID, instance name, and state of the instance (active or delete).

## Request Syntax
<a name="API_ListInstances_RequestSyntax"></a>

```
GET /api/instance?instanceNameFilter={{instanceNameFilter}}&instanceStateFilter={{instanceStateFilter}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListInstances_RequestParameters"></a>

The request uses the following URI parameters.

 ** [instanceNameFilter](#API_ListInstances_RequestSyntax) **   <a name="supplychain-ListInstances-request-uri-instanceNameFilter"></a>
The filter to ListInstances based on their names.
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Length Constraints: Minimum length of 0. Maximum length of 63.
Pattern: `(?![ _ʼ'%-])[a-zA-Z0-9 _ʼ'%-]{0,62}[a-zA-Z0-9]`

 ** [instanceStateFilter](#API_ListInstances_RequestSyntax) **   <a name="supplychain-ListInstances-request-uri-instanceStateFilter"></a>
The filter to ListInstances based on their state.
Array Members: Minimum number of 0 items. Maximum number of 6 items.
Valid Values: `Initializing | Active | CreateFailed | DeleteFailed | Deleting | Deleted`

 ** [maxResults](#API_ListInstances_RequestSyntax) **   <a name="supplychain-ListInstances-request-uri-maxResults"></a>
Specify the maximum number of instances to fetch in this paginated request.
Valid Range: Minimum value of 0. Maximum value of 20.

 ** [nextToken](#API_ListInstances_RequestSyntax) **   <a name="supplychain-ListInstances-request-uri-nextToken"></a>
The pagination token to fetch the next page of instances.
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Request Body
<a name="API_ListInstances_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListInstances_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "instances": [
      {
         "awsAccountId": "string",
         "createdTime": number,
         "errorMessage": "string",
         "instanceDescription": "string",
         "instanceId": "string",
         "instanceName": "string",
         "kmsKeyArn": "string",
         "lastModifiedTime": number,
         "state": "string",
         "versionNumber": number,
         "webAppDnsDomain": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListInstances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [instances](#API_ListInstances_ResponseSyntax) **   <a name="supplychain-ListInstances-response-instances"></a>
The list of instances resource data details.
Type: Array of [Instance](API_Instance.md) objects

 ** [nextToken](#API_ListInstances_ResponseSyntax) **   <a name="supplychain-ListInstances-response-nextToken"></a>
The pagination token to fetch the next page of instances.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_ListInstances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have the required privileges to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
Request would cause a service quota to be exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
Request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListInstances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/supplychain-2024-01-01/ListInstances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/supplychain-2024-01-01/ListInstances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/ListInstances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/supplychain-2024-01-01/ListInstances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/ListInstances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/supplychain-2024-01-01/ListInstances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/supplychain-2024-01-01/ListInstances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/supplychain-2024-01-01/ListInstances)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/supplychain-2024-01-01/ListInstances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/ListInstances)
