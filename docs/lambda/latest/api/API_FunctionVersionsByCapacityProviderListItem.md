---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_FunctionVersionsByCapacityProviderListItem.html
---

# FunctionVersionsByCapacityProviderListItem
<a name="API_FunctionVersionsByCapacityProviderListItem"></a>

Information about a function version that uses a specific capacity provider, including its ARN and current state.

## Contents
<a name="API_FunctionVersionsByCapacityProviderListItem_Contents"></a>

 ** FunctionArn **   <a name="lambda-Type-FunctionVersionsByCapacityProviderListItem-FunctionArn"></a>
The Amazon Resource Name (ARN) of the function version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000.
Pattern: `arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_\.]+(:(\$LATEST(\.PUBLISHED)?|[a-zA-Z0-9-_]+))?`
Required: Yes

 ** State **   <a name="lambda-Type-FunctionVersionsByCapacityProviderListItem-State"></a>
The current state of the function version.
Type: String
Valid Values: `Pending | Active | Inactive | Failed | Deactivating | Deactivated | ActiveNonInvocable | Deleting`
Required: Yes

## See Also
<a name="API_FunctionVersionsByCapacityProviderListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/FunctionVersionsByCapacityProviderListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/FunctionVersionsByCapacityProviderListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/FunctionVersionsByCapacityProviderListItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
