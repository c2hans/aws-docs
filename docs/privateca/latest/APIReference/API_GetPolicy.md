---
source_url: https://docs.aws.amazon.com/privateca/latest/APIReference/API_GetPolicy.html
---

# GetPolicy
<a name="API_GetPolicy"></a>

Retrieves the resource-based policy attached to a private CA. If either the private CA resource or the policy cannot be found, this action returns a `ResourceNotFoundException`.

The policy can be attached or updated with [PutPolicy](https://docs.aws.amazon.com/privateca/latest/APIReference/API_PutPolicy.html) and removed with [DeletePolicy](https://docs.aws.amazon.com/privateca/latest/APIReference/API_DeletePolicy.html).

**About Policies**
+ A policy grants access on a private CA to an AWS customer account, to AWS Organizations, or to an AWS Organizations unit. Policies are under the control of a CA administrator. For more information, see [Using a Resource Based Policy with AWS Private CA](https://docs.aws.amazon.com/privateca/latest/userguide/pca-rbp.html).
+ A policy permits a user of AWS Certificate Manager (ACM) to issue ACM certificates signed by a CA in another account.
+ For ACM to manage automatic renewal of these certificates, the ACM user must configure a Service Linked Role (SLR). The SLR allows the ACM service to assume the identity of the user, subject to confirmation against the AWS Private CA policy. For more information, see [Using a Service Linked Role with ACM](https://docs.aws.amazon.com/acm/latest/userguide/acm-slr.html).
+ Updates made in AWS Resource Manager (RAM) are reflected in policies. For more information, see [Attach a Policy for Cross-Account Access](https://docs.aws.amazon.com/privateca/latest/userguide/pca-ram.html).

## Request Syntax
<a name="API_GetPolicy_RequestSyntax"></a>

```
{
   "ResourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_GetPolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceArn](#API_GetPolicy_RequestSyntax) **   <a name="privateca-GetPolicy-request-ResourceArn"></a>
The Amazon Resource Number (ARN) of the private CA that will have its policy retrieved. You can find the CA's ARN by calling the ListCertificateAuthorities action.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:[\w+=/,.@-]+:acm-pca:[\w+=/,.@-]*:[0-9]*:[\w+=,.@-]+(/[\w+=,.@-]+)*`
Required: Yes

## Response Syntax
<a name="API_GetPolicy_ResponseSyntax"></a>

```
{
   "Policy": "string"
}
```

## Response Elements
<a name="API_GetPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Policy](#API_GetPolicy_ResponseSyntax) **   <a name="privateca-GetPolicy-response-Policy"></a>
The policy attached to the private CA as a JSON document.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 81920.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`

## Errors
<a name="API_GetPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidArnException **
The requested Amazon Resource Name (ARN) does not refer to an existing resource.
HTTP Status Code: 400

 ** InvalidStateException **
The state of the private CA does not allow this action to occur.
HTTP Status Code: 400

 ** RequestFailedException **
The request has failed for an unspecified reason.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource such as a private CA, S3 bucket, certificate, audit report, or policy cannot be found.
HTTP Status Code: 400

## See Also
<a name="API_GetPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-pca-2017-08-22/GetPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-pca-2017-08-22/GetPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-pca-2017-08-22/GetPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-pca-2017-08-22/GetPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-pca-2017-08-22/GetPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-pca-2017-08-22/GetPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-pca-2017-08-22/GetPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-pca-2017-08-22/GetPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/acm-pca-2017-08-22/GetPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-pca-2017-08-22/GetPolicy)
