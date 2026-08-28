---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_LifeCycleLastTestInitiated.html
---

# LifeCycleLastTestInitiated
<a name="API_LifeCycleLastTestInitiated"></a>

Lifecycle last Test initiated.

## Contents
<a name="API_LifeCycleLastTestInitiated_Contents"></a>

 ** apiCallDateTime **   <a name="mgn-Type-LifeCycleLastTestInitiated-apiCallDateTime"></a>
Lifecycle last Test initiated API call date and time.
Type: String
Length Constraints: Minimum length of 19. Maximum length of 32.
Pattern: `[1-9][0-9]*-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?Z`
Required: No

 ** jobID **   <a name="mgn-Type-LifeCycleLastTestInitiated-jobID"></a>
Lifecycle last Test initiated Job ID.
Type: String
Length Constraints: Fixed length of 24.
Pattern: `mgnjob-[0-9a-zA-Z]{17}`
Required: No

## See Also
<a name="API_LifeCycleLastTestInitiated_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/LifeCycleLastTestInitiated)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/LifeCycleLastTestInitiated)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/LifeCycleLastTestInitiated)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
