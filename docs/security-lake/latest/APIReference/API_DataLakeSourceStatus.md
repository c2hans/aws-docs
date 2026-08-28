---
source_url: https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DataLakeSourceStatus.html
---

# DataLakeSourceStatus
<a name="API_DataLakeSourceStatus"></a>

Retrieves the Logs status for the Amazon Security Lake account.

## Contents
<a name="API_DataLakeSourceStatus_Contents"></a>

 ** resource **   <a name="securitylake-Type-DataLakeSourceStatus-resource"></a>
Defines path the stored logs are available which has information on your systems, applications, and services.
Type: String
Required: No

 ** status **   <a name="securitylake-Type-DataLakeSourceStatus-status"></a>
The health status of services, including error codes and patterns.
Type: String
Valid Values: `COLLECTING | MISCONFIGURED | NOT_COLLECTING`
Required: No

## See Also
<a name="API_DataLakeSourceStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securitylake-2018-05-10/DataLakeSourceStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securitylake-2018-05-10/DataLakeSourceStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securitylake-2018-05-10/DataLakeSourceStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Security Lake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-lake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
