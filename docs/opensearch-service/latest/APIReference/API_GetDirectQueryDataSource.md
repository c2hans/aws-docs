---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetDirectQueryDataSource.html
---

# GetDirectQueryDataSource
<a name="API_GetDirectQueryDataSource"></a>

 Returns detailed configuration information for a specific direct query data source in Amazon OpenSearch Service.

## Request Syntax
<a name="API_GetDirectQueryDataSource_RequestSyntax"></a>

```
GET /2021-01-01/opensearch/directQueryDataSource/{{DataSourceName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDirectQueryDataSource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DataSourceName](#API_GetDirectQueryDataSource_RequestSyntax) **   <a name="opensearchservice-GetDirectQueryDataSource-request-uri-DataSourceName"></a>
 A unique, user-defined label that identifies the data source within your OpenSearch Service environment.
Length Constraints: Minimum length of 3. Maximum length of 80.
Pattern: `[a-z][a-z0-9_]+`
Required: Yes

## Request Body
<a name="API_GetDirectQueryDataSource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDirectQueryDataSource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DataSourceAccessPolicy": "string",
   "DataSourceArn": "string",
   "DataSourceName": "string",
   "DataSourceType": { ... },
   "Description": "string",
   "OpenSearchArns": [ "string" ]
}
```

## Response Elements
<a name="API_GetDirectQueryDataSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DataSourceAccessPolicy](#API_GetDirectQueryDataSource_ResponseSyntax) **   <a name="opensearchservice-GetDirectQueryDataSource-response-DataSourceAccessPolicy"></a>
 The IAM access policy document that defines the permissions for accessing the direct query data source. Returns the current policy configuration in JSON format, or null if no custom policy is configured.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 102400.
Pattern: `.*`

 ** [DataSourceArn](#API_GetDirectQueryDataSource_ResponseSyntax) **   <a name="opensearchservice-GetDirectQueryDataSource-response-DataSourceArn"></a>
 The unique, system-generated identifier that represents the data source.
Type: String

 ** [DataSourceName](#API_GetDirectQueryDataSource_ResponseSyntax) **   <a name="opensearchservice-GetDirectQueryDataSource-response-DataSourceName"></a>
 A unique, user-defined label to identify the data source within your OpenSearch Service environment.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 80.
Pattern: `[a-z][a-z0-9_]+`

 ** [DataSourceType](#API_GetDirectQueryDataSource_ResponseSyntax) **   <a name="opensearchservice-GetDirectQueryDataSource-response-DataSourceType"></a>
 The supported AWS service that is used as the source for direct queries in OpenSearch Service.
Type: [DirectQueryDataSourceType](API_DirectQueryDataSourceType.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [Description](#API_GetDirectQueryDataSource_ResponseSyntax) **   <a name="opensearchservice-GetDirectQueryDataSource-response-Description"></a>
 A description that provides additional context and details about the data source.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `^([a-zA-Z0-9_])*[\\a-zA-Z0-9_@#%*+=:?./!\s-]*$`

 ** [OpenSearchArns](#API_GetDirectQueryDataSource_ResponseSyntax) **   <a name="opensearchservice-GetDirectQueryDataSource-response-OpenSearchArns"></a>
 A list of Amazon Resource Names (ARNs) for the OpenSearch collections that are associated with the direct query data source.
Type: Array of strings
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*`

## Errors
<a name="API_GetDirectQueryDataSource_Errors"></a>

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
<a name="API_GetDirectQueryDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/GetDirectQueryDataSource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/GetDirectQueryDataSource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/GetDirectQueryDataSource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/GetDirectQueryDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/GetDirectQueryDataSource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/GetDirectQueryDataSource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/GetDirectQueryDataSource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/GetDirectQueryDataSource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/GetDirectQueryDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/GetDirectQueryDataSource)
