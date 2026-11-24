---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-ai-security-role.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# The IAM role for AI Security

This section describes the AWS Identity and Access Management (IAM) role that AWS WAF uses to call Amazon Bedrock on your behalf, and how to set it up.

If your AI Security rule group configuration is `ProtectRequestOnly` or `ProtectRequestAndResponse`, you must supply the ARN of an IAM role. AWS WAF assumes that role and uses the resulting credentials to call Amazon Bedrock Guardrails. The call is signed with your role's credentials. As a result, your Amazon Bedrock permissions govern the call, the call counts against your Amazon Bedrock service quotas, and Amazon Bedrock charges apply to your account.

The role is the only input that the rule group takes from you. You don't create or select a guardrail. For the reason, see [Configuring AI Security](waf-ai-security-configuring.md).

## Permissions policy for the role
<a name="waf-ai-security-role-permissions"></a>

The role needs permission to call the Amazon Bedrock Guardrails checks operation.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "bedrock:InvokeGuardrailChecks",
      "Resource": "*"
    }
  ]
}
```

The policy must allow `bedrock:InvokeGuardrailChecks`. A policy that allows only other Amazon Bedrock operations, such as `ApplyGuardrail` or `InvokeModel`, doesn't grant `InvokeGuardrailChecks`. AWS WAF accepts the configuration in that case, and the problem appears only at assessment time. AWS WAF adds a `guardrails:call_failed` label in that scenario.

The resource must be `*`. The operation doesn't act on a resource. The IAM action reference lists no resource types and no action-specific condition keys for `bedrock:InvokeGuardrailChecks`, so you can't scope the policy to a guardrail ARN.

To narrow how the role can be used, use these condition keys:

**Condition keys to narrow how the role is used**

| Condition key | Use it to require |
| --- | --- |
| aws:SourceArn | the role is used only for one protection pack (web ACL) |
| aws:RequestedRegion | the call is made only in the Region you expect |

For a protection pack (web ACL) that protects an Amazon CloudFront distribution, you can't choose the Region. Content from one distribution can be assessed in more than one supported Region, so an `aws:RequestedRegion` condition that names one Region might deny some calls.

**Note**
If you already use Amazon Bedrock Guardrails through another service, you might have a role that seems suitable. Check both of its policies before you reuse it. These roles don't work for AI Security:
An Amazon Bedrock AgentCore Gateway role allows `bedrock:InvokeGuardrailChecks` but trusts `bedrock-agentcore.amazonaws.com`, so AWS WAF can't assume it. The resulting `access_denied` failure looks like a permissions problem, but the cause is the trust policy.
An AWS WAF logging role trusts AWS WAF but grants only `logs:PutLogEvents`.
An Amazon Bedrock Guardrails read-only role trusts AWS WAF but grants only `bedrock:GetGuardrail`.

## Trust policy for the role
<a name="waf-ai-security-role-trust"></a>

The role must trust the AWS WAF service principal, `wafv2.amazonaws.com`.

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Principal": { "Service": "wafv2.amazonaws.com" },
    "Action": "sts:AssumeRole",
    "Condition": {
      "StringEquals": { "aws:SourceAccount": "{{123456789012}}" },
      "ArnEquals": { "aws:SourceArn":
    "arn:aws:wafv2:{{us-east-1}}:{{123456789012}}:regional/webacl/{{my-acl}}/{{EXAMPLE1}}" }
    }
  }]
}
```

Replace {{123456789012}} with your account ID, {{us-east-1}} with the Region of the protection pack (web ACL), {{my-acl}} with the name of the protection pack (web ACL), and {{EXAMPLE1}} with its ID.

AWS WAF reaches your role through infrastructure that is registered under `wafv2.amazonaws.com`. You don't need to name any other principal.

When AWS WAF assumes the role, it sends the account and the ARN of the protection pack (web ACL) that uses the rule group. These values arrive as the `aws:SourceAccount` and `aws:SourceArn` condition keys:
+ `aws:SourceAccount` is the account that owns the protection pack (web ACL).
+ `aws:SourceArn` is the full ARN of the protection pack (web ACL). For a regional protection pack, the form is `arn:aws:wafv2:REGION:ACCOUNT:regional/webacl/NAME/ID`. For a protection pack that protects Amazon CloudFront, the form is `arn:aws:wafv2:us-east-1:ACCOUNT:global/webacl/NAME/ID`.

This integration doesn't use an external ID. The `aws:SourceAccount` and `aws:SourceArn` conditions are the protection against the confused deputy problem. Without them, AWS WAF can assume the role on behalf of any protection pack (web ACL) that names it. We recommend that you include both conditions in the trust policy.

## Permissions the caller needs
<a name="waf-ai-security-role-passrole"></a>

To create or update a protection pack (web ACL) whose AI Security configuration names a role, the caller needs `iam:PassRole` on that role. This permission is in addition to the AWS WAF permissions for `CreateWebACL` or `UpdateWebACL`. AWS WAF checks `iam:PassRole` for every role ARN in the protection pack (web ACL).

The following rules also apply to these roles:
+ The role must be in the same account as the protection pack (web ACL). AWS WAF rejects a role in another account with the message "Cross-account pass role is not allowed".
+ The role must be in the same partition as the protection pack (web ACL).
+ A protection pack (web ACL) can name at most 10 distinct roles across all of its AI Security rule group statements. Each rule group statement takes one configuration with one role, so this limit applies only when you add the rule group more than once, for example with different scope-down statements. A request over the limit fails with `WAFLimitsExceededException`.

