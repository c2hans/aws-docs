---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListUseCases.html
---

# ListUseCases
<a name="API_ListUseCases"></a>

Lists the use cases for the integration association.

## Request Syntax
<a name="API_ListUseCases_RequestSyntax"></a>

```
GET /instance/{{InstanceId}}/integration-associations/{{IntegrationAssociationId}}/use-cases?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListUseCases_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_ListUseCases_RequestSyntax) **   <a name="connect-ListUseCases-request-uri-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [IntegrationAssociationId](#API_ListUseCases_RequestSyntax) **   <a name="connect-ListUseCases-request-uri-IntegrationAssociationId"></a>
The identifier for the integration association.
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

 ** [MaxResults](#API_ListUseCases_RequestSyntax) **   <a name="connect-ListUseCases-request-uri-MaxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListUseCases_RequestSyntax) **   <a name="connect-ListUseCases-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

## Request Body
<a name="API_ListUseCases_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListUseCases_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "UseCaseSummaryList": [
      {
         "UseCaseArn": "string",
         "UseCaseId": "string",
         "UseCaseType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListUseCases_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListUseCases_ResponseSyntax) **   <a name="connect-ListUseCases-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String

 ** [UseCaseSummaryList](#API_ListUseCases_ResponseSyntax) **   <a name="connect-ListUseCases-response-UseCaseSummaryList"></a>
The use cases.
Type: Array of [UseCase](API_UseCase.md) objects

## Errors
<a name="API_ListUseCases_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_ListUseCases_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListUseCases)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListUseCases)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListUseCases)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListUseCases)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListUseCases)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListUseCases)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListUseCases)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListUseCases)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListUseCases)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListUseCases)
