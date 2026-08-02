---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/authorizations.html
---

# SAP authorizations
<a name="authorizations"></a>

The authorization required to configure the SDK is dependent on the SDK edition.

**Topics**
+ [Authorizations for configuration](#configuration-authorizations)
+ [SAP authorizations for end users](#user-authorizations)

## Authorizations for configuration
<a name="configuration-authorizations"></a>

See the following tabs for more details.

------
#### [ SDK for SAP ABAP ]

The following authorizations are required to configure SDK for SAP ABAP.
+ S\_`TCODE`
  +  `TCD` = `/AWS1/IMG`
+ `S_TABU_DIS`
  +  `ACTVT` = `02`, `03`
  + `DICBERCLS`

**Choose from the following authorization groups.**
    + `/AWS1/CFG` - AWS SDK for SAP ABAP v1 - Config
    + `/AWS1/MOD` - AWS SDK for SAP ABAP v1 - Runtime
    + `/AWS1/PFL` - AWS SDK for SAP ABAP v1 - SDK Profile
    + `/AWS1/RES` - AWS SDK for SAP ABAP v1 - Logical Resources
    + `/AWS1/TRC` - AWS SDK for SAP ABAP v1 - Trace

------
#### [ SDK for SAP ABAP - BTP edition ]

Use the following steps to allow SDK for SAP ABAP - BTP edition access to the configuration.

1. Create a new business role using the `SAP_BR_BPC_EXPERT` business role template. This template provides access to the Cutsom Business Configuration application.

1. Under **General Role Details**, go to **Access Categories**, and choose **Unrestricted** for *Read, Write, Value Help*.

1. Go to the **Business Catalog** tab, and assign the `/AWS1/RTBTP_BCAT` business catalog to provide access to the SDK configuration.

1. Go to the **Business Users** tab, and assign business users to grant access to the SDK configuration.

------

## SAP authorizations for end users
<a name="user-authorizations"></a>

 **Prerequisite: Define SDK Profiles**

Before the SAP security administrator can define their roles, the Business Analyst will define SDK profiles in transaction `/AWS1/IMG` for AWS SDK for SAP ABAP or the Custom Business Configuration application for SDK for SAP ABAP - BTP edition. Typically, an SDK profile will be named according to its business function: ZFINANCE, ZBILLING, ZMFG, ZPAYROLL, etc. For each SDK profile, the Business Analyst will define logical IAM roles with short names, such as CFO, AUDITOR, REPORTING. These will be mapped to the real IAM roles by the IAM security administrator.

 **Define PFCG or Business Roles**

**Note**
PFCG roles are called Business Roles in SAP BTP, ABAP environment.

The SAP security administrator will then add authorization object `/AWS1/SESS` to grant access to an SDK profile.

Auth Object `/AWS1/SESS`
+ Field `/AWS1/PROF` = `ZFINANCE`

Users should also be mapped to logical IAM roles for each SDK profile, depending on their job function. For example, a financial auditor with reporting access might be authorized for a logical IAM role called `AUDITOR`.

Auth Object `/AWS1/LROL`
+  Field `/AWS1/PROF` = `ZFINANCE`
+  Field `/AWS1/LROL` = `AUDITOR`

Meanwhile, the CFO, with read/write authorizations, might have a PFCG role authorizing them the logical role of `CFO`.

Auth Object `/AWS1/LROL`
+ Field `/AWS1/PROF` = `ZFINANCE`
+ Field `/AWS1/LROL` = `CFO`

In general, a user should be authorized for only one logical IAM role per SDK profile. If a user is authorized for more than one IAM role (for example, if the CFO is authorized for both `CFO` and `AUDITOR` logical IAM roles), then AWS SDK breaks the tie by ensuring that the higher priority (lower sequence number) role takes effect.

As with all security scenarios, users should be given least privilege to perform their job functions. A simple strategy for managing PFCG roles would be to name Single PFCG roles according to the SDK profile and logical role they authorize. For example, role `Z_AWS_PFL_ZFINANCE_CFO` grants access to profile `ZFINANCE` and logical IAM role `CFO`. These single roles can then be assigned to composite roles that define job functions. Each company has their own strategy for role management, and we encourage you to define a PFCG strategy that works for you.
