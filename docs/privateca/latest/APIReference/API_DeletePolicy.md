---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeletePolicy.html
---

# DeletePolicy
<a name="API_DeletePolicy"></a>

Deletes the resource-based policy attached to a private CA. Deletion will remove any access that the policy has granted. If there is no policy attached to the private CA, this action will return successful.

If you delete a policy that was applied through AWS Resource Access Manager (RAM), the CA will be removed from all shares in which it was included.

The AWS Certificate Manager Service Linked Role that the policy supports is not affected when you delete the policy.

The current policy can be shown with [GetPolicy](https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetPolicy.html) and updated with [PutPolicy](https://docs.aws.amazon.com/privateca/latest/APIReference/API_PutPolicy.html).

**About Policies**
+ A policy grants access on a private CA to an AWS customer account, to AWS Organizations, or to an AWS Organizations unit. Policies are under the control of a CA administrator. For more information, see [Using a Resource Based Policy with AWS Private CA](https://docs.aws.amazon.com/privateca/latest/userguide/pca-rbp.html).
+ A policy permits a user of AWS Certificate Manager (ACM) to issue ACM certificates signed by a CA in another account.
+ For ACM to manage automatic renewal of these certificates, the ACM user must configure a Service Linked Role (SLR). The SLR allows the ACM service to assume the identity of the user, subject to confirmation against the AWS Private CA policy. For more information, see [Using a Service Linked Role with ACM](https://docs.aws.amazon.com/acm/latest/userguide/acm-slr.html).
+ Updates made in AWS Resource Manager (RAM) are reflected in policies. For more information, see [Attach a Policy for Cross-Account Access](https://docs.aws.amazon.com/privateca/latest/userguide/pca-ram.html).

## Request Syntax
<a name="API_DeletePolicy_RequestSyntax"></a>

```
{
   "ResourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DeletePolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceArn](#API_DeletePolicy_RequestSyntax) **   <a name="privateca-DeletePolicy-request-ResourceArn"></a>
The Amazon Resource Number (ARN) of the private CA that will have its policy deleted. You can find the CA's ARN by calling the [ListCertificateAuthorities](https://docs.aws.amazon.com/privateca/latest/APIReference/API_ListCertificateAuthorities.html) action. The ARN value must have the form `arn:aws:acm-pca:region:account:certificate-authority/01234567-89ab-cdef-0123-0123456789ab`.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w+=/,.@-]+:acm-pca:[\w+=/,.@-]*:[0-9]*:[\w+=,.@-]+(/[\w+=,.@-]+)*`
Required: Yes

## Response Elements
<a name="API_DeletePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeletePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
A previous update to your private CA is still ongoing.
HTTP Status Code: 400

 ** InvalidArnException **
The requested Amazon Resource Name (ARN) does not refer to an existing resource.
HTTP Status Code: 400

 ** InvalidStateException **
The state of the private CA does not allow this action to occur.
HTTP Status Code: 400

 ** LockoutPreventedException **
The current action was prevented because it would lock the caller out from performing subsequent actions. Verify that the specified parameters would not result in the caller being denied access to the resource.
HTTP Status Code: 400

 ** RequestFailedException **
The request has failed for an unspecified reason.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource such as a private CA, S3 bucket, certificate, audit report, or policy cannot be found.
HTTP Status Code: 400

## See Also
<a name="API_DeletePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-pca-2017-08-22/DeletePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-pca-2017-08-22/DeletePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/DeletePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-pca-2017-08-22/DeletePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/DeletePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-pca-2017-08-22/DeletePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-pca-2017-08-22/DeletePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-pca-2017-08-22/DeletePolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/acm-pca-2017-08-22/DeletePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/DeletePolicy)
