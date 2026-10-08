---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_FindingsOutputSummary.html
---

# FindingsOutputSummary
<a name="API_FindingsOutputSummary"></a>

A summary of the output configuration for a findings export, returned by `ListExportJobsV2`. Unlike the configuration returned by `GetExportJobV2`, it reports only the output format.

## Contents
<a name="API_FindingsOutputSummary_Contents"></a>

 ** Format **   <a name="securityhub-Type-FindingsOutputSummary-Format"></a>
The output format of the export. `CSV` produces comma-separated rows that are suitable for spreadsheets and analysis tools. `OCSF_JSON` produces newline-delimited JSON records in the Open Cybersecurity Schema Framework (OCSF) format used elsewhere in Security Hub.
Type: String
Valid Values: `CSV | OCSF_JSON`
Required: Yes

## See Also
<a name="API_FindingsOutputSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/FindingsOutputSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/FindingsOutputSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/FindingsOutputSummary)
