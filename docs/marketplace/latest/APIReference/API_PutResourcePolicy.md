---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_PutResourcePolicy.html
---

# PutResourcePolicy
<a name="API_PutResourcePolicy"></a>

Attaches a resource-based policy to an entity. Examples of an entity include: `AmiProduct` and `ContainerProduct`.

## Request Syntax
<a name="API_PutResourcePolicy_RequestSyntax"></a>

```
POST /PutResourcePolicy HTTP/1.1
Content-type: application/json

{
   "Policy": "{{string}}",
   "ResourceArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutResourcePolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutResourcePolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Policy](#API_PutResourcePolicy_RequestSyntax) **   <a name="AWSMarketplaceService-PutResourcePolicy-request-Policy"></a>
The policy document to set; formatted in JSON.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.
Pattern: `^[\u0009\u000A\u000D\u0020-\u00FF]+$`
Required: Yes

 ** [ResourceArn](#API_PutResourcePolicy_RequestSyntax) **   <a name="AWSMarketplaceService-PutResourcePolicy-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the entity resource you want to associate with a resource policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^arn:[\w+=/,.@-]+:aws-marketplace:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*$`
Required: Yes

## Response Syntax
<a name="API_PutResourcePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutResourcePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied.
HTTP status code: 403
HTTP Status Code: 403

 ** InternalServiceException **
There was an internal service exception.
HTTP status code: 500
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource wasn't found.
HTTP status code: 404
HTTP Status Code: 404

 ** ThrottlingException **
Too many requests.
HTTP status code: 429
HTTP Status Code: 429

 ** ValidationException **
An error occurred during validation.
HTTP status code: 422
HTTP Status Code: 422

## See Also
<a name="API_PutResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/marketplace-catalog-2018-09-17/PutResourcePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/marketplace-catalog-2018-09-17/PutResourcePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/PutResourcePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/marketplace-catalog-2018-09-17/PutResourcePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/PutResourcePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/marketplace-catalog-2018-09-17/PutResourcePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/marketplace-catalog-2018-09-17/PutResourcePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/marketplace-catalog-2018-09-17/PutResourcePolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/marketplace-catalog-2018-09-17/PutResourcePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/PutResourcePolicy)
