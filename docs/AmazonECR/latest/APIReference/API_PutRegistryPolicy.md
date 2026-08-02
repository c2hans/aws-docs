---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_PutRegistryPolicy.html
---

# PutRegistryPolicy
<a name="API_PutRegistryPolicy"></a>

Creates or updates the permissions policy for your registry.

A registry policy is used to specify permissions for another AWS account and is used when configuring cross-account replication. For more information, see [Registry permissions](https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry-permissions.html) in the *Amazon Elastic Container Registry User Guide*.

## Request Syntax
<a name="API_PutRegistryPolicy_RequestSyntax"></a>

```
{
   "policyText": "{{string}}"
}
```

## Request Parameters
<a name="API_PutRegistryPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [policyText](#API_PutRegistryPolicy_RequestSyntax) **   <a name="ECR-PutRegistryPolicy-request-policyText"></a>
The JSON policy text to apply to your registry. The policy text follows the same format as IAM policy text. For more information, see [Registry permissions](https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry-permissions.html) in the *Amazon Elastic Container Registry User Guide*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10240.
Required: Yes

## Response Syntax
<a name="API_PutRegistryPolicy_ResponseSyntax"></a>

```
{
   "policyText": "string",
   "registryId": "string"
}
```

## Response Elements
<a name="API_PutRegistryPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [policyText](#API_PutRegistryPolicy_ResponseSyntax) **   <a name="ECR-PutRegistryPolicy-response-policyText"></a>
The JSON policy text for your registry.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10240.

 ** [registryId](#API_PutRegistryPolicy_ResponseSyntax) **   <a name="ECR-PutRegistryPolicy-response-registryId"></a>
The registry ID associated with the request.
Type: String
Pattern: `[0-9]{12}`

## Errors
<a name="API_PutRegistryPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
The specified parameter is invalid. Review the available parameters for the API request.
 ** message **
The error message associated with the exception.
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
<a name="API_PutRegistryPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ecr-2015-09-21/PutRegistryPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ecr-2015-09-21/PutRegistryPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/PutRegistryPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ecr-2015-09-21/PutRegistryPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/PutRegistryPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ecr-2015-09-21/PutRegistryPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ecr-2015-09-21/PutRegistryPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ecr-2015-09-21/PutRegistryPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ecr-2015-09-21/PutRegistryPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/PutRegistryPolicy)
