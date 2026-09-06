---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_DeleteRegistryPolicy.html
---

# DeleteRegistryPolicy
<a name="API_DeleteRegistryPolicy"></a>

Deletes the registry permissions policy.

## Response Syntax
<a name="API_DeleteRegistryPolicy_ResponseSyntax"></a>

```
{
   "policyText": "string",
   "registryId": "string"
}
```

## Response Elements
<a name="API_DeleteRegistryPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [policyText](#API_DeleteRegistryPolicy_ResponseSyntax) **   <a name="ECR-DeleteRegistryPolicy-response-policyText"></a>
The contents of the registry permissions policy that was deleted.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10240.

 ** [registryId](#API_DeleteRegistryPolicy_ResponseSyntax) **   <a name="ECR-DeleteRegistryPolicy-response-registryId"></a>
The registry ID associated with the request.
Type: String
Pattern: `[0-9]{12}`

## Errors
<a name="API_DeleteRegistryPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
 ** message **
The error message associated with the exception.
HTTP Status Code: 400

 ** RegistryPolicyNotFoundException **
The registry doesn't have an associated registry policy.
HTTP Status Code: 400

 ** ServerException **
These errors are usually caused by a server-side issue.
 ** message **
The error message associated with the exception.
HTTP Status Code: 500

 ** ValidationException **
There was an exception validating this request.
HTTP Status Code: 400

## See Also
<a name="API_DeleteRegistryPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/DeleteRegistryPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/DeleteRegistryPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/DeleteRegistryPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/DeleteRegistryPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/DeleteRegistryPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/DeleteRegistryPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/DeleteRegistryPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/DeleteRegistryPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/DeleteRegistryPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/DeleteRegistryPolicy)
