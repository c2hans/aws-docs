---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_CoveredResource.html
---

# CoveredResource
<a name="API_CoveredResource"></a>

An object that contains details about a resource covered by Amazon Inspector.

## Contents
<a name="API_CoveredResource_Contents"></a>

 ** accountId **   <a name="inspector2-Type-CoveredResource-accountId"></a>
The AWS account ID of the covered resource.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

 ** resourceId **   <a name="inspector2-Type-CoveredResource-resourceId"></a>
The ID of the covered resource.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1024.
Pattern: `.*(^arn:.*:ecr:.*:\d{12}:repository\/[a-zA-Z0-9._\/-]+(\/sha256:[a-z0-9]{64})?$)|(^i-([a-z0-9]{8}|[a-z0-9]{17}|\\*)$|(^arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_\.]+(:(\$LATEST|[a-zA-Z0-9-_]+))?$)|(^arn:(aws[a-zA-Z-]*)?:inspector2:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:codesecurity-integration\/[a-f0-9-]{36}\/project-[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$))|(^\/subscriptions\/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}\/resourcegroups\/[a-z0-9_\-\.()]+\/providers\/(microsoft\.compute\/virtualmachines\/[a-z0-9_\-]+|microsoft\.web\/sites\/[a-z0-9_\-]+|microsoft\.containerregistry\/registries\/[a-z0-9_\-]+(\/repositories\/[a-z0-9_\-\/]+\/images?\/sha256:[a-f0-9]{64})?)$).*`
Required: Yes

 ** resourceType **   <a name="inspector2-Type-CoveredResource-resourceType"></a>
The type of the covered resource.
Type: String
Valid Values: `AWS_EC2_INSTANCE | AWS_ECR_CONTAINER_IMAGE | AWS_ECR_REPOSITORY | AWS_LAMBDA_FUNCTION | CODE_REPOSITORY | Microsoft.Compute/virtualMachines | Microsoft.ContainerRegistry/registry/containerImage | Microsoft.ContainerRegistry/registry/containerRepository | Microsoft.Web/sites | Microsoft.ContainerRegistry/registries`
Required: Yes

 ** scanType **   <a name="inspector2-Type-CoveredResource-scanType"></a>
The Amazon Inspector scan type covering the resource.
Type: String
Valid Values: `NETWORK | PACKAGE | CODE`
Required: Yes

 ** lastScannedAt **   <a name="inspector2-Type-CoveredResource-lastScannedAt"></a>
The date and time the resource was last checked for vulnerabilities.
Type: Timestamp
Required: No

 ** provider **   <a name="inspector2-Type-CoveredResource-provider"></a>
The cloud provider of the covered resource.
Type: String
Valid Values: `AWS | AZURE`
Required: No

 ** providerAccountId **   <a name="inspector2-Type-CoveredResource-providerAccountId"></a>
The cloud provider account ID of the covered resource.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 36.
Pattern: `(\d{12}|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})`
Required: No

 ** providerOrgId **   <a name="inspector2-Type-CoveredResource-providerOrgId"></a>
The cloud provider organization ID of the covered resource.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 36.
Pattern: `(o-[a-z0-9]{10,32}|[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})`
Required: No

 ** providerPartition **   <a name="inspector2-Type-CoveredResource-providerPartition"></a>
The cloud provider partition of the covered resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(aws(-[a-z]+)*|Azure[A-Za-z]+)`
Required: No

 ** providerRegion **   <a name="inspector2-Type-CoveredResource-providerRegion"></a>
The cloud provider region of the covered resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `([a-z]{2}(-[a-z]+)+-\d+|[a-z][a-z0-9]+)`
Required: No

 ** resourceMetadata **   <a name="inspector2-Type-CoveredResource-resourceMetadata"></a>
An object that contains details about the metadata.
Type: [ResourceScanMetadata](API_ResourceScanMetadata.md) object
Required: No

 ** scanMode **   <a name="inspector2-Type-CoveredResource-scanMode"></a>
The scan method that is applied to the instance.
Type: String
Valid Values: `EC2_SSM_AGENT_BASED | EC2_AGENTLESS | EC2_INSPECTOR_AGENT_BASED | VM_INSPECTOR_AGENT_BASED`
Required: No

 ** scanStatus **   <a name="inspector2-Type-CoveredResource-scanStatus"></a>
The status of the scan covering the resource.
Type: [ScanStatus](API_ScanStatus.md) object
Required: No

## See Also
<a name="API_CoveredResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/CoveredResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/CoveredResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/CoveredResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
