---
source_url: https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreateAccountStatus.html
---

# CreateAccountStatus
<a name="API_CreateAccountStatus"></a>

Contains the status about a [CreateAccount](API_CreateAccount.md) or [CreateGovCloudAccount](API_CreateGovCloudAccount.md) request to create an AWS account or an AWS GovCloud (US) account in an organization.

## Contents
<a name="API_CreateAccountStatus_Contents"></a>

 ** AccountId **   <a name="organizations-Type-CreateAccountStatus-AccountId"></a>
If the account was created successfully, the unique identifier (ID) of the new account.
The [regex pattern](http://wikipedia.org/wiki/regex) for an account ID string requires exactly 12 digits.
Type: String
Length Constraints: Maximum length of 12.
Pattern: `^\d{12}$`
Required: No

 ** AccountName **   <a name="organizations-Type-CreateAccountStatus-AccountName"></a>
The account name given to the account when it was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[\u0020-\u007E]+`
Required: No

 ** CompletedTimestamp **   <a name="organizations-Type-CreateAccountStatus-CompletedTimestamp"></a>
The date and time that the account was created and the request completed.
Type: Timestamp
Required: No

 ** FailureReason **   <a name="organizations-Type-CreateAccountStatus-FailureReason"></a>
If the request failed, a description of the reason for the failure.
+ ACCOUNT\_LIMIT\_EXCEEDED: The account couldn't be created because you reached the limit on the number of accounts in your organization.
+ CONCURRENT\_ACCOUNT\_MODIFICATION: You already submitted a request with the same information.
+ EMAIL\_ALREADY\_EXISTS: The account could not be created because another AWS account with that email address already exists.
+ FAILED\_BUSINESS\_VALIDATION: The AWS account that owns your organization failed to receive business license validation.
+ GOVCLOUD\_ACCOUNT\_ALREADY\_EXISTS: The account in the AWS GovCloud (US) Region could not be created because this Region already includes an account with that email address.
+ IDENTITY\_INVALID\_BUSINESS\_VALIDATION: The AWS account that owns your organization can't complete business license validation because it doesn't have valid identity data.
+ INVALID\_ADDRESS: The account could not be created because the address you provided is not valid.
+ INVALID\_EMAIL: The account could not be created because the email address you provided is not valid.
+ INVALID\_PAYMENT\_INSTRUMENT: The AWS account that owns your organization does not have a supported payment method associated with the account. AWS does not support cards issued by financial institutions in Russia or Belarus. For more information, see [Managing your AWS payments](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-general.html).
+ INTERNAL\_FAILURE: The account could not be created because of an internal failure. Try again later. If the problem persists, contact AWS Customer Support.
+ MISSING\_BUSINESS\_VALIDATION: The AWS account that owns your organization has not received Business Validation.
+  MISSING\_PAYMENT\_INSTRUMENT: You must configure the management account with a valid payment method, such as a credit card.
+ PENDING\_BUSINESS\_VALIDATION: The AWS account that owns your organization is still in the process of completing business license validation.
+ UNKNOWN\_BUSINESS\_VALIDATION: The AWS account that owns your organization has an unknown issue with business license validation.
Type: String
Valid Values: `ACCOUNT_LIMIT_EXCEEDED | EMAIL_ALREADY_EXISTS | INVALID_ADDRESS | INVALID_EMAIL | CONCURRENT_ACCOUNT_MODIFICATION | INTERNAL_FAILURE | GOVCLOUD_ACCOUNT_ALREADY_EXISTS | MISSING_BUSINESS_VALIDATION | FAILED_BUSINESS_VALIDATION | PENDING_BUSINESS_VALIDATION | INVALID_IDENTITY_FOR_BUSINESS_VALIDATION | UNKNOWN_BUSINESS_VALIDATION | MISSING_PAYMENT_INSTRUMENT | INVALID_PAYMENT_INSTRUMENT | UPDATE_EXISTING_RESOURCE_POLICY_WITH_TAGS_NOT_SUPPORTED`
Required: No

 ** GovCloudAccountId **   <a name="organizations-Type-CreateAccountStatus-GovCloudAccountId"></a>
If the account was created successfully, the ID for the new account in the AWS GovCloud (US) Region.
Type: String
Length Constraints: Maximum length of 12.
Pattern: `^\d{12}$`
Required: No

 ** Id **   <a name="organizations-Type-CreateAccountStatus-Id"></a>
The unique identifier (ID) that references this request. You get this value from the response of the initial [CreateAccount](API_CreateAccount.md) request to create the account.
The [regex pattern](http://wikipedia.org/wiki/regex) for a create account request ID string requires "car-" followed by from 8 to 32 lowercase letters or digits.
Type: String
Length Constraints: Maximum length of 36.
Pattern: `^car-[a-z0-9]{8,32}$`
Required: No

 ** RequestedTimestamp **   <a name="organizations-Type-CreateAccountStatus-RequestedTimestamp"></a>
The date and time that the request was made for the account creation.
Type: Timestamp
Required: No

 ** State **   <a name="organizations-Type-CreateAccountStatus-State"></a>
The status of the asynchronous request to create an AWS account.
Type: String
Valid Values: `IN_PROGRESS | SUCCEEDED | FAILED`
Required: No

## See Also
<a name="API_CreateAccountStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/organizations-2016-11-28/CreateAccountStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/organizations-2016-11-28/CreateAccountStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/organizations-2016-11-28/CreateAccountStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Organizations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query organizations` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
