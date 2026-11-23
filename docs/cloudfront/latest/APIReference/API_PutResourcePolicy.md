---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_PutResourcePolicy.html
---

# PutResourcePolicy

Creates a resource control policy for a given CloudFront resource.

## Request Syntax
<a name="API_PutResourcePolicy_RequestSyntax"></a>

```
POST /2020-05-31/put-resource-policy HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<PutResourcePolicyRequest xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <PolicyDocument>{{string}}</PolicyDocument>
   <ResourceArn>{{string}}</ResourceArn>
</PutResourcePolicyRequest>
```

## URI Request Parameters
<a name="API_PutResourcePolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutResourcePolicy_RequestBody"></a>

The request accepts the following data in XML format.

 ** [PutResourcePolicyRequest](#API_PutResourcePolicy_RequestSyntax) **   <a name="cloudfront-PutResourcePolicy-request-PutResourcePolicyRequest"></a>
Root level tag for the PutResourcePolicyRequest parameters.
Required: Yes

 ** [PolicyDocument](#API_PutResourcePolicy_RequestSyntax) **   <a name="cloudfront-PutResourcePolicy-request-PolicyDocument"></a>
The JSON-formatted resource policy to create.
Type: String
Required: Yes

 ** [ResourceArn](#API_PutResourcePolicy_RequestSyntax) **   <a name="cloudfront-PutResourcePolicy-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the CloudFront resource for which the policy is being created.
Type: String
Required: Yes

## Response Syntax
<a name="API_PutResourcePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<PutResourcePolicyResult>
   <ResourceArn>string</ResourceArn>
</PutResourcePolicyResult>
```

## Response Elements
<a name="API_PutResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in XML format by the service.

 ** [PutResourcePolicyResult](#API_PutResourcePolicy_ResponseSyntax) **   <a name="cloudfront-PutResourcePolicy-response-PutResourcePolicyResult"></a>
Root level tag for the PutResourcePolicyResult parameters.
Required: Yes

 ** [ResourceArn](#API_PutResourcePolicy_ResponseSyntax) **   <a name="cloudfront-PutResourcePolicy-response-ResourceArn"></a>
The Amazon Resource Name (ARN) of the CloudFront resource for which the policy was created.
Type: String

## Errors
<a name="API_PutResourcePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDenied **
Access denied.
HTTP Status Code: 403

 ** EntityNotFound **
The entity was not found.
HTTP Status Code: 404

 ** IllegalUpdate **
The update contains modifications that are not allowed.
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
<a name="API_PutResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/PutResourcePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cloudfront-2020-05-31/PutResourcePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/PutResourcePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/PutResourcePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/PutResourcePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/PutResourcePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/PutResourcePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/PutResourcePolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/PutResourcePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/PutResourcePolicy)
