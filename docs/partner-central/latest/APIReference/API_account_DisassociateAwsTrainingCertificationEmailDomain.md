---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_DisassociateAwsTrainingCertificationEmailDomain.html
---

# DisassociateAwsTrainingCertificationEmailDomain
<a name="API_account_DisassociateAwsTrainingCertificationEmailDomain"></a>

Removes the association between an email domain and AWS training and certification for the partner account.

## Request Syntax
<a name="API_account_DisassociateAwsTrainingCertificationEmailDomain_RequestSyntax"></a>

```
{
   "Catalog": "{{string}}",
   "ClientToken": "{{string}}",
   "DomainName": "{{string}}",
   "Identifier": "{{string}}"
}
```

## Request Parameters
<a name="API_account_DisassociateAwsTrainingCertificationEmailDomain_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [Catalog](#API_account_DisassociateAwsTrainingCertificationEmailDomain_RequestSyntax) **   <a name="AWSPartnerCentral-account_DisassociateAwsTrainingCertificationEmailDomain-request-Catalog"></a>
The catalog identifier for the partner account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-]+`
Required: Yes

 ** [DomainName](#API_account_DisassociateAwsTrainingCertificationEmailDomain_RequestSyntax) **   <a name="AWSPartnerCentral-account_DisassociateAwsTrainingCertificationEmailDomain-request-DomainName"></a>
The domain name to disassociate from AWS training and certification.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*`
Required: Yes

 ** [Identifier](#API_account_DisassociateAwsTrainingCertificationEmailDomain_RequestSyntax) **   <a name="AWSPartnerCentral-account_DisassociateAwsTrainingCertificationEmailDomain-request-Identifier"></a>
The unique identifier of the partner account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `(partner-[A-Za-z0-9]{13}|arn:[a-z-]+:partnercentral:[a-z0-9-]+:[0-9]{12}:catalog/[A-Za-z-_]+/partner/partner-[A-Za-z0-9]{13})`
Required: Yes

 ** [ClientToken](#API_account_DisassociateAwsTrainingCertificationEmailDomain_RequestSyntax) **   <a name="AWSPartnerCentral-account_DisassociateAwsTrainingCertificationEmailDomain-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`
Required: No

## Response Elements
<a name="API_account_DisassociateAwsTrainingCertificationEmailDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_account_DisassociateAwsTrainingCertificationEmailDomain_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.
 ** Reason **
The specific reason for the access denial.
HTTP Status Code: 400

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.
 ** Reason **
The specific reason for the conflict.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.
 ** Reason **
The specific reason why the resource was not found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.
 ** QuotaCode **
The quota code associated with the throttling error.
 ** ServiceCode **
The service code associated with the throttling error.
HTTP Status Code: 400

 ** ValidationException **
The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.
 ** ErrorDetails **
A list of detailed validation errors that occurred during request processing.
 ** Reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_account_DisassociateAwsTrainingCertificationEmailDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-account-2025-04-04/DisassociateAwsTrainingCertificationEmailDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-account-2025-04-04/DisassociateAwsTrainingCertificationEmailDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-account-2025-04-04/DisassociateAwsTrainingCertificationEmailDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-account-2025-04-04/DisassociateAwsTrainingCertificationEmailDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-account-2025-04-04/DisassociateAwsTrainingCertificationEmailDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-account-2025-04-04/DisassociateAwsTrainingCertificationEmailDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-account-2025-04-04/DisassociateAwsTrainingCertificationEmailDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-account-2025-04-04/DisassociateAwsTrainingCertificationEmailDomain)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/partnercentral-account-2025-04-04/DisassociateAwsTrainingCertificationEmailDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-account-2025-04-04/DisassociateAwsTrainingCertificationEmailDomain)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Partner Central. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query partner-central` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
