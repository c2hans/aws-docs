---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_invoicing_TagResource.html
---

# TagResource
<a name="API_invoicing_TagResource"></a>

Adds a tag to a resource.

## Request Syntax
<a name="API_invoicing_TagResource_RequestSyntax"></a>

```
{
   "ResourceArn": "{{string}}",
   "ResourceTags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_invoicing_TagResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceArn](#API_invoicing_TagResource_RequestSyntax) **   <a name="awscostmanagement-invoicing_TagResource-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the tags.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:(invoicing)::[0-9]{12}:[-a-zA-Z0-9/:_]+`
Required: Yes

 ** [ResourceTags](#API_invoicing_TagResource_RequestSyntax) **   <a name="awscostmanagement-invoicing_TagResource-request-ResourceTags"></a>
 Adds a tag to a resource.
Type: Array of [ResourceTag](API_invoicing_ResourceTag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: Yes

## Response Elements
<a name="API_invoicing_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_invoicing_TagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
 ** resourceName **
You don't have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The processing request failed because of an unknown error, exception, or failure.
 ** retryAfterSeconds **
The processing request failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource could not be found.
 ** resourceName **
The resource could not be found.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
The request was rejected because it attempted to create resources beyond the current AWS account limits. The error message describes the limit exceeded.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
 The input fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
 The input fails to satisfy the constraints specified by an AWS service.
 ** reason **
You don't have sufficient access to perform this action.
 ** resourceName **
You don't have sufficient access to perform this action.
HTTP Status Code: 400

## See Also
<a name="API_invoicing_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/invoicing-2024-12-01/TagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/invoicing-2024-12-01/TagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/invoicing-2024-12-01/TagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/invoicing-2024-12-01/TagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/invoicing-2024-12-01/TagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/invoicing-2024-12-01/TagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/invoicing-2024-12-01/TagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/invoicing-2024-12-01/TagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/invoicing-2024-12-01/TagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/invoicing-2024-12-01/TagResource)
