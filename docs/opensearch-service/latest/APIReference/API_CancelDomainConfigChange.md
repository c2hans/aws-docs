---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CancelDomainConfigChange.html
---

# CancelDomainConfigChange
<a name="API_CancelDomainConfigChange"></a>

Cancels a pending configuration change on an Amazon OpenSearch Service domain.

## Request Syntax
<a name="API_CancelDomainConfigChange_RequestSyntax"></a>

```
POST /2021-01-01/opensearch/domain/{{DomainName}}/config/cancel HTTP/1.1
Content-type: application/json

{
   "DryRun": {{boolean}}
}
```

## URI Request Parameters
<a name="API_CancelDomainConfigChange_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_CancelDomainConfigChange_RequestSyntax) **   <a name="opensearchservice-CancelDomainConfigChange-request-uri-DomainName"></a>
The name of an OpenSearch Service domain. Domain names are unique across the domains owned by an account within an AWS Region.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

## Request Body
<a name="API_CancelDomainConfigChange_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DryRun](#API_CancelDomainConfigChange_RequestSyntax) **   <a name="opensearchservice-CancelDomainConfigChange-request-DryRun"></a>
When set to `True`, returns the list of change IDs and properties that will be cancelled without actually cancelling the change.
Type: Boolean
Required: No

## Response Syntax
<a name="API_CancelDomainConfigChange_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CancelledChangeIds": [ "string" ],
   "CancelledChangeProperties": [
      {
         "ActiveValue": "string",
         "CancelledValue": "string",
         "PropertyName": "string"
      }
   ],
   "DryRun": boolean
}
```

## Response Elements
<a name="API_CancelDomainConfigChange_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CancelledChangeIds](#API_CancelDomainConfigChange_ResponseSyntax) **   <a name="opensearchservice-CancelDomainConfigChange-response-CancelledChangeIds"></a>
The unique identifiers of the changes that were cancelled.
Type: Array of strings
Length Constraints: Fixed length of 36.
Pattern: `\p{XDigit}{8}-\p{XDigit}{4}-\p{XDigit}{4}-\p{XDigit}{4}-\p{XDigit}{12}`

 ** [CancelledChangeProperties](#API_CancelDomainConfigChange_ResponseSyntax) **   <a name="opensearchservice-CancelDomainConfigChange-response-CancelledChangeProperties"></a>
The domain change properties that were cancelled.
Type: Array of [CancelledChangeProperty](API_CancelledChangeProperty.md) objects

 ** [DryRun](#API_CancelDomainConfigChange_ResponseSyntax) **   <a name="opensearchservice-CancelDomainConfigChange-response-DryRun"></a>
Whether or not the request was a dry run. If `True`, the changes were not actually cancelled.
Type: Boolean

## Errors
<a name="API_CancelDomainConfigChange_Errors"></a>

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
<a name="API_CancelDomainConfigChange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/CancelDomainConfigChange)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/CancelDomainConfigChange)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/CancelDomainConfigChange)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/CancelDomainConfigChange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/CancelDomainConfigChange)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/CancelDomainConfigChange)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/CancelDomainConfigChange)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/CancelDomainConfigChange)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/CancelDomainConfigChange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/CancelDomainConfigChange)
