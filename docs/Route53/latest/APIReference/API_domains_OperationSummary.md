---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_OperationSummary.html
---

# OperationSummary
<a name="API_domains_OperationSummary"></a>

OperationSummary includes the following elements.

## Contents
<a name="API_domains_OperationSummary_Contents"></a>

 ** DomainName **   <a name="Route53Domains-Type-domains_OperationSummary-DomainName"></a>
 Name of the domain.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** LastUpdatedDate **   <a name="Route53Domains-Type-domains_OperationSummary-LastUpdatedDate"></a>
 The date when the last change was made in Unix time format and Coordinated Universal Time (UTC).
Type: Timestamp
Required: No

 ** Message **   <a name="Route53Domains-Type-domains_OperationSummary-Message"></a>
 Message about the operation.
Type: String
Required: No

 ** OperationId **   <a name="Route53Domains-Type-domains_OperationSummary-OperationId"></a>
Identifier returned to track the requested action.
Type: String
Length Constraints: Maximum length of 255.
Required: No

 ** Status **   <a name="Route53Domains-Type-domains_OperationSummary-Status"></a>
The current status of the requested operation in the system.
Type: String
Valid Values: `SUBMITTED | IN_PROGRESS | ERROR | SUCCESSFUL | FAILED`
Required: No

 ** StatusFlag **   <a name="Route53Domains-Type-domains_OperationSummary-StatusFlag"></a>
 Automatically checks whether there are no outstanding operations on domains that need customer attention.
 Valid values are:
+  `PENDING_ACCEPTANCE`: The operation is waiting for acceptance from the account that is receiving the domain.
+  `PENDING_CUSTOMER_ACTION`: The operation is waiting for customer action, for example, returning an email.
+  `PENDING_AUTHORIZATION`: The operation is waiting for the form of authorization. For more information, see [ResendOperationAuthorization](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ResendOperationAuthorization.html).
+  `PENDING_PAYMENT_VERIFICATION`: The operation is waiting for the payment method to validate.
+  `PENDING_SUPPORT_CASE`: The operation includes a support case and is waiting for its resolution.
Type: String
Valid Values: `PENDING_ACCEPTANCE | PENDING_CUSTOMER_ACTION | PENDING_AUTHORIZATION | PENDING_PAYMENT_VERIFICATION | PENDING_SUPPORT_CASE`
Required: No

 ** SubmittedDate **   <a name="Route53Domains-Type-domains_OperationSummary-SubmittedDate"></a>
The date when the request was submitted.
Type: Timestamp
Required: No

 ** Type **   <a name="Route53Domains-Type-domains_OperationSummary-Type"></a>
Type of the action requested.
Type: String
Valid Values: `REGISTER_DOMAIN | DELETE_DOMAIN | TRANSFER_IN_DOMAIN | UPDATE_DOMAIN_CONTACT | UPDATE_NAMESERVER | CHANGE_PRIVACY_PROTECTION | DOMAIN_LOCK | ENABLE_AUTORENEW | DISABLE_AUTORENEW | ADD_DNSSEC | REMOVE_DNSSEC | EXPIRE_DOMAIN | TRANSFER_OUT_DOMAIN | CHANGE_DOMAIN_OWNER | RENEW_DOMAIN | PUSH_DOMAIN | INTERNAL_TRANSFER_OUT_DOMAIN | INTERNAL_TRANSFER_IN_DOMAIN | RELEASE_TO_GANDI | TRANSFER_ON_RENEW | RESTORE_DOMAIN`
Required: No

## See Also
<a name="API_domains_OperationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53domains-2014-05-15/OperationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53domains-2014-05-15/OperationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53domains-2014-05-15/OperationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
