---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ResendOperationAuthorization.html
---

# ResendOperationAuthorization
<a name="API_domains_ResendOperationAuthorization"></a>

 Resend the form of authorization email for this operation.

## Request Syntax
<a name="API_domains_ResendOperationAuthorization_RequestSyntax"></a>

```
{
   "OperationId": "{{string}}"
}
```

## Request Parameters
<a name="API_domains_ResendOperationAuthorization_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [OperationId](#API_domains_ResendOperationAuthorization_RequestSyntax) **   <a name="Route53Domains-domains_ResendOperationAuthorization-request-OperationId"></a>
 Operation ID.
Type: String
Length Constraints: Maximum length of 255.
Required: Yes

## Response Elements
<a name="API_domains_ResendOperationAuthorization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_domains_ResendOperationAuthorization_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The requested item is not acceptable. For example, for APIs that accept a domain name, the request might specify a domain name that doesn't belong to the account that submitted the request. For `AcceptDomainTransferFromAnotherAwsAccount`, the password might be invalid.
 ** message **
The requested item is not acceptable. For example, for an OperationId it might refer to the ID of an operation that is already completed. For a domain name, it might not be a valid domain name or belong to the requester account.
HTTP Status Code: 400

## See Also
<a name="API_domains_ResendOperationAuthorization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53domains-2014-05-15/ResendOperationAuthorization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53domains-2014-05-15/ResendOperationAuthorization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53domains-2014-05-15/ResendOperationAuthorization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53domains-2014-05-15/ResendOperationAuthorization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53domains-2014-05-15/ResendOperationAuthorization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53domains-2014-05-15/ResendOperationAuthorization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53domains-2014-05-15/ResendOperationAuthorization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53domains-2014-05-15/ResendOperationAuthorization)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53domains-2014-05-15/ResendOperationAuthorization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53domains-2014-05-15/ResendOperationAuthorization)
