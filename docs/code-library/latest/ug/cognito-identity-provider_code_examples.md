---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cognito-identity-provider_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Code examples for Amazon Cognito Identity Provider using AWS SDKs
<a name="cognito-identity-provider_code_examples"></a>

The following code examples show you how to use Amazon Cognito Identity Provider with an AWS software development kit (SDK).

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

**More resources**
+  **[ Amazon Cognito Identity Provider Developer Guide](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html)** – More information about Amazon Cognito Identity Provider.
+ **[Amazon Cognito Identity Provider API Reference](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/Welcome.html)** – Details about all available Amazon Cognito Identity Provider actions.
+ **[AWS Developer Center](https://aws.amazon.com/developer/code-examples/?awsf.sdk-code-examples-product=product%23cognito)** – Code examples that you can filter by category or full-text search.
+ **[AWS SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples)** – GitHub repo with complete code in preferred languages. Includes instructions for setting up and running the code.

**Contents**
+ [Basics](cognito-identity-provider_code_examples_basics.md)
  + [Hello Amazon Cognito](cognito-identity-provider_example_cognito-identity-provider_Hello_section.md)
  + [Actions](cognito-identity-provider_code_examples_actions.md)
    + [`AdminCreateUser`](cognito-identity-provider_example_cognito-identity-provider_AdminCreateUser_section.md)
    + [`AdminGetUser`](cognito-identity-provider_example_cognito-identity-provider_AdminGetUser_section.md)
    + [`AdminInitiateAuth`](cognito-identity-provider_example_cognito-identity-provider_AdminInitiateAuth_section.md)
    + [`AdminRespondToAuthChallenge`](cognito-identity-provider_example_cognito-identity-provider_AdminRespondToAuthChallenge_section.md)
    + [`AdminSetUserPassword`](cognito-identity-provider_example_cognito-identity-provider_AdminSetUserPassword_section.md)
    + [`AssociateSoftwareToken`](cognito-identity-provider_example_cognito-identity-provider_AssociateSoftwareToken_section.md)
    + [`ConfirmDevice`](cognito-identity-provider_example_cognito-identity-provider_ConfirmDevice_section.md)
    + [`ConfirmForgotPassword`](cognito-identity-provider_example_cognito-identity-provider_ConfirmForgotPassword_section.md)
    + [`ConfirmSignUp`](cognito-identity-provider_example_cognito-identity-provider_ConfirmSignUp_section.md)
    + [`CreateUserPool`](cognito-identity-provider_example_cognito-identity-provider_CreateUserPool_section.md)
    + [`CreateUserPoolClient`](cognito-identity-provider_example_cognito-identity-provider_CreateUserPoolClient_section.md)
    + [`DeleteUser`](cognito-identity-provider_example_cognito-identity-provider_DeleteUser_section.md)
    + [`ForgotPassword`](cognito-identity-provider_example_cognito-identity-provider_ForgotPassword_section.md)
    + [`InitiateAuth`](cognito-identity-provider_example_cognito-identity-provider_InitiateAuth_section.md)
    + [`ListUserPools`](cognito-identity-provider_example_cognito-identity-provider_ListUserPools_section.md)
    + [`ListUsers`](cognito-identity-provider_example_cognito-identity-provider_ListUsers_section.md)
    + [`ResendConfirmationCode`](cognito-identity-provider_example_cognito-identity-provider_ResendConfirmationCode_section.md)
    + [`RespondToAuthChallenge`](cognito-identity-provider_example_cognito-identity-provider_RespondToAuthChallenge_section.md)
    + [`SignUp`](cognito-identity-provider_example_cognito-identity-provider_SignUp_section.md)
    + [`UpdateUserPool`](cognito-identity-provider_example_cognito-identity-provider_UpdateUserPool_section.md)
    + [`VerifySoftwareToken`](cognito-identity-provider_example_cognito-identity-provider_VerifySoftwareToken_section.md)
+ [Scenarios](cognito-identity-provider_code_examples_scenarios.md)
  + [Automatically confirm known users with a Lambda function](cognito-identity-provider_example_cross_CognitoAutoConfirmUser_section.md)
  + [Automatically migrate known users with a Lambda function](cognito-identity-provider_example_cross_CognitoAutoMigrateUser_section.md)
  + [Getting started with user pools](cognito-identity-provider_example_cognito_identity_provider_GettingStarted_066_section.md)
  + [Sign up a user with a user pool that requires MFA](cognito-identity-provider_example_cognito-identity-provider_Scenario_SignUpUserWithMfa_section.md)
  + [Use Amazon Cognito identity pools](cognito-identity-provider_example_cross_CognitoFlows_section.md)
  + [Write custom activity data with a Lambda function after Amazon Cognito user authentication](cognito-identity-provider_example_cross_CognitoCustomActivityLog_section.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
