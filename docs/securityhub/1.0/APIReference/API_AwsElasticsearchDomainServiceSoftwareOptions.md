---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsElasticsearchDomainServiceSoftwareOptions.html
---

# AwsElasticsearchDomainServiceSoftwareOptions
<a name="API_AwsElasticsearchDomainServiceSoftwareOptions"></a>

Information about the state of the domain relative to the latest service software.

## Contents
<a name="API_AwsElasticsearchDomainServiceSoftwareOptions_Contents"></a>

 ** AutomatedUpdateDate **   <a name="securityhub-Type-AwsElasticsearchDomainServiceSoftwareOptions-AutomatedUpdateDate"></a>
The epoch time when the deployment window closes for required updates. After this time, Amazon OpenSearch Service schedules the software upgrade automatically.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Cancellable **   <a name="securityhub-Type-AwsElasticsearchDomainServiceSoftwareOptions-Cancellable"></a>
Whether a request to update the domain can be canceled.
Type: Boolean
Required: No

 ** CurrentVersion **   <a name="securityhub-Type-AwsElasticsearchDomainServiceSoftwareOptions-CurrentVersion"></a>
The version of the service software that is currently installed on the domain.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Description **   <a name="securityhub-Type-AwsElasticsearchDomainServiceSoftwareOptions-Description"></a>
A more detailed description of the service software status.
Type: String
Pattern: `.*\S.*`
Required: No

 ** NewVersion **   <a name="securityhub-Type-AwsElasticsearchDomainServiceSoftwareOptions-NewVersion"></a>
The most recent version of the service software.
Type: String
Pattern: `.*\S.*`
Required: No

 ** UpdateAvailable **   <a name="securityhub-Type-AwsElasticsearchDomainServiceSoftwareOptions-UpdateAvailable"></a>
Whether a service software update is available for the domain.
Type: Boolean
Required: No

 ** UpdateStatus **   <a name="securityhub-Type-AwsElasticsearchDomainServiceSoftwareOptions-UpdateStatus"></a>
The status of the service software update. Valid values are as follows:
+  `COMPLETED`
+  `ELIGIBLE`
+  `IN_PROGRESS`
+  `NOT_ELIGIBLE`
+  `PENDING_UPDATE`
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsElasticsearchDomainServiceSoftwareOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsElasticsearchDomainServiceSoftwareOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsElasticsearchDomainServiceSoftwareOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsElasticsearchDomainServiceSoftwareOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
