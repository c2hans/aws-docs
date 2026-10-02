---
source_url: https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeEffectivePolicy.html
---

# DescribeEffectivePolicy
<a name="API_DescribeEffectivePolicy"></a>

Returns the contents of the effective policy for specified policy type and account. The effective policy is the aggregation of any policies of the specified type that the account inherits, plus any policy of that type that is directly attached to the account.

This operation applies only to management policies. It does not apply to authorization policies: service control policies (SCPs) and resource control policies (RCPs).

For more information about policy inheritance, see [Understanding management policy inheritance](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_inheritance_mgmt.html) in the * AWS Organizations User Guide*.

You can call this operation from any account in a organization.

## Request Syntax
<a name="API_DescribeEffectivePolicy_RequestSyntax"></a>

```
{
   "PolicyType": "{{string}}",
   "TargetId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeEffectivePolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [PolicyType](#API_DescribeEffectivePolicy_RequestSyntax) **   <a name="organizations-DescribeEffectivePolicy-request-PolicyType"></a>
The type of policy that you want information about. You can specify one of the following values:
+  [DECLARATIVE\_POLICY\_EC2](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_declarative.html)
+  [BACKUP\_POLICY](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_backup.html)
+  [TAG\_POLICY](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html)
+  [CHATBOT\_POLICY](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_chatbot.html)
+  [AISERVICES\_OPT\_OUT\_POLICY](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out.html)
+  [SECURITYHUB\_POLICY](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_security_hub.html)
+  [UPGRADE\_ROLLOUT\_POLICY](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_upgrade_rollout.html)
+  [INSPECTOR\_POLICY](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_inspector.html)
+  [BEDROCK\_POLICY](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_bedrock.html)
+  [S3\_POLICY](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_s3.html)
+  [NETWORK\_SECURITY\_DIRECTOR\_POLICY](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_network_security_director.html)
+  [GUARDDUTY\_POLICY](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_guardduty.html)
Type: String
Valid Values: `TAG_POLICY | BACKUP_POLICY | AISERVICES_OPT_OUT_POLICY | CHATBOT_POLICY | DECLARATIVE_POLICY_EC2 | SECURITYHUB_POLICY | INSPECTOR_POLICY | UPGRADE_ROLLOUT_POLICY | BEDROCK_POLICY | S3_POLICY | NETWORK_SECURITY_DIRECTOR_POLICY`
Required: Yes

 ** [TargetId](#API_DescribeEffectivePolicy_RequestSyntax) **   <a name="organizations-DescribeEffectivePolicy-request-TargetId"></a>
When you're signed in as the management account, specify the ID of the account that you want details about. Specifying an organization root or organizational unit (OU) as the target is not supported.
Type: String
Length Constraints: Maximum length of 100.
Pattern: `^(r-[0-9a-z]{4,32})|(\d{12})|(ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})$`
Required: No

## Response Syntax
<a name="API_DescribeEffectivePolicy_ResponseSyntax"></a>

```
{
   "EffectivePolicy": {
      "LastUpdatedTimestamp": number,
      "PolicyContent": "string",
      "PolicyType": "string",
      "TargetId": "string"
   }
}
```

## Response Elements
<a name="API_DescribeEffectivePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EffectivePolicy](#API_DescribeEffectivePolicy_ResponseSyntax) **   <a name="organizations-DescribeEffectivePolicy-response-EffectivePolicy"></a>
The contents of the effective policy.
Type: [EffectivePolicy](API_EffectivePolicy.md) object

## Errors
<a name="API_DescribeEffectivePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permissions to perform the requested operation. The user or role that is making the request must have at least one IAM permissions policy attached that grants the required permissions. For more information, see [Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html) in the *IAM User Guide*.
HTTP Status Code: 400

 ** AWSOrganizationsNotInUseException **
Your account isn't a member of an organization. To make this request, you must use the credentials of an account that belongs to an organization.
HTTP Status Code: 400

 ** ConstraintViolationException **
Performing this operation violates a minimum or maximum value limit. For example, attempting to remove the last service control policy (SCP) from an OU or root, inviting or creating too many accounts to the organization, or attaching too many policies to an account, OU, or root. This exception includes a reason that contains additional information about the violated limit:
Some of the reasons in the following list might not be applicable to this specific API or operation.
+ ACCOUNT\_CANNOT\_LEAVE\_ORGANIZATION: You attempted to remove the management account from the organization. You can't remove the management account. Instead, after you remove all member accounts, delete the organization itself.
+ ACCOUNT\_CANNOT\_LEAVE\_WITHOUT\_PHONE\_VERIFICATION: You attempted to remove an account from the organization that doesn't yet have enough information to exist as a standalone account. This account requires you to first complete phone verification. Follow the steps at [Removing a member account from your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_remove.html#orgs_manage_accounts_remove-from-master) in the * AWS Organizations User Guide*.
+ ACCOUNT\_CREATION\_RATE\_LIMIT\_EXCEEDED: You attempted to exceed the number of accounts that can be in progress at a time.
+ ACCOUNT\_CREATION\_NOT\_COMPLETE: Your account setup isn't complete or your account isn't fully active. You must complete the account setup before you create an organization.
+ ACCOUNT\_NOT\_ACTIVE\_FOR\_TRANSFER\_RESPONSIBILITY: Your account setup isn't complete or your account isn't fully active to invite or accept a Billing Transfer invitation.
+ ACTIVE\_RESPONSIBILITY\_TRANSFER\_PROCESS: You cannot delete organization due to an ongoing responsibility transfer process. For example, a pending invitation or an in-progress transfer. To delete the organization, you must resolve the current transfer process.
+ ACCOUNT\_NUMBER\_LIMIT\_EXCEEDED: You attempted to exceed the limit on the number of accounts in an organization. If you need more accounts, contact [AWS Support](https://console.aws.amazon.com/support/home#/) to request an increase in your limit.

  Or the number of invitations that you tried to send would cause you to exceed the limit of accounts in your organization. Send fewer invitations or contact AWS Support to request an increase in the number of accounts.
**Note**
Deleted and closed accounts still count toward your limit.
**Important**
If you get this exception when running a command immediately after creating the organization, wait one hour and try again. After an hour, if the command continues to fail with this error, contact [AWS Support](https://console.aws.amazon.com/support/home#/).
+ ALL\_FEATURES\_MIGRATION\_ORGANIZATION\_SIZE\_LIMIT\_EXCEEDED: Your organization has more than 5000 accounts, and you can only use the standard migration process for organizations with less than 5000 accounts. Use the assisted migration process to enable all features mode, or create a support case for assistance if you are unable to use assisted migration.
+ CANNOT\_REGISTER\_SUSPENDED\_ACCOUNT\_AS\_DELEGATED\_ADMINISTRATOR: You cannot register a suspended account as a delegated administrator.
+ CANNOT\_REGISTER\_MASTER\_AS\_DELEGATED\_ADMINISTRATOR: You attempted to register the management account of the organization as a delegated administrator for an AWS service integrated with Organizations. You can designate only a member account as a delegated administrator.
+ CANNOT\_CLOSE\_MANAGEMENT\_ACCOUNT: You attempted to close the management account. To close the management account for the organization, you must first either remove or close all member accounts in the organization. Follow standard account closure process using root credentials.​
+ CANNOT\_REMOVE\_DELEGATED\_ADMINISTRATOR\_FROM\_ORG: You attempted to remove an account that is registered as a delegated administrator for a service integrated with your organization. To complete this operation, you must first deregister this account as a delegated administrator.
+ CLOSE\_ACCOUNT\_QUOTA\_EXCEEDED: You have exceeded close account quota for the past 30 days.
+ CLOSE\_ACCOUNT\_REQUESTS\_LIMIT\_EXCEEDED: You attempted to exceed the number of accounts that you can close at a time. ​
+ CREATE\_ORGANIZATION\_IN\_BILLING\_MODE\_UNSUPPORTED\_REGION: To create an organization in the specified region, you must enable all features mode.
+ DELEGATED\_ADMINISTRATOR\_EXISTS\_FOR\_THIS\_SERVICE: You attempted to register an AWS account as a delegated administrator for an AWS service that already has a delegated administrator. To complete this operation, you must first deregister any existing delegated administrators for this service.
+ EMAIL\_VERIFICATION\_CODE\_EXPIRED: The email verification code is only valid for a limited period of time. You must resubmit the request and generate a new verification code.
+ HANDSHAKE\_RATE\_LIMIT\_EXCEEDED: You attempted to exceed the number of handshakes that you can send in one day.
+ INVALID\_PAYMENT\_INSTRUMENT: You cannot remove an account because no supported payment method is associated with the account. AWS does not support cards issued by financial institutions in Russia or Belarus. For more information, see [Managing your AWS payments](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-general.html).
+ MASTER\_ACCOUNT\_ADDRESS\_DOES\_NOT\_MATCH\_MARKETPLACE: To create an account in this organization, you first must migrate the organization's management account to the marketplace that corresponds to the management account's address. All accounts in an organization must be associated with the same marketplace.
+ MASTER\_ACCOUNT\_MISSING\_BUSINESS\_LICENSE: Applies only to the AWS Regions in China. To create an organization, the master must have a valid business license. For more information, contact customer support.
+ MASTER\_ACCOUNT\_MISSING\_CONTACT\_INFO: To complete this operation, you must first provide a valid contact address and phone number for the management account. Then try the operation again.
+ MASTER\_ACCOUNT\_NOT\_GOVCLOUD\_ENABLED: To complete this operation, the management account must have an associated account in the AWS GovCloud (US-West) Region. For more information, see [AWS Organizations](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-organizations.html) in the * AWS GovCloud User Guide*.
+ MASTER\_ACCOUNT\_PAYMENT\_INSTRUMENT\_REQUIRED: To create an organization with this management account, you first must associate a valid payment instrument, such as a credit card, with the account. For more information, see [Considerations before removing an account from an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_account-before-remove.html) in the * AWS Organizations User Guide*.
+ MAX\_DELEGATED\_ADMINISTRATORS\_FOR\_SERVICE\_LIMIT\_EXCEEDED: You attempted to register more delegated administrators than allowed for the service principal.
+ MAX\_POLICY\_TYPE\_ATTACHMENT\_LIMIT\_EXCEEDED: You attempted to exceed the number of policies of a certain type that can be attached to an entity at one time.
+ MAX\_TAG\_LIMIT\_EXCEEDED: You have exceeded the number of tags allowed on this resource.
+ MEMBER\_ACCOUNT\_PAYMENT\_INSTRUMENT\_REQUIRED: To complete this operation with this member account, you first must associate a valid payment instrument, such as a credit card, with the account. For more information, see [Considerations before removing an account from an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_account-before-remove.html) in the * AWS Organizations User Guide*.
+ MIN\_POLICY\_TYPE\_ATTACHMENT\_LIMIT\_EXCEEDED: You attempted to detach a policy from an entity that would cause the entity to have fewer than the minimum number of policies of a certain type required.
+ ORGANIZATION\_NOT\_IN\_ALL\_FEATURES\_MODE: You attempted to perform an operation that requires the organization to be configured to support all features. An organization that supports only consolidated billing features can't perform this operation.
+ OU\_DEPTH\_LIMIT\_EXCEEDED: You attempted to create an OU tree that is too many levels deep.
+ OU\_NUMBER\_LIMIT\_EXCEEDED: You attempted to exceed the number of OUs that you can have in an organization.
+ POLICY\_CONTENT\_LIMIT\_EXCEEDED: You attempted to create a policy that is larger than the maximum size.
+ POLICY\_NUMBER\_LIMIT\_EXCEEDED: You attempted to exceed the number of policies that you can have in an organization.
+ POLICY\_TYPE\_ENABLED\_FOR\_THIS\_SERVICE: You attempted to disable service access before you disabled the policy type (for example, SECURITYHUB\_POLICY). To complete this operation, you must first disable the policy type.
+ RESPONSIBILITY\_TRANSFER\_MAX\_INBOUND\_QUOTA\_VIOLATION: You have exceeded your inbound transfers limit.
+ RESPONSIBILITY\_TRANSFER\_MAX\_LEVEL\_VIOLATION: You have exceeded the maximum length of your transfer chain.
+ RESPONSIBILITY\_TRANSFER\_MAX\_OUTBOUND\_QUOTA\_VIOLATION: You have exceeded your outbound transfers limit.
+ RESPONSIBILITY\_TRANSFER\_MAX\_TRANSFERS\_QUOTA\_VIOLATION: You have exceeded the maximum number of inbound transfers allowed in a transfer chain.
+ SERVICE\_ACCESS\_NOT\_ENABLED:
  + You attempted to register a delegated administrator before you enabled service access. Call the `EnableAWSServiceAccess` API first.
  + You attempted to enable a policy type before you enabled service access. Call the `EnableAWSServiceAccess` API first.
+ TAG\_POLICY\_VIOLATION: You attempted to create or update a resource with tags that are not compliant with the tag policy requirements for this account.
+ TRANSFER\_RESPONSIBILITY\_SOURCE\_DELETION\_IN\_PROGRESS: The source organization cannot accept this transfer invitation because it is marked for deletion.
+ TRANSFER\_RESPONSIBILITY\_TARGET\_DELETION\_IN\_PROGRESS: The source organization cannot accept this transfer invitation because target organization is marked for deletion.
+ TRANSFER\_RESPONSIBILITY\_UPDATE\_NOT\_ALLOWED: You cannot update this transfer because it is no longer active. Transfers that have been withdrawn, declined, expired, or cancelled cannot be modified.
+ UNMET\_BILLING\_PREREQUISITE: Your current billing configuration is unsupported. Contact AWS Support for assistance.
+ UNSUPPORTED\_PRICING: Ineligible for Billing Transfer. Your organization is subject to a pricing agreement with AWS that Billing Transfer does not support.
+ WAIT\_PERIOD\_ACTIVE: After you create an AWS account, you must wait until at least four days after the account was created. Invited accounts aren't subject to this waiting period.
HTTP Status Code: 400

 ** EffectivePolicyNotFoundException **
If you ran this action on the management account, this policy type is not enabled. If you ran the action on a member account, the account doesn't have an effective policy of this type. Contact the administrator of your organization about attaching a policy of this type to the account.
HTTP Status Code: 400

 ** InvalidInputException **
The requested operation failed because you provided invalid values for one or more of the request parameters. This exception includes a reason that contains additional information about the violated limit:
Some of the reasons in the following list might not be applicable to this specific API or operation.
+ CALLER\_REQUIRED\_FIELD\_MISSING: At least one of the required field is missing: Caller Account Id, Management Account Id or Organization Id.
+ DUPLICATE\_TAG\_KEY: Tag keys must be unique among the tags attached to the same entity.
+ END\_DATE\_NOT\_END\_OF\_MONTH: You provided an invalid end date. The end date must be the end of the last day of the month (23.59.59.999).
+ END\_DATE\_TOO\_EARLY: You provided an invalid end date. The end date is too early.
+ END\_DATE\_TOO\_LATE: You provided an invalid end date. The end date is too late.
+ IMMUTABLE\_POLICY: You specified a policy that is managed by AWS and can't be modified.
+ INPUT\_REQUIRED: You must include a value for all required parameters.
+ INVALID\_EMAIL\_ADDRESS\_TARGET: You specified an invalid email address for the invited account owner.
+ INVALID\_END\_DATE: The selected withdrawal date doesn't meet the minimum notice period required by your partner agreement. Visit AWS Partner Central or contact your AWS Channel Partner for help.
+ INVALID\_ENUM: You specified an invalid value.
+ INVALID\_ENUM\_POLICY\_TYPE: You specified an invalid policy type string.
+ INVALID\_FULL\_NAME\_TARGET: You specified a full name that contains invalid characters.
+ INVALID\_LIST\_MEMBER: You provided a list to a parameter that contains at least one invalid value.
+ INVALID\_PAGINATION\_TOKEN: Get the value for the `NextToken` parameter from the response to a previous call of the operation.
+ INVALID\_PARTY\_TYPE\_TARGET: You specified the wrong type of entity (account, organization, or email) as a party.
+ INVALID\_PATTERN: You provided a value that doesn't match the required pattern. The service also validates your free-text field values against common cross-site scripting (XSS) patterns and rejects requests that contain matching values.
+ INVALID\_PATTERN\_TARGET\_ID: You specified a policy target ID that doesn't match the required pattern.
+ INVALID\_PRINCIPAL: You specified an invalid principal element in the policy.
+ INVALID\_ROLE\_NAME: You provided a role name that isn't valid. A role name can't begin with the reserved prefix `AWSServiceRoleFor`.
+ INVALID\_START\_DATE: The start date doesn't meet the minimum requirements.
+ INVALID\_SYNTAX\_ORGANIZATION\_ARN: You specified an invalid Amazon Resource Name (ARN) for the organization.
+ INVALID\_SYNTAX\_POLICY\_ID: You specified an invalid policy ID.
+ INVALID\_SYSTEM\_TAGS\_PARAMETER: You specified a tag key that is a system tag. You can’t add, edit, or delete system tag keys because they're reserved for AWS use. System tags don’t count against your tags per resource limit.
+ MAX\_FILTER\_LIMIT\_EXCEEDED: You can specify only one filter parameter for the operation.
+ MAX\_LENGTH\_EXCEEDED: You provided a string parameter that is longer than allowed.
+ MAX\_VALUE\_EXCEEDED: You provided a numeric parameter that has a larger value than allowed.
+ MIN\_LENGTH\_EXCEEDED: You provided a string parameter that is shorter than allowed.
+ MIN\_VALUE\_EXCEEDED: You provided a numeric parameter that has a smaller value than allowed.
+ MOVING\_ACCOUNT\_BETWEEN\_DIFFERENT\_ROOTS: You can move an account only between entities in the same root.
+ NON\_DETACHABLE\_POLICY: You can't detach this AWS Managed Policy.
+ START\_DATE\_NOT\_BEGINNING\_OF\_DAY: You provided an invalid start date. The start date must be the beginning of the day (00:00:00.000).
+ START\_DATE\_NOT\_BEGINNING\_OF\_MONTH: You provided an invalid start date. The start date must be the first day of the month.
+ START\_DATE\_TOO\_EARLY: You provided an invalid start date. The start date is too early.
+ START\_DATE\_TOO\_LATE: You provided an invalid start date. The start date is too late.
+ TARGET\_NOT\_SUPPORTED: You can't perform the specified operation on that target entity.
+ UNRECOGNIZED\_SERVICE\_PRINCIPAL: You specified a service principal that isn't recognized.
+ UNSUPPORTED\_ACTION\_IN\_RESPONSIBILITY\_TRANSFER: You provided a value that is not supported by this operation.
HTTP Status Code: 400

 ** ServiceException **
 AWS Organizations can't complete your request because of an internal service error. Try again later.
HTTP Status Code: 500

 ** TargetNotFoundException **
We can't find a root, OU, account, or policy with the `TargetId` that you specified.
HTTP Status Code: 400

 ** TooManyRequestsException **
You have sent too many requests in too short a period of time. The quota helps protect against denial-of-service attacks. Try again later.
For information about quotas that affect AWS Organizations, see [Quotas for AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_limits.html) in the * AWS Organizations User Guide*.
HTTP Status Code: 400

 ** UnsupportedAPIEndpointException **
This action isn't available in the current AWS Region.
HTTP Status Code: 400

## See Also
<a name="API_DescribeEffectivePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/organizations-2016-11-28/DescribeEffectivePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/organizations-2016-11-28/DescribeEffectivePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/organizations-2016-11-28/DescribeEffectivePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/organizations-2016-11-28/DescribeEffectivePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/organizations-2016-11-28/DescribeEffectivePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/organizations-2016-11-28/DescribeEffectivePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/organizations-2016-11-28/DescribeEffectivePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/organizations-2016-11-28/DescribeEffectivePolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/organizations-2016-11-28/DescribeEffectivePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/organizations-2016-11-28/DescribeEffectivePolicy)
