---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_AccountPoolSummary.html
---

# AccountPoolSummary
<a name="API_AccountPoolSummary"></a>

The summary of the account pool.

## Contents
<a name="API_AccountPoolSummary_Contents"></a>

 ** createdBy **   <a name="datazone-Type-AccountPoolSummary-createdBy"></a>
The user who created the account pool.
Type: String
Required: No

 ** domainId **   <a name="datazone-Type-AccountPoolSummary-domainId"></a>
The ID of the domain.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: No

 ** domainUnitId **   <a name="datazone-Type-AccountPoolSummary-domainUnitId"></a>
The ID of the domain unit.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-z0-9_\-]+`
Required: No

 ** id **   <a name="datazone-Type-AccountPoolSummary-id"></a>
The ID of the account pool.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** name **   <a name="datazone-Type-AccountPoolSummary-name"></a>
The name of the account pool.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`
Required: No

 ** resolutionStrategy **   <a name="datazone-Type-AccountPoolSummary-resolutionStrategy"></a>
The mechanism used to resolve the account selection from the account pool.
Type: String
Valid Values: `MANUAL`
Required: No

 ** updatedBy **   <a name="datazone-Type-AccountPoolSummary-updatedBy"></a>
The user who updated the account pool.
Type: String
Required: No

## See Also
<a name="API_AccountPoolSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/AccountPoolSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/AccountPoolSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/AccountPoolSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
