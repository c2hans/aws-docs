---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-managed-identity-saml.html
---

# Use SAML federated identities for ACL-aware retrieval

By default, ACL-aware retrieval filters results by the email address that your application passes in `userContext.userId`. If your users sign in through a SAML 2.0 identity provider, such as Okta, Microsoft Entra ID, or Ping Identity, that is federated with IAM, you can configure the knowledge base to read each user's email from the session credentials that sign the request instead. You configure the IAM SAML identity provider to add the user's identity to the role sessions it issues. This topic calls such a session a *federated session*. Your application then calls the knowledge base with that session, and Bedrock Managed Knowledge Base filters results by the email in the session. For how ACL filtering works, see [Access Control Lists awareness enablement](kb-managed-acl.md).

The identity comes from the SAML assertion that your identity provider signed, so your application can't substitute a different user's email for a signed-in user. This topic covers SAML federation with IAM. If your users sign in through IAM Identity Center, see [Use IAM Identity Center identities for ACL-aware retrieval](kb-managed-identity-idc.md).

The identity setting applies to the following runtime operations: `Retrieve`, `AgenticRetrieveStream`, and `GetDocumentContent`.

## Prerequisites
<a name="kb-managed-identity-saml-prereq"></a>
+ A Bedrock Managed Knowledge Base with at least one data source that has ACL awareness turned on.
+ A SAML 2.0 identity provider that issues assertions for your users.
+ A SAML assertion that carries each user's email address, and that email exactly matches the email that the user has in your connected data sources.
+ Permission to create or update an IAM SAML identity provider and an IAM role.

## How it works
<a name="kb-managed-identity-saml-how"></a>

1. The user signs in to your identity provider, which returns a signed SAML assertion that contains the user's email.

1. Your application calls `AssumeRoleWithSAML` with the assertion. Because the IAM SAML identity provider has trusted identity propagation turned on, AWS STS adds the user's identity to the role session.

1. Your application calls the knowledge base with that session's credentials.

1. Bedrock Managed Knowledge Base checks whether it trusts the IAM SAML identity provider that issued the session. If it doesn't, it treats the session as having no identity. For details, see [Choose the identity sources that the knowledge base trusts](#kb-managed-identity-saml-trusted).

1. Bedrock Managed Knowledge Base reads the user's email from the session. The *session subject* is the user identifier that AWS STS copies into the session from the SAML attribute that you choose in Step 2. The knowledge base uses the subject when it is an email address. Otherwise, it uses the `email` runtime claim in the session's identity context.

1. The knowledge base's user context mode decides how that email is combined with any `userContext` in the request.

**Note**
The email is read from the session itself, so Bedrock Managed Knowledge Base doesn't look up the user in another directory. If you also link the IAM SAML identity provider to an IAM Identity Center instance, the email still comes from the SAML assertion.

## Step 1: Set the user context mode on the knowledge base
<a name="kb-managed-identity-saml-mode"></a>

The `userContextModeForRetrieval` setting controls which identity the knowledge base trusts. You can set it when you create the knowledge base, or change it later with `UpdateKnowledgeBase`. The following table describes each mode.

**User context modes**

| Mode | Behavior |
| --- | --- |
| API\_INPUT\_ONLY (default) | Uses only the userContext in the request. The session identity is ignored. |
| IDENTITY\_ENHANCED\_SESSION\_ELSE\_API\_INPUT | Uses the session identity when the session has one. If the request also includes userContext.userId, that value must match the session user's email, ignoring case. Otherwise, the request fails with ValidationException. If the session has no identity, the knowledge base uses the userContext in the request. Use this mode while you move callers from userContext to federated sessions. |
| IDENTITY\_ENHANCED\_SESSION | Uses only the session identity. Any userContext in the request is ignored. If the session has no identity, the request is treated as having no user, so ACL-enabled data sources return no results. Data sources without ACLs still return results. |