AWS WAF runs the `iam:PassRole` check before it validates the request parameters. A caller without the permission gets `AccessDeniedException`, even when the configuration has other errors. A `Disable` configuration carries no role, so AWS WAF doesn't run the check for it.

The following example identity policy allows a caller to pass the AI Security role:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "iam:PassRole",
      "Resource": "arn:aws:iam::{{123456789012}}:role/{{AWSWAFAISecurityRole}}"
    }
  ]
}
```

Replace {{123456789012}} with your account ID and {{AWSWAFAISecurityRole}} with the name of your role.

## Role sessions that AWS WAF creates
<a name="waf-ai-security-role-sessions"></a>

You can see these sessions in AWS CloudTrail. They help you confirm that the integration works.

**Role session properties**

| Property | Value |
| --- | --- |
| Session name | waf-aisec- followed by the protection pack (web ACL) id |
| Duration | 1 hour, the maximum for a chained role session |
| Reuse | The same credentials are reused for about an hour, so a steady workload costs about one AssumeRole call per hour per protection pack (web ACL) and role |

## Role ARN format
<a name="waf-ai-security-role-arn"></a>

The role ARN must match this pattern and be between 20 and 2,048 characters long:

```text
^arn:aws[a-zA-Z-]*:iam::\d{12}:role/(?:[\x21-\x7F]+/)?[\w+=,.@-]+$
```

The pattern allows a path. For example, `arn:aws:iam::111122223333:role/security/AWSWAFAISecurityRole` is valid.

## Create the role
<a name="waf-ai-security-role-creating"></a>

**To create the role**

1. Create an IAM role with a custom trust policy. Use the policy in [Trust policy for the role](#waf-ai-security-role-trust), with your own account ID and protection pack (web ACL) ARN.

1. Attach a permissions policy that allows `bedrock:InvokeGuardrailChecks`.

1. Confirm that Amazon Bedrock is available in the Region of your protection pack (web ACL). Also confirm that AWS Security Token Service (AWS STS) is enabled for your account in that Region.

1. Confirm that the user or role that creates or updates the protection pack (web ACL) has `iam:PassRole` on the new role. See [Permissions the caller needs](#waf-ai-security-role-passrole).

1. Add the role ARN to your AI Security rule group configuration. See [Configuring AI Security](waf-ai-security-configuring.md).

1. Send a representative request. Confirm that you see protocol recognition labels and no `guardrails:call_failed` label.

In the AWS WAF console, you set the role in the **AI Security configuration** pane. When **Send inspected traffic to Amazon Bedrock Guardrails** is on, choose a role or enter its ARN in the **Service role** field. **Create role** opens the create-role page of the IAM console. It doesn't create the role for you. Add the trust policy, the permissions policy, and the `aws:SourceArn` and `aws:RequestedRegion` conditions yourself. To review an existing role, choose **View role details in IAM**.

## Role and quota failures
<a name="waf-ai-security-role-failures"></a>

A role problem doesn't block traffic. When the call to Amazon Bedrock fails, the rule group adds the `guardrails:call_failed` label with a reason. The `Guardrails_CallFailed` rule counts by default, so the message passes without assessment and your request handling doesn't change. A broken role therefore shows as an absence of findings. To change this default, see [Failed Amazon Bedrock calls](waf-ai-security-components.md#waf-ai-security-components-call-failed).

These role problems publish the `access_denied` reason:
+ **The trust policy doesn't allow AWS WAF to assume the role.** Check the service principal. Also check that the `aws:SourceArn` condition names the protection pack (web ACL) that uses the rule group.
+ **The permissions policy doesn't allow **`bedrock:InvokeGuardrailChecks`**.** This happens when a policy was written for `ApplyGuardrail`, which is a different operation.
+ **The role trusts a different service.** A role built for another Amazon Bedrock Guardrails integration can have the right permission and the wrong trust policy.
+ **AWS STS isn't enabled for your account in the Region.** AWS WAF can't assume the role at all. This is an account-level AWS STS setting, separate from Amazon Bedrock.

If your Amazon Bedrock quota is exhausted, Amazon Bedrock throttles the call and the reason is `throttling`. This is a quota problem, separate from the role.

AWS WAF also holds back calls after repeated failures, including failures that your role or your quota causes, and labels those messages with the reason `service_unavailable`. As a result, a broken role or an exhausted quota can appear mostly as `service_unavailable`. For how to read this reason, see [Failed Amazon Bedrock calls](waf-ai-security-components.md#waf-ai-security-components-call-failed).

**Note**
An `access_denied` failure on assuming the role doesn't identify which side of the trust relationship rejected the call. Your trust policy and your permissions policy are the most likely causes, so check both first. If you've verified both and the failure continues, contact AWS Support instead of changing your policies further.

**Important**
Before you rely on this rule group, create an Amazon CloudWatch alarm on the `guardrails:call_failed` label metric. A broken role produces no error in your traffic, and the only signal is that findings stop. For an example alarm that covers both phases, see [Alarming on failed Amazon Bedrock calls](waf-ai-security-example-call-failed-alarm.md).

## Roles when you use the rule group more than once
<a name="waf-ai-security-role-multiple"></a>

You can add the AI Security rule group to one protection pack (web ACL) more than once, for example with different scope-down statements and overrides. Each instance applies its own scope-down statement and overrides, and the instances can name different roles.

AWS WAF assesses content once per phase. The request phase uses the role of the first instance that evaluates the request. The response phase uses the role of the first instance that inspects responses. For example, if a `ProtectRequestOnly` instance comes before a `ProtectRequestAndResponse` instance, one request uses both roles.

In that case, both roles must work. If one role fails, call failures appear in one phase only.
