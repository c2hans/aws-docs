---
source_url: https://docs.aws.amazon.com/acm/latest/APIReference/API_CreateAcmeDomainValidation.html
---

# CreateAcmeDomainValidation
<a name="API_CreateAcmeDomainValidation"></a>

Creates a domain validation for an ACME endpoint. Domain validations authorize the endpoint to issue certificates for specified domain names. You configure prevalidation to prove domain ownership.

## Request Syntax
<a name="API_CreateAcmeDomainValidation_RequestSyntax"></a>

```
{
   "AcmeEndpointArn": "{{string}}",
   "DomainName": "{{string}}",
   "IdempotencyToken": "{{string}}",
   "PrevalidationOptions": { ... },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateAcmeDomainValidation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [AcmeEndpointArn](#API_CreateAcmeDomainValidation_RequestSyntax) **   <a name="ACM-CreateAcmeDomainValidation-request-AcmeEndpointArn"></a>
The Amazon Resource Name (ARN) of the ACME endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:aws[a-z-]*:acm:[a-z0-9-]+:[0-9]{12}:acme-endpoint/[a-zA-Z0-9-]+`
Required: Yes

 ** [DomainName](#API_CreateAcmeDomainValidation_RequestSyntax) **   <a name="ACM-CreateAcmeDomainValidation-request-DomainName"></a>
The domain name to validate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `([a-z0-9]([a-z0-9-]*[a-z0-9])?\.)*[a-z0-9]([a-z0-9-]*[a-z0-9])?`
Required: Yes

 ** [PrevalidationOptions](#API_CreateAcmeDomainValidation_RequestSyntax) **   <a name="ACM-CreateAcmeDomainValidation-request-PrevalidationOptions"></a>
The prevalidation options for the domain.
Type: [PrevalidationOptions](API_PrevalidationOptions.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [IdempotencyToken](#API_CreateAcmeDomainValidation_RequestSyntax) **   <a name="ACM-CreateAcmeDomainValidation-request-IdempotencyToken"></a>
A unique, case-sensitive identifier to ensure idempotency of the request.
Type: String
Required: No

 ** [Tags](#API_CreateAcmeDomainValidation_RequestSyntax) **   <a name="ACM-CreateAcmeDomainValidation-request-Tags"></a>
One or more tags to associate with the domain validation.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateAcmeDomainValidation_ResponseSyntax"></a>

```
{
   "AcmeDomainValidationArn": "string"
}
```

## Response Elements
<a name="API_CreateAcmeDomainValidation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AcmeDomainValidationArn](#API_CreateAcmeDomainValidation_ResponseSyntax) **   <a name="ACM-CreateAcmeDomainValidation-response-AcmeDomainValidationArn"></a>
The Amazon Resource Name (ARN) of the created domain validation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:aws[a-z-]*:acm:[a-z0-9-]+:[0-9]{12}:acme-endpoint/[a-zA-Z0-9-]+/acme-domain-validation/[a-zA-Z0-9-]+`

## Errors
<a name="API_CreateAcmeDomainValidation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have access required to perform this action.
HTTP Status Code: 400

 ** ConflictException **
You are trying to update a resource or configuration that is already being created or updated. Wait for the previous operation to finish and try again.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified certificate cannot be found in the caller's account or the caller's account cannot be found.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
A service quota has been exceeded.
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
<a name="API_CreateAcmeDomainValidation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/acm-2015-12-08/CreateAcmeDomainValidation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/acm-2015-12-08/CreateAcmeDomainValidation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/CreateAcmeDomainValidation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/acm-2015-12-08/CreateAcmeDomainValidation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/CreateAcmeDomainValidation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/acm-2015-12-08/CreateAcmeDomainValidation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/acm-2015-12-08/CreateAcmeDomainValidation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/acm-2015-12-08/CreateAcmeDomainValidation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/acm-2015-12-08/CreateAcmeDomainValidation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/CreateAcmeDomainValidation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ACM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query acm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