We recommend that you start with `IDENTITY_ENHANCED_SESSION_ELSE_API_INPUT`. In this mode, callers that don't send a federated session yet keep working, because the knowledge base uses the `userContext` in their requests. To set the mode on an existing knowledge base, call `UpdateKnowledgeBase`. The request must also include the knowledge base's current `name`, `roleArn`, and `knowledgeBaseConfiguration`, which you can read with `GetKnowledgeBase`. `userContextModeForRetrieval` is a top-level field in the request:

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
Don't set `IDENTITY_ENHANCED_SESSION` until you complete the remaining steps and verify your configuration. In that mode, the knowledge base ignores `userContext`, so ACL-enabled data sources return no results to callers that don't send a federated session. To switch modes after verification, see [Verify your configuration](#kb-managed-identity-saml-verify).

### Choose the identity sources that the knowledge base trusts
<a name="kb-managed-identity-saml-trusted"></a>

In both identity modes, the knowledge base uses a session's identity only if it trusts the session's identity source. For a federated session, the identity source is the IAM SAML identity provider that issued the session. The `trustedIdentitySources` setting controls which IAM SAML identity providers the knowledge base trusts:
+ If you don't set `trustedIdentitySources`, or set it to an empty list, the knowledge base trusts IAM SAML identity providers in the same AWS account as the knowledge base.
+ If you set `trustedIdentitySources`, the knowledge base trusts only the IAM SAML identity providers in the list. It no longer trusts IAM SAML identity providers in its own account automatically, so add them to the list if you still need them.

The knowledge base checks the account of the IAM SAML identity provider that issued the session, not the account of the role that calls the knowledge base. Assuming a role in the knowledge base's account doesn't change which identity provider issued the session.

If the knowledge base doesn't trust a session's identity source, it treats the session as having no identity. In `IDENTITY_ENHANCED_SESSION_ELSE_API_INPUT` mode, it uses the `userContext` in the request. In `IDENTITY_ENHANCED_SESSION` mode, ACL-enabled data sources return no results.

The list can contain up to 5 entries. Each entry sets exactly one of `identityStoreArn` or `identityProviderArn`, and the list can't contain duplicates. To set the list, include it in the `CreateKnowledgeBase` or `UpdateKnowledgeBase` request. Replace {{account-id}} and {{provider-name}} with your values:

```json
"trustedIdentitySources": [
    { "identityProviderArn": "arn:aws:iam::{{account-id}}:saml-provider/{{provider-name}}" }
]
```

In an `UpdateKnowledgeBase` request, if you leave out `trustedIdentitySources`, the knowledge base keeps its current list. To remove all entries, pass an empty list.

## Step 2: Turn on trusted identity propagation for the SAML provider
<a name="kb-managed-identity-saml-idp"></a>

In the IAM console, choose **Identity providers**, choose **Add provider**, and then choose **SAML**. Upload your identity provider's metadata document, or open an existing SAML provider. Turn on trusted identity propagation for the provider, and set the following values:
+ **Subject** – The name of the SAML attribute that contains the user's email address. If your identity provider sends the user's email in an attribute named `email`, with a value such as `jane@example.com`, enter `email`. Bedrock Managed Knowledge Base uses the subject as the user's email when it is an email address.
+ **Subject type** – `user`.
+ **Runtime claims** – Add a claim with the key `email` whose value comes from the same email attribute. Bedrock Managed Knowledge Base uses this claim when the subject isn't an email address.

For general guidance on SAML identity providers, see [Create a SAML identity provider in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_saml.html) in the *IAM User Guide*.

## Step 3: Configure the SAML application in your identity provider
<a name="kb-managed-identity-saml-assertion"></a>

In your identity provider's SAML application for AWS, send the user's email address in the attribute that you chose as the subject. Set the `NameID` to the email address as well. Keep the `Role` and `RoleSessionName` attributes that AWS SAML federation requires. For the required attributes, see [Configure SAML assertions for the authentication response](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_saml_assertions.html) in the *IAM User Guide*.

## Step 4: Create the federated role
<a name="kb-managed-identity-saml-role"></a>

Create the role that your users assume through SAML. The trust policy must allow both `sts:AssumeRoleWithSAML` and `sts:SetContext`. Replace {{account-id}} and {{provider-name}} with your values.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Federated": "arn:aws:iam::{{account-id}}:saml-provider/{{provider-name}}"
            },
            "Action": [
                "sts:AssumeRoleWithSAML",
                "sts:SetContext"
            ],
            "Condition": {
                "StringEquals": {
                    "SAML:aud": "https://signin.aws.amazon.com/saml"
                }
            }
        }
    ]
}
```

Attach a policy to the role that allows the runtime operations your application calls on the knowledge base. Replace {{region}}, {{account-id}}, and {{knowledge-base-id}} with your values.

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

## Step 5: Call the knowledge base with the federated session
<a name="kb-managed-identity-saml-session"></a>

After the user signs in, run the following AWS CLI command to exchange the SAML assertion for role credentials. Replace {{account-id}}, {{role-name}}, and {{provider-name}} with your values, and {{base64-encoded-saml-response}} with the SAML response that your identity provider returned:

```bash
aws sts assume-role-with-saml \
    --role-arn arn:aws:iam::{{account-id}}:role/{{role-name}} \
    --principal-arn arn:aws:iam::{{account-id}}:saml-provider/{{provider-name}} \
    --saml-assertion {{base64-encoded-saml-response}}
