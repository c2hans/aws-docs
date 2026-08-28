---
source_url: https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_ListDomainNames.html
---

# ListDomainNames
<a name="API_ListDomainNames"></a>

## Description
<a name="API_ListDomainNames_Description"></a>

Lists all search domains owned by an account.

## Response Elements
<a name="API_ListDomainNames_ResponseElements"></a>

 The following element is returned in a structure named `ListDomainNamesResult`.

 **DomainNames**
The names of the search domains owned by an account.
Type: String to String map

## Errors
<a name="API_ListDomainNames_Errors"></a>

 For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 **Base**
An error occurred while processing the request.
 HTTP Status Code: 400

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cloud Search. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudsearch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
