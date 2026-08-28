---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/releases.html
---

# AWS SDK for SAP ABAP releases
<a name="releases"></a>

AWS SDK for SAP ABAP is delivered in transports, and AWS SDK for SAP ABAP - BTP edition is delivered as add-ons. The mechanism to import transports and add-ons is different but the technical functionality is the same. For more information, see [Setting up](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/setup.html).

**Topics**
+ [Release strategy](#release-strategy)
+ [Best practices](#best-practices)
+ [Patching SDK for SAP ABAP](#patching)
+ [Installing an additional module](#additional-module)
+ [Uninstalling SDK for SAP ABAP](#uninstalling)

## Release strategy
<a name="release-strategy"></a>

Version 1 of AWS SDK for SAP ABAP is updated frequently. New patches are released weekly or daily based on the releases and updates of AWS services. The patches for AWS services can include bug fixes and other changes that update patch level of the SDK. the For more information, see [AWS SDKs and Tools maintenance policy](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html).

## Best practices
<a name="best-practices"></a>

We recommended retaining same patch level of SDK for SAP ABAP for all SAP systems (development, QA, and production).

When patching the SDK, import the latest version in your sandbox. You can then import it to the development, QA,and production systems, following your normal change control procedures.

## Patching SDK for SAP ABAP
<a name="patching"></a>

Each SDK for SAP ABAP release is delivered as a set of cumulative transports, including all bug fixes, features, and updates. There is no difference between a patch and an installation transport. You must import the latest transports to patch SDK for SAP ABAP.

Due to dependencies of `core` Runtime and API modules, individual API modules cannot be patched separately. When patching, you must update the `core` module and all other API modules that have been installed, even if certain modules are no longer in use.

The following scenarios describe the patching process:
+ <a name="sdk-version-update"></a>**Scenario 1: Regular SDK Version Update**

  When patching to the latest SDK version:
  + Import all transports (core and installed API modules) simultaneously
  + No specific import sequence is required
  + For example, if you imported the `core`, `ec2`, and `lmd` transports when you installed the SDK, you must import the latest transports for `core`, `ec2`, and `lmd` when patching.
+ **Scenario 2: Adding a New API Module**

  When importing a new API module (e.g., Amazon Textract `tex`) from a different SDK release than your currently installed modules:
  + All existing modules must be patched to match the SDK release version of the new module
  + Import simultaneously (no specific sequence):
    + Latest transports for all existing modules (`core` and installed API modules)
    + Transports for the new API module `tex`
+ **Scenario 3: Updating an Existing API Module**

  When updating an existing API module (e.g., Amazon Translate `xl8`) to the latest SDK version, individual module updates are not supported due to interdependencies. You must patch the entire SDK by updating the `core` module and all installed API modules together, following the process outlined in [Regular SDK Version Update](#sdk-version-update).

## Installing an additional module
<a name="additional-module"></a>

Import the transport for the new module at the same patch level as your existing `core` and modules to install an additional API module in your SAP system. Follow the guidelines in [Patching SDK for SAP ABAP](#patching) if you want to import a more recent version of the module. This ensures that the patch levels are compatible across all SDK modules.

## Uninstalling SDK for SAP ABAP
<a name="uninstalling"></a>

To uninstall SDK for SAP ABAP, you must download a *deletion transports* kit from [https://sdk-for-sapabap.aws.amazon.com/awsSdkSapabapV1/release/uninstall-abapsdk-LATEST.zip](https://sdk-for-sapabap.aws.amazon.com/awsSdkSapabapV1/release/uninstall-abapsdk-LATEST.zip).

```
curl "https://sdk-for-sapabap.aws.amazon.com/awsSdkSapabapV1/release/uninstall-abapsdk-LATEST.zip" -o "uninstall-abapsdk-LATEST.zip"
```

You can download a signature file from [https://sdk-for-sapabap.aws.amazon.com/awsSdkSapabapV1/release/uninstall-abapsdk-LATEST.sig](https://sdk-for-sapabap.aws.amazon.com/awsSdkSapabapV1/release/uninstall-abapsdk-LATEST.sig). To validate the file, see [Verify SDK for SAP ABAP](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/installation.html#verification).

For each SDK module installed on your SAP system, the corresponding *deletion transport* must be imported from the preceding ZIP file. You can remove a single module without uninstalling the entire SDK. You can do so by importing only the *deletion transport* for module you want to remove. If you are uninstalling the entire SDK with all of its modules, then the *core deletion transport* must be imported last.

We recommend that you test the uninstallation in a sandbox before attempting in development, QA or production systems.

**Considerations**

Before uninstalling the SDK, see the following considerations.
+ SDK configuration settings from will be lost. The `IMG` must be reconfigured on installation.
+ If you have Z programs that rely on the SDK, they will generate syntax errors after the removal of the SDK.
+ PFCG or Business roles containing SDK authorization references will have invalid authorizations after the removal of the SDK. Remove SDK authorization references from the PFCG roles before uninstalling the SDK.

**Note**
AWS SDK for SAP ABAP - BTP edition cannot be uninstalled during the developer preview.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for SAP ABAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-sapabap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
