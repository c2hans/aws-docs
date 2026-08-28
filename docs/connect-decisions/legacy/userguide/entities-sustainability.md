---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/entities-sustainability.html
---

# Sustainability
<a name="entities-sustainability"></a>

The table below list the data entities and columns used by Sustainability for partner invitations and onboarding.

**Note**
**How to read the table:**
**Required** – The column name is mandatory in your dataset and you must populate the column name with values.
**Optional** – The column name is optional. For enhanced feature output, it is recommended to add the column name with values.
**Not required** – Data entity not required.

- ** [trading\_partner](organization-trading-partner-entity.md) **
  - **Column:** id / **Is the column used by Sustainability?:** Required
  - **Column:** tpartner\_type / **Is the column used by Sustainability?:** Required – When you ingest data from SAP or EDI, the default value for string is SCN\_RESERVED\_NO\_VALUE\_PROVIDED. When you upload data using the Amazon S3 connector, you must enter a value or use SCN\_RESERVED\_NO\_VALUE\_PROVIDED for successful ingestion.
  - **Column:** geo\_id / **Is the column used by Sustainability?:** Required – When you ingest data from SAP or EDI, the default value for string is SCN\_RESERVED\_NO\_VALUE\_PROVIDED. When you upload data using the Amazon S3 connector, you must enter a value or use SCN\_RESERVED\_NO\_VALUE\_PROVIDED for successful ingestion.
  - **Column:** eff\_end\_date / **Is the column used by Sustainability?:** Required – You must enter a value for eff\_start\_date and eff\_end\_date. If you don't have a value, enter **1900-01-01 00:00:00** for eff\_start\_date, and **9999-12-31 23:59:59** for eff\_end\_date.
  - **Column:** eff\_start\_date / **Is the column used by Sustainability?:** Required – You must enter a value for eff\_start\_date and eff\_end\_date. If you don't have a value, enter **1900-01-01 00:00:00** for eff\_start\_date, and **9999-12-31 23:59:59** for eff\_end\_date.

- ** [trading\_partner\_poc](organization-trading-partner-poc-entity.md) **
  - **Column:** tpartner\_id / **Is the column used by Sustainability?:** Required
  - **Column:** email / **Is the column used by Sustainability?:** Required

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Decisions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect-decisions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
