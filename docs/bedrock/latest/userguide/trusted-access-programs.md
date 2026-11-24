---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/trusted-access-programs.html
---

# Trusted access programs in Amazon Bedrock

A trusted access program is an offer from a model provider that changes which of the provider's models you can use or how Amazon Bedrock handles your requests to them, such as how Amazon Bedrock retains and reviews them. To participate, you must get approval for your account, your organization in AWS Organizations, or a project, and you must opt in. Some programs enroll approved accounts for you. The program's page says whether you need to opt in.

You use the Amazon Bedrock API to find programs, check your status, request approval, and opt in or out. You control who can opt in with IAM policies and service control policies (SCPs).

## How trusted access programs work
<a name="tap-how-it-works"></a>

Trusted access programs use the following concepts:

Program
An offer from a model provider. Each program has a program ID, a provider, and a page that describes what the program changes.

Approval
A decision by the model provider or AWS that your project, account, or organization can participate. The program's page says who approves requests. The API calls approval *eligibility*.

Enrollment
Your choice to participate. You set enrollment to `enabled`, `disabled`, or `inherit`.

Scope
The level where approval and enrollment apply. A program supports one or more of project, account, and organization scope. Project scope covers one named Amazon Bedrock project.

Status
The result that Amazon Bedrock computes from your approval and enrollment. The status shows whether the program takes effect for your requests.

## Available programs
<a name="tap-available-programs"></a>

The following table lists the trusted access programs in Amazon Bedrock. For a program's eligibility, supported scopes, how to request approval, and what the program changes, see the program's page.

| Program | Program ID | Provider |
| --- | --- | --- |
| [Anthropic Enterprise Frontier Safeguards (EFS)](anthropic-efs-enterprise-data-controls.md) | anthropic-efs | Anthropic |
| [Anthropic Enterprise Data Controls (EDC)](anthropic-efs-enterprise-data-controls.md) | anthropic-edc | Anthropic |

You can use trusted access programs in the commercial AWS Regions where Amazon Bedrock is available. For the endpoints, see [Amazon Bedrock endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/bedrock.html) in the AWS General Reference.

## Program status
<a name="tap-status"></a>

[ListTrustedAccessPrograms](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListTrustedAccessPrograms.html) returns only the programs that are offered to your account. For a program that isn't offered to your account, [GetTrustedAccessProgram](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetTrustedAccessProgram.html) returns a `ResourceNotFoundException` error. The following table describes the statuses that a program can return for your account or project.

| Status | Description | Next step |
| --- | --- | --- |
| requestable | No approval covers you at any scope, or the provider or AWS declined your request. The program doesn't take effect for your requests. | Request approval. For instructions, see [Opting in to a program](#tap-opt-in). |
| eligible | An approval covers you, and you haven't opted in. The program doesn't take effect for your requests. | Opt in to participate. |
| enabled | An approval covers you, and you opted in. The program takes effect for your requests. | To stop participating, opt out. |
| disabled | An approval covers you, and you opted out. The program doesn't take effect for your requests. | To participate again, opt in. |
| revoked | The provider or AWS withdrew the approval. The program doesn't take effect for your requests. Amazon Bedrock keeps your enrollment setting, and statusReason gives the reason. | Contact your AWS account team. If the provider or AWS restores the approval, your saved setting takes effect again. |

Each program in the [ListTrustedAccessPrograms](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListTrustedAccessPrograms.html) and [GetTrustedAccessProgram](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetTrustedAccessProgram.html) responses includes the following fields:

`programId`
The program ID.

`name`
The program's name.

`description`
A summary of what the program changes.

`providerName`
The model provider that offers the program.

`detailsUrl`
The program's page, which describes what the program changes and how to request approval.

`status`
Your status in the program.

`statusReason`
Why the program is `requestable` or `revoked`, and what to do next. The response includes this field only for those statuses.

`enrollmentUrl`
The provider's application page. The response includes this field only when you can start an application and the provider uses an application page.

`source`
The scope that decided the status. The value is `project`, `account`, or `organization`, or `program_default` when no scope has a setting.

`eligibilityScope`
The scope of the approval or revocation that applies to you. The response omits this field when no approval or revocation applies.

`resolvedFor`
The account that the status applies to, and the project ARN when you specify a project.

`optIn`
Your enrollment setting after project, account, and organization settings combine.

`updatedAt`
When that enrollment setting last changed. The response includes this field only when `optIn` is `enabled` or `disabled`.

Amazon Bedrock can add new values for `status`, `source`, and `optIn`. Write code that handles values that this page doesn't list.