```

Set the temporary credentials from the `AssumeRoleWithSAML` response as environment variables. Replace each value with the matching field from the `Credentials` object in the response:

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

The request doesn't include a `userContext`. The knowledge base reads the user's email from the session and returns only the documents that the user can access.

## Use a knowledge base in a different account
<a name="kb-managed-identity-saml-cross-account"></a>

To call a knowledge base in another AWS account, your application can assume a role in the knowledge base's account from the federated session. The user's identity carries over to the new session. If the IAM SAML identity provider is in a different account from the knowledge base, add the provider's ARN to the knowledge base's `trustedIdentitySources`. For details, see [Choose the identity sources that the knowledge base trusts](#kb-managed-identity-saml-trusted).

To call a knowledge base in another account without assuming a role there, the knowledge base needs a resource-based policy that allows your account. For more information, see [Resource policies for managed knowledge bases](kb-managed-cross-account.md).

## Verify your configuration
<a name="kb-managed-identity-saml-verify"></a>

1. Pick a document in an ACL-enabled data source that the test user can access, and one that the user can't access.

1. Sign in as the test user and exchange the assertion with `AssumeRoleWithSAML`.

1. With that session, call `Retrieve` without a `userContext`, using a query that matches both documents. Confirm that the response includes the document that the user can access and not the other one.

1. (Optional) After all callers send federated sessions, update the knowledge base to `IDENTITY_ENHANCED_SESSION` so that it trusts only the session identity and ignores `userContext`. Wait about 5 minutes for the change to apply, and then repeat the previous step.

## Troubleshooting
<a name="kb-managed-identity-saml-troubleshooting"></a>

Several problems return only documents from data sources without ACLs. To narrow them down, check whether the session has a user identity that the knowledge base trusts. Set the knowledge base to `IDENTITY_ENHANCED_SESSION_ELSE_API_INPUT`, and send a `Retrieve` request with the federated session and a `userContext.userId` that belongs to a different user. If the request fails with the mismatch `ValidationException`, the session has an identity that the knowledge base trusts.

**SAML federated identity issues, causes, and fixes**

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| Only documents from data sources without ACLs are returned, and the session has no trusted identity. | Trusted identity propagation isn't turned on for the IAM SAML identity provider. | Turn on trusted identity propagation as described in [Step 2: Turn on trusted identity propagation for the SAML provider](#kb-managed-identity-saml-idp). |
| Only documents from data sources without ACLs are returned, and the IAM SAML identity provider is in a different account from the knowledge base. | The knowledge base doesn't trust the IAM SAML identity provider. By default, it trusts only identity sources in its own account. If trustedIdentitySources is set, it trusts only the sources in that list. | Add the ARN of the IAM SAML identity provider to trustedIdentitySources, as described in [Choose the identity sources that the knowledge base trusts](#kb-managed-identity-saml-trusted). |
| Only documents from data sources without ACLs are returned, and the session has a trusted identity. | The subject isn't an email address and there is no email runtime claim, or the email differs from the one in the data source. | Set the subject or the email runtime claim to the attribute that carries the user's email, and make sure it matches the data source. |
| ValidationException: The userContext.userId in the request does not match the verified user identity on the session. | The knowledge base uses IDENTITY\_ENHANCED\_SESSION\_ELSE\_API\_INPUT, and the request's userContext.userId is a different user. | Remove userContext from the request, or pass the signed-in user's email. |
