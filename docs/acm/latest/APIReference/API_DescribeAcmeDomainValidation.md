---
source_url: https://docs.aws.amazon.com/acm/latest/APIReference/API_DescribeAcmeDomainValidation.html
---

# DescribeAcmeDomainValidation
<a name="API_DescribeAcmeDomainValidation"></a>

Returns detailed metadata about the specified domain validation, including its status, domain scope, and DNS resource records required for validation.

## Request Syntax
<a name="API_DescribeAcmeDomainValidation_RequestSyntax"></a>

```
{
   "AcmeDomainValidationArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeAcmeDomainValidation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [AcmeDomainValidationArn](#API_DescribeAcmeDomainValidation_RequestSyntax) **   <a name="ACM-DescribeAcmeDomainValidation-request-AcmeDomainValidationArn"></a>
The Amazon Resource Name (ARN) of the ACME domain validation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:aws[a-z-]*:acm:[a-z0-9-]+:[0-9]{12}:acme-endpoint/[a-zA-Z0-9-]+/acme-domain-validation/[a-zA-Z0-9-]+`
Required: Yes

## Response Syntax
<a name="API_DescribeAcmeDomainValidation_ResponseSyntax"></a>

```
{
   "AcmeDomainValidation": {
      "AcmeDomainValidationArn": "string",
      "AcmeEndpointArn": "string",
      "CreatedAt": number,
      "DomainName": "string",
      "FailureDetails": {
         "Message": "string",
         "Reason": "string"
      },
      "PrevalidationDetails": { ... },
      "PrevalidationType": "string",
      "Status": "string",
      "UpdatedAt": number
   }
}
```

## Response Elements
<a name="API_DescribeAcmeDomainValidation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AcmeDomainValidation](#API_DescribeAcmeDomainValidation_ResponseSyntax) **   <a name="ACM-DescribeAcmeDomainValidation-response-AcmeDomainValidation"></a>
The ACME domain validation details.
Type: [AcmeDomainValidation](API_AcmeDomainValidation.md) object

## Errors
<a name="API_DescribeAcmeDomainValidation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have access required to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified certificate cannot be found in the caller's account or the caller's account cannot be found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied because it exceeded a quota.
 ** throttlingReasons **
One or more reasons why the request was throttled.
HTTP Status Code: 400

 ** ValidationException **
The supplied input failed to satisfy constraints of an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_DescribeAcmeDomainValidation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-2015-12-08/DescribeAcmeDomainValidation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-2015-12-08/DescribeAcmeDomainValidation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/DescribeAcmeDomainValidation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-2015-12-08/DescribeAcmeDomainValidation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/DescribeAcmeDomainValidation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-2015-12-08/DescribeAcmeDomainValidation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-2015-12-08/DescribeAcmeDomainValidation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-2015-12-08/DescribeAcmeDomainValidation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/acm-2015-12-08/DescribeAcmeDomainValidation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/DescribeAcmeDomainValidation)
