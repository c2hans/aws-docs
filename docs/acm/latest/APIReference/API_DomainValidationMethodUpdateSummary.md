---
source_url: https://docs.aws.amazon.com/acm/latest/APIReference/API_DomainValidationMethodUpdateSummary.html
---

# DomainValidationMethodUpdateSummary
<a name="API_DomainValidationMethodUpdateSummary"></a>

Contains information about a domain validation method migration, including the previous validation method and the target validation method.

## Contents
<a name="API_DomainValidationMethodUpdateSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** From **   <a name="ACM-Type-DomainValidationMethodUpdateSummary-From"></a>
The validation method that the certificate was using before the update.
Type: String
Valid Values: `EMAIL | DNS | HTTP`
Required: No

 ** To **   <a name="ACM-Type-DomainValidationMethodUpdateSummary-To"></a>
The target validation method for the update.
Type: String
Valid Values: `EMAIL | DNS | HTTP`
Required: No

## See Also
<a name="API_DomainValidationMethodUpdateSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/acm-2015-12-08/DomainValidationMethodUpdateSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/acm-2015-12-08/DomainValidationMethodUpdateSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/acm-2015-12-08/DomainValidationMethodUpdateSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ACM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query acm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
