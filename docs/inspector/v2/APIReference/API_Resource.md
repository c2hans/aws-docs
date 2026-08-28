---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_Resource.html
---

# Resource
<a name="API_Resource"></a>

Details about the resource involved in a finding.

## Contents
<a name="API_Resource_Contents"></a>

 ** id **   <a name="inspector2-Type-Resource-id"></a>
The ID of the resource.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** type **   <a name="inspector2-Type-Resource-type"></a>
The type of resource.
Type: String
Valid Values: `AWS_EC2_INSTANCE | AWS_ECR_CONTAINER_IMAGE | AWS_ECR_REPOSITORY | AWS_LAMBDA_FUNCTION | CODE_REPOSITORY | Microsoft.Compute/virtualMachines | Microsoft.ContainerRegistry/registry/containerImage | Microsoft.Web/sites`
Required: Yes

 ** details **   <a name="inspector2-Type-Resource-details"></a>
An object that contains details about the resource involved in a finding.
Type: [ResourceDetails](API_ResourceDetails.md) object
Required: No

 ** partition **   <a name="inspector2-Type-Resource-partition"></a>
The partition of the resource.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** provider **   <a name="inspector2-Type-Resource-provider"></a>
The cloud provider of the resource.
Type: String
Valid Values: `AWS | AZURE`
Required: No

 ** providerAccountId **   <a name="inspector2-Type-Resource-providerAccountId"></a>
The cloud provider account ID of the resource.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 36.
Pattern: `(\d{12}|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})`
Required: No

 ** providerOrgId **   <a name="inspector2-Type-Resource-providerOrgId"></a>
The cloud provider organization ID of the resource.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 36.
Pattern: `(o-[a-z0-9]{10,32}|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})`
Required: No

 ** region **   <a name="inspector2-Type-Resource-region"></a>
The AWS Region the impacted resource is located in.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** tags **   <a name="inspector2-Type-Resource-tags"></a>
The tags attached to the resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_Resource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/Resource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/Resource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/Resource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
