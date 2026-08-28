---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_JiraCloudDetail.html
---

# JiraCloudDetail
<a name="API_JiraCloudDetail"></a>

Information about the configuration and status of a Jira Cloud integration.

## Contents
<a name="API_JiraCloudDetail_Contents"></a>

 ** AuthStatus **   <a name="securityhub-Type-JiraCloudDetail-AuthStatus"></a>
The status of the authorization between Jira Cloud and the service.
Type: String
Valid Values: `ACTIVE | FAILED`
Required: No

 ** AuthUrl **   <a name="securityhub-Type-JiraCloudDetail-AuthUrl"></a>
The URL to provide to customers for OAuth auth code flow.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CloudId **   <a name="securityhub-Type-JiraCloudDetail-CloudId"></a>
The cloud id of the Jira Cloud.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Domain **   <a name="securityhub-Type-JiraCloudDetail-Domain"></a>
The URL domain of your Jira Cloud instance.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ProjectKey **   <a name="securityhub-Type-JiraCloudDetail-ProjectKey"></a>
The projectKey of Jira Cloud.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_JiraCloudDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/JiraCloudDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/JiraCloudDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/JiraCloudDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
