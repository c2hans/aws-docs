---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_CreateBlueprintVersion.html
---

# CreateBlueprintVersion

Creates a new, immutable version of an existing blueprint so that projects can pin to a specific version.

## Request Syntax
<a name="API_CreateBlueprintVersion_RequestSyntax"></a>

```
{
   "BlueprintArn": "{{string}}",
   "ClientRequestToken": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateBlueprintVersion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BlueprintArn](#API_CreateBlueprintVersion_RequestSyntax) **   <a name="Textract-CreateBlueprintVersion-request-BlueprintArn"></a>
The Amazon Resource Name (ARN) of the blueprint to create a new version of.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^arn:aws(|-cn|-iso|-iso-[a-z]|-us-gov):textract:[a-zA-Z0-9-]*:(aws|[0-9]{12}):blueprint/(public-[a-zA-Z0-9-_]{1,30}|[a-zA-Z0-9-]{12,36})$`
Required: Yes

 ** [ClientRequestToken](#API_CreateBlueprintVersion_RequestSyntax) **   <a name="Textract-CreateBlueprintVersion-request-ClientRequestToken"></a>
A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If you use the same token for a request that matches a previous request, the service ignores the request, but does not return an error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-_]+$`
Required: No

## Response Syntax
<a name="API_CreateBlueprintVersion_ResponseSyntax"></a>

```
{
   "BlueprintArn": "string",
   "BlueprintVersion": "string"
}
```

## Response Elements
<a name="API_CreateBlueprintVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BlueprintArn](#API_CreateBlueprintVersion_ResponseSyntax) **   <a name="Textract-CreateBlueprintVersion-response-BlueprintArn"></a>
The Amazon Resource Name (ARN) of the blueprint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^arn:aws(|-cn|-iso|-iso-[a-z]|-us-gov):textract:[a-zA-Z0-9-]*:(aws|[0-9]{12}):blueprint/(public-[a-zA-Z0-9-_]{1,30}|[a-zA-Z0-9-]{12,36})$`

 ** [BlueprintVersion](#API_CreateBlueprintVersion_ResponseSyntax) **   <a name="Textract-CreateBlueprintVersion-response-BlueprintVersion"></a>
The version of the blueprint that was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[0-9]*$`

## Errors
<a name="API_CreateBlueprintVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You aren't authorized to perform the action. Use the Amazon Resource Name (ARN) of an authorized user or IAM role to perform the operation.
HTTP Status Code: 400

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 400

 ** InternalServerError **
Amazon Textract experienced a service issue. Try your call again.
HTTP Status Code: 500

 ** InvalidParameterException **
An input parameter violated a constraint. For example, in synchronous operations, an `InvalidParameterException` exception occurs when neither of the `S3Object` or `Bytes` values are supplied in the `Document` request parameter. Validate your parameter before calling the API operation again.
HTTP Status Code: 400

 ** LimitExceededException **
An Amazon Textract service limit was exceeded. For example, if you start too many asynchronous jobs concurrently, calls to start operations (`StartDocumentTextDetection`, for example) raise a LimitExceededException exception (HTTP status code: 400) until the number of concurrently running jobs is below the Amazon Textract service limit.
HTTP Status Code: 400

 ** ProvisionedThroughputExceededException **
The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Textract.
HTTP Status Code: 400

 ** ResourceNotFoundException **
 Returned when an operation tried to access a nonexistent resource.
HTTP Status Code: 400

 ** ValidationException **
 Indicates that a request was not valid. Check request for proper formatting.
HTTP Status Code: 400

## See Also
<a name="API_CreateBlueprintVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/textract-2018-06-27/CreateBlueprintVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/textract-2018-06-27/CreateBlueprintVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/CreateBlueprintVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/textract-2018-06-27/CreateBlueprintVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/CreateBlueprintVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/textract-2018-06-27/CreateBlueprintVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/textract-2018-06-27/CreateBlueprintVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/textract-2018-06-27/CreateBlueprintVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/textract-2018-06-27/CreateBlueprintVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/CreateBlueprintVersion)
