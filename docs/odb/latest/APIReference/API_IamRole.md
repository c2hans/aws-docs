---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_IamRole.html
---

# IamRole
<a name="API_IamRole"></a>

Information about an AWS Identity and Access Management (IAM) service role associated with a resource.

## Contents
<a name="API_IamRole_Contents"></a>

 ** awsIntegration **   <a name="odb-Type-IamRole-awsIntegration"></a>
The AWS integration configuration settings for the AWS Identity and Access Management (IAM) service role.
Type: String
Valid Values: `KmsTde`
Required: No

 ** iamRoleArn **   <a name="odb-Type-IamRole-iamRoleArn"></a>
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) service role.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):iam::[0-9]{12}:role/.+`
Required: No

 ** status **   <a name="odb-Type-IamRole-status"></a>
The current status of the AWS Identity and Access Management (IAM) service role.
Type: String
Valid Values: `ASSOCIATING | DISASSOCIATING | FAILED | CONNECTED | DISCONNECTED | PARTIALLY_CONNECTED | UNKNOWN`
Required: No

 ** statusReason **   <a name="odb-Type-IamRole-statusReason"></a>
Additional information about the current status of the AWS Identity and Access Management (IAM) service role, if applicable.
Type: String
Required: No

## See Also
<a name="API_IamRole_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/IamRole)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/IamRole)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/IamRole)
