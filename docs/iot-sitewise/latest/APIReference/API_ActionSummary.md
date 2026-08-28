---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ActionSummary.html
---

# ActionSummary
<a name="API_ActionSummary"></a>

Contains the summary of the actions, including information about where the action resolves to.

## Contents
<a name="API_ActionSummary_Contents"></a>

 ** actionDefinitionId **   <a name="iotsitewise-Type-ActionSummary-actionDefinitionId"></a>
The ID of the action definition.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: No

 ** actionId **   <a name="iotsitewise-Type-ActionSummary-actionId"></a>
The ID of the action.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: No

 ** resolveTo **   <a name="iotsitewise-Type-ActionSummary-resolveTo"></a>
The detailed resource this action resolves to.
Type: [ResolveTo](API_ResolveTo.md) object
Required: No

 ** targetResource **   <a name="iotsitewise-Type-ActionSummary-targetResource"></a>
The resource the action will be taken on.
Type: [TargetResource](API_TargetResource.md) object
Required: No

## See Also
<a name="API_ActionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ActionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ActionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ActionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
