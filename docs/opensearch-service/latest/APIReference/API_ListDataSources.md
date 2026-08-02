---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListDataSources.html
---

# ListDataSources
<a name="API_ListDataSources"></a>

Lists direct-query data sources for a specific domain. For more information, see For more information, see [Working with Amazon OpenSearch Service direct queries with Amazon S3](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/direct-query-s3.html).

## Request Syntax
<a name="API_ListDataSources_RequestSyntax"></a>

```
GET /2021-01-01/opensearch/domain/{{DomainName}}/dataSource HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDataSources_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_ListDataSources_RequestSyntax) **   <a name="opensearchservice-ListDataSources-request-uri-DomainName"></a>
The name of the domain.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

## Request Body
<a name="API_ListDataSources_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDataSources_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DataSources": [
      {
         "DataSourceType": { ... },
         "Description": "string",
         "Name": "string",
         "Status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListDataSources_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DataSources](#API_ListDataSources_ResponseSyntax) **   <a name="opensearchservice-ListDataSources-response-DataSources"></a>
A list of data sources associated with specified domain.
Type: Array of [DataSourceDetails](API_DataSourceDetails.md) objects

## Errors
<a name="API_ListDataSources_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

 ** DependencyFailureException **
An exception for when a failure in one of the dependencies results in the service being unable to fetch details about the resource.
HTTP Status Code: 424

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
<a name="API_ListDataSources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/ListDataSources)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/ListDataSources)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/ListDataSources)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/ListDataSources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/ListDataSources)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/ListDataSources)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/ListDataSources)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/ListDataSources)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/ListDataSources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/ListDataSources)
