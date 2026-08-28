---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/getting-started.html
---

# Getting started with AWS SDK for SAP ABAP
<a name="getting-started"></a>

This section describes how to get started with the SDK. It includes information about installing the SDK, performing basic configuration, and creating a Hello World code example that translates a phrase from one language to another. If you are new to AWS SDK, we recommend performing these steps in a sandbox environment.

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [Step 1: Prepare your AWS account](#prepare-account)
+ [Step 2: Install the SDK](#installation-sdk)
+ [Step 3: Configure the SDK](#configure)
+ [Step 4: Functional setup](#functional-setup)
+ [Step 5: Authorize SAP Users](#authorize-users)
+ [Step 6: Write the code](#write-code)
+ [Step 7: Run the application](#run-application)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Step 1: Prepare your AWS account
<a name="prepare-account"></a>

To get started with SDK for SAP ABAP, you must have an active AWS account . You need an AWS account even if your SAP system is hosted on-premises, on SAP Business Technology Platform (BTP) or with another cloud provider.

If your SAP system is running on AWS Cloud, then you will be making calls to AWS services in your AWS account.

**Topics**
+ [IAM role for SAP users](#iamrole)
+ [Authentication](#authentication)

### IAM role for SAP users
<a name="iamrole"></a>
+ Create an IAM role with the instructions provided in the *AWS Identity and Access Management User Guide*. For more information, see [Creating a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html). Note the Amazon Resource Name (ARN) of the IAM role for later use.
+ Select Amazon EC2 as the use case.
+ Use `SapDemoTranslate` as the name of the role.
+ Attach `TranslateReadOnly` profile to the role.
+ The role must have the following entities to enable the SAP system to assume the role. Replace `{{"111122223333"}}` with your AWS account number.

------
#### [ JSON ]

****

  ```
  {
      "Version":"2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": [
                  "sts:AssumeRole"
              ],
              "Principal": {
                  "AWS": "{{111122223333}}"
              }
          }
      ]
  }
  ```

------

  This example shows that any principal from the AWS account `{{"111122223333"}}` can assume the role. This is a broad permission that is suitable for proof-of-concept. You can use a narrower principal for production, such as the following examples.
  + A specific user – when the SAP system is using either one of the following:
    + SSF-encrypted credentials from an on-premises SAP system
    + Credentials from SAP Credential Store service on SAP BTP, ABAP environment
  + A specific role – when the SAP system is on Amazon EC2 and there is an instance profile.
  + Amazon EC2 – when the SAP system is on Amazon EC2 and there is *no* instance profile.

For more information, see [Best practices for IAM Security](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/best-practices.html).

### Authentication
<a name="authentication"></a>

Authentication depends on where your SAP system is hosted.

**Topics**
+ [On AWS Cloud](#aws-cloud)
+ [On-premises, SAP BTP or other cloud](#on-premises-other)

#### On AWS Cloud
<a name="aws-cloud"></a>

Ensure that the EC2 instance on which your SAP system is running has an instance profile with the following permissions.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Resource": "{{arn:aws:iam::111122223333:role/SapDemoTranslate}}"
        }
    ]
}
```

------

Add the ARN that you noted in the previous step.

This permission enables your SAP system to assume the `SapDemoTranslate` role on behalf of the ABAP user.

#### On-premises, SAP BTP or other cloud
<a name="on-premises-other"></a>

If your SAP system is located on-premises, on SAP BTP or on other cloud, use the following steps to establish a connection for authentication using secret access key.

1. Create an IAM user. For more information, see [Creating IAM users (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console).

1. Use `SapDemoSID` as the name of the IAM user. `SID` is the system ID of your SAP system.

1. Assign `SapDemoTranslate` role to this user.

Retain the `access_key` and `secret_access_key`. You must configure these credentials in your SAP system.

**Note**
If your SAP system is located on-premises, on SAP BTP or on other cloud, you can authenticate using one of the following options.
[Secret access key authentication](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/system-authentication.html#key-authentication) using SSF or SAP Credential Store
[Using certificates with IAM Roles Anywhere](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/using-iam.html)

## Step 2: Install the SDK
<a name="installation-sdk"></a>

See the following tabs for installation instructions.

------
#### [ SDK for SAP ABAP ]

Import SDK for SAP ABAP transports in your SAP system. You can import the transports into any client. For more information, see [Installing SDK for SAP ABAP](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/installation.html).

------
#### [ SDK for SAP ABAP - BTP edition ]

Install SDK for SAP ABAP - BTP edition using the **Deploy Product** application. For more information, see [Installing SDK for SAP ABAP - BTP edition](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/installation-btp.html).

------

## Step 3: Configure the SDK
<a name="configure"></a>

Before configuring the SDK, ensure that you have the required authorizations. For more information, see [SAP authorizations](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/authorizations.html).

See the following tabs for configuration instructions.

------
#### [ SDK for SAP ABAP ]

Run the `/AWS1/IMG` transaction to open the Implementation Guide for SDK for SAP ABAP. To run this transaction, enter `/n/AWS1/IMG ` in the command bar of your SAP system, and then choose **Enter**.

Complete the following configurations.
+ Go to **Technical Prerequisites**.
  + Review the recommended [Parameters](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/prerequisites.html#parameters) and [HTTPS connectivity](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/prerequisites.html#https-connectivity).
+ Go to **Global Settings** → **Configure Scenarios**.
  + Change the settings, according to the recommendations in [Global settings](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/global-settings.html).
+ Go to **Global Settings** → **Technical Settings**.
  + Change the settings, according to the recommendations in [Global settings](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/global-settings.html).
+ Go to **Runtime Settings** → **Log And Trace**.
  + Select **New Entries**.
    + **Trace level**: No Trace.
    + **Maximum Dump Lines**: `100`.
    + **OPT-IN: enh telemetry**: Keep this blank.
  + Select **Save**.
+ Go to **Runtime Settings** → **Active Scenario**.
  + Under **New Scenario**, select `DEFAULT`.
  + Select **Commit Scenario Change**.
  + Accept the prompt.

 **Prerequisites for On-Premises Systems**

If your SAP system is running on-premises or in another cloud, then the credentials must be stored in your SAP database. The credentials are encrypted using SAP SSF and require a configured cryptographic library, such as SAP’s CommonCryptoLib.

The steps for configuring SSF for SDK for SAP ABAP are described in the `/AWS1/IMG` transaction.

**Note**
 The preceding prerequisite does not apply if your SAP system is running on Amazon EC2. SAP systems running on Amazon EC2 retrieve short-lived, automatically rotating credentials from the Amazon EC2 instance metadata.

------
#### [ SDK for SAP ABAP - BTP edition ]

Open your ABAP environment in a web browser, and navigate to the Custom Business Configurations application.

Complete the following configurations.
+ Go to **Configure Scenarios**.
  + Change the settings, according to the recommendations in [Global settings](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/global-settings.html).
+ Go to **Technical Settings**.
  + Change the settings, according to the recommendations in [Global settings](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/global-settings.html).

------

## Step 4: Functional setup
<a name="functional-setup"></a>

See the following tabs for setup instructions.

------
#### [ SDK for SAP ABAP ]

Run transaction `/AWS1/IMG` (enter `/n/AWS1/IMG` in the command bar, and choose **Enter**) to open the implementation guide for AWS SDK.
+ Go to **Application Configuration** → **SDK Profile**.
  + Select **New Entries**.
    + **Profile**: `DEMO`.
    + **Description**: `Demo profile`.
    + Select **Save**.
+ Highlight the entry that you created and click on the **Authentication And Settings** tree branch.
  + Select **New Entries**.
    + **SID**: The system ID of the SAP system that you are currently in.
    + **Client**: The client of the SAP system that you are currently in.
    + **Scenario ID**: The dropdown list where you'll find the DEFAULT scenario created by your Basis administrator.
    + **AWS Region**: enter the AWS Region that you want to make calls to. If your SAP system is running in AWS, enter the AWS Region that it is running in.
    + Authentication Method:
      + Select **Instance Role via Metadata** if your SAP system is running on Amazon EC2.
      + Select **Credentials from SSF Storage** if your SAP system is running on-premises or in another cloud.
        + Select **Set Credentials**.
        + Enter the Access Key ID and Secret Access Key that you created in the previous step.
  + Keep **Disable IAM roles** blank.
  + Select **Save**.
+ Click on the **IAM Role Mapping **tree branch.
  + Select **New Entries**.
    + Enter **Sequence number**: 010.
    + Enter **Logical IAM role**: TESTUSER.
    + Enter **IAM Role ARN**: enter the arn:aws: of the IAM role containing the `TranslateReadOnly` policy created in the previous step.

------
#### [ SDK for SAP ABAP - BTP edition ]

Set up authentication using SAP Credential Store. For more information, see [Using SAP Credential Store](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/credential-store.html).

Open your ABAP environment in a web browser, and navigate to the Custom Business Configurations application.
+ Go to **SDK Profile**.
  + Select **Edit** to create a new profile.
    + **Profile**: `DEMO`.
    + **Description**: `Demo profile`.
+ Select the right arrow key next to the created entry to navigate to **Authentication and Settings** tab.

  Select **New Entries**.
  + **SID**: The system ID of the SAP system that you are currently in.
  + **Client**: The client of the SAP system that you are currently in.
  + **Scenario ID**: The dropdown list where you'll find the DEFAULT scenario created by your Basis administrator.
  + **AWS Region**: enter the AWS Region that you want to make calls to. If your SAP system is running in AWS, enter the AWS Region that it is running in.
  + Authentication Method: Select **Credentials from SAP Credential Store**.
  + Enter the **Namespace** and **Key name** of the credentials stored in SAP Credentials Store.
  + Enter the name of the **Communication Arrangement** created to establish communication between SDK for SAP ABAP - BTP edition and SAP Credential Store.
  + Keep **Disable IAM roles** blank.
+ Right-click on the right arrow key next to the created entry to navigate to **IAM Role Mapping ** tab.

  Select **New Entries**.
  + Enter **Sequence number**: 010.
  + Enter **Logical IAM role**: TESTUSER.
  + Enter **IAM Role ARN**: enter the arn:aws: of the IAM role containing the `TranslateReadOnly` policy created in the previous step.

------

## Step 5: Authorize SAP Users
<a name="authorize-users"></a>

SAP users are not authorized to use AWS functionality by default. The users must be explicitly authorized using SAP authorizations. See the following tabs for more details.

------
#### [ SDK for SAP ABAP ]

**Create a PFCG role**
+ Go to transaction `PFCG`
+ Enter the role name `ZAWS_SDK_DEMO_TESTUSER` and select **Create Single Role**.
  + **Description**: `Role for demo AWS SDK functionality`.
  + Go to the **Authorizations** tab.
  + Select **Change Authorization Data** and accept the informational pop-up.
  + At the *Choose Template* pop-up, select **Do not select templates**.
  + Select **Add Manually** from the toolbar.
  +  Add the following authorization objects:
    +  `/AWS1/LROL`
    +  `/AWS1/SESS`
  +  In the authorization tree, enter:
    +  Profile for accessing AWS APIs: `DEMO`
    +  Logical IAM Role: `TESTUSER`
  + Select **Save**.
  + Select **Generate**.
  + Select **Back**.
  + Select **Save** to save the role.

**Assign the PFCG role to SAP users**

Any user who has the `ZAWS_SDK_DEMO_TESTUSER` role assigned will be authorized to use AWS SDK functions with the settings configured in `DEMO` SDK profile. The authorized user will also assume the IAM role mapped to the `TESTUSER` logical IAM role in that profile.
+ Run transaction `SU01`.
  + Enter the user ID of an SAP user who will be testing AWS SDK functionality.
  + Select **Change**.
  + Go to the **Roles** tab and assign `ZAWS_SDK_DEMO_TESTUSER` role to the user.
  + Select **Save**.

------
#### [ SDK for SAP ABAP - BTP edition ]

**Create a Business role**
+ Open your ABAP environment in a web browser, and navigate to the **Maintain Business Roles** application.
+ Select **Create from Template**, and enter the following details.
  + **Template** – Choose `/AWS1/RT_BTP_ENDUSER`.
  + **New Business Role ID** – Enter an ID.
  + **New Business Role Description** – Enter a description.
+ Select **OK** to see the page for the business role.
+ Under **General Role Details** tab, go to **Access Categories**, and set the **Write, Read, Value Help** field as **Restricted**.
+ Select **Maintain Restrictions**, and expand **Assigned Restriction Types** from the left navigation pane. Update the following field in the **Restrictions and Values** section.
  + Under **Choose SDK Session**, select the pencil icon next to **SDK Profile**, and navigate to the **Ranges** tab. Enter `DEMO`, and select **Add**.
  + Under **Choose Logical IAM Role**, select the pencil icon next to **Logical IAM Role**, and navigate to the **Ranges** tab. Enter `TESTUSER`, and select **Add**.

    Select the pencil icon next to **SDK Profile**, and navigate to the **Ranges** tab. Enter `DEMO`, and select **Add**
+ Navigate back to the Business Role template, and open the **Business Users** tab. Select **Add** to assign the newly created Business Role to an SAP business user who will test the SDK functionality. Select **Save**.

Any business user assigned to the created Business Role will be authorized to use AWS SDK functions with the settings configured in `DEMO` SDK profile. The authorized user will also assume the IAM role mapped to the `TESTUSER` logical IAM role in that profile.

------

## Step 6: Write the code
<a name="write-code"></a>

See the following tabs for more details.

------
#### [ SDK for SAP ABAP ]

1. Open transaction `SE38`.
   + Enter `ZDEMO_TRANSLATE_HELLO_WORLD` as the program name.
   + Select `Create`.
   + Enter `AWS SDK Hello World In Any Language` as the title.
   + Type: choose **Executable Program**.
   + Status: choose **Test Program**.
   + Select **Save**.
   + Save the program as a **Local Object**.

**Add the following code**.

```
*&---------------------------------------------------------------------*
*& Report  ZAWS1_DEMO_XL8_SIMPLE
*&
*&---------------------------------------------------------------------*
*& A simple demo of language translation with AWS Translate
*&
*&---------------------------------------------------------------------*
REPORT zaws1_demo_xl8_simple.

START-OF-SELECTION.
  PARAMETERS pv_text TYPE /aws1/xl8boundedlengthstring DEFAULT 'Hello, World' OBLIGATORY.

  PARAMETERS pv_lang1 TYPE languageiso DEFAULT 'EN' OBLIGATORY.
  PARAMETERS pv_lang2 TYPE languageiso DEFAULT 'ES' OBLIGATORY.

  TRY.
      DATA(go_session) = /aws1/cl_rt_session_aws=>create( 'DEMO' ).
      DATA(go_xl8)     = /aws1/cl_xl8_factory=>create( go_session ).
      DATA(lo_output) = go_xl8->translatetext(
           iv_text               = pv_text
           iv_sourcelanguagecode = CONV /aws1/xl8languagecodestring( pv_lang1 )
           iv_targetlanguagecode = CONV /aws1/xl8languagecodestring( pv_lang2 )
      ).

      WRITE: / 'Source Phrase: ', pv_text.
      WRITE: / 'Target Phrase: ', lo_output->get_translatedtext( ).
    CATCH /aws1/cx_xl8unsuppedlanguage00 INTO DATA(lo_lang).
      WRITE: / 'ERROR' COLOR COL_NEGATIVE,
               'Cannot translate from',
               lo_lang->sourcelanguagecode,
               'to',
               lo_lang->targetlanguagecode.
    CATCH cx_root INTO DATA(lo_root).
      WRITE: / 'ERROR' COLOR COL_NEGATIVE, lo_root->get_text( ).
  ENDTRY.
```

------
#### [ SDK for SAP ABAP - BTP edition ]

1. Right-click on the package where the ABAP class needs to be created, then select **New** > **ABAP class**.

1. Enter `ZCL_DEMO_XL8_SIMPLE` for Class name, and add a Class description. Select **Next**.

1. Create or choose a transport request. Select **Finish**.

**Add the following code**.

```
CLASS zcl_demo_xl8_simple DEFINITION
  PUBLIC
  FINAL
  CREATE PUBLIC .

  PUBLIC SECTION.
    INTERFACES if_oo_adt_classrun.
  PROTECTED SECTION.
  PRIVATE SECTION.
ENDCLASS.

CLASS zcl_demo_xl8_simple IMPLEMENTATION.
  METHOD if_oo_adt_classrun~main.

    TRY.
        " input parameters
        DATA(pv_text) = |Hello, World|.
        DATA(pv_lang1) = |EN|.
        DATA(pv_lang2) = |ES|.

        DATA(go_session) = /aws1/cl_rt_session_aws=>create( 'DEMO' ).
        DATA(go_xl8)     = /aws1/cl_xl8_factory=>create( go_session ).
        DATA(lo_output) = go_xl8->translatetext(
             iv_text               = pv_text
             iv_sourcelanguagecode = pv_lang1
             iv_targetlanguagecode = pv_lang2
        ).

        out->write( |Source Phrase: { pv_text }| ).
        out->write( |Target Phrase: { lo_output->get_translatedtext( ) }| ).
      CATCH /aws1/cx_xl8unsuppedlanguage00 INTO DATA(lo_lang).
        out->write( |ERROR - Cannot translate from { lo_lang->sourcelanguagecode } to { lo_lang->targetlanguagecode }| ).
      CATCH cx_root INTO DATA(lo_root).
        out->write( |ERROR - { lo_root->get_text( ) }| ).
    ENDTRY.
  ENDMETHOD.
ENDCLASS.
```

------

For details on how to write ABAP code that uses the SDK, see [Using AWS SDK for SAP ABAP](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/using-sdk.html).

## Step 7: Run the application
<a name="run-application"></a>

See the following tabs for more details.

------
#### [ SDK for SAP ABAP ]

Run the application in `SE38`. If successful, the following will be your output.

```
Source Phrase: Hello, World
Target Phrase: Hola, mundo
```

If you are missing authorizations, configuration, or Basis prerequisites, you might get an error message. See the following example.

```
ERROR Could not find configuration under profile DEMO with
scenario DEFAULT for SBX:001
```

If your SAP role authorizes you to use an SDK profile and map it to a logical IAM role while your IAM permissions are not configured for the SAP system to assume the IAM role, the following will be your output.

```
ERROR Could not assume role {{arn:aws:iam::111122223333:role/SapDemoTranslate}}
```

In this case, review your IAM permissions and trust configuration on the IAM roles, users, or both defined in [Step 1: Prepare your AWS account](#prepare-account).

------
#### [ SDK for SAP ABAP - BTP edition ]

Run the application on **Eclipse** > **Run As** > **ABAP Application (Console)**. If successful, the following will be your output.

```
Source Phrase: Hello, World
Target Phrase: Hola, mundo
```

If you are missing authorizations, configuration, or Basis prerequisites, you might get an error message. See the following example.

```
ERROR Could not find configuration under profile DEMO with
scenario DEFAULT for SBX:001
```

If your SAP role authorizes you to use an SDK profile and map it to a logical IAM role while your IAM permissions are not configured for the SAP system to assume the IAM role, the following will be your output.

```
ERROR Could not assume role {{arn:aws:iam::111122223333:role/SapDemoTranslate}}
```

In this case, review your IAM permissions and trust configuration on the IAM roles, users, or both defined in [Step 1: Prepare your AWS account](#prepare-account).

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for SAP ABAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-sapabap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
