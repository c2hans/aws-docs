---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_budgets_Action.html
---

# Action
<a name="API_budgets_Action"></a>

A budget action resource.

## Contents
<a name="API_budgets_Action_Contents"></a>

 ** ActionId **   <a name="awscostmanagement-Type-budgets_Action-ActionId"></a>
A system-generated universally unique identifier (UUID) for the action.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$`
Required: Yes

 ** ActionThreshold **   <a name="awscostmanagement-Type-budgets_Action-ActionThreshold"></a>
The trigger threshold of the action.
Type: [ActionThreshold](API_budgets_ActionThreshold.md) object
Required: Yes

 ** ActionType **   <a name="awscostmanagement-Type-budgets_Action-ActionType"></a>
The type of action. This defines the type of tasks that can be carried out by this action. This field also determines the format for definition.
Type: String
Valid Values: `APPLY_IAM_POLICY | APPLY_SCP_POLICY | RUN_SSM_DOCUMENTS`
Required: Yes

 ** ApprovalModel **   <a name="awscostmanagement-Type-budgets_Action-ApprovalModel"></a>
This specifies if the action needs manual or automatic approval.
Type: String
Valid Values: `AUTOMATIC | MANUAL`
Required: Yes

 ** BudgetName **   <a name="awscostmanagement-Type-budgets_Action-BudgetName"></a>
 A string that represents the budget name. The ":" and "\\" characters, and the "/action/" substring, aren't allowed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(?![^:\\]*/action/|(?i).*<script>.*</script>.*)[^:\\]+$`
Required: Yes

 ** Definition **   <a name="awscostmanagement-Type-budgets_Action-Definition"></a>
Where you specify all of the type-specific parameters.
Type: [Definition](API_budgets_Definition.md) object
Required: Yes

 ** ExecutionRoleArn **   <a name="awscostmanagement-Type-budgets_Action-ExecutionRoleArn"></a>
The role passed for action execution and reversion. Roles and actions must be in the same account.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 618.
Pattern: `^arn:aws(-eusc|-cn|-us-gov|-iso|-iso-[a-z]{1})?:iam::\d{12}:role(\u002F[\u0021-\u007F]+\u002F|\u002F)[\w+=,.@-]+$`
Required: Yes

 ** NotificationType **   <a name="awscostmanagement-Type-budgets_Action-NotificationType"></a>
 The type of a notification. It must be ACTUAL or FORECASTED.
Type: String
Valid Values: `ACTUAL | FORECASTED`
Required: Yes

 ** Status **   <a name="awscostmanagement-Type-budgets_Action-Status"></a>
The status of the action.
Type: String
Valid Values: `STANDBY | PENDING | EXECUTION_IN_PROGRESS | EXECUTION_SUCCESS | EXECUTION_FAILURE | REVERSE_IN_PROGRESS | REVERSE_SUCCESS | REVERSE_FAILURE | RESET_IN_PROGRESS | RESET_FAILURE`
Required: Yes

 ** Subscribers **   <a name="awscostmanagement-Type-budgets_Action-Subscribers"></a>
 A list of subscribers.
Type: Array of [Subscriber](API_budgets_Subscriber.md) objects
Array Members: Minimum number of 1 item. Maximum number of 11 items.
Required: Yes

## See Also
<a name="API_budgets_Action_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/budgets-2016-10-20/Action)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/budgets-2016-10-20/Action)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/budgets-2016-10-20/Action)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
