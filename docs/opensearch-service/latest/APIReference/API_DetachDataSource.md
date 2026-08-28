---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DetachDataSource.html
---

# DetachDataSource
<a name="API_DetachDataSource"></a>

Removes a data source from an OpenSearch application. The application must be in the `ACTIVE` state. This operation removes the data source saved object from the application and deletes the attachment record. Throws a `ConflictException` if the specified data source has a `PENDING` attachment, and a `ResourceNotFoundException` if the data source is not currently attached to the application.

## Request Syntax
<a name="API_DetachDataSource_RequestSyntax"></a>

```
POST /2021-01-01/opensearch/application/{{id}}/detachDataSource HTTP/1.1
Content-type: application/json

{
   "dataSourceArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DetachDataSource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_DetachDataSource_RequestSyntax) **   <a name="opensearchservice-DetachDataSource-request-uri-id"></a>
The unique identifier or name of the OpenSearch application to detach the data source from.
Pattern: `[a-z0-9]{3,30}`
Required: Yes

## Request Body
<a name="API_DetachDataSource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [dataSourceArn](#API_DetachDataSource_RequestSyntax) **   <a name="opensearchservice-DetachDataSource-request-dataSourceArn"></a>
The Amazon Resource Name (ARN) of the domain. See [Identifiers for IAM Entities ](https://docs.aws.amazon.com/IAM/latest/UserGuide/index.html) in *Using AWS Identity and Access Management* for more information.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*`
Required: Yes

## Response Syntax
<a name="API_DetachDataSource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "dataSourceArn": "string",
   "id": "string"
}
```

## Response Elements
<a name="API_DetachDataSource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_DetachDataSource_ResponseSyntax) **   <a name="opensearchservice-DetachDataSource-response-arn"></a>
The Amazon Resource Name (ARN) of the domain. See [Identifiers for IAM Entities ](https://docs.aws.amazon.com/IAM/latest/UserGuide/index.html) in *Using AWS Identity and Access Management* for more information.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*`

 ** [dataSourceArn](#API_DetachDataSource_ResponseSyntax) **   <a name="opensearchservice-DetachDataSource-response-dataSourceArn"></a>
The Amazon Resource Name (ARN) of the domain. See [Identifiers for IAM Entities ](https://docs.aws.amazon.com/IAM/latest/UserGuide/index.html) in *Using AWS Identity and Access Management* for more information.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*`

 ** [id](#API_DetachDataSource_ResponseSyntax) **   <a name="opensearchservice-DetachDataSource-response-id"></a>
The unique identifier of the OpenSearch application.
Type: String
Pattern: `[a-z0-9]{3,30}`

## Errors
<a name="API_DetachDataSource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An error occurred because you don't have permissions to access the resource.
HTTP Status Code: 403

 ** ConflictException **
An error occurred because the client attempts to remove a resource that is currently in use.
HTTP Status Code: 409

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
<a name="API_DetachDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/DetachDataSource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/DetachDataSource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DetachDataSource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/DetachDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DetachDataSource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/DetachDataSource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/DetachDataSource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/DetachDataSource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/DetachDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DetachDataSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
