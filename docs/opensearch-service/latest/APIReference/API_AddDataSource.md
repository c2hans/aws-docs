---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AddDataSource.html
---

# AddDataSource
<a name="API_AddDataSource"></a>

Creates a new direct-query data source to the specified domain. For more information, see [Creating Amazon OpenSearch Service data source integrations with Amazon S3](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/direct-query-s3-creating.html).

## Request Syntax
<a name="API_AddDataSource_RequestSyntax"></a>

```
POST /2021-01-01/opensearch/domain/{{DomainName}}/dataSource HTTP/1.1
Content-type: application/json

{
   "DataSourceType": { ... },
   "Description": "{{string}}",
   "Name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AddDataSource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_AddDataSource_RequestSyntax) **   <a name="opensearchservice-AddDataSource-request-uri-DomainName"></a>
The name of the domain to add the data source to.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

## Request Body
<a name="API_AddDataSource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DataSourceType](#API_AddDataSource_RequestSyntax) **   <a name="opensearchservice-AddDataSource-request-DataSourceType"></a>
The type of data source.
Type: [DataSourceType](API_DataSourceType.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [Description](#API_AddDataSource_RequestSyntax) **   <a name="opensearchservice-AddDataSource-request-Description"></a>
A description of the data source.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `^([a-zA-Z0-9_])*[\\a-zA-Z0-9_@#%*+=:?./!\s-]*$`
Required: No

 ** [Name](#API_AddDataSource_RequestSyntax) **   <a name="opensearchservice-AddDataSource-request-Name"></a>
A name for the data source.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 80.
Pattern: `[a-z][a-z0-9_]+`
Required: Yes

## Response Syntax
<a name="API_AddDataSource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Message": "string"
}
```

## Response Elements
<a name="API_AddDataSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Message](#API_AddDataSource_ResponseSyntax) **   <a name="opensearchservice-AddDataSource-response-Message"></a>
A message associated with creation of the data source.
Type: String

## Errors
<a name="API_AddDataSource_Errors"></a>

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

 ** LimitExceededException **
An exception for trying to create more than the allowed number of resources or sub-resources.
HTTP Status Code: 409

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_AddDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/AddDataSource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/AddDataSource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/AddDataSource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/AddDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/AddDataSource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/AddDataSource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/AddDataSource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/AddDataSource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/AddDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/AddDataSource)
