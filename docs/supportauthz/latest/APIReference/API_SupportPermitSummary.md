---
source_url: https://docs.aws.amazon.com/supportauthz/latest/APIReference/API_SupportPermitSummary.html
---

# SupportPermitSummary
<a name="API_SupportPermitSummary"></a>

A summary of a support permit.

## Contents
<a name="API_SupportPermitSummary_Contents"></a>

 ** arn **   <a name="supportauthorization-Type-SupportPermitSummary-arn"></a>
The ARN of the support permit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:[a-z0-9-]+:[a-z0-9-]+:[a-z0-9-]*:[0-9]{12}:.+`
Required: Yes

 ** createdAt **   <a name="supportauthorization-Type-SupportPermitSummary-createdAt"></a>
The timestamp when the permit was created.
Type: Timestamp
Required: Yes

 ** name **   <a name="supportauthorization-Type-SupportPermitSummary-name"></a>
The name of the support permit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9]{1,256}`
Required: Yes

 ** permit **   <a name="supportauthorization-Type-SupportPermitSummary-permit"></a>
The permit definition.
Type: [Permit](API_Permit.md) object
Required: Yes

 ** signingKeyInfo **   <a name="supportauthorization-Type-SupportPermitSummary-signingKeyInfo"></a>
The signing key information for the permit.
Type: [SigningKeyInfo](API_SigningKeyInfo.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** status **   <a name="supportauthorization-Type-SupportPermitSummary-status"></a>
The current status of the support permit.
Type: String
Valid Values: `ACTIVE | INACTIVE | DELETING`
Required: Yes

 ** supportCaseDisplayId **   <a name="supportauthorization-Type-SupportPermitSummary-supportCaseDisplayId"></a>
The display identifier of the support case associated with the permit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[a-zA-Z0-9:/-]{1,512}`
Required: No

## See Also
<a name="API_SupportPermitSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supportauthz-2026-06-30/SupportPermitSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supportauthz-2026-06-30/SupportPermitSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supportauthz-2026-06-30/SupportPermitSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Support authorization. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query supportauthz` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
