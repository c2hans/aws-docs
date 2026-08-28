---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsServiceServiceRegistriesDetails.html
---

# AwsEcsServiceServiceRegistriesDetails
<a name="API_AwsEcsServiceServiceRegistriesDetails"></a>

Information about a service discovery registry to assign to the service.

## Contents
<a name="API_AwsEcsServiceServiceRegistriesDetails_Contents"></a>

 ** ContainerName **   <a name="securityhub-Type-AwsEcsServiceServiceRegistriesDetails-ContainerName"></a>
The container name value to use for the service discovery service.
If the task definition uses the `bridge` or `host` network mode, you must specify `ContainerName` and `ContainerPort`.
If the task definition uses the `awsvpc` network mode and a type SRV DNS record, you must specify either `ContainerName` and `ContainerPort`, or `Port` , but not both.
Type: String
Pattern: `.*\S.*`
Required: No

 ** ContainerPort **   <a name="securityhub-Type-AwsEcsServiceServiceRegistriesDetails-ContainerPort"></a>
The port value to use for the service discovery service.
If the task definition uses the `bridge` or `host` network mode, you must specify `ContainerName` and `ContainerPort`.
If the task definition uses the `awsvpc` network mode and a type SRV DNS record, you must specify either `ContainerName` and `ContainerPort`, or `Port` , but not both.
Type: Integer
Required: No

 ** Port **   <a name="securityhub-Type-AwsEcsServiceServiceRegistriesDetails-Port"></a>
The port value to use for a service discovery service that specifies an SRV record. This field can be used if both the `awsvpc`awsvpc network mode and SRV records are used.
Type: Integer
Required: No

 ** RegistryArn **   <a name="securityhub-Type-AwsEcsServiceServiceRegistriesDetails-RegistryArn"></a>
The ARN of the service registry.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEcsServiceServiceRegistriesDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsServiceServiceRegistriesDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsServiceServiceRegistriesDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsServiceServiceRegistriesDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
