---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetDataSource.html
---

# GetDataSource
<a name="API_GetDataSource"></a>

Retrieves information about a direct query data source.

## Request Syntax
<a name="API_GetDataSource_RequestSyntax"></a>

```
GET /2021-01-01/opensearch/domain/{{DomainName}}/dataSource/{{DataSourceName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDataSource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_GetDataSource_RequestSyntax) **   <a name="opensearchservice-GetDataSource-request-uri-DomainName"></a>
The name of the domain.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

 ** [DataSourceName](#API_GetDataSource_RequestSyntax) **   <a name="opensearchservice-GetDataSource-request-uri-Name"></a>
The name of the data source to get information about.
Length Constraints: Minimum length of 3. Maximum length of 80.
Pattern: `[a-z][a-z0-9_]+`
Required: Yes

## Request Body
<a name="API_GetDataSource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDataSource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DataSourceType": { ... },
   "Description": "string",
   "Name": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_GetDataSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DataSourceType](#API_GetDataSource_ResponseSyntax) **   <a name="opensearchservice-GetDataSource-response-DataSourceType"></a>
The type of data source.
Type: [DataSourceType](API_DataSourceType.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [Description](#API_GetDataSource_ResponseSyntax) **   <a name="opensearchservice-GetDataSource-response-Description"></a>
A description of the data source.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `^([a-zA-Z0-9_])*[\\a-zA-Z0-9_@#%*+=:?./!\s-]*$`

 ** [Name](#API_GetDataSource_ResponseSyntax) **   <a name="opensearchservice-GetDataSource-response-Name"></a>
The name of the data source.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 80.
Pattern: `[a-z][a-z0-9_]+`

 ** [Status](#API_GetDataSource_ResponseSyntax) **   <a name="opensearchservice-GetDataSource-response-Status"></a>
The status of the data source.
Type: String
Valid Values: `ACTIVE | DISABLED`

## Errors
<a name="API_GetDataSource_Errors"></a>

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
<a name="API_GetDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/GetDataSource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/GetDataSource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/GetDataSource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/GetDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/GetDataSource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/GetDataSource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/GetDataSource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/GetDataSource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/GetDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/GetDataSource)
