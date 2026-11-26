---
source_url: https://docs.aws.amazon.com/signin/latest/userguide/oauth-sign-in-session-management.html
---

# Sign-in session management

Sign-in sessions enable developers and applications to maintain authenticated access to supported AWS services without frequently signing in or managing long-lived static credentials. Administrators can configure sign-in sessions lasting up to 90 days for individual IAM roles and users, providing flexibility to support long-running workflows while maintaining control over authentication.

A sign-in session represents an authenticated relationship between a user and AWS Sign-In. Each session has a unique identifier, creation time, and expiration time. During an active session, applications use short-lived OAuth access tokens to access supported AWS services. These tokens can be renewed using refresh tokens without requiring the user to authenticate again.

Sign-in sessions provide the following benefits:
+ **Extended authentication**: Maintain authenticated access for up to 90 days without repeated sign-ins.
+ **Improved security**: Use short-lived access tokens instead of long-lived static credentials.
+ **Granular configuration**: Configure session durations for individual IAM users and roles.
+ **Session management**: View, monitor, and revoke active sessions when needed.

AWS Sign-In supports sign-in sessions for the AWS CLI, agentic tools, and other OAuth-enabled applications.

**Note**
Extended sign-in sessions are not supported for AWS Management Console sessions. Console sessions continue to follow their existing session duration settings.

## Configure sign-in duration
<a name="oauth-sign-in-session-configure-duration"></a>

When a user authenticates through AWS Sign-In using OAuth, AWS establishes a sign-in session that represents the user's authenticated access and enables applications to obtain short-lived credentials without requiring repeated sign-ins. Sign-in duration is a configurable AWS Identity and Access Management (IAM) setting that determines how long this session can remain active.

Administrators can configure the maximum sign-in session duration for individual IAM roles and users. The default session duration is 12 hours, and the maximum configurable duration is 90 days.

Configuring durations at the principal level allows organizations to provide longer sessions to users and roles that require extended access, while maintaining shorter sessions for other workloads.

### Configure sign-in duration for an IAM role
<a name="oauth-sign-in-session-configure-duration-role"></a>

1. Sign in to the AWS Management Console and open the IAM console.

1. In the navigation pane, choose **Roles**.

1. Select the IAM role you want to configure.

1. Navigate to the role's sign-in session duration setting.

1. Choose **Edit** and specify the maximum duration, up to 90 days.

1. Choose **Save changes**.

The configured duration applies to new sign-in sessions established using the role. For more information about configuring role settings, see [Updating role settings](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_update-role-settings.html) in the *AWS Identity and Access Management User Guide*.

### Configure sign-in duration for an IAM user
<a name="oauth-sign-in-session-configure-duration-user"></a>

1. Open the IAM console.

1. In the navigation pane, choose **Users**.

1. Select the IAM user you want to configure.

1. Navigate to the user's sign-in session duration setting.

1. Choose **Edit** and specify the maximum duration, up to 90 days.

1. Choose **Save changes**.

The configured duration applies to new sign-in sessions established using the IAM user. For more information about IAM users, see [IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html) in the *AWS Identity and Access Management User Guide*.

**Note**
For supported CLI and OAuth authentication flows, sign-in session duration takes precedence over the existing IAM role Maximum Session Duration setting. The role's Maximum Session Duration continues to govern the lifetime of individual temporary AWS Security Token Service (AWS STS) credentials.

## Use sign-in sessions with the AWS CLI, agentic tools, and other OAuth applications
<a name="oauth-sign-in-session-using-cli"></a>

AWS CLI supports sign-in sessions through the `aws login` command. After an administrator configures the session duration for an IAM role or user, you can authenticate once, and then continue using the AWS CLI for the configured duration without repeatedly signing in.

The following AWS CLI command establishes a session:

```bash
aws login
```

After successful authentication, AWS Sign-In establishes a session associated with the authenticated principal. The AWS CLI obtains temporary credentials for accessing AWS services and automatically renews credentials as needed while the session remains active.

When the sign-in session expires or is revoked, the user must authenticate again to establish a new session.

