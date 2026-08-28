---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsOpenSearchServiceDomainServiceSoftwareOptionsDetails.html
---

# AwsOpenSearchServiceDomainServiceSoftwareOptionsDetails
<a name="API_AwsOpenSearchServiceDomainServiceSoftwareOptionsDetails"></a>

Provides information about the state of the domain relative to the latest service software.

## Contents
<a name="API_AwsOpenSearchServiceDomainServiceSoftwareOptionsDetails_Contents"></a>

 ** AutomatedUpdateDate **   <a name="securityhub-Type-AwsOpenSearchServiceDomainServiceSoftwareOptionsDetails-AutomatedUpdateDate"></a>
The epoch time when the deployment window closes for required updates. After this time, OpenSearch Service schedules the software upgrade automatically.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Cancellable **   <a name="securityhub-Type-AwsOpenSearchServiceDomainServiceSoftwareOptionsDetails-Cancellable"></a>
Whether a request to update the domain can be canceled.
Type: Boolean
Required: No

 ** CurrentVersion **   <a name="securityhub-Type-AwsOpenSearchServiceDomainServiceSoftwareOptionsDetails-CurrentVersion"></a>
The version of the service software that is currently installed on the domain.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Description **   <a name="securityhub-Type-AwsOpenSearchServiceDomainServiceSoftwareOptionsDetails-Description"></a>
A more detailed description of the service software status.
Type: String
Pattern: `.*\S.*`
Required: No

 ** NewVersion **   <a name="securityhub-Type-AwsOpenSearchServiceDomainServiceSoftwareOptionsDetails-NewVersion"></a>
The most recent version of the service software.
Type: String
Pattern: `.*\S.*`
Required: No

 ** OptionalDeployment **   <a name="securityhub-Type-AwsOpenSearchServiceDomainServiceSoftwareOptionsDetails-OptionalDeployment"></a>
Whether the service software update is optional.
Type: Boolean
Required: No

 ** UpdateAvailable **   <a name="securityhub-Type-AwsOpenSearchServiceDomainServiceSoftwareOptionsDetails-UpdateAvailable"></a>
Whether a service software update is available for the domain.
Type: Boolean
Required: No

 ** UpdateStatus **   <a name="securityhub-Type-AwsOpenSearchServiceDomainServiceSoftwareOptionsDetails-UpdateStatus"></a>
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
<a name="API_AwsOpenSearchServiceDomainServiceSoftwareOptionsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsOpenSearchServiceDomainServiceSoftwareOptionsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsOpenSearchServiceDomainServiceSoftwareOptionsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsOpenSearchServiceDomainServiceSoftwareOptionsDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
