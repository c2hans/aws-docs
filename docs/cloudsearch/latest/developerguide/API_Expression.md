---
source_url: https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_Expression.html
---

# Expression
<a name="API_Expression"></a>

## Description
<a name="API_Expression_Description"></a>

A named expression that can be evaluated at search time. Can be used to sort the search results, define other expressions, or return computed information in the search results.

## Contents
<a name="API_Expression_Contents"></a>

 **ExpressionName**
Names must begin with a letter and can contain the following characters: a-z (lowercase), 0-9, and \_ (underscore).
Type: String
 Length constraints: Minimum length of 1. Maximum length of 64.
 Required: Yes

 **ExpressionValue**
The expression to evaluate for sorting while processing a search request. The `Expression` syntax is based on JavaScript expressions. For more information, see [Configuring Expressions](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-expressions.html) in the *Amazon CloudSearch Developer Guide*.
Type: String
 Length constraints: Minimum length of 1. Maximum length of 10240.
 Required: Yes

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cloud Search. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudsearch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