## How project, account, and organization settings combine
<a name="tap-scopes"></a>

Project, account, and organization settings combine in the following ways:
+ Organization scope covers every current and future member account in your organization. Only the management account or an account registered as a delegated administrator for Amazon Bedrock can request approval, opt in, or view enrollment for the organization.
+ Project scope covers one named project in the AWS Region where you created it. You can't set it for your account's default project. Requests that don't use a named project use the account and organization settings. You can read the settings of an archived project until it expires, but you can't change its enrollment or start an application for it.
+ A project setting takes precedence over the account setting, and an account setting takes precedence over the organization setting. For example, a member account can set enrollment to `disabled` while its organization is `enabled`. To follow the broader setting again, set enrollment to `inherit`.
+ An approval also covers narrower scopes. An organization approval lets a member account or its projects opt in. An account approval doesn't let the organization opt in, and a project approval doesn't let the account opt in.
+ A revocation at any scope that applies to you takes precedence over every approval.
+ Account and organization settings apply in every AWS Region where trusted access programs are available. A change can take several minutes to reach every Region.
+ Program settings are separate from data retention settings, which you set in each Region. For more information, see [Data retention](data-retention.md).

[ListTrustedAccessPrograms](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListTrustedAccessPrograms.html) and [GetTrustedAccessProgram](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetTrustedAccessProgram.html) return your status after project, account, and organization settings combine. To see the setting stored at one scope, use [GetTrustedAccessProgramAccountEnrollment](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetTrustedAccessProgramAccountEnrollment.html), [GetTrustedAccessProgramOrganizationEnrollment](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetTrustedAccessProgramOrganizationEnrollment.html), or [GetTrustedAccessProgramProjectEnrollment](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetTrustedAccessProgramProjectEnrollment.html). These operations return `optIn` and `updatedAt` for that scope only. If no setting is stored at that scope, they return `inherit`.

## Prerequisites
<a name="tap-prerequisites"></a>

