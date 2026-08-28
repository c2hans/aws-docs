---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DataClassificationDetails.html
---

# DataClassificationDetails
<a name="API_DataClassificationDetails"></a>

Provides details about sensitive data that was detected on a resource.

## Contents
<a name="API_DataClassificationDetails_Contents"></a>

 ** DetailedResultsLocation **   <a name="securityhub-Type-DataClassificationDetails-DetailedResultsLocation"></a>
The path to the folder or file that contains the sensitive data.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Result **   <a name="securityhub-Type-DataClassificationDetails-Result"></a>
The details about the sensitive data that was detected on the resource.
Type: [ClassificationResult](API_ClassificationResult.md) object
Required: No

## See Also
<a name="API_DataClassificationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/DataClassificationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/DataClassificationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/DataClassificationDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
