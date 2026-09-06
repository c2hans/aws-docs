---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpdateDirectQueryDataSource.html
---

# UpdateDirectQueryDataSource
<a name="API_UpdateDirectQueryDataSource"></a>

 Updates the configuration or properties of an existing direct query data source in Amazon OpenSearch Service.

## Request Syntax
<a name="API_UpdateDirectQueryDataSource_RequestSyntax"></a>

```
PUT /2021-01-01/opensearch/directQueryDataSource/{{DataSourceName}} HTTP/1.1
Content-type: application/json

{
   "DataSourceAccessPolicy": "{{string}}",
   "DataSourceType": { ... },
   "Description": "{{string}}",
   "OpenSearchArns": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_UpdateDirectQueryDataSource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DataSourceName](#API_UpdateDirectQueryDataSource_RequestSyntax) **   <a name="opensearchservice-UpdateDirectQueryDataSource-request-uri-DataSourceName"></a>
 A unique, user-defined label to identify the data source within your OpenSearch Service environment.
Length Constraints: Minimum length of 3. Maximum length of 80.
Pattern: `[a-z][a-z0-9_]+`
Required: Yes

## Request Body
<a name="API_UpdateDirectQueryDataSource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DataSourceAccessPolicy](#API_UpdateDirectQueryDataSource_RequestSyntax) **   <a name="opensearchservice-UpdateDirectQueryDataSource-request-DataSourceAccessPolicy"></a>
 An optional IAM access policy document that defines the updated permissions for accessing the direct query data source. The policy document must be in valid JSON format and follow IAM policy syntax. If not specified, the existing access policy if present remains unchanged.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 102400.
Pattern: `.*`
Required: No

 ** [DataSourceType](#API_UpdateDirectQueryDataSource_RequestSyntax) **   <a name="opensearchservice-UpdateDirectQueryDataSource-request-DataSourceType"></a>
 The supported AWS service that you want to use as the source for direct queries in OpenSearch Service.
Type: [DirectQueryDataSourceType](API_DirectQueryDataSourceType.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [Description](#API_UpdateDirectQueryDataSource_RequestSyntax) **   <a name="opensearchservice-UpdateDirectQueryDataSource-request-Description"></a>
 An optional text field for providing additional context and details about the data source.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `^([a-zA-Z0-9_])*[\\a-zA-Z0-9_@#%*+=:?./!\s-]*$`
Required: No

 ** [OpenSearchArns](#API_UpdateDirectQueryDataSource_RequestSyntax) **   <a name="opensearchservice-UpdateDirectQueryDataSource-request-OpenSearchArns"></a>
 An optional list of Amazon Resource Names (ARNs) for the OpenSearch collections that are associated with the direct query data source. This field is required for CloudWatchLogs and SecurityLake datasource types.
Type: Array of strings
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*`
Required: No

## Response Syntax
<a name="API_UpdateDirectQueryDataSource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DataSourceArn": "string"
}
```

## Response Elements
<a name="API_UpdateDirectQueryDataSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DataSourceArn](#API_UpdateDirectQueryDataSource_ResponseSyntax) **   <a name="opensearchservice-UpdateDirectQueryDataSource-response-DataSourceArn"></a>
 The unique, system-generated identifier that represents the data source.
Type: String

## Errors
<a name="API_UpdateDirectQueryDataSource_Errors"></a>

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
<a name="API_UpdateDirectQueryDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/UpdateDirectQueryDataSource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/UpdateDirectQueryDataSource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/UpdateDirectQueryDataSource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/UpdateDirectQueryDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/UpdateDirectQueryDataSource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/UpdateDirectQueryDataSource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/UpdateDirectQueryDataSource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/UpdateDirectQueryDataSource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/UpdateDirectQueryDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/UpdateDirectQueryDataSource)
