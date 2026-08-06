---
source_url: https://docs.aws.amazon.com/clouddirectory/latest/APIReference/API_ListPublishedSchemaArns.html
---

Amazon Cloud Directory is no longer open to new customers, and will reach end of support on July 24, 2027. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and [Amazon Neptune](https://aws.amazon.com/neptune/). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/).

# ListPublishedSchemaArns
<a name="API_ListPublishedSchemaArns"></a>

Lists the major version families of each published schema. If a major version ARN is provided as `SchemaArn`, the minor version revisions in that family are listed instead.

## Request Syntax
<a name="API_ListPublishedSchemaArns_RequestSyntax"></a>

```
POST /amazonclouddirectory/2017-01-11/schema/published HTTP/1.1
Content-type: application/json

{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SchemaArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListPublishedSchemaArns_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListPublishedSchemaArns_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListPublishedSchemaArns_RequestSyntax) **   <a name="amazoncds-ListPublishedSchemaArns-request-MaxResults"></a>
The maximum number of results to retrieve.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [NextToken](#API_ListPublishedSchemaArns_RequestSyntax) **   <a name="amazoncds-ListPublishedSchemaArns-request-NextToken"></a>
The pagination token.
Type: String
Required: No

 ** [SchemaArn](#API_ListPublishedSchemaArns_RequestSyntax) **   <a name="amazoncds-ListPublishedSchemaArns-request-SchemaArn"></a>
The response for `ListPublishedSchemaArns` when this parameter is used will list all minor version ARNs for a major version.
Type: String
Required: No

## Response Syntax
<a name="API_ListPublishedSchemaArns_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "SchemaArns": [ "string" ]
}
```

## Response Elements
<a name="API_ListPublishedSchemaArns_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListPublishedSchemaArns_ResponseSyntax) **   <a name="amazoncds-ListPublishedSchemaArns-response-NextToken"></a>
The pagination token.
Type: String

 ** [SchemaArns](#API_ListPublishedSchemaArns_ResponseSyntax) **   <a name="amazoncds-ListPublishedSchemaArns-response-SchemaArns"></a>
The ARNs of published schemas.
Type: Array of strings

## Errors
<a name="API_ListPublishedSchemaArns_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access denied or directory not found. Either you don't have permissions for this directory or the directory does not exist. Try calling [ListDirectories](API_ListDirectories.md) and check your permissions.
HTTP Status Code: 403

 ** InternalServiceException **
Indicates a problem that must be resolved by Amazon Web Services. This might be a transient error in which case you can retry your request until it succeeds. Otherwise, go to the [AWS Service Health Dashboard](http://status.aws.amazon.com/) site to see if there are any operational issues with the service.
HTTP Status Code: 500

 ** InvalidArnException **
Indicates that the provided ARN value is not valid.
HTTP Status Code: 400

 ** InvalidNextTokenException **
Indicates that the `NextToken` value is not valid.
HTTP Status Code: 400

 ** LimitExceededException **
Indicates that limits are exceeded. See [Limits](https://docs.aws.amazon.com/clouddirectory/latest/developerguide/limits.html) for more information.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource could not be found.
HTTP Status Code: 404

 ** RetryableConflictException **
Occurs when a conflict with a previous successful write is detected. For example, if a write operation occurs on an object and then an attempt is made to read the object using “SERIALIZABLE” consistency, this exception may result. This generally occurs when the previous write did not have time to propagate to the host serving the current request. A retry (with appropriate backoff logic) is the recommended response to this exception.
HTTP Status Code: 409

 ** ValidationException **
Indicates that your request is malformed in some manner. See the exception message.
HTTP Status Code: 400

## See Also
<a name="API_ListPublishedSchemaArns_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/clouddirectory-2017-01-11/ListPublishedSchemaArns)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/clouddirectory-2017-01-11/ListPublishedSchemaArns)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/clouddirectory-2017-01-11/ListPublishedSchemaArns)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/clouddirectory-2017-01-11/ListPublishedSchemaArns)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/clouddirectory-2017-01-11/ListPublishedSchemaArns)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/clouddirectory-2017-01-11/ListPublishedSchemaArns)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/clouddirectory-2017-01-11/ListPublishedSchemaArns)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/clouddirectory-2017-01-11/ListPublishedSchemaArns)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/clouddirectory-2017-01-11/ListPublishedSchemaArns)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/clouddirectory-2017-01-11/ListPublishedSchemaArns)
