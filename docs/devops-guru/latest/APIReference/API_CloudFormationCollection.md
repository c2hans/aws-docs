---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_CloudFormationCollection.html
---

# CloudFormationCollection
<a name="API_CloudFormationCollection"></a>

 Information about AWS CloudFormation stacks. You can use up to 1000 stacks to specify which AWS resources in your account to analyze. For more information, see [Stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks.html) in the * AWS CloudFormation User Guide*.

## Contents
<a name="API_CloudFormationCollection_Contents"></a>

 ** StackNames **   <a name="DevOpsGuru-Type-CloudFormationCollection-StackNames"></a>
 An array of CloudFormation stack names.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z*]+[a-zA-Z0-9-]*$`
Required: No

## See Also
<a name="API_CloudFormationCollection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/CloudFormationCollection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/CloudFormationCollection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/CloudFormationCollection)
