---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/data-validation-report-access.html
---

# Data Validation Report Access
<a name="data-validation-report-access"></a>

When creating a forecast for the first time, navigate to the **Demand Planning** module in Supply Chain and choose **Create a Plan**. The system guides you through three steps: Data Ingestion, Plan Configuration, and finally, Forecast Generation. After completing data ingestion and plan configuration, choose **Generate Forecast** to initiate data validation. Each new forecast generation creates a fresh validation report based on the current state of your data.

 Data Structure validation failures (such as missing tables or columns) appear as banner messages at the top of your screen. These fundamental issues must be resolved before proceeding. After data structure validation passes, the system proceeds with Data Quality and Forecasting Eligibility validations. Any failures in these stages are detailed in the validation report, accessible by choosing **Data Validations**.

## Subsequent Forecast Creation
<a name="subsequent-forecast"></a>

For subsequent forecasts, choose **Generate Forecast**. You will see a banner displaying three steps, with data validation as the first step. The same validation behavior applies. Structural issues appear as banners, while other validation failures are available in the detailed report.

## Report Content
<a name="report-content"></a>

The Data Validation Issues report provides a comprehensive view of Data Quality and Forecasting Eligibility validation failures that need to be addressed. The report displays the following:
+ Dataset: Identifies the specific dataset where the issue occurs
+ Rule: Describes the type of validation that failed
+ Error Date/Time: Shows when the error was detected
+ Status Message: Provides detailed information about the records affected and recommended actions

To help navigate and resolve these issues, you can do the following:
+ Use the search box to find specific types of errors
+ Filter by dataset using the drop-down menu
+ Download a detailed report containing all validation failures
+ View **Records affected** for each validation to understand the scope of the issue

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
