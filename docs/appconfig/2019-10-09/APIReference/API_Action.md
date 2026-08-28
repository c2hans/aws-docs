---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_Action.html
---

# Action
<a name="API_Action"></a>

An action defines the tasks that the extension performs during the AWS AppConfig workflow. Each action includes an action point, as shown in the following list:
+  `PRE_CREATE_HOSTED_CONFIGURATION_VERSION`
+  `PRE_START_DEPLOYMENT`
+  `AT_DEPLOYMENT_TICK`
+  `ON_DEPLOYMENT_START`
+  `ON_DEPLOYMENT_STEP`
+  `ON_DEPLOYMENT_BAKING`
+  `ON_DEPLOYMENT_COMPLETE`
+  `ON_DEPLOYMENT_ROLLED_BACK`

Each action also includes a name, a URI to an AWS Lambda function, and an Amazon Resource Name (ARN) for an AWS Identity and Access Management assume role. You specify the name, URI, and ARN for each *action point* defined in the extension.

## Contents
<a name="API_Action_Contents"></a>

 ** Description **   <a name="appconfig-Type-Action-Description"></a>
Information about the action.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** Name **   <a name="appconfig-Type-Action-Name"></a>
The action name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** RoleArn **   <a name="appconfig-Type-Action-RoleArn"></a>
An Amazon Resource Name (ARN) for an AWS Identity and Access Management assume role.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:[a-z]+:((eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1})?:(\d{12})?:[a-zA-Z0-9-_/:.]+`
Required: No

 ** Uri **   <a name="appconfig-Type-Action-Uri"></a>
The extension URI associated to the action point in the extension definition. The URI can be an Amazon Resource Name (ARN) for one of the following: an AWS Lambda function, an Amazon Simple Queue Service queue, an Amazon Simple Notification Service topic, or the Amazon EventBridge default event bus.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_Action_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/Action)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/Action)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/Action)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppConfig. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appconfig` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
