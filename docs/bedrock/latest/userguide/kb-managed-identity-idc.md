---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-managed-identity-idc.html
---

# Use IAM Identity Center identities for ACL-aware retrieval

By default, ACL-aware retrieval filters results by the email address that your application passes in `userContext.userId`. If your users sign in through IAM Identity Center, you can configure the knowledge base to read each user's identity from the session credentials that sign the request instead. Your application calls the knowledge base with an *identity-enhanced session*, which is an IAM role session that AWS STS issues with the user's IAM Identity Center identity attached. Bedrock Managed Knowledge Base looks up that user's email address in the IAM Identity Center identity store and uses it to filter results. For how ACL filtering works, see [Access Control Lists awareness enablement](kb-managed-acl.md).

The identity comes from the session that AWS issued, so your application can't substitute a different user's email for a signed-in user. This topic covers IAM Identity Center. If your users sign in through a SAML 2.0 identity provider that is federated with IAM, see [Use SAML federated identities for ACL-aware retrieval](kb-managed-identity-saml.md).

The identity setting applies to the following runtime operations: `Retrieve`, `AgenticRetrieveStream`, and `GetDocumentContent`.

## Prerequisites
<a name="kb-managed-identity-idc-prereq"></a>
+ A Bedrock Managed Knowledge Base with at least one data source that has ACL awareness turned on.
+ An IAM Identity Center instance that contains your users.
+ An email address on each IAM Identity Center user that exactly matches the email that the user has in your connected data sources. Bedrock Managed Knowledge Base uses the user's primary email address. If no email is marked as primary, it uses the first email address on the user.
+ An application that signs in your users and obtains an identity-enhanced session for each user. The ways to obtain one are described in [Step 2: Obtain an identity-enhanced session](#kb-managed-identity-idc-session).
+ If your IAM Identity Center instance uses a customer managed AWS Key Management Service (AWS KMS) key, a key policy that lets AWS managed applications use the key. For details, see [Use an IAM Identity Center instance with a customer managed key](#kb-managed-identity-idc-cmk).

## How it works
<a name="kb-managed-identity-idc-how"></a>

1. The user signs in, and your application obtains an identity-enhanced session for that user. The session carries the user's IAM Identity Center user ID and the ARN of the identity store that contains the user.

1. Your application calls the knowledge base with that session's credentials.

1. Bedrock Managed Knowledge Base reads the user ID and identity store from the session. If the knowledge base trusts that identity store, it looks up the user in the identity store. Otherwise, it treats the session as having no identity. For details, see [Choose the identity sources that the knowledge base trusts](#kb-managed-identity-idc-trusted). If the user no longer exists or is disabled, the request fails with `AccessDeniedException`.

1. Bedrock Managed Knowledge Base uses the user's email address as the user identity for ACL filtering. The knowledge base's user context mode decides how that email is combined with any `userContext` in the request.

**Note**
The calling role doesn't need any IAM Identity Center or identity store permissions. Bedrock Managed Knowledge Base performs the identity store lookup on your behalf.

## Step 1: Set the user context mode on the knowledge base
<a name="kb-managed-identity-idc-mode"></a>

The `userContextModeForRetrieval` setting controls which identity the knowledge base trusts. You can set it when you create the knowledge base, or change it later with `UpdateKnowledgeBase`. The following table describes each mode.

**User context modes**

| Mode | Behavior |
| --- | --- |
| API\_INPUT\_ONLY (default) | Uses only the userContext in the request. The session identity is ignored. |
| IDENTITY\_ENHANCED\_SESSION\_ELSE\_API\_INPUT | Uses the session identity when the session has one. If the request also includes userContext.userId, that value must match the session user's email, ignoring case. Otherwise, the request fails with ValidationException. If the session has no identity, the knowledge base uses the userContext in the request. Use this mode while you move callers from userContext to identity-enhanced sessions. |
| IDENTITY\_ENHANCED\_SESSION | Uses only the session identity. Any userContext in the request is ignored. If the session has no identity, the request is treated as having no user, so ACL-enabled data sources return no results. Data sources without ACLs still return results. |

We recommend that you start with `IDENTITY_ENHANCED_SESSION_ELSE_API_INPUT`. In this mode, callers that don't send an identity-enhanced session yet keep working, because the knowledge base uses the `userContext` in their requests. To set the mode on an existing knowledge base, call `UpdateKnowledgeBase`. The request must also include the knowledge base's current `name`, `roleArn`, and `knowledgeBaseConfiguration`, which you can read with `GetKnowledgeBase`. `userContextModeForRetrieval` is a top-level field in the request:

```json
{
    "name": "{{knowledge-base-name}}",
    "roleArn": "{{knowledge-base-role-arn}}",
    "knowledgeBaseConfiguration": {{current-knowledge-base-configuration}},
    "userContextModeForRetrieval": "IDENTITY_ENHANCED_SESSION_ELSE_API_INPUT"
}
```

You can also set `userContextModeForRetrieval` when you create the knowledge base with `CreateKnowledgeBase`.

A mode change can take up to about 5 minutes to apply. Until then, some requests can still use the previous mode.

**Important**
Don't set `IDENTITY_ENHANCED_SESSION` until you complete the remaining steps and verify your configuration. In that mode, the knowledge base ignores `userContext`, so ACL-enabled data sources return no results to callers that don't send an identity-enhanced session. To switch modes after verification, see [Verify your configuration](#kb-managed-identity-idc-verify).

### Choose the identity sources that the knowledge base trusts
<a name="kb-managed-identity-idc-trusted"></a>

In both identity modes, the knowledge base uses a session's identity only if it trusts the session's identity source. For an IAM Identity Center session, the identity source is the identity store that contains the user. The `trustedIdentitySources` setting controls which identity stores the knowledge base trusts:
+ If you don't set `trustedIdentitySources`, or set it to an empty list, the knowledge base trusts identity stores in the same AWS account as the knowledge base.
+ If you set `trustedIdentitySources`, the knowledge base trusts only the identity stores in the list. It no longer trusts identity stores in its own account automatically, so add them to the list if you still need them.

If the knowledge base doesn't trust a session's identity source, it treats the session as having no identity. In `IDENTITY_ENHANCED_SESSION_ELSE_API_INPUT` mode, it uses the `userContext` in the request. In `IDENTITY_ENHANCED_SESSION` mode, ACL-enabled data sources return no results.

The list can contain up to 5 entries. Each entry sets exactly one of `identityStoreArn` or `identityProviderArn`, and the list can't contain duplicates. To set the list, include it in the `CreateKnowledgeBase` or `UpdateKnowledgeBase` request. Replace {{account-id}} and {{identity-store-id}} with your values:

```json
"trustedIdentitySources": [
    { "identityStoreArn": "arn:aws:identitystore::{{account-id}}:identitystore/{{identity-store-id}}" }
]
```

In an `UpdateKnowledgeBase` request, if you leave out `trustedIdentitySources`, the knowledge base keeps its current list. To remove all entries, pass an empty list.

## Step 2: Obtain an identity-enhanced session
<a name="kb-managed-identity-idc-session"></a>

Bedrock Managed Knowledge Base accepts identity-enhanced sessions that IAM Identity Center issues through trusted identity propagation. Choose the method that matches how your application signs in users.

### Your application uses its own identity provider
<a name="kb-managed-identity-idc-session-tti"></a>

If your application signs users in with an OAuth 2.0 identity provider, such as Okta, Microsoft Entra ID, or Amazon Cognito, register that provider as a trusted token issuer in IAM Identity Center. Then exchange the user's JSON Web Token (JWT) from that provider for an IAM Identity Center token, and use it to assume a role. For the setup, see [Using applications with a trusted token issuer](https://docs.aws.amazon.com/singlesignon/latest/userguide/using-apps-with-trusted-token-issuer.html) in the *IAM Identity Center User Guide*.

Before you run the commands, make sure that your setup includes the following:
+ A customer managed application in IAM Identity Center with a JWT bearer grant (`urn:ietf:params:oauth:grant-type:jwt-bearer`) that names your trusted token issuer. Set the grant's audience to your identity provider's client ID.
+ An IAM authentication method on the application whose policy allows the principal that runs `create-token-with-iam` to call `sso-oauth:CreateTokenWithIAM`.
+ User assignment on the application turned off, or the user assigned to the application.
+ A role whose trust policy allows both `sts:AssumeRole` and `sts:SetContext` for the principal that calls `AssumeRole`. For more information, see [Identity-enhanced IAM role sessions](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-identity-enhanced-iam-role-sessions.html) in the *IAM Identity Center User Guide*.

1. Run the following AWS CLI command to exchange the user's token from your identity provider for an IAM Identity Center token. Replace {{application-arn}} with the ARN of your customer managed application in IAM Identity Center, and {{user-jwt}} with the JWT that your identity provider issued to the user:

   ```bash
   aws sso-oidc create-token-with-iam \
       --client-id {{application-arn}} \
       --grant-type urn:ietf:params:oauth:grant-type:jwt-bearer \
       --assertion {{user-jwt}}
   ```

   The response contains an `idToken`, which is a JWT. Its payload is the second dot-separated part, encoded as base64url. The following command decodes the payload and prints the `sts:identity_context` claim. Replace {{id-token}} with the `idToken` value:

   ```bash
   python3 -c 'import base64, json, sys; p = sys.argv[1].split(".")[1]; print(json.loads(base64.urlsafe_b64decode(p + "=" * (-len(p) % 4)))["sts:identity_context"])' {{id-token}}
   ```

1. Run the following AWS CLI command to assume the role that calls the knowledge base and pass the identity context. Replace {{role-arn}} with the ARN of that role, {{session-name}} with a name for the session, and {{identity-context}} with the `sts:identity_context` value from the previous step:

   ```bash
   aws sts assume-role \
       --role-arn {{role-arn}} \
       --role-session-name {{session-name}} \
       --provided-contexts ProviderArn=arn:aws:iam::aws:contextProvider/IdentityCenter,ContextAssertion={{identity-context}}
   ```

1. Set the temporary credentials from the `AssumeRole` response as environment variables. Replace each value with the matching field from the `Credentials` object in the response:

   ```bash
   export AWS_ACCESS_KEY_ID={{access-key-id}}
   export AWS_SECRET_ACCESS_KEY={{secret-access-key}}
   export AWS_SESSION_TOKEN={{session-token}}
   ```

   Then run the following command to call the knowledge base. Replace {{knowledge-base-id}} with the ID of your knowledge base, and {{query}} with your query text:

   ```bash
   aws bedrock-agent-runtime retrieve \
       --knowledge-base-id {{knowledge-base-id}} \
       --retrieval-query '{"text": "{{query}}"}'
   ```

   The request doesn't include a `userContext`. The knowledge base reads the user from the session and returns only the documents that the user can access.

### Your users sign in to IAM Identity Center directly
<a name="kb-managed-identity-idc-session-portal"></a>

If your users sign in through the AWS access portal and use a permission set, turn on identity-enhanced sessions for your IAM Identity Center instance. The role sessions that users receive then carry their IAM Identity Center user ID and identity store ARN. Identity-enhanced sessions require an organization instance of IAM Identity Center, and your users need the `sts:SetContext` permission. For the steps, see [Enabling identity-enhanced console sessions](https://docs.aws.amazon.com/singlesignon/latest/userguide/identity-aware-sessions.html) in the *IAM Identity Center User Guide*.

Grant the permission set the knowledge base permissions described in [Step 3: Grant the role permission to call the knowledge base](#kb-managed-identity-idc-permissions). After a user signs in, call the knowledge base with the permission set's credentials. To do this with the AWS CLI, add `--profile {{profile-name}}` to the `retrieve` command shown in the previous section.

## Step 3: Grant the role permission to call the knowledge base
<a name="kb-managed-identity-idc-permissions"></a>

Attach a policy to the role (or permission set) that allows the runtime operations your application calls on the knowledge base. Replace {{region}}, {{account-id}}, and {{knowledge-base-id}} with your values.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "bedrock:Retrieve",
                "bedrock:AgenticRetrieveStream",
                "bedrock:GetDocumentContent"
            ],
            "Resource": "arn:aws:bedrock:{{region}}:{{account-id}}:knowledge-base/{{knowledge-base-id}}"
        }
    ]
}
```

## Call a knowledge base in a different account
<a name="kb-managed-identity-idc-cross-account"></a>

The IAM Identity Center instance and the knowledge base can be in different AWS accounts. To call a knowledge base in another account, your application can assume a role in the knowledge base's account from the identity-enhanced session. The user's identity carries over to the new session. Because the identity store is in a different account from the knowledge base, add the identity store's ARN to the knowledge base's `trustedIdentitySources`. For details, see [Choose the identity sources that the knowledge base trusts](#kb-managed-identity-idc-trusted).

To call a knowledge base in another account without assuming a role there, the knowledge base needs a resource-based policy that allows your account. For more information, see [Resource policies for managed knowledge bases](kb-managed-cross-account.md).

## Use an IAM Identity Center instance with a customer managed key
<a name="kb-managed-identity-idc-cmk"></a>

If your IAM Identity Center instance encrypts its data with a customer managed AWS KMS key, Bedrock Managed Knowledge Base needs permission to decrypt identity data when it looks up a user. Make sure that the key policy includes the statement that allows AWS managed applications to use the key. That statement allows `kms:Decrypt` when `aws:PrincipalIsAWSService` is `true` and the request comes through IAM Identity Center or the identity store. For the statement, see [Baseline KMS key policy](https://docs.aws.amazon.com/singlesignon/latest/userguide/baseline-KMS-key-policy.html) in the *IAM Identity Center User Guide*.

If the key policy doesn't allow this, requests that need the user's email fail with `InternalServerException`.

## Verify your configuration
<a name="kb-managed-identity-idc-verify"></a>

1. Pick a document in an ACL-enabled data source that the test user can access, and one that the user can't access.

1. Obtain an identity-enhanced session for the test user.

1. With that session, call `Retrieve` without a `userContext`, using a query that matches both documents. Confirm that the response includes the document that the user can access and not the other one.

1. (Optional) After all callers send identity-enhanced sessions, update the knowledge base to `IDENTITY_ENHANCED_SESSION` so that it trusts only the session identity and ignores `userContext`. Wait about 5 minutes for the change to apply, and then repeat the previous step.

## Troubleshooting
<a name="kb-managed-identity-idc-troubleshooting"></a>

Several problems return only documents from data sources without ACLs. To narrow them down, check whether the session has a user identity that the knowledge base trusts. Set the knowledge base to `IDENTITY_ENHANCED_SESSION_ELSE_API_INPUT`, and send a `Retrieve` request with the identity-enhanced session and a `userContext.userId` that belongs to a different user. If the request fails with the mismatch `ValidationException`, the session has an identity that the knowledge base trusts.

**IAM Identity Center identity issues, causes, and fixes**

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| Only documents from data sources without ACLs are returned, and the session has no trusted identity. | The request uses an ordinary role session that doesn't carry the user's IAM Identity Center identity. | Obtain the session as described in [Step 2: Obtain an identity-enhanced session](#kb-managed-identity-idc-session). |
| Only documents from data sources without ACLs are returned, and the identity store is in a different account from the knowledge base. | The knowledge base doesn't trust the identity store. By default, it trusts only identity sources in its own account. If trustedIdentitySources is set, it trusts only the sources in that list. | Add the ARN of the identity store to trustedIdentitySources, as described in [Choose the identity sources that the knowledge base trusts](#kb-managed-identity-idc-trusted). |
| Only documents from data sources without ACLs are returned, and the session has a trusted identity. | The user has no email address in the identity store, or the email differs from the one in the data source. | Set the user's primary email in IAM Identity Center to the email that the user has in the data source. |
| AccessDeniedException: The IAM Identity Center user on this request is no longer valid. | The user was deleted or disabled in IAM Identity Center, or the session doesn't contain a user ID. | Confirm that the user exists and is enabled, then obtain a new session. |
| ValidationException: The userContext.userId in the request does not match the verified user identity on the session. | The knowledge base uses IDENTITY\_ENHANCED\_SESSION\_ELSE\_API\_INPUT, and the request's userContext.userId is a different user. | Remove userContext from the request, or pass the signed-in user's email. |
| InternalServerException | Bedrock Managed Knowledge Base couldn't read the user from the identity store. If your IAM Identity Center instance uses a customer managed key, the key policy might not allow AWS managed applications to decrypt identity data. | Check the key policy as described in [Use an IAM Identity Center instance with a customer managed key](#kb-managed-identity-idc-cmk). Otherwise, retry the request, and if the error continues, contact AWS Support. |
