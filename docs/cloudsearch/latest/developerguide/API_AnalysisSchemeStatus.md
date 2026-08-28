---
source_url: https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_AnalysisSchemeStatus.html
---

# AnalysisSchemeStatus
<a name="API_AnalysisSchemeStatus"></a>

## Description
<a name="API_AnalysisSchemeStatus_Description"></a>

The status and configuration of an `AnalysisScheme`.

## Contents
<a name="API_AnalysisSchemeStatus_Contents"></a>

 **Options**
Configuration information for an analysis scheme. Each analysis scheme has a unique name and specifies the language of the text to be processed. The following options can be configured for an analysis scheme: `Synonyms`, `Stopwords`, `StemmingDictionary`, `JapaneseTokenizationDictionary` and `AlgorithmicStemming`.
Type: [AnalysisScheme](API_AnalysisScheme.md)
 Required: Yes

 **Status**
The status of domain configuration option.
Type: [OptionStatus](API_OptionStatus.md)
 Required: Yes

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cloud Search. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudsearch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
