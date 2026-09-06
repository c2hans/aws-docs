---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_DeleteAccessPointPolicyForObjectLambda.html
---

# DeleteAccessPointPolicyForObjectLambda
<a name="API_control_DeleteAccessPointPolicyForObjectLambda"></a>

**Note**
This operation is not supported by directory buckets.

Removes the resource policy for an Object Lambda Access Point.

The following actions are related to `DeleteAccessPointPolicyForObjectLambda`:
+  [GetAccessPointPolicyForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointPolicyForObjectLambda.html)
+  [PutAccessPointPolicyForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointPolicyForObjectLambda.html)

## Request Syntax
<a name="API_control_DeleteAccessPointPolicyForObjectLambda_RequestSyntax"></a>

```
DELETE /v20180820/accesspointforobjectlambda/{{name}}/policy HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
```

## URI Request Parameters
<a name="API_control_DeleteAccessPointPolicyForObjectLambda_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_control_DeleteAccessPointPolicyForObjectLambda_RequestSyntax) **   <a name="AmazonS3-control_DeleteAccessPointPolicyForObjectLambda-request-uri-uri-Name"></a>
The name of the Object Lambda Access Point you want to delete the policy for.
Length Constraints: Minimum length of 3. Maximum length of 45.
Pattern: `^[a-z0-9]([a-z0-9\-]*[a-z0-9])?$`
Required: Yes

 ** [x-amz-account-id](#API_control_DeleteAccessPointPolicyForObjectLambda_RequestSyntax) **   <a name="AmazonS3-control_DeleteAccessPointPolicyForObjectLambda-request-header-AccountId"></a>
The account ID for the account that owns the specified Object Lambda Access Point.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_DeleteAccessPointPolicyForObjectLambda_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_control_DeleteAccessPointPolicyForObjectLambda_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_control_DeleteAccessPointPolicyForObjectLambda_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## See Also
<a name="API_control_DeleteAccessPointPolicyForObjectLambda_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/DeleteAccessPointPolicyForObjectLambda)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/DeleteAccessPointPolicyForObjectLambda)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/DeleteAccessPointPolicyForObjectLambda)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/DeleteAccessPointPolicyForObjectLambda)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/DeleteAccessPointPolicyForObjectLambda)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/DeleteAccessPointPolicyForObjectLambda)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/DeleteAccessPointPolicyForObjectLambda)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/DeleteAccessPointPolicyForObjectLambda)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/DeleteAccessPointPolicyForObjectLambda)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/DeleteAccessPointPolicyForObjectLambda)
