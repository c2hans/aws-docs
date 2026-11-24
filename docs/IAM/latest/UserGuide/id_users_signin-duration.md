---
source_url: https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_signin-duration.html
---

# Update the sign-in duration for an IAM user

The **Sign-in duration** setting determines the maximum length of time an IAM user can maintain an authenticated AWS Sign-In session. This limit applies when the IAM user accesses supported AWS services using OAuth. You can configure the duration from a minimum of 1 hour up to a maximum of 90 days.

With extended sign-in sessions, IAM users can maintain authenticated access without frequently signing in or managing long-lived static credentials. Applications continue to use short-lived OAuth access tokens that can be refreshed throughout the session.

You can configure this setting for individual IAM users based on their access requirements.

**Note**
The **Sign-in duration** setting applies to supported OAuth authentication flows, including the AWS CLI and AWS MCP Server. It does not affect AWS Management Console sessions.

## To configure the sign-in duration for an IAM user (console)
<a name="id_users_signin-duration-console"></a>

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Users**.

1. Choose the name of the IAM user to modify.

1. In the **Summary** section, choose **Edit**.

1. For **Sign-in duration**, select a duration. Alternatively, choose **Custom duration** and specify a value up to 90 days.

1. Choose **Save changes**.

The updated duration applies to new sign-in sessions that the IAM user establishes. Existing sessions retain their previously configured expiration time.

For more information about managing and revoking sign-in sessions, see [Sign-in session management](https://docs.aws.amazon.com/signin/latest/userguide/oauth-sign-in-session-management.html) in the AWS Sign-In User Guide.

## To configure the sign-in duration for an IAM user (AWS CLI)
<a name="id_users_signin-duration-cli"></a>

You can configure the maximum sign-in session duration when creating a new IAM user or updating an existing user.

1. To configure the sign-in session duration when creating an IAM user, run the following command with the `--max-signin-session-duration` parameter:

   ```bash
   aws iam create-login-profile --user-name ExampleUser --max-signin-session-duration 7776000
   ```

1. To update the sign-in session duration for an existing IAM user, run the following command:

   ```bash
   aws iam update-login-profile --user-name ExampleUser --max-signin-session-duration 7776000
   ```

You specify the duration in seconds, with a minimum of 3,600 seconds (1 hour) and a maximum of 7,776,000 seconds (90 days).

## To configure the sign-in duration for an IAM user (AWS API)
<a name="id_users_signin-duration-api"></a>

You can configure the maximum sign-in session duration programmatically with the following IAM API operations:
+ To specify the duration when creating an IAM user, call the `CreateLoginProfile` operation with the `MaxSigninSessionDuration` parameter.
+ To modify the duration for an existing IAM user, call the `UpdateLoginProfile` operation with the `MaxSigninSessionDuration` parameter.

For more information, see [Sign-in session management](https://docs.aws.amazon.com/signin/latest/userguide/oauth-sign-in-session-management.html) in the AWS Sign-In User Guide.
