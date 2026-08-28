---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/view-application-version.html
---

# Viewing all the AWS Resilience Hub application versions
<a name="view-application-version"></a>

To help track the application changes, AWS Resilience Hub displays the previous versions of your application from the time it was created on AWS Resilience Hub.

**To view all the versions of your application**

1.  In the navigation pane, choose **Applications**.

1.  On the **Applications** page, choose the name of the application.

1. Choose the **Application structure** tab.

1. To view all the previous versions of your application, choose the plus sign (**\+**) before **View all versions**. AWS Resilience Hub indicates the draft version and recently released version of your application using **Draft** and **Current release** statuses, respectively. You can choose any version of your application to views its resources, AppComponent, input sources and other associated information.

   In addition, you can also filter the list by using one of the following options:
   + **Filter by version name** – Enter a name to filter the results by the name of your application version.
   + **Filter by a date and time range** – To apply this filter, choose the calendar icon and select one of the following options to filter by the results that matches the time range:
     + **Relative range** – Select one of the available options and choose **Apply**.

       If you choose **Custom range** option, enter a duration in **Enter duration** box and select the appropriate unit of time from **Unit of time** dropdown list, then choose **Apply**.
     + **Relative range** – To specify the date and time range, provide the start time and end time, and then choose **Apply**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
