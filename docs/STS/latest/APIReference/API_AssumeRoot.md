---
source_url: https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoot.html
---

# AssumeRoot
<a name="API_AssumeRoot"></a>

Returns a set of short term credentials you can use to perform privileged tasks on a member account in your organization. You must use credentials from an AWS Organizations management account or a delegated administrator account for IAM to call `AssumeRoot`. You cannot use root user credentials to make this call.

Before you can launch a privileged session, you must have centralized root access in your organization. For steps to enable this feature, see [Centralize root access for member accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-enable-root-access.html) in the *IAM User Guide*.

**Note**
The AWS STS global endpoint is not supported for AssumeRoot. You must send this request to a Regional AWS STS endpoint. For more information, see [Endpoints](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html#sts-endpoints).

You can track AssumeRoot in AWS CloudTrail logs to determine what actions were performed in a session. For more information, see [Track privileged tasks in AWS CloudTrail](https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-track-privileged-tasks.html) in the *IAM User Guide*.

When granting access to privileged tasks you should only grant the necessary permissions required to perform that task. For more information, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html). In addition, you can use [service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) (SCPs) to manage and limit permissions in your organization. See [General examples](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_general.html) in the * AWS Organizations User Guide* for more information on SCPs.

## Request Parameters
<a name="API_AssumeRoot_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DurationSeconds **
The duration, in seconds, of the privileged session. The value can range from 0 seconds up to the maximum session duration of 900 seconds (15 minutes). If you specify a value higher than this setting, the operation fails.
By default, the value is set to `900` seconds.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 900.
Required: No

 ** TargetPrincipal **
The member account principal ARN or account ID.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 2048.
Required: Yes

 ** TaskPolicyArn **
The identity based policy that scopes the session to the privileged tasks that can be performed. You must use one of following AWS managed policies to scope root session actions:
+  [IAMAuditRootUserCredentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-iam-awsmanpol.html#security-iam-awsmanpol-IAMAuditRootUserCredentials)
+  [IAMCreateRootUserPassword](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-iam-awsmanpol.html#security-iam-awsmanpol-IAMCreateRootUserPassword)
+  [IAMDeleteRootUserCredentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-iam-awsmanpol.html#security-iam-awsmanpol-IAMDeleteRootUserCredentials)
+  [S3UnlockBucketPolicy](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-iam-awsmanpol.html#security-iam-awsmanpol-S3UnlockBucketPolicy)
+  [SQSUnlockQueuePolicy](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-iam-awsmanpol.html#security-iam-awsmanpol-SQSUnlockQueuePolicy)
Type: [PolicyDescriptorType](API_PolicyDescriptorType.md) object
Required: Yes

## Response Elements
<a name="API_AssumeRoot_ResponseElements"></a>

The following elements are returned by the service.

 ** Credentials **
The temporary security credentials, which include an access key ID, a secret access key, and a security token.
The size of the security token that AWS STS API operations return is not fixed. We strongly recommend that you make no assumptions about the maximum size.
Type: [Credentials](API_Credentials.md) object

 ** SourceIdentity **
The source identity specified by the principal that is calling the `AssumeRoot` operation.
You can use the `aws:SourceIdentity` condition key to control access based on the value of source identity. For more information about using source identity, see [Monitor and control actions taken with assumed roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html) in the *IAM User Guide*.
The regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@-
Type: String
Length Constraints: Minimum length of 2. Maximum length of 64.
Pattern: `[\w+=,.@-]*`

## Errors
<a name="API_AssumeRoot_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ExpiredToken **
The web identity token that was passed is expired or is not valid. Get a new identity token from the identity provider and then retry the request.
HTTP Status Code: 400

 ** RegionDisabled **
 AWS STS is not activated in the requested region for the account that is being asked to generate credentials. The account administrator must use the IAM console to activate AWS STS in that region. For more information, see [Activating and Deactivating AWS STS in an AWS Region](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html#sts-regions-activate-deactivate) in the *IAM User Guide*.
HTTP Status Code: 403

## Examples
<a name="API_AssumeRoot_Examples"></a>

### Example
<a name="API_AssumeRoot_Example_1"></a>

This example illustrates one usage of AssumeRoot.

#### Sample Request
<a name="API_AssumeRoot_Example_1_Request"></a>

```
https://sts.amazonaws.com/
?Version=2011-06-15
&Action=AssumeRoot
&DurationSeconds=900
&TargetPrincipal=111122223333
&TaskPolicyArn.arn=arn:aws:iam::aws:policy/root-task/IAMDeleteRootUserCredentials
```

#### Sample Response
<a name="API_AssumeRoot_Example_1_Response"></a>

```
<AssumeRootResponse xmlns="https://sts.amazonaws.com/doc/2011-06-15/">
  <AssumeRootResult>
  <SourceIdentity>Alice</SourceIdentity>
    <Credentials>
      <AccessKeyId>ASIAIOSFODNN7EXAMPLE</AccessKeyId>
      <SecretAccessKey>wJalrXUtnFEMI/K7MDENG/bPxRfiCYzEXAMPLEKEY</SecretAccessKey>
      <SessionToken>
       AQoDYXdzEPT//////////wEXAMPLEtc764bNrC9SAPBSM22wDOk4x4HIZ8j4FZTwdQW
       LWsKWHGBuFqwAeMicRXmxfpSPfIeoIYRqTflfKD8YUuwthAx7mSEI/qkPpKPi/kMcGd
       QrmGdeehM4IC1NtBmUpp2wUE8phUZampKsburEDy0KPkyQDYwT7WZ0wq5VSXDvp75YU
       9HFvlRd8Tx6q6fE8YQcHNVXAkiY9q6d+xo0rKwT38xVqr7ZD0u0iPPkUL64lIZbqBAz
       +scqKmlzm8FDrypNC9Yjc8fPOLn9FX9KSYvKTr4rvx3iSIlTJabIQwj2ICCR/oLxBA==
      </SessionToken>
      <Expiration>2019-11-09T13:34:41Z</Expiration>
    </Credentials>
  </AssumeRoleResult>
  <ResponseMetadata>
    <RequestId>c6104cbe-af31-11e0-8154-cbc7ccf896c7</RequestId>
  </ResponseMetadata>
</AssumeRootResponse>
```

## See Also
<a name="API_AssumeRoot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sts-2011-06-15/AssumeRoot)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sts-2011-06-15/AssumeRoot)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sts-2011-06-15/AssumeRoot)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sts-2011-06-15/AssumeRoot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sts-2011-06-15/AssumeRoot)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sts-2011-06-15/AssumeRoot)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sts-2011-06-15/AssumeRoot)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sts-2011-06-15/AssumeRoot)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sts-2011-06-15/AssumeRoot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sts-2011-06-15/AssumeRoot)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Token Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query STS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