Before you opt in to a program, make sure that you have the following:
+ An IAM identity with permission for the trusted access program actions that you use. For the actions, see [Controlling enrollment with IAM](#tap-iam).
+ For organization scope, an organization in AWS Organizations with all features enabled, and access to its management account or to an account registered as a delegated administrator for Amazon Bedrock. The caller needs permission for `organizations:DescribeOrganization`. A caller in a delegated administrator account also needs permission for `organizations:ListDelegatedAdministrators`. For more information, see [Delegated administrator for AWS services that work with Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_delegated_admin.html) in the *AWS Organizations User Guide*.
+ For project scope, a named Amazon Bedrock project in the AWS Region where you call the API. For more information, see [Projects](projects.md).
+ To start an application with a provider, which only some programs accept, outbound identity federation turned on for your AWS account, permission for `sts:GetWebIdentityToken` and `sts:TagGetWebIdentityToken`, and a session with at least one hour remaining. For more information, see [Getting started with outbound identity federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_outbound_getting_started.html) in the *IAM User Guide*.

## Opting in to a program
<a name="tap-opt-in"></a>

To participate in a program, check your status, request approval if you don't have it, and then opt in. The following procedure uses AWS CLI version 2.42.0 or later. In the commands, replace {{program-id}} with the program ID from [Available programs](#tap-available-programs). The AWS CLI examples are formatted for Unix, Linux, and macOS.

**To opt in to a trusted access program (AWS CLI)**

1. Run the following command to list the programs and check your status. To check a named project, add `--project-identifier` with the project ID.

   ```bash
   aws bedrock list-trusted-access-programs
   ```

   The following example shows one program in the response for an account that doesn't have approval.

   ```json
   {
     "programSummaries": [
       {
         "programId": "{{program-id}}",
         "name": "Program name",
         "description": "Program description",
         "providerName": "Provider name",
         "detailsUrl": "https://docs.aws.amazon.com/bedrock/latest/userguide/efs-anthropic.html",
         "status": "requestable",
         "statusReason": "Contact your AWS account team to request access to this program.",
         "source": "program_default",
         "resolvedFor": { "accountId": "111122223333" },
         "optIn": "inherit"
       }
     ]
   }
   ```

1. Read the program's page to learn what the program changes and who approves requests. For the pages, see [Available programs](#tap-available-programs). Then use the status from step 1 to choose the next step.
   + If the status is `requestable`, go to step 3.
   + If the status is `eligible` or `disabled`, go to step 7.
   + If the status is `enabled`, the program already takes effect for your requests, and you don't need to do anything else.
   + If the status is `revoked`, you can't opt in. Contact your AWS account team.

1. Check whether the program accepts an application from you. If the response includes `enrollmentUrl`, or `statusReason` tells you to apply with the provider, go to step 4. Otherwise, the program doesn't accept applications from you. Request approval as `statusReason` describes, such as through your AWS account team, and then go to step 6.

1. Run one of the following commands to start an application at the scope that you want approved.
   + To apply for your account, run the following command.

     ```bash
     aws bedrock start-trusted-access-program-account-application \
         --program-identifier {{program-id}}
     ```
   + To apply for your organization, run the following command from the management account or a delegated administrator account.

     ```bash
     aws bedrock start-trusted-access-program-organization-application \
         --program-identifier {{program-id}}
     ```
   + To apply for a named project, run the following command. Replace {{proj\_abcdefghijklmnopqrst}} with your project ID.

     ```bash
     aws bedrock start-trusted-access-program-project-application \
         --program-identifier {{program-id}} \
         --project-identifier {{proj_abcdefghijklmnopqrst}}
     ```

   The following example shows the response.

   ```json
   {
     "result": {
       "providerHandoff": {
         "enrollmentUrl": "https://www.example.com/apply",
         "applicationToken": "eyJ2ZXJzaW9uIjoxLCJpZGVudGl0eVRva2Vu...",
         "applicationTokenExpiresAt": "2026-11-17T19:00:00Z"
       }
     }
   }
   ```

1. Give the complete `applicationToken` value to the provider. If the response includes `enrollmentUrl`, open it and paste the token into the provider's application form. If the response doesn't include `enrollmentUrl`, give the token to the provider as the program's page describes. Treat the token as sensitive. Don't log it or share it with anyone other than the provider.

1. After the provider or AWS approves your request, run the command in step 1 again, and confirm that the status is `eligible`.

1. Run one of the following commands to opt in.
   + To opt in your account, run the following command.

     ```bash
     aws bedrock put-trusted-access-program-account-enrollment \
         --program-identifier {{program-id}} \
         --opt-in enabled
     ```
   + To opt in your organization, run the following command from the management account or a delegated administrator account.

     ```bash
     aws bedrock put-trusted-access-program-organization-enrollment \
         --program-identifier {{program-id}} \
         --opt-in enabled
     ```
   + To opt in a named project, run the following command. Replace {{proj\_abcdefghijklmnopqrst}} with your project ID.

     ```bash
     aws bedrock put-trusted-access-program-project-enrollment \
         --program-identifier {{program-id}} \
         --project-identifier {{proj_abcdefghijklmnopqrst}} \
         --opt-in enabled
     ```

1. Run the following command to confirm that the status is `enabled`.

   ```bash
   aws bedrock get-trusted-access-program --program-identifier {{program-id}}
   ```

   If you opted in a named project, add `--project-identifier` with the project ID. Without it, the command returns your account's status, which can differ from the project's status.

   ```bash
   aws bedrock get-trusted-access-program \
       --program-identifier {{program-id}} \
       --project-identifier {{proj_abcdefghijklmnopqrst}}
   ```

   The following example shows part of the response for an account that opted in.

   ```json
   {
     "programId": "{{program-id}}",
     "status": "enabled",
     "source": "account",
     "eligibilityScope": "account",
     "resolvedFor": { "accountId": "111122223333" },
     "optIn": "enabled",
     "updatedAt": "2026-11-17T18:30:00Z"
   }
   ```

Starting an application doesn't approve your request or opt you in. If the program doesn't accept applications from your account, the command in step 4 fails with a `ValidationException` error. The application token expires at the time in `applicationTokenExpiresAt`. If the token expires before the provider accepts your application, run the command in step 4 again.

If no approval covers the scope where you opt in, or a revocation applies, the command fails with a `ConflictException` error. An organization opt-in requires an organization approval.

Some programs need more setup after you opt in. The program's page describes any other steps.

## Opting out of a program
<a name="tap-opt-out"></a>

To stop participating, set enrollment to `disabled` at the scope where you opted in. After the change takes effect, the program stops affecting new requests, and requests already in progress keep the program's handling. Your approval stays in place, so you can opt in again without a new request. To follow the broader setting instead, set enrollment to `inherit`. You can opt out even if you have no approval or your approval is revoked.

Some programs need more steps when you opt out, such as changing a storage configuration that you set up for the program. Otherwise, requests that use it can fail. The program's page describes these steps.

The following example opts your account out of a program.

```bash
aws bedrock put-trusted-access-program-account-enrollment \
    --program-identifier {{program-id}} \
    --opt-in disabled
```

Opting out your organization doesn't opt out member accounts or projects that set enrollment to `enabled` themselves. To prevent member accounts from opting in, use the SCP in [Example: Deny opting in to trusted access programs](#tap-scp-example).

## Controlling enrollment with IAM
<a name="tap-iam"></a>

Each operation has an IAM action with the same name, such as `bedrock:PutTrustedAccessProgramAccountEnrollment`. The resource is the program Amazon Resource Name (ARN), `arn:aws:bedrock::aws:trusted-access-program/{{program-id}}`, which doesn't include an AWS Region or account ID. Operations that take a project also authorize the project ARN, so the caller needs permission for both resources. Organization operations also need the AWS Organizations permissions in [Prerequisites](#tap-prerequisites). You can pass the program ID or the program ARN to any operation that takes a program. The following table lists the resources and condition keys for each operation.

| Operation | Resources | Condition keys |
| --- | --- | --- |
| [ListTrustedAccessPrograms](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListTrustedAccessPrograms.html) | trusted-access-program/\*, plus the project when you specify one | None |
| [GetTrustedAccessProgram](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetTrustedAccessProgram.html) | Program, plus the project when you specify one | bedrock:Provider |
| [StartTrustedAccessProgramAccountApplication](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_StartTrustedAccessProgramAccountApplication.html) | Program | bedrock:Provider |
| [StartTrustedAccessProgramOrganizationApplication](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_StartTrustedAccessProgramOrganizationApplication.html) | Program | bedrock:Provider |
| [StartTrustedAccessProgramProjectApplication](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_StartTrustedAccessProgramProjectApplication.html) | Program and project | bedrock:Provider |
| [GetTrustedAccessProgramAccountEnrollment](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetTrustedAccessProgramAccountEnrollment.html) | Program | bedrock:Provider |
| [PutTrustedAccessProgramAccountEnrollment](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_PutTrustedAccessProgramAccountEnrollment.html) | Program | bedrock:Provider, bedrock:TrustedAccessProgramOptIn |
| [GetTrustedAccessProgramOrganizationEnrollment](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetTrustedAccessProgramOrganizationEnrollment.html) | Program | bedrock:Provider |
| [PutTrustedAccessProgramOrganizationEnrollment](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_PutTrustedAccessProgramOrganizationEnrollment.html) | Program | bedrock:Provider, bedrock:TrustedAccessProgramOptIn |
| [GetTrustedAccessProgramProjectEnrollment](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetTrustedAccessProgramProjectEnrollment.html) | Program and project | bedrock:Provider |
| [PutTrustedAccessProgramProjectEnrollment](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_PutTrustedAccessProgramProjectEnrollment.html) | Program and project | bedrock:Provider, bedrock:TrustedAccessProgramOptIn |

The `bedrock:TrustedAccessProgramOptIn` condition key contains the requested value, which is `enabled`, `disabled`, or `inherit`. Use it to control who can opt in while allowing anyone to opt out. The `bedrock:Provider` condition key contains the program's provider, such as `anthropic`. For more information, see [Actions, resources, and condition keys for Amazon Bedrock](https://docs.aws.amazon.com/service-authorization/latest/reference/list_bedrock.html) in the *Service Authorization Reference*.

### Example: Deny opting in to trusted access programs
<a name="tap-scp-example"></a>

The following service control policy (SCP) prevents users and roles in member accounts from setting enrollment to `enabled` for any trusted access program. They can still set enrollment to `disabled` or `inherit`, and existing enrollments don't change. SCPs don't affect users and roles in the management account, so use IAM policies to control who opts in from that account.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyTrustedAccessProgramOptIn",
      "Effect": "Deny",
      "Action": [
        "bedrock:PutTrustedAccessProgramAccountEnrollment",
        "bedrock:PutTrustedAccessProgramOrganizationEnrollment",
        "bedrock:PutTrustedAccessProgramProjectEnrollment"
      ],
      "Resource": "arn:aws:bedrock::aws:trusted-access-program/*",
      "Condition": {
        "StringEquals": {
          "bedrock:TrustedAccessProgramOptIn": "enabled"
        }
      }
    }
  ]
}
```

To deny one program, replace `*` in `Resource` with the program ID. For more information, see [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) in the *AWS Organizations User Guide*.

## Tracking enrollment changes with AWS CloudTrail
<a name="tap-cloudtrail"></a>

AWS CloudTrail records each call to these operations in your account, including the principal that made the call. Use these records to show who opted in and when. CloudTrail in your account doesn't record approvals or revocations that the provider or AWS makes. To learn whether an approval changed, check the program's status. For more information, see [Monitor Amazon Bedrock API calls using CloudTrail](logging-using-cloudtrail.md).
