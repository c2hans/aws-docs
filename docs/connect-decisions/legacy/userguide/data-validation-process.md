---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/data-validation-process.html
---

# Data Validation Process
<a name="data-validation-process"></a>

After the preprocessing process described above completes, the data validation process begins. Data validation consists of three steps:

1. Data Structure Validation[Demand Planning](required_entities.md) - This step includes checks to ensure all required tables and columns exist and have data before any transformation begins. This stage confirms your data tables are properly set up.

1. Data Quality Validation - This step ensures that data content is complete and error-free. It checks for:
   + Missing values in essential fields
   + Validation checks on data formats and validity of dates
   + Data completeness required for building forecast input

   This ensures all necessary data is present and valid before proceeding with transformations.

1. Forecasting Eligibility Validation: This step ensures that sufficient data is provided to create a forecast, including:
   + Minimum historical data requirements
   + Time series length limitations
   + Other algorithm-specific constraints

   This stage ensures that your data is suitable for generating forecasts.

Even a single validation failure will stop the forecast creation process. You must work with your data administrator to correct the underlying data issues, then choose **Retry** to try forecast creation again.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
