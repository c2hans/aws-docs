---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/source-profile.html
---

# Using Source Profile for Cross-Account Access
<a name="source-profile"></a>

Source profile enables SAP systems to access AWS resources across multiple accounts by chaining IAM role assumptions. One profile assumes a role, which then assumes another role, and so on, similar to the `source_profile` parameter in AWS CLI. This is useful for cross-account access scenarios where you need to traverse multiple AWS accounts to reach your target resources.

**Example:** Your SAP system runs in Account A (111111111111) and needs to access Amazon S3 buckets in Account C (333333333333). You configure three profiles:

1. `DEV_BASE` gets base credentials from Amazon EC2 instance metadata and assumes Role P in Account A

1. `SHARED_SERVICES` uses `DEV_BASE` credentials to assume Role Q in Account B (222222222222)

1. `PROD_S3_ACCESS` uses `SHARED_SERVICES` credentials to assume Role R in Account C

When your application uses `PROD_S3_ACCESS`, the SDK automatically executes the chain: get credentials from instance metadata → assume Role P → assume Role Q → assume Role R.

## Prerequisites
<a name="source-profile-prerequisites"></a>

The following prerequisites must be met before configuring source profile:
+ IAM roles for each step in the chain must be created by the IAM administrator. Each role must have:
  + Permissions to call the required AWS services
  + Trust relationship configured to allow the previous role in the chain to assume it

  For more information, see [Best practices for IAM Security](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/best-practices.html).
+ Create authorization to run `/AWS1/IMG` transaction. For more information, see [Authorizations for configuration](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/authorizations.html#configuration-authorizations).
+ Users must have `/AWS1/SESS` authorization for ALL profiles in the chain, including intermediate profiles.

## Procedure
<a name="source-profile-procedure"></a>

Follow these instructions to configure source profile.

**Topics**
+ [Step 1 – Configure the base profile](#step1-base-profile)
+ [Step 2 – Configure chained profiles](#step2-chained-profiles)

### Step 1 – Configure the base profile
<a name="step1-base-profile"></a>

The base profile is the first profile in the chain and must use a standard authentication method.

1. Run the `/n/AWS1/IMG` transaction to launch AWS SDK for SAP ABAP Implementation Guide (IMG).

1. Select **AWS SDK for SAP ABAP Settings** > **Application Configurations** > **SDK Profile**.

1. Create a new profile to use as your base profile by selecting **New Entries** and enter profile name and description. Select **Save**.
**Note**
If you are using an existing profile that is already configured with a standard authentication method (INST, SSF, or RLA), you can skip the remaining steps in this section and proceed directly to [Step 2 – Configure chained profiles](#step2-chained-profiles).

1. Select the profile you created, then select **Authentication and Settings** > **New Entries**, and enter the following details:
   + **SID**: The system ID of the SAP system
   + **Client**: The client of the SAP system
   + **Scenario ID**: Select the `DEFAULT` scenario created by your Basis administrator
   + **AWS Region**: AWS Region that you want to make calls to
   + **Authentication Method**: Select one of the following:
     + **Instance Role via Metadata** for SAP systems running on Amazon EC2
     + **Credentials from SSF Storage** for on-premises or other cloud systems
     + **IAM Roles Anywhere** for certificate-based authentication

   Select **Save**.

1. Select **IAM Role Mapping** > **New Entries**, and enter:
   + **Sequence number**: 1
   + **Logical IAM Role**: A descriptive name (e.g., `DEV_BASE_ROLE`)
   + **IAM Role ARN**: The ARN of the IAM role in the first account (e.g., `arn:aws:iam::111111111111:role/DevBaseRole`)

   Select **Save**.

### Step 2 – Configure chained profiles
<a name="step2-chained-profiles"></a>

Configure each intermediate and final profile in the chain.

**For `SHARED_SERVICES` profile (chains from `DEV_BASE`):**

1. Run the `/n/AWS1/IMG` transaction.

1. Select **AWS SDK for SAP ABAP Settings** > **Application Configurations** > **SDK Profile**.

1. Select **New Entries**. Enter profile name (e.g., `SHARED_SERVICES`) and description. Select **Save**.

1. Select the profile you created, then select **Authentication and Settings** > **New Entries** and enter the following details:
   + **SID**: The system ID of the SAP system
   + **Client**: The client of the SAP system
   + **Scenario ID**: Select the `DEFAULT` scenario created by your Basis administrator
   + **AWS Region**: AWS Region that you want to make calls to
   + **Authentication Method**: Select **Source Profile** from the dropdown
   + **Source Profile ID**: Enter the profile ID of the base profile (e.g., `DEV_BASE`)

   Select **Save**.

1. Select **IAM Role Mapping** > **New Entries**, and enter:
   + **Sequence number**: 1
   + **Logical IAM Role**: A descriptive name (e.g., `SHARED_ROLE`)
   + **IAM Role ARN**: `arn:aws:iam::222222222222:role/SharedServicesRole`

   Select **Save**.

**For `PROD_S3_ACCESS` profile (chains from `SHARED_SERVICES`):**

Repeat the same steps as `SHARED_SERVICES`, but:
+ Use `PROD_S3_ACCESS` as the name
+ Set **Source Profile ID** to `SHARED_SERVICES`
+ Use `PROD_S3_ROLE` and `arn:aws:iam::333333333333:role/ProdS3AccessRole` in IAM Role Mapping

For security best practices including IAM role management, trust policy configuration, and authorization requirements, see [Best practices for IAM Security](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/best-practices.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for SAP ABAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-sapabap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
