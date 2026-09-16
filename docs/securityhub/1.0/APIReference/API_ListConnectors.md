---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListConnectors.html
---

# ListConnectors
<a name="API_ListConnectors"></a>

Lists the CSPM connectors and their metadata for the calling account.

## Request Syntax
<a name="API_ListConnectors_RequestSyntax"></a>

```
GET /connectors?ConnectorStatus={{ConnectorStatus}}&EnablementStatus={{EnablementStatus}}&MaxResults={{MaxResults}}&NextToken={{NextToken}}&ProviderName={{ProviderName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListConnectors_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ConnectorStatus](#API_ListConnectors_RequestSyntax) **   <a name="securityhub-ListConnectors-request-uri-ConnectorStatus"></a>
The connectivity status to filter connectors by.
Valid Values: `CONNECTED | DEGRADED | FAILED_TO_CONNECT | UNKNOWN`

 ** [EnablementStatus](#API_ListConnectors_RequestSyntax) **   <a name="securityhub-ListConnectors-request-uri-EnablementStatus"></a>
The enablement status to filter connectors by.
Valid Values: `ENABLED | PENDING_ENABLEMENT | PENDING_UPDATE | PENDING_DELETION`

 ** [MaxResults](#API_ListConnectors_RequestSyntax) **   <a name="securityhub-ListConnectors-request-uri-MaxResults"></a>
The maximum number of results to return.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListConnectors_RequestSyntax) **   <a name="securityhub-ListConnectors-request-uri-NextToken"></a>
The pagination token to request the next page of results.

 ** [ProviderName](#API_ListConnectors_RequestSyntax) **   <a name="securityhub-ListConnectors-request-uri-ProviderName"></a>
The name of the cloud provider to filter connectors by.
Valid Values: `AZURE`

## Request Body
<a name="API_ListConnectors_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListConnectors_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Connectors": [
      {
         "ConnectorArn": "string",
         "ConnectorId": "string",
         "CreatedAt": "string",
         "CreatedBy": "string",
         "Description": "string",
         "EnablementStatus": "string",
         "Name": "string",
         "ProviderSummary": {
            "ConnectorStatus": "string",
            "ProviderConfiguration": { ... },
            "ProviderName": "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListConnectors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Connectors](#API_ListConnectors_ResponseSyntax) **   <a name="securityhub-ListConnectors-response-Connectors"></a>
An array of connector summaries.
Type: Array of [CspmConnectorSummary](API_CspmConnectorSummary.md) objects

 ** [NextToken](#API_ListConnectors_ResponseSyntax) **   <a name="securityhub-ListConnectors-response-NextToken"></a>
The pagination token to use to request the next page of results. If there are no additional results, this value is null.
Type: String

## Errors
<a name="API_ListConnectors_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

 ** ConflictException **
The request causes conflict with the current state of the service resource.
HTTP Status Code: 409

 ** InternalServerException **
 The request has failed due to an internal failure of the service.
HTTP Status Code: 500

 ** InvalidAccessException **
The account doesn't have permission to perform this action.
HTTP Status Code: 401

 ** ResourceNotFoundException **
The request was rejected because we can't find the specified resource.
HTTP Status Code: 404

 ** ThrottlingException **
 The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation because it's missing required fields or has invalid inputs.
HTTP Status Code: 400

## See Also
<a name="API_ListConnectors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/ListConnectors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/ListConnectors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ListConnectors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/ListConnectors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ListConnectors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/ListConnectors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/ListConnectors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/ListConnectors)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/ListConnectors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ListConnectors)
