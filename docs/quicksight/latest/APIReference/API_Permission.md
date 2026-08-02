---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Permission.html
---

# Permission
<a name="API_Permission"></a>

A structure that contains the permission information for one principal against one flow.

## Contents
<a name="API_Permission_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Actions **   <a name="QS-Type-Permission-Actions"></a>
A list of actions that the principal can perform against the flow.
The following are the list of values to set a principal as a flow owner:
+ quicksight:PublishFlow
+ quicksight:GetFlow
+ quicksight:UpdateFlowPermissions
+ quicksight:GetFlowSession
+ quicksight:StartFlowSession
+ quicksight:StopFlowSession
+ quicksight:UpdateFlowSession
+ quicksight:UnpublishFlow
+ quicksight:GetFlowStages
+ quicksight:DeleteFlow
+ quicksight:DescribeFlowPermissions
+ quicksight:UpdateFlow
+ quicksight:CreatePresignedUrl
The following are the list of values to set a principal as a flow viewer:
+ quicksight:GetFlow
+ quicksight:UpdateFlowSession
+ quicksight:StartFlowSession
+ quicksight:StopFlowSession
+ quicksight:GetFlowSession
+ quicksight:CreatePresignedUrl
+ quicksight:GetFlowStages
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** Principal **   <a name="QS-Type-Permission-Principal"></a>
The Amazon Resource Name (ARN) of the principal. This can be an Amazon Quick user, group or namespace associated with the flow. Namespace principal can only be set as a viewer and will grant everyone in the same namespace viewer permissions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_Permission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/Permission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/Permission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/Permission)
