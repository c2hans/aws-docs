---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cognito-identity-provider_example_cognito-identity-provider_ForgotPassword_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ForgotPassword` with an AWS SDK or CLI
<a name="cognito-identity-provider_example_cognito-identity-provider_ForgotPassword_section"></a>

The following code examples show how to use `ForgotPassword`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Automatically migrate known users with a Lambda function](cognito-identity-provider_example_cross_CognitoAutoMigrateUser_section.md)

------
#### [ CLI ]

**AWS CLI**
**To force a password change**
The following `forgot-password` example sends a message to jane@example.com to change their password.

```
aws cognito-idp forgot-password --client-id {{38fjsnc484p94kpqsnet7mpld0}} --username {{jane@example.com}}
```
Output:

```
{
    "CodeDeliveryDetails": {
        "Destination": "j***@e***.com",
        "DeliveryMedium": "EMAIL",
        "AttributeName": "email"
    }
}
```
+  For API details, see [ForgotPassword](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/forgot-password.html) in *AWS CLI Command Reference*.

------
#### [ Go ]

**SDK for Go V2**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/cognito#code-examples).

```
import (
	"context"
	"errors"
	"log"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider"
	"github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider/types"
)

type CognitoActions struct {
	CognitoClient *cognitoidentityprovider.Client
}

// ForgotPassword starts a password recovery flow for a user. This flow typically sends a confirmation code
// to the user's configured notification destination, such as email.
func (actor CognitoActions) ForgotPassword(ctx context.Context, clientId string, userName string) (*types.CodeDeliveryDetailsType, error) {
	output, err := actor.CognitoClient.ForgotPassword(ctx, &cognitoidentityprovider.ForgotPasswordInput{
		ClientId: aws.String(clientId),
		Username: aws.String(userName),
	})
	if err != nil {
		log.Printf("Couldn't start password reset for user '%v'. Here;s why: %v\n", userName, err)
	}
	return output.CodeDeliveryDetails, err
}
```
+  For API details, see [ForgotPassword](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/cognitoidentityprovider#Client.ForgotPassword) in *AWS SDK for Go API Reference*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
