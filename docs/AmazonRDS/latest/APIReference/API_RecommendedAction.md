---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RecommendedAction.html
---

# RecommendedAction
<a name="API_RecommendedAction"></a>

The recommended actions to apply to resolve the issues associated with your DB instances, DB clusters, and DB parameter groups.

## Contents
<a name="API_RecommendedAction_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ActionId **
The unique identifier of the recommended action.
Type: String
Required: No

 ** ApplyModes.member.N **
The methods to apply the recommended action.
Valid values:
+  `manual` - The action requires you to resolve the recommendation manually.
+  `immediately` - The action is applied immediately.
+  `next-maintainance-window` - The action is applied during the next scheduled maintainance.
Type: Array of strings
Required: No

 ** ContextAttributes.member.N **
The supporting attributes to explain the recommended action.
Type: Array of [ContextAttribute](API_ContextAttribute.md) objects
Required: No

 ** Description **
A detailed description of the action. The description might contain markdown.
Type: String
Required: No

 ** IssueDetails **
The details of the issue.
Type: [IssueDetails](API_IssueDetails.md) object
Required: No

 ** Operation **
An API operation for the action.
Type: String
Required: No

 ** Parameters.member.N **
The parameters for the API operation.
Type: Array of [RecommendedActionParameter](API_RecommendedActionParameter.md) objects
Required: No

 ** Status **
The status of the action.
+  `ready`
+  `applied`
+  `scheduled`
+  `resolved`
Type: String
Required: No

 ** Title **
A short description to summarize the action. The description might contain markdown.
Type: String
Required: No

## See Also
<a name="API_RecommendedAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/RecommendedAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/RecommendedAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/RecommendedAction)
