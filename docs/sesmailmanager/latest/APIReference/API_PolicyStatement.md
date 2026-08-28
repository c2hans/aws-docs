---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_PolicyStatement.html
---

# PolicyStatement
<a name="API_PolicyStatement"></a>

The structure containing traffic policy conditions and actions.

## Contents
<a name="API_PolicyStatement_Contents"></a>

 ** Action **   <a name="sesmailmanager-Type-PolicyStatement-Action"></a>
The action that informs a traffic policy resource to either allow or block the email if it matches a condition in the policy statement.
Type: String
Valid Values: `ALLOW | DENY`
Required: Yes

 ** Conditions **   <a name="sesmailmanager-Type-PolicyStatement-Conditions"></a>
The list of conditions to apply to incoming messages for filtering email traffic.
Type: Array of [PolicyCondition](API_PolicyCondition.md) objects
Array Members: Minimum number of 1 item.
Required: Yes

## See Also
<a name="API_PolicyStatement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/PolicyStatement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/PolicyStatement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/PolicyStatement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
