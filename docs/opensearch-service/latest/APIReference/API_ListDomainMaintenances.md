---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListDomainMaintenances.html
---

# ListDomainMaintenances
<a name="API_ListDomainMaintenances"></a>

A list of maintenance actions for the domain.

## Request Syntax
<a name="API_ListDomainMaintenances_RequestSyntax"></a>

```
GET /2021-01-01/opensearch/domain/{{DomainName}}/domainMaintenances?action={{Action}}&maxResults={{MaxResults}}&nextToken={{NextToken}}&status={{Status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDomainMaintenances_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Action](#API_ListDomainMaintenances_RequestSyntax) **   <a name="opensearchservice-ListDomainMaintenances-request-uri-Action"></a>
The name of the action.
Valid Values: `REBOOT_NODE | RESTART_SEARCH_PROCESS | RESTART_DASHBOARD`

 ** [DomainName](#API_ListDomainMaintenances_RequestSyntax) **   <a name="opensearchservice-ListDomainMaintenances-request-uri-DomainName"></a>
The name of the domain.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

 ** [MaxResults](#API_ListDomainMaintenances_RequestSyntax) **   <a name="opensearchservice-ListDomainMaintenances-request-uri-MaxResults"></a>
An optional parameter that specifies the maximum number of results to return. You can use `nextToken` to get the next page of results.
Valid Range: Maximum value of 100.

 ** [NextToken](#API_ListDomainMaintenances_RequestSyntax) **   <a name="opensearchservice-ListDomainMaintenances-request-uri-NextToken"></a>
If your initial `ListDomainMaintenances` operation returns a `nextToken`, include the returned `nextToken` in subsequent `ListDomainMaintenances` operations, which returns results in the next page.

 ** [Status](#API_ListDomainMaintenances_RequestSyntax) **   <a name="opensearchservice-ListDomainMaintenances-request-uri-Status"></a>
The status of the action.
Valid Values: `PENDING | IN_PROGRESS | COMPLETED | FAILED | TIMED_OUT`

## Request Body
<a name="API_ListDomainMaintenances_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDomainMaintenances_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DomainMaintenances": [
      {
         "Action": "string",
         "CreatedAt": number,
         "DomainName": "string",
         "MaintenanceId": "string",
         "NodeId": "string",
         "Status": "string",
         "StatusMessage": "string",
         "UpdatedAt": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListDomainMaintenances_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DomainMaintenances](#API_ListDomainMaintenances_ResponseSyntax) **   <a name="opensearchservice-ListDomainMaintenances-response-DomainMaintenances"></a>
A list of the submitted maintenance actions.
Type: Array of [DomainMaintenanceDetails](API_DomainMaintenanceDetails.md) objects

 ** [NextToken](#API_ListDomainMaintenances_ResponseSyntax) **   <a name="opensearchservice-ListDomainMaintenances-response-NextToken"></a>
When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.
Type: String

## Errors
<a name="API_ListDomainMaintenances_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

 ** DisabledOperationException **
An error occured because the client wanted to access an unsupported operation.
HTTP Status Code: 409

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_ListDomainMaintenances_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/ListDomainMaintenances)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/ListDomainMaintenances)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/ListDomainMaintenances)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/ListDomainMaintenances)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/ListDomainMaintenances)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/ListDomainMaintenances)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/ListDomainMaintenances)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/ListDomainMaintenances)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/ListDomainMaintenances)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/ListDomainMaintenances)
