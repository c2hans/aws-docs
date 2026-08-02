---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_LogicalResourceId.html
---

# LogicalResourceId
<a name="API_LogicalResourceId"></a>

Defines a logical resource identifier.

## Contents
<a name="API_LogicalResourceId_Contents"></a>

 ** identifier **   <a name="resiliencehub-Type-LogicalResourceId-identifier"></a>
Identifier of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** eksSourceName **   <a name="resiliencehub-Type-LogicalResourceId-eksSourceName"></a>
Name of the Amazon Elastic Kubernetes Service cluster and namespace this resource belongs to.
This parameter accepts values in "eks-cluster/namespace" format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** logicalStackName **   <a name="resiliencehub-Type-LogicalResourceId-logicalStackName"></a>
The name of the CloudFormation stack this resource belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** resourceGroupName **   <a name="resiliencehub-Type-LogicalResourceId-resourceGroupName"></a>
The name of the resource group that this resource belongs to.
Type: String
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`
Required: No

 ** terraformSourceName **   <a name="resiliencehub-Type-LogicalResourceId-terraformSourceName"></a>
 The name of the Terraform S3 state file this resource belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_LogicalResourceId_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/LogicalResourceId)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/LogicalResourceId)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/LogicalResourceId)
