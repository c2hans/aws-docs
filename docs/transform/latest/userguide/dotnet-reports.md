---
source_url: https://docs.aws.amazon.com/transform/latest/userguide/dotnet-reports.html
---

# Transformation Reports
<a name="dotnet-reports"></a>

After your .NET transformation job completes these transformation reports are available:
+ [Transformation Summary Report](#transformation-summary-report)
+ [Transformation Detail Report](#transformation-detail-report)

## Transformation Summary Report
<a name="transformation-summary-report"></a>

After a transformation job completes, a transformation summary report is available in the web console. Download the transformation summary report from the **Dashboard** tab. Select **Download Transformation Summary Report**, and choose **Download as HTML** or **Download as JSON**.

The Transformation Summary Report provides an overview of the transformation and information specific to each repository that was transformed, including:
+ Job Details
  + Transformation job overview
  + Transformation results overview
  + Files overview
+ Repositories list, and for each repository:
  + Repository Name Overview
  + Solution Transformation Summary
  + Project Details, including Status, Type, .NET Version, Total Lines of Code, Transformed Lines of Code, and Files Changed

## Transformation Detail Report
<a name="transformation-detail-report"></a>

After a transformation job finishes, transformation detail reports are available for both web console and IDE users.
+ Web console users: a detail report is available for each transformed repository. On the **Dashboard** tab, use the **Download detailed report** links in the repository list to download a detail report.
+ IDE users: download the transformation report from the **AWS Transform Job Plan** window using the download icon.

The transformation detail report is an interactive HTML report. It contains in-depth information about the transformation, including the reasons for file changes and actionable error details. The information is arranged in the following hierarchy:
+ Job Information
+ For each solution:
  + Solution Transformation Summary
  + Transformation Overview
  + Projects
  + For each project:
    + Project Summary
    + Build Errors Summary
    + NuGet package changes
    + File Changes
    + Build Errors
  + Unit Test Results
  + Linux Readiness Report

For a walk-through of the transformation detail report sections with examples, refer to the blog post [Announcing AWS Transform for .NET detailed transformation reports](https://aws.amazon.com/blogs/dotnet/announcing-aws-transform-for-net-detailed-transformation-reports/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transform. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transform` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
