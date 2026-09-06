---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_CloudFormationCostEstimationResourceCollectionFilter.html
---

# CloudFormationCostEstimationResourceCollectionFilter
<a name="API_CloudFormationCostEstimationResourceCollectionFilter"></a>

Information about an AWS CloudFormation stack used to create a monthly cost estimate for DevOps Guru to analyze AWS resources. The maximum number of stacks you can specify for a cost estimate is one. The estimate created is for the cost to analyze the AWS resources defined by the stack. For more information, see [Stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks.html) in the * AWS CloudFormation User Guide*.

## Contents
<a name="API_CloudFormationCostEstimationResourceCollectionFilter_Contents"></a>

 ** StackNames **   <a name="DevOpsGuru-Type-CloudFormationCostEstimationResourceCollectionFilter-StackNames"></a>
An array of CloudFormation stack names. Its size is fixed at 1 item.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z*]+[a-zA-Z0-9-]*$`
Required: No

## See Also
<a name="API_CloudFormationCostEstimationResourceCollectionFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/CloudFormationCostEstimationResourceCollectionFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/CloudFormationCostEstimationResourceCollectionFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/CloudFormationCostEstimationResourceCollectionFilter)
