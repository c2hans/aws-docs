---
source_url: https://docs.aws.amazon.com/cur/latest/userguide/view-latest-cur.html
---

# Viewing the latest report version
<a name="view-latest-cur"></a>

AWS updates your Cost and Usage Report at least once a day until your charges are finalized. When you create a report, you can choose to create new report versions or overwrite the existing report version with every update.

If you configured your report to create new report versions with every update, then use the **assemblyId** in the manifest file to find the latest report files.

**To view your latest report files when you have multiple report versions**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, under **Legacy Pages**, choose **Cost and Usage Reports**.

1. From your list of reports, choose the name of the report that you want to view.

1. On the **Report Details** page, note the **Report path prefix**.

1. Choose the bucket name listed under Amazon S3 bucket. The link opens this bucket in the Amazon S3 console.

1. From the list of objects in the bucket, choose the folder named with the first part of the **Report path prefix** that you noted in step 4. For example, if your **Report path prefix** is **example-report-prefix/example-report-name**, then choose the folder named **example-report-prefix**.

1. From the list of objects in the folder, choose the folder named with the second part of the **Report path prefix** that you noted in step 4. For example, if your **Report path prefix** is **example-report-prefix/example-report-name**, then choose the folder named **example-report-name**.

1. Open the folder named with the latest billing period (in the YYYYMMDD-YYYYMMDD format).

1. Open the ****example-report-name**-Manifest.json** file.

1. In the manifest file, note the **assemblyId**. The **assemblyId** value corresponds to the name of the folder with the latest report files.

1. Return to the Amazon S3 console page where you’re viewing the folder named with the latest billing period.

1. Open the folder named with the **assemblyId** value that you noted in step 10. For example, if the **assemblyId** value is **20210129T123456Z**, then open the folder named **20210129T123456Z/**. This folder contains your latest report files.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cur` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