**Note**
For enhanced security when using extended sign-in sessions with the AWS CLI, use the credential daemon to securely manage refresh tokens. The credential daemon stores refresh tokens encrypted at rest and prevents direct access by the AWS CLI and SDKs, which receive only short-lived credentials that are automatically renewed during the session. This reduces the risk of credential exposure while supporting extended authentication sessions.
For more information about configuring and using the credential daemon, see [Configure the credential daemon](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-credsd-install.html).

## Manage active sign-in sessions
<a name="oauth-sign-in-session-manage"></a>

AWS Sign-In provides APIs to programmatically view and manage active sign-in sessions using the AWS CLI and SDKs. With these APIs, you can list existing sessions, retrieve detailed information about individual sessions, and revoke sessions when access is no longer required.

Access to session management operations is controlled through AWS Identity and Access Management (IAM) permissions. Administrators with the appropriate permissions can view and manage sessions across IAM users and roles within their account, while individual users can view and manage only their own sessions. This enables organizations to maintain centralized administrative oversight while allowing users to manage their own authenticated sessions.

### List active sessions
<a name="oauth-sign-in-session-list"></a>

You can retrieve sign-in sessions associated with an IAM user or role to review existing authenticated sessions.

The following AWS CLI command lists the sessions associated with an IAM role:

```bash
aws signin list-sessions \
  --principal-arn arn:aws:iam::{{123456789012}}:role/{{DeveloperRole}}
```

This operation provides visibility into sessions associated with the specified principal, including session identifiers, expiration times, and session status.

### Get session details
<a name="oauth-sign-in-session-get"></a>

You can retrieve detailed information about a specific sign-in session using its session ARN. The following AWS CLI command gets the details for a session:

```bash
aws signin get-session \
  --session-arn arn:aws:signin:us-east-1:{{123456789012}}:session/{{my-session-id}}
```

Session details help administrators identify the associated principal, review session activity and expiration, and determine whether a session requires revocation.

### Revoke sessions
<a name="oauth-sign-in-session-revoke"></a>

Administrators can revoke sign-in sessions when access is no longer required or when suspicious activity is identified.

You can revoke a specific session or multiple sessions in a single request.

The following AWS CLI command revokes a session:

```bash
aws signin batch-revoke-sessions \
  --session-arns arn:aws:signin:us-east-1:{{123456789012}}:session/{{my-session-id}}
```

When a session is revoked, AWS Sign-In prevents further renewal of access tokens associated with that session after revocation takes effect. Already-issued access tokens can remain valid until they expire.

**Note**
Session revocation can take up to one hour to take effect. Revoking a session affects only the targeted session and does not automatically revoke other sessions associated with the same IAM user or role.

## Monitor sign-in sessions using AWS CloudTrail
<a name="oauth-sign-in-session-monitor-cloudtrail"></a>

AWS Sign-In integrates with AWS CloudTrail to provide visibility into authentication and session management activities.

CloudTrail records OAuth authorization and token lifecycle activities, helping administrators monitor how applications access AWS services and investigate security events.

You can use CloudTrail to review the following activities:
+ **Session creation**: Identify when authentication sessions are established.
+ **Token activity**: Monitor OAuth token issuance and renewal activity.
+ **Session management**: Audit operations that list, retrieve, or revoke sign-in sessions.
+ **Administrative changes**: Review supported changes to session duration configurations.

CloudTrail records include relevant information about the calling principal, event time, API operation, and associated request details, where available.

Administrators can use these records to investigate access activity, monitor session usage, and support security and compliance requirements.

The following example shows a AWS CloudTrail event recorded when AWS Sign-In creates an OAuth token for a sign-in session:

