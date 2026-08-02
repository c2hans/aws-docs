---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeDataSourceAttachment.html
---

# DescribeDataSourceAttachment
<a name="API_DescribeDataSourceAttachment"></a>

Returns the current status and details of a specific data source attachment for an OpenSearch application. Throws a `ResourceNotFoundException` if no attachment record exists for the specified application and data source combination.

## Request Syntax
<a name="API_DescribeDataSourceAttachment_RequestSyntax"></a>

```
POST /2021-01-01/opensearch/application/{{id}}/describeDataSourceAttachment HTTP/1.1
Content-type: application/json

{
   "dataSourceArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeDataSourceAttachment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_DescribeDataSourceAttachment_RequestSyntax) **   <a name="opensearchservice-DescribeDataSourceAttachment-request-uri-id"></a>
The unique identifier or name of the OpenSearch application.
Pattern: `[a-z0-9]{3,30}`
Required: Yes

## Request Body
<a name="API_DescribeDataSourceAttachment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [dataSourceArn](#API_DescribeDataSourceAttachment_RequestSyntax) **   <a name="opensearchservice-DescribeDataSourceAttachment-request-dataSourceArn"></a>
The Amazon Resource Name (ARN) of the domain. See [Identifiers for IAM Entities ](https://docs.aws.amazon.com/IAM/latest/UserGuide/index.html) in *Using AWS Identity and Access Management* for more information.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*`
Required: Yes

## Response Syntax
<a name="API_DescribeDataSourceAttachment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "attachmentId": "string",
   "dataSourceArn": "string",
   "id": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_DescribeDataSourceAttachment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_DescribeDataSourceAttachment_ResponseSyntax) **   <a name="opensearchservice-DescribeDataSourceAttachment-response-arn"></a>
The Amazon Resource Name (ARN) of the domain. See [Identifiers for IAM Entities ](https://docs.aws.amazon.com/IAM/latest/UserGuide/index.html) in *Using AWS Identity and Access Management* for more information.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*`

 ** [attachmentId](#API_DescribeDataSourceAttachment_ResponseSyntax) **   <a name="opensearchservice-DescribeDataSourceAttachment-response-attachmentId"></a>
The unique identifier assigned to the data source attachment.
Type: String

 ** [dataSourceArn](#API_DescribeDataSourceAttachment_ResponseSyntax) **   <a name="opensearchservice-DescribeDataSourceAttachment-response-dataSourceArn"></a>
The Amazon Resource Name (ARN) of the domain. See [Identifiers for IAM Entities ](https://docs.aws.amazon.com/IAM/latest/UserGuide/index.html) in *Using AWS Identity and Access Management* for more information.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*`

 ** [id](#API_DescribeDataSourceAttachment_ResponseSyntax) **   <a name="opensearchservice-DescribeDataSourceAttachment-response-id"></a>
The unique identifier of the OpenSearch application.
Type: String
Pattern: `[a-z0-9]{3,30}`

 ** [status](#API_DescribeDataSourceAttachment_ResponseSyntax) **   <a name="opensearchservice-DescribeDataSourceAttachment-response-status"></a>
The status of the data source attachment. Valid values are `PENDING`, `ATTACHED`, and `FAILED`.
Type: String
Valid Values: `PENDING | ATTACHED | FAILED`

## Errors
<a name="API_DescribeDataSourceAttachment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
An error occurred because you don't have permissions to access the resource.
HTTP Status Code: 403

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
<a name="API_DescribeDataSourceAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/DescribeDataSourceAttachment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/DescribeDataSourceAttachment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DescribeDataSourceAttachment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/DescribeDataSourceAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DescribeDataSourceAttachment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/DescribeDataSourceAttachment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/DescribeDataSourceAttachment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/DescribeDataSourceAttachment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/DescribeDataSourceAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DescribeDataSourceAttachment)
