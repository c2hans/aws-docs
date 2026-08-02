---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_UntagResource.html
---

# UntagResource
<a name="API_UntagResource"></a>

Removes the specified tags from the specified resource.

## Request Syntax
<a name="API_UntagResource_RequestSyntax"></a>

```
{
   "ResourceArn": "{{string}}",
   "TagKeys": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_UntagResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceArn](#API_UntagResource_RequestSyntax) **   <a name="licensemanager-UntagResource-request-ResourceArn"></a>
Amazon Resource Name (ARN) of the resource.
Type: String
Required: Yes

 ** [TagKeys](#API_UntagResource_RequestSyntax) **   <a name="licensemanager-UntagResource-request-TagKeys"></a>
Keys identifying the tags to remove.
Type: Array of strings
Required: Yes

## Response Elements
<a name="API_UntagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UntagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to resource denied.
HTTP Status Code: 400

 ** AuthorizationException **
The AWS user account does not have permission to perform the action. Check the IAM policy associated with this account.
HTTP Status Code: 400

 ** InvalidParameterValueException **
One or more parameter values are not valid.
HTTP Status Code: 400

 ** RateLimitExceededException **
Too many requests have been submitted. Try again after a brief wait.
HTTP Status Code: 400

 ** ServerInternalException **
The server experienced an internal error. Try again.
HTTP Status Code: 500

 ** ValidationException **
The provided input is not valid. Try your request again.
HTTP Status Code: 400

## See Also
<a name="API_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-2018-08-01/UntagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-2018-08-01/UntagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/UntagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-2018-08-01/UntagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/UntagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-2018-08-01/UntagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-2018-08-01/UntagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-2018-08-01/UntagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/license-manager-2018-08-01/UntagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/UntagResource)
