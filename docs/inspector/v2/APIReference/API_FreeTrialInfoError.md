---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_FreeTrialInfoError.html
---

# FreeTrialInfoError
<a name="API_FreeTrialInfoError"></a>

Information about an error received while accessing free trail data for an account.

## Contents
<a name="API_FreeTrialInfoError_Contents"></a>

 ** accountId **   <a name="inspector2-Type-FreeTrialInfoError-accountId"></a>
The account associated with the Amazon Inspector free trial information.
Type: String
Pattern: `.*[0-9]{12}.*`
Required: Yes

 ** code **   <a name="inspector2-Type-FreeTrialInfoError-code"></a>
The error code.
Type: String
Valid Values: `ACCESS_DENIED | INTERNAL_ERROR`
Required: Yes

 ** message **   <a name="inspector2-Type-FreeTrialInfoError-message"></a>
The error message returned.
Type: String
Required: Yes

## See Also
<a name="API_FreeTrialInfoError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/FreeTrialInfoError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/FreeTrialInfoError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/FreeTrialInfoError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
