---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SharePointParameters.html
---

# SharePointParameters
<a name="API_SharePointParameters"></a>

The connection parameters for a SharePoint data source. Provide these parameters in the `DataSourceParameters` object when you create or update a data source that uses SharePoint.

## Contents
<a name="API_SharePointParameters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** SharePointDomain **   <a name="QS-Type-SharePointParameters-SharePointDomain"></a>
The SharePoint domain for the data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** AuthType **   <a name="QS-Type-SharePointParameters-AuthType"></a>
The authentication type for the SharePoint data source. Valid values include:
+  `TWO_LEGGED_OAUTH` – Server-to-server authentication using client credentials that do not require user interaction.
+  `THREE_LEGGED_OAUTH` – Interactive OAuth that requires user consent.
Type: String
Valid Values: `THREE_LEGGED_OAUTH | TWO_LEGGED_OAUTH | SERVICE_ACCOUNT`
Required: No

 ** ClientId **   <a name="QS-Type-SharePointParameters-ClientId"></a>
The client ID for the SharePoint data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** TenantId **   <a name="QS-Type-SharePointParameters-TenantId"></a>
The tenant ID for the SharePoint data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## See Also
<a name="API_SharePointParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SharePointParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SharePointParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SharePointParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
