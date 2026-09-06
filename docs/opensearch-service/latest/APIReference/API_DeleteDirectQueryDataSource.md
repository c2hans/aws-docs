---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DeleteDirectQueryDataSource.html
---

# DeleteDirectQueryDataSource
<a name="API_DeleteDirectQueryDataSource"></a>

 Deletes a previously configured direct query data source from Amazon OpenSearch Service.

## Request Syntax
<a name="API_DeleteDirectQueryDataSource_RequestSyntax"></a>

```
DELETE /2021-01-01/opensearch/directQueryDataSource/{{DataSourceName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteDirectQueryDataSource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DataSourceName](#API_DeleteDirectQueryDataSource_RequestSyntax) **   <a name="opensearchservice-DeleteDirectQueryDataSource-request-uri-DataSourceName"></a>
 A unique, user-defined label to identify the data source within your OpenSearch Service environment.
Length Constraints: Minimum length of 3. Maximum length of 80.
Pattern: `[a-z][a-z0-9_]+`
Required: Yes

## Request Body
<a name="API_DeleteDirectQueryDataSource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteDirectQueryDataSource_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteDirectQueryDataSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteDirectQueryDataSource_Errors"></a>

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
<a name="API_DeleteDirectQueryDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/DeleteDirectQueryDataSource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/DeleteDirectQueryDataSource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DeleteDirectQueryDataSource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/DeleteDirectQueryDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DeleteDirectQueryDataSource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/DeleteDirectQueryDataSource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/DeleteDirectQueryDataSource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/DeleteDirectQueryDataSource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/DeleteDirectQueryDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DeleteDirectQueryDataSource)