```json
{
   "eventVersion":"1.11",
   "userIdentity":{
      "type":"AssumedRole",
      "principalId":"AROA123456789EXAMPLE:example-session",
      "arn":"arn:aws:sts::123456789012:assumed-role/DeveloperRole/example-session",
      "accountId":"123456789012",
      "sessionContext":{
         "sessionIssuer":{
            "type":"Role",
            "principalId":"AROA123456789EXAMPLE",
            "arn":"arn:aws:iam::123456789012:role/DeveloperRole",
            "accountId":"123456789012",
            "userName":"DeveloperRole"
         },
         "attributes":{
            "creationDate":"2026-11-17T06:18:21Z",
            "mfaAuthenticated":"false"
         }
      }
   },
   "eventTime":"2026-11-17T06:18:22Z",
   "eventSource":"signin.amazonaws.com",
   "eventName":"CreateOAuth2Token",
   "awsRegion":"us-east-1",
   "sourceIPAddress":"192.0.2.0",
   "userAgent":"Python-urllib/3.12",
   "requestParameters":{
      "resource":"https://signin-mcp.us-east-1.api.aws/mcp",
      "client_id":"arn:aws:signin:us-east-1::external-client/dcr/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
   },
   "responseElements":null,
   "additionalEventData":{
      "signInSessionArn":"arn:aws:signin:us-east-1:123456789012:session/my-session-id",
      "SignInSessionExtended":"true",
      "grant_type":"authorization_code",
      "success":"true"
   },
   "requestID":"0905655e-04d6-471f-bcf8-EXAMPLE14ff",
   "eventID":"4f4eaa15-7d87-47eb-a9df-EXAMPLE25bd",
   "readOnly":true,
   "eventType":"AwsApiCall",
   "managementEvent":true,
   "recipientAccountId":"123456789012",
   "eventCategory":"Management",
   "tlsDetails":{
      "tlsVersion":"TLSv1.3",
      "cipherSuite":"TLS_AES_128_GCM_SHA256",
      "clientProvidedHostHeader":"us-east-1.oauth.signin.aws"
   }
}
```

## Monitoring extended sign-in sessions
<a name="oauth-sign-in-session-monitor-extended"></a>

AWS CloudTrail records OAuth token issuance and renewal through `CreateOAuth2Token` events. These events include information about the associated sign-in session and whether an extended sign-in duration is configured.

The following example shows a `CreateOAuth2Token` event. The `additionalEventData` object contains the following fields:
+ `SignInSessionExtended` indicates whether the sign-in session uses an explicitly configured sign-in duration.
+ `SignInDuration` shows the configured session duration, in seconds.
+ `signInSessionArn` identifies the sign-in session associated with the token request.

```json
{
   "eventVersion":"1.11",
   "userIdentity":{
      "type":"IAMUser",
      "principalId":"AIDA123456789EXAMPLE",
      "arn":"arn:aws:iam::111122223333:user/example-user",
      "accountId":"111122223333",
      "userName":"example-user",
      "sessionContext":{
         "attributes":{
            "creationDate":"2026-11-19T02:28:36Z",
            "mfaAuthenticated":"false"
         }
      }
   },
   "eventTime":"2026-11-19T02:29:07Z",
   "eventSource":"signin.amazonaws.com",
   "eventName":"CreateOAuth2Token",
   "awsRegion":"us-west-2",
   "sourceIPAddress":"192.0.2.1",
   "userAgent":"curl/8.3.0",
   "requestParameters":{
      "resource":"https://signin-mcp.us-west-2.api.aws/mcp",
      "client_id":"arn:aws:signin:us-west-2::external-client/dcr/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333"
   },
   "responseElements":null,
   "additionalEventData":{
      "signInSessionArn":"arn:aws:signin:us-west-2:111122223333:session/a1b2c3d4-5678-90ab-cdef-EXAMPLE44444",
      "SignInSessionExtended":"true",
      "grant_type":"authorization_code",
      "success":"true",
      "SignInDuration":"7775999"
   },
   "requestID":"a1b2c3d4-5678-90ab-cdef-EXAMPLE55555",
   "eventID":"a1b2c3d4-5678-90ab-cdef-EXAMPLE66666",
   "readOnly":true,
   "eventType":"AwsApiCall",
   "managementEvent":true,
   "recipientAccountId":"111122223333",
   "eventCategory":"Management",
   "tlsDetails":{
      "tlsVersion":"TLSv1.3",
      "cipherSuite":"TLS_AES_128_GCM_SHA256",
      "clientProvidedHostHeader":"us-west-2.oauth.signin.aws"
   }
}
```
