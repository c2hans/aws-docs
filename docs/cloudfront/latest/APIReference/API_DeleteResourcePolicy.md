---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_DeleteResourcePolicy.html
---

# DeleteResourcePolicy

Deletes the resource policy attached to the CloudFront resource.

## Request Syntax
<a name="API_DeleteResourcePolicy_RequestSyntax"></a>

```
POST /2020-05-31/delete-resource-policy HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<DeleteResourcePolicyRequest xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <ResourceArn>{{string}}</ResourceArn>
</DeleteResourcePolicyRequest>
```

## URI Request Parameters
<a name="API_DeleteResourcePolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteResourcePolicy_RequestBody"></a>

The request accepts the following data in XML format.

 ** [DeleteResourcePolicyRequest](#API_DeleteResourcePolicy_RequestSyntax) **   <a name="cloudfront-DeleteResourcePolicy-request-DeleteResourcePolicyRequest"></a>
Root level tag for the DeleteResourcePolicyRequest parameters.
Required: Yes

 ** [ResourceArn](#API_DeleteResourcePolicy_RequestSyntax) **   <a name="cloudfront-DeleteResourcePolicy-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the CloudFront resource for which the resource policy should be deleted.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeleteResourcePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteResourcePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **
Access denied.
HTTP Status Code: 403

 ** EntityNotFound **
The entity was not found.
HTTP Status Code: 404

 ** IllegalDelete **
Deletion is not allowed for this entity.
HTTP Status Code: 400

 ** InvalidArgument **
An argument is invalid.
HTTP Status Code: 400

 ** PreconditionFailed **
The precondition in one or more of the request fields evaluated to `false`.
HTTP Status Code: 412

 ** UnsupportedOperation **
This operation is not supported in this AWS Region.
HTTP Status Code: 400

## See Also
<a name="API_DeleteResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/DeleteResourcePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/DeleteResourcePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DeleteResourcePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/DeleteResourcePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DeleteResourcePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/DeleteResourcePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/DeleteResourcePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/DeleteResourcePolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/DeleteResourcePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DeleteResourcePolicy)
