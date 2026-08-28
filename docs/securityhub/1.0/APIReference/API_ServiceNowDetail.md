---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ServiceNowDetail.html
---

# ServiceNowDetail
<a name="API_ServiceNowDetail"></a>

Information about a ServiceNow ITSM integration.

## Contents
<a name="API_ServiceNowDetail_Contents"></a>

 ** AuthStatus **   <a name="securityhub-Type-ServiceNowDetail-AuthStatus"></a>
The status of the authorization between ServiceNow and the service.
Type: String
Valid Values: `ACTIVE | FAILED`
Required: Yes

 ** SecretArn **   <a name="securityhub-Type-ServiceNowDetail-SecretArn"></a>
The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that contains the ServiceNow credentials.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** InstanceName **   <a name="securityhub-Type-ServiceNowDetail-InstanceName"></a>
The instanceName of ServiceNow ITSM.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_ServiceNowDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ServiceNowDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ServiceNowDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ServiceNowDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
