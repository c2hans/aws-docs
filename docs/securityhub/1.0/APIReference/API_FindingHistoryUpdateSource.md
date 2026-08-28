---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_FindingHistoryUpdateSource.html
---

# FindingHistoryUpdateSource
<a name="API_FindingHistoryUpdateSource"></a>

 Identifies the source of the finding change event.

## Contents
<a name="API_FindingHistoryUpdateSource_Contents"></a>

 ** Identity **   <a name="securityhub-Type-FindingHistoryUpdateSource-Identity"></a>
 The identity of the source that initiated the finding change event. For example, the Amazon Resource Name (ARN) of a partner that calls BatchImportFindings or of a customer that calls BatchUpdateFindings.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Type **   <a name="securityhub-Type-FindingHistoryUpdateSource-Type"></a>
 Describes the type of finding change event, such as a call to [`BatchImportFindings`](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchImportFindings.html) (by an integrated AWS service or third party partner integration) or [`BatchUpdateFindings`](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateFindings.html) (by a Security Hub CSPM customer).
Type: String
Valid Values: `BATCH_UPDATE_FINDINGS | BATCH_IMPORT_FINDINGS`
Required: No

## See Also
<a name="API_FindingHistoryUpdateSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/FindingHistoryUpdateSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/FindingHistoryUpdateSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/FindingHistoryUpdateSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
