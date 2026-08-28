---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_AdminPasswordSourceSummary.html
---

# AdminPasswordSourceSummary
<a name="API_AdminPasswordSourceSummary"></a>

A summary of the admin password source configuration for an Autonomous Database.

## Contents
<a name="API_AdminPasswordSourceSummary_Contents"></a>

 ** adminPasswordSource **   <a name="odb-Type-AdminPasswordSourceSummary-adminPasswordSource"></a>
The source of the admin password for the Autonomous Database.
Type: String
Valid Values: `CUSTOMER_MANAGED_AWS_SECRET | API_REQUEST_PARAMETER`
Required: No

 ** adminPasswordSourceConfiguration **   <a name="odb-Type-AdminPasswordSourceSummary-adminPasswordSourceConfiguration"></a>
The configuration of the admin password source for the Autonomous Database.
Type: [AdminPasswordSourceConfiguration](API_AdminPasswordSourceConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_AdminPasswordSourceSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/AdminPasswordSourceSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/AdminPasswordSourceSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/AdminPasswordSourceSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Oracle Database@AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query odb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
