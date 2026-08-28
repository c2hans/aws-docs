---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-invoke-api-integrated-with-cognito-user-pool.html
---

# Call a REST API integrated with an Amazon Cognito user pool
<a name="apigateway-invoke-api-integrated-with-cognito-user-pool"></a>

To call a method with a user pool authorizer configured, the client must do the following:
+ Enable the user to sign up with the user pool.
+ Enable the user to sign in to the user pool.
+ Obtain an [identity or access token](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-tokens-with-identity-providers.html) of the signed-in user from the user pool.
+ Include the token in the `Authorization` header (or another header you specified when you created the authorizer).

You can use [AWS Amplify]() to perform these tasks. See [Integrating Amazon Cognito With Web and Mobile Apps](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-integrate-apps.html) for more information.
+ For Android, see [Getting Started with Amplify for Android](https://docs.amplify.aws/android/build-a-backend/auth/).
+ To use iOS see [Getting started with Amplify for iOS](https://docs.amplify.aws/swift/build-a-backend/auth/).
+ To use JavaScript, see [Getting Started with Amplify for Javascript](https://docs.amplify.aws/javascript/build-a-backend/auth/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon API Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query apigateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
