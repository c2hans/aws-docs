---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GoogleDriveParameters.html
---

# GoogleDriveParameters
<a name="API_GoogleDriveParameters"></a>

The connection parameters for a Google Drive data source. Provide these parameters in the `DataSourceParameters` object when you create or update a data source that uses Google Drive.

## Contents
<a name="API_GoogleDriveParameters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AuthType **   <a name="QS-Type-GoogleDriveParameters-AuthType"></a>
The authentication type for the Google Drive data source. Valid values include:
+  `SERVICE_ACCOUNT` – Server-to-server authentication using a Google service account key.
+  `THREE_LEGGED_OAUTH` – Interactive OAuth that requires user consent.
Type: String
Valid Values: `THREE_LEGGED_OAUTH | TWO_LEGGED_OAUTH | SERVICE_ACCOUNT`
Required: No

## See Also
<a name="API_GoogleDriveParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/GoogleDriveParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/GoogleDriveParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/GoogleDriveParameters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
