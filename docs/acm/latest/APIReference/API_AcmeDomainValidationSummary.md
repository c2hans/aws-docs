---
source_url: https://docs.aws.amazon.com/acm/latest/APIReference/API_AcmeDomainValidationSummary.html
---

# AcmeDomainValidationSummary
<a name="API_AcmeDomainValidationSummary"></a>

Contains summary information about an ACME domain validation.

## Contents
<a name="API_AcmeDomainValidationSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AcmeDomainValidationArn **   <a name="ACM-Type-AcmeDomainValidationSummary-AcmeDomainValidationArn"></a>
The Amazon Resource Name (ARN) of the ACME domain validation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:aws[a-z-]*:acm:[a-z0-9-]+:[0-9]{12}:acme-endpoint/[a-zA-Z0-9-]+/acme-domain-validation/[a-zA-Z0-9-]+`
Required: No

 ** AcmeEndpointArn **   <a name="ACM-Type-AcmeDomainValidationSummary-AcmeEndpointArn"></a>
The Amazon Resource Name (ARN) of the ACME endpoint.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:aws[a-z-]*:acm:[a-z0-9-]+:[0-9]{12}:acme-endpoint/[a-zA-Z0-9-]+`
Required: No

 ** CreatedAt **   <a name="ACM-Type-AcmeDomainValidationSummary-CreatedAt"></a>
The time at which the domain validation was created.
Type: Timestamp
Required: No

 ** DomainName **   <a name="ACM-Type-AcmeDomainValidationSummary-DomainName"></a>
The domain name being validated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `([a-z0-9]([a-z0-9-]*[a-z0-9])?\.)*[a-z0-9]([a-z0-9-]*[a-z0-9])?`
Required: No

 ** FailureDetails **   <a name="ACM-Type-AcmeDomainValidationSummary-FailureDetails"></a>
Details about the failure, if the validation failed.
Type: [FailureDetails](API_FailureDetails.md) object
Required: No

 ** PrevalidationDetails **   <a name="ACM-Type-AcmeDomainValidationSummary-PrevalidationDetails"></a>
Details about the prevalidation configuration.
Type: [PrevalidationDetails](API_PrevalidationDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** PrevalidationType **   <a name="ACM-Type-AcmeDomainValidationSummary-PrevalidationType"></a>
The type of prevalidation used.
Type: String
Valid Values: `DNS_PREVALIDATION`
Required: No

 ** Status **   <a name="ACM-Type-AcmeDomainValidationSummary-Status"></a>
The status of the domain validation.
Type: String
Valid Values: `VALIDATING | VALID | INVALID | DELETING`
Required: No

 ** UpdatedAt **   <a name="ACM-Type-AcmeDomainValidationSummary-UpdatedAt"></a>
The time at which the domain validation was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_AcmeDomainValidationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/AcmeDomainValidationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/AcmeDomainValidationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/AcmeDomainValidationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ACM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query acm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
