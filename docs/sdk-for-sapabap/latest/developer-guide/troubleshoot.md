---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/troubleshoot.html
---

# Troubleshoot AWS SDK for SAP ABAP
<a name="troubleshoot"></a>

This section provides troubleshooting steps for possible error scenarios.

**Topics**
+ [Import failure](#import-failure)
+ [Unspecified location constraint](#unspecified-constraint)
+ [SSL errors](#ssl-error)
+ [Profile configuration](#profile-configuration)
+ [IAM authorization](#iam-authorization)
+ [Authorization for performing required actions](#action-authorization)
+ [Active scenario](#active-scenario)
+ [Special characters in code](#special-characters)
+ [Connectivity](#connectivity)

## Import failure
<a name="import-failure"></a>

**Problem** – Class ‘CL\_SYSTEM\_UUID’ doesn't contain an interface ‘IF\_SYSTEM\_UUID\_RFC4122\_STATIC

**Cause** – SAP Note 0002619546 is missing on your system.

**Resolution** – Ensure that the [SAP Note 0002619546](https://launchpad.support.sap.com/#/notes/0002619546) is applied to your system.

## Unspecified location constraint
<a name="unspecified-constraint"></a>

**Problem** – The unspecified location constraint is incompatible for the `region` specific endpoint this request was sent to

**Cause** – Your Amazon S3 bucket is missing the AWS Region in `io_createbucketconfiguration` parameter.

**Resolution** – When creating a bucket in any Region, except `us-east-1`, specify your Amazon S3 bucket's Region using `io_createbucketconfiguration` parameter in `createbucket()`. You don't have to specify a constraint for `us-east-1`.

The following example shows a correctly configured `io_createbucketconfiguration` parameter.

```
createbucket(
    iv_bucket = 'amzn-s3-demo-bucket'
    io_createbucketconfiguration = NEW /aws1/cl_s3_createbucketconf( 'us-west-1' )
).
```

## SSL errors
<a name="ssl-error"></a>

**Problem** – SSL Server Certificate Hostname Mismatch *or* SSL handshake with docs.aws.amazon.com:443 failed: SSSLERR\_NO\_SSL\_RESPONSE

**Cause** – `icm/HTTPS/client_sni_enabled` parameter is not set to `TRUE` in the `DEFAULT` profile.

**Resolution** – Use the following steps to troubleshoot the given problems or any other SSL-related problem.

1. Open the SAPGUI and go to the command bar.

1. Run transaction `RZ10`.

1. Go to **Profile** and choose `DEFAULT` profile. The version is populated automatically.

1. In the **Edit Profile** section, select **Extended maintenance**, and then select **Change**.

1. Search for the `icm/HTTPS/client_sni_enabled` parameter.
   + If the parameter exists, edit the **Parameter value** and set it to `TRUE`.
   + If the parameter doesn't exist, create a parameter using the following steps.

     1. Select **Parameter**.
**Note**
Ensure that you are selecting the Parameter for creation, and not editing (pencil icon).

     1. Enter `icm/HTTPS/client_sni_enabled` in the **Parameter Name** field.

     1. Enter `TRUE` in the **Parameter value** field.

     1. Select **Save**.

1. Save these changes in the `DEFAULT` profile, and Exit.

## Profile configuration
<a name="profile-configuration"></a>

**Problem** – Could not find configuration under profile <profile\_name> with scenario DEFAULT for <sid>:<client>

**Causes** – The <profile\_name> is incorrect or hasn't been configured.

**Resolution** – Use the following steps to configure the profile.

1. Open SAPGUI and run transaction `/n/AWS1/IMG`.

1. Go to **Application Configuration** > **SDK Profile**.
   + If your profile is configured, verify that the profile name is correct.
   + If your profile is not configured, follow along the steps to configure a profile.

1. Select **New Entries**.

   1. Enter a Name and Description for the profile.

   1. Select **Save**.

1. Choose the entry you created in the previous step, and then select **Authentication and Settings**.

1. Select **New Entries**, enter the following details, and then select **Save**.
   + SID
   + Client
   + Scenario ID
   + AWS Region
   + Authentication Method
     + Select *Instance Role via Metadata* for SAP systems running in AWS.
     + Select *Credentials from SSF Storage* for SAP systems running on-premises or other cloud.

1. Select **IAM Role Mapping** > **New Entries**, enter the following details, and select **Save**.
   + Sequence number
   + Logical IAM Role
   + IAM Role ARN

## IAM authorization
<a name="iam-authorization"></a>

**Problem** – Could not assume role <iam\_role\_arn> or User: <user\_arn> is not authorized to perform: sts:AssumeRole on resource:<iam\_role\_arn>

**Causes** – the following may be the possible reasons for this error.
+ Incorrect IAM role ARN has been specified
+ IAM user lacks permission to access the IAM role
+ Lack of trust relationship between the assumed IAM role and the assuming IAM role or IAM user

**Resolution** – Use the following steps to ensure that the IAM role ARN is correct.

1. Open SAPGUI and run transaction `/n/AWS1/IMG`.

1. Go to **Application Configuration** > **SDK Profile**, and choose the profile that has been configured with your IAM role.

1. Select **IAM Role Mapping** and verify or correct your IAM role ARN.

   1. If your IAM role ARN is correct, ensure that your IAM role has been configured properly. For more information, see [Troubleshooting IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_roles.html#troubleshoot_roles_cant-assume-role).

## Authorization for performing required actions
<a name="action-authorization"></a>

**Problem** – User <user\_arn> is not authorized to perform: <action> on resource: <resource\_arn>

**Cause** – User does not have permissions to perform an action.

**Resolution** – `user_arn` must be set up with required permissions on `resource_arn` to perform a specified `action`. For more information, see [Permissions required to access IAM resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_permissions-required.html).

## Active scenario
<a name="active-scenario"></a>

**Problem** – No active scenario configured

**Cause** – The setup of active scenario was missed.

**Resolution** – See [Runtime settings](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/runtime-settings.html) to configure an active scenario.

## Special characters in code
<a name="special-characters"></a>

**Warning** – The character 0x00A0 cannot be part of an ABAP word

**Note**
This warning may be preceded by varied error messages.

**Cause** – Copying and pasting code from different sources can insert special characters in your code.

**Resolution** – When you paste any code in the ABAP source code editor, you see the following pop-up.

*Non-breaking space characters were detected. Convert to spaces?*

Choose **Yes** to answer this question. Also, we recommend selecting the code to copy it, instead of using the copy button in code boxes.

## Connectivity
<a name="connectivity"></a>

**Problem** – SCLNT\_HTTP(411) : Direct connect to tla.region.amazonaws.com:443 failed: NIECONN\_REFUSED(-10)

**Cause** – The SAP system does not have internet connectivity, and cannot establish a TCP/IP connection to port 443 of tla.region.amazonaws.com.

**Resolution** – The SAP system must be able to establish connection to AWS endpoints on HTTPS port 443, either directly or through a proxy server. You can establish/verify internet connectivity with one of the following options.
+ Direct outbound connection to internet through a NAT or internet gateway
+ Connection through a proxy server

  For more information, see [Connection through a proxy server](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/connectivity-scenarios.html#proxy-server).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for SAP ABAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-sapabap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
