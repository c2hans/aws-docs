---
source_url: https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_Suggester.html
---

# Suggester
<a name="API_Suggester"></a>

## Description
<a name="API_Suggester_Description"></a>

Configuration information for a search suggester. Each suggester has a unique name and specifies the text field you want to use for suggestions. The following options can be configured for a suggester: `FuzzyMatching`, `SortExpression`.

## Contents
<a name="API_Suggester_Contents"></a>

 **DocumentSuggesterOptions**
Options for a search suggester.
Type: [DocumentSuggesterOptions](API_DocumentSuggesterOptions.md)
 Required: Yes

 **SuggesterName**
Names must begin with a letter and can contain the following characters: a-z (lowercase), 0-9, and \_ (underscore).
Type: String
 Length constraints: Minimum length of 1. Maximum length of 64.
 Required: Yes

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cloud Search. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudsearch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
