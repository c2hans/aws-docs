---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_Component.html
---

# Component
<a name="API_Component"></a>

The SAP component of your application.

## Contents
<a name="API_Component_Contents"></a>

 ** ApplicationId **   <a name="ssmsap-Type-Component-ApplicationId"></a>
The ID of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Pattern: `[\w\d\.-]+`
Required: No

 ** Arn **   <a name="ssmsap-Type-Component-Arn"></a>
The Amazon Resource Name (ARN) of the component.
Type: String
Pattern: `arn:(.+:){2,4}.+$|^arn:(.+:){1,3}.+\/.+`
Required: No

 ** AssociatedHost **   <a name="ssmsap-Type-Component-AssociatedHost"></a>
The associated host of the component.
Type: [AssociatedHost](API_AssociatedHost.md) object
Required: No

 ** ChildComponents **   <a name="ssmsap-Type-Component-ChildComponents"></a>
The child components of a highly available environment. For example, in a highly available SAP on AWS workload, the child component consists of the primary and secondar instances.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\d-]+`
Required: No

 ** ComponentId **   <a name="ssmsap-Type-Component-ComponentId"></a>
The ID of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\d-]+`
Required: No

 ** ComponentType **   <a name="ssmsap-Type-Component-ComponentType"></a>
The type of the component.
Type: String
Valid Values: `HANA | HANA_NODE | ABAP | ASCS | DIALOG | WEBDISP | WD | ERS`
Required: No

 ** DatabaseConnection **   <a name="ssmsap-Type-Component-DatabaseConnection"></a>
The connection specifications for the database of the component.
Type: [DatabaseConnection](API_DatabaseConnection.md) object
Required: No

 ** Databases **   <a name="ssmsap-Type-Component-Databases"></a>
The SAP HANA databases of the component.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `.*[\w\d]+`
Required: No

 ** HdbVersion **   <a name="ssmsap-Type-Component-HdbVersion"></a>
The SAP HANA version of the component.
Type: String
Required: No

 ** Hosts **   <a name="ssmsap-Type-Component-Hosts"></a>
 *This member has been deprecated.*
The hosts of the component.
Type: Array of [Host](API_Host.md) objects
Required: No

 ** LastUpdated **   <a name="ssmsap-Type-Component-LastUpdated"></a>
The time at which the component was last updated.
Type: Timestamp
Required: No

 ** ParentComponent **   <a name="ssmsap-Type-Component-ParentComponent"></a>
The parent component of a highly available environment. For example, in a highly available SAP on AWS workload, the parent component consists of the entire setup, including the child components.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\d-]+`
Required: No

 ** PrimaryHost **   <a name="ssmsap-Type-Component-PrimaryHost"></a>
 *This member has been deprecated.*
The primary host of the component.
Type: String
Required: No

 ** Resilience **   <a name="ssmsap-Type-Component-Resilience"></a>
Details of the SAP HANA system replication for the component.
Type: [Resilience](API_Resilience.md) object
Required: No

 ** SapFeature **   <a name="ssmsap-Type-Component-SapFeature"></a>
The SAP feature of the component.
Type: String
Required: No

 ** SapHostname **   <a name="ssmsap-Type-Component-SapHostname"></a>
The hostname of the component.
Type: String
Required: No

 ** SapKernelVersion **   <a name="ssmsap-Type-Component-SapKernelVersion"></a>
The kernel version of the component.
Type: String
Required: No

 ** Sid **   <a name="ssmsap-Type-Component-Sid"></a>
The SAP System Identifier of the application component.
Type: String
Pattern: `[A-Z][A-Z0-9]{2}`
Required: No

 ** Status **   <a name="ssmsap-Type-Component-Status"></a>
The status of the component.
+ ACTIVATED - this status has been deprecated.
+ STARTING - the component is in the process of being started.
+ STOPPED - the component is not running.
+ STOPPING - the component is in the process of being stopped.
+ RUNNING - the component is running.
+ RUNNING\_WITH\_ERROR - one or more child component(s) of the parent component is not running. Call [`GetComponent`](https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_GetComponent.html) to review the status of each child component.
+ UNDEFINED - AWS Systems Manager for SAP cannot provide the component status based on the discovered information. Verify your SAP application.
Type: String
Valid Values: `ACTIVATED | STARTING | STOPPED | STOPPING | RUNNING | RUNNING_WITH_ERROR | UNDEFINED`
Required: No

 ** SystemNumber **   <a name="ssmsap-Type-Component-SystemNumber"></a>
The SAP system number of the application component.
Type: String
Pattern: `[0-9]{2}`
Required: No

## See Also
<a name="API_Component_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/Component)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/Component)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/Component)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager for SAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ssmsap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
