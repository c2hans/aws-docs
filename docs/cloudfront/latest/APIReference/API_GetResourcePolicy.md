---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_GetResourcePolicy.html
---

# GetResourcePolicy

Retrieves the resource policy for the specified CloudFront resource that you own and have shared.

## Request Syntax
<a name="API_GetResourcePolicy_RequestSyntax"></a>

```
POST /2020-05-31/get-resource-policy HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<GetResourcePolicyRequest xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <ResourceArn>{{string}}</ResourceArn>
</GetResourcePolicyRequest>
```

## URI Request Parameters
<a name="API_GetResourcePolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetResourcePolicy_RequestBody"></a>

The request accepts the following data in XML format.

 ** [GetResourcePolicyRequest](#API_GetResourcePolicy_RequestSyntax) **   <a name="cloudfront-GetResourcePolicy-request-GetResourcePolicyRequest"></a>
Root level tag for the GetResourcePolicyRequest parameters.
Required: Yes

 ** [ResourceArn](#API_GetResourcePolicy_RequestSyntax) **   <a name="cloudfront-GetResourcePolicy-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the CloudFront resource that is associated with the resource policy.
Type: String
Required: Yes

## Response Syntax
<a name="API_GetResourcePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<GetResourcePolicyResult>
   <PolicyDocument>string</PolicyDocument>
   <ResourceArn>string</ResourceArn>
</GetResourcePolicyResult>
```

## Response Elements
<a name="API_GetResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [GetResourcePolicyResult](#API_GetResourcePolicy_ResponseSyntax) **   <a name="cloudfront-GetResourcePolicy-response-GetResourcePolicyResult"></a>
Root level tag for the GetResourcePolicyResult parameters.
Required: Yes

 ** [PolicyDocument](#API_GetResourcePolicy_ResponseSyntax) **   <a name="cloudfront-GetResourcePolicy-response-PolicyDocument"></a>
The resource policy in JSON format.
Type: String

 ** [ResourceArn](#API_GetResourcePolicy_ResponseSyntax) **   <a name="cloudfront-GetResourcePolicy-response-ResourceArn"></a>
The Amazon Resource Name (ARN) of the CloudFront resource that is associated with the resource policy.
Type: String

## Errors
<a name="API_GetResourcePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **
Access denied.
HTTP Status Code: 403

 ** EntityNotFound **
The entity was not found.
HTTP Status Code: 404

 ** InvalidArgument **
An argument is invalid.
HTTP Status Code: 400

 ** UnsupportedOperation **
This operation is not supported in this AWS Region.
HTTP Status Code: 400

## See Also
<a name="API_GetResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetResourcePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/GetResourcePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetResourcePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetResourcePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetResourcePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetResourcePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetResourcePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetResourcePolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetResourcePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetResourcePolicy)
