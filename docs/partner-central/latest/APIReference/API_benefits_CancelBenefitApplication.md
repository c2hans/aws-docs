---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_benefits_CancelBenefitApplication.html
---

# CancelBenefitApplication
<a name="API_benefits_CancelBenefitApplication"></a>

Cancels a benefit application that is currently in progress, preventing further processing.

## Request Syntax
<a name="API_benefits_CancelBenefitApplication_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "ClientToken": "{{string}}",
   "Identifier": "{{string}}",
   "Reason": "{{string}}"
}
```

## Request Parameters
<a name="API_benefits_CancelBenefitApplication_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_benefits_CancelBenefitApplication_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_CancelBenefitApplication-request-Catalog"></a>
The catalog identifier that specifies which benefit catalog the application belongs to.
Type: String
Pattern: `[A-Za-z0-9_-]+`
Required: Yes

 ** [ClientToken](#API_benefits_CancelBenefitApplication_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_CancelBenefitApplication-request-ClientToken"></a>
A unique, case-sensitive identifier to ensure idempotent processing of the cancellation request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]{1,64}`
Required: Yes

 ** [Identifier](#API_benefits_CancelBenefitApplication_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_CancelBenefitApplication-request-Identifier"></a>
The unique identifier of the benefit application to cancel.
Type: String
Pattern: `(arn:.+|benappl-[0-9a-z]{14})`
Required: Yes

 ** [Reason](#API_benefits_CancelBenefitApplication_RequestSyntax) **   <a name="AWSPartnerCentral-benefits_CancelBenefitApplication-request-Reason"></a>
A descriptive reason explaining why the benefit application is being cancelled.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `[\s\S]{1,1000}`
Required: No

## Response Elements
<a name="API_benefits_CancelBenefitApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_benefits_CancelBenefitApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Thrown when the caller does not have sufficient permissions to perform the requested operation.
 ** Message **
A message describing the access denial.
HTTP Status Code: 400

 ** ConflictException **
Thrown when the request conflicts with the current state of the resource, such as attempting to modify a resource that has been changed by another process.
 ** Message **
A message describing the conflict.
HTTP Status Code: 400

 ** InternalServerException **
Thrown when an unexpected error occurs on the server side during request processing.
 ** Message **
A message describing the internal server error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Thrown when the requested resource cannot be found or does not exist.
 ** Message **
A message describing the resource not found error.
HTTP Status Code: 400

 ** ThrottlingException **
Thrown when the request rate exceeds the allowed limits and the request is being throttled.
 ** Message **
A message describing the throttling error.
HTTP Status Code: 400

 ** ValidationException **
Thrown when the request contains invalid parameters or fails input validation requirements.
 ** FieldList **
A list of fields that failed validation.
 ** Message **
A message describing the validation error.
 ** Reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_benefits_CancelBenefitApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-benefits-2018-05-10/CancelBenefitApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-benefits-2018-05-10/CancelBenefitApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-benefits-2018-05-10/CancelBenefitApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-benefits-2018-05-10/CancelBenefitApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-benefits-2018-05-10/CancelBenefitApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-benefits-2018-05-10/CancelBenefitApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-benefits-2018-05-10/CancelBenefitApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-benefits-2018-05-10/CancelBenefitApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-benefits-2018-05-10/CancelBenefitApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-benefits-2018-05-10/CancelBenefitApplication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
