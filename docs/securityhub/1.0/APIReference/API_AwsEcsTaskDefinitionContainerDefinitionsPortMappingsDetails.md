---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetails.html
---

# AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetails
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetails"></a>

A port mapping for the container.

## Contents
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetails_Contents"></a>

 ** ContainerPort **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetails-ContainerPort"></a>
The port number on the container that is bound to the user-specified or automatically assigned host port.
Type: Integer
Required: No

 ** HostPort **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetails-HostPort"></a>
The port number on the container instance to reserve for the container.
Type: Integer
Required: No

 ** Protocol **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetails-Protocol"></a>
The protocol used for the port mapping. The default is `tcp`.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsPortMappingsDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
