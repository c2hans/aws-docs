---
source_url: https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DataLakeAutoEnableNewAccountConfiguration.html
---

# DataLakeAutoEnableNewAccountConfiguration
<a name="API_DataLakeAutoEnableNewAccountConfiguration"></a>

Automatically enable new organization accounts as member accounts from an Amazon Security Lake administrator account.

## Contents
<a name="API_DataLakeAutoEnableNewAccountConfiguration_Contents"></a>

 ** region **   <a name="securitylake-Type-DataLakeAutoEnableNewAccountConfiguration-region"></a>
The AWS Regions where Security Lake is automatically enabled.
Type: String
Pattern: `(us(-gov)?|af|ap|ca|eu|me|sa)-(central|north|(north(?:east|west))|south|south(?:east|west)|east|west)-\d+`
Required: Yes

 ** sources **   <a name="securitylake-Type-DataLakeAutoEnableNewAccountConfiguration-sources"></a>
The AWS sources that are automatically enabled in Security Lake.
Type: Array of [AwsLogSourceResource](API_AwsLogSourceResource.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

## See Also
<a name="API_DataLakeAutoEnableNewAccountConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securitylake-2018-05-10/DataLakeAutoEnableNewAccountConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securitylake-2018-05-10/DataLakeAutoEnableNewAccountConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securitylake-2018-05-10/DataLakeAutoEnableNewAccountConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Security Lake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-lake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
