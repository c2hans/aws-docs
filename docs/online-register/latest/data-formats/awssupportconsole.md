---
source_url: https://docs.aws.amazon.com/online-register/latest/data-formats/awssupportconsole.html
---

# Data retrieval APIs for AWS Support Console
<a name="awssupportconsole"></a>

AWS Support Console provides the following APIs for data retrieval.

| Actions | Description | Access level |
| --- | --- | --- |
| <a name="support-console-CheckSubscription"></a>[CheckSubscription](${AuthZDocPage}) | Check whether the account has access to given product | Read |
| <a name="support-console-DescribeDynamicHelp"></a>[DescribeDynamicHelp](${AuthZDocPage}) | Get dynamic help resources for given service and category | Read |
| <a name="support-console-GetAccountGovCloudEnabled"></a>[GetAccountGovCloudEnabled](${AuthZDocPage}) | Determines whether the calling account is GovCloud enabled | Read |
| <a name="support-console-GetAccountState"></a>[GetAccountState](${AuthZDocPage}) | Get the state of the calling account | Read |
| <a name="support-console-GetBanner"></a>[GetBanner](${AuthZDocPage}) | Get the support banner information | Read |
| <a name="support-console-GetCaseDraft"></a>[GetCaseDraft](${AuthZDocPage}) | Get a case draft for given case type | Read |
| <a name="support-console-GetIssueClassificationPredictions"></a>[GetIssueClassificationPredictions](${AuthZDocPage}) | Get classification predictions of an issue | Read |
| <a name="support-console-GetIssueTextSummary"></a>[GetIssueTextSummary](${AuthZDocPage}) | Get a generated text summary of an issue | Read |
| <a name="support-console-GetQuestionnaire"></a>[GetQuestionnaire](${AuthZDocPage}) | Get a feedback questionnaire | Read |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for none. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query online-register` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
