---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_PutResourcePolicy.html
---

# PutResourcePolicy
<a name="API_osis_PutResourcePolicy"></a>

Attaches a resource-based policy to an OpenSearch Ingestion resource. Resource-based policies grant permissions to principals to perform actions on the resource.

## Request Syntax
<a name="API_osis_PutResourcePolicy_RequestSyntax"></a>

```
PUT /2022-01-01/osis/resourcePolicy/{{ResourceArn}} HTTP/1.1
Content-type: application/json

{
   "Policy": "{{string}}"
}
```

## URI Request Parameters
<a name="API_osis_PutResourcePolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ResourceArn](#API_osis_PutResourcePolicy_RequestSyntax) **   <a name="opensearchservice-osis_PutResourcePolicy-request-uri-ResourceArn"></a>
The Amazon Resource Name (ARN) of the resource to attach the policy to.
Length Constraints: Minimum length of 46. Maximum length of 76.
Pattern: `^arn:(aws|aws\-cn|aws\-us\-gov|aws\-iso|aws\-iso\-b):osis:.+:pipeline\/.+$`
Required: Yes

## Request Body
<a name="API_osis_PutResourcePolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Policy](#API_osis_PutResourcePolicy_RequestSyntax) **   <a name="opensearchservice-osis_PutResourcePolicy-request-Policy"></a>
The resource-based policy document in JSON format.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 204800.
Required: Yes

## Response Syntax
<a name="API_osis_PutResourcePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Policy": "string",
   "ResourceArn": "string"
}
```

## Response Elements
<a name="API_osis_PutResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Policy](#API_osis_PutResourcePolicy_ResponseSyntax) **   <a name="opensearchservice-osis_PutResourcePolicy-response-Policy"></a>
The resource-based policy document that was attached to the resource.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 204800.

 ** [ResourceArn](#API_osis_PutResourcePolicy_ResponseSyntax) **   <a name="opensearchservice-osis_PutResourcePolicy-response-ResourceArn"></a>
The Amazon Resource Name (ARN) of the resource.
Type: String
Length Constraints: Minimum length of 46. Maximum length of 76.
Pattern: `^arn:(aws|aws\-cn|aws\-us\-gov|aws\-iso|aws\-iso\-b):osis:.+:pipeline\/.+$`

## Errors
<a name="API_osis_PutResourcePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permissions to access the resource.
HTTP Status Code: 403

 ** DisabledOperationException **
Exception is thrown when an operation has been disabled.
HTTP Status Code: 409

 ** InternalException **
The request failed because of an unknown error, exception, or failure (the failure is internal to the service).
HTTP Status Code: 500

 ** LimitExceededException **
You attempted to create more than the allowed number of tags.
HTTP Status Code: 409

 ** ResourceNotFoundException **
You attempted to access or delete a resource that does not exist.
HTTP Status Code: 404

 ** ValidationException **
An exception for missing or invalid input fields.
HTTP Status Code: 400

## See Also
<a name="API_osis_PutResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/osis-2022-01-01/PutResourcePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/osis-2022-01-01/PutResourcePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/osis-2022-01-01/PutResourcePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/osis-2022-01-01/PutResourcePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/osis-2022-01-01/PutResourcePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/osis-2022-01-01/PutResourcePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/osis-2022-01-01/PutResourcePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/osis-2022-01-01/PutResourcePolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/osis-2022-01-01/PutResourcePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/osis-2022-01-01/PutResourcePolicy)
