---
source_url: https://docs.aws.amazon.com/inspector/v1/userguide/inspector_reports.html
---

 End of support notice: On May 20, 2026, AWS will end support for Amazon Inspector Classic. After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. Amazon Inspector Classic no longer available to new accounts and accounts that have not completed an assessment in the last 6 months. For all other accounts, access will remain valid until May 20, 2026, after which you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

# Assessment reports
<a name="inspector_reports"></a>

An Amazon Inspector Classic *assessment report* is a document that details what is tested in the assessment run and the results of the assessment. You can store the reports, share them with your team for remediation actions, or use them to augment your compliance audit data. You can generate a report for an assessment run after the run has successfully completed.

**Note**
 You can generate reports only for assessment runs that occur after April 25, 2017, which is when assessment reports in Amazon Inspector Classic became available.

You can view the following types of assessment reports:
+ **Findings report** – this report contains the following information:
  + Summary of the assessment
  + EC2 instances evaluated during the assessment run
  + Rules packages included in the assessment run
  + Detailed information about each finding, including all EC2 instances that had the finding
+ **Full report** – this report contains all the information that is included in a findings report, and additionally provides the list of rules that were checked against the instances in the assessment target.

**To generate an assessment report**

1. On the **Assessment runs** page, locate the assessment run that you want to generate a report for. Make sure that its status is set to **Analysis complete**.

1. Under the **Reports** column for this assessment run, choose the reports icon.
**Important**
 Starting on March 24, 2025, asssessment reports will no longer include severity information for network reachability findings. This information is available in the Amazon Inspector console.

1. In the **Assessment report** dialog box, choose the type of report that you want to view (either a **Findings** or a **Full** report) and the report format (HTML or PDF). Then choose **Generate report**.

You can also generate assessment reports through the [GetAssessmentReport](http://docs.aws.amazon.com/inspector/latest/APIReference/API_GetAssessmentReport.html) API.

To delete an assessment report, perform the following procedure.

**To delete a report**
+ On the **Assessment runs** page, choose the run that the report that you want to delete is based on, and then choose **Delete**. When prompted for confirmation, choose **Yes**.
**Important**
In Amazon Inspector Classic, you can't delete individual reports. When you delete an assessment run, all versions of the report from that run and all findings are also deleted.

  You can also delete an assessment run by using the [DeleteAssessmentRun](https://docs.aws.amazon.com/inspector/latest/APIReference/API_DeleteAssessmentRun.html) API.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
