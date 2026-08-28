---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_Database.html
---

# Database
<a name="API_Database"></a>

The SAP HANA database of the application registered with AWS Systems Manager for SAP.

## Contents
<a name="API_Database_Contents"></a>

 ** ApplicationId **   <a name="ssmsap-Type-Database-ApplicationId"></a>
The ID of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Pattern: `[\w\d\.-]+`
Required: No

 ** Arn **   <a name="ssmsap-Type-Database-Arn"></a>
The Amazon Resource Name (ARN) of the database.
Type: String
Pattern: `arn:(.+:){2,4}.+$|^arn:(.+:){1,3}.+\/.+`
Required: No

 ** ComponentId **   <a name="ssmsap-Type-Database-ComponentId"></a>
The ID of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\d-]+`
Required: No

 ** ConnectedComponentArns **   <a name="ssmsap-Type-Database-ConnectedComponentArns"></a>
The Amazon Resource Names of the connected AWS Systems Manager for SAP components.
Type: Array of strings
Pattern: `arn:(.+:){2,4}.+$|^arn:(.+:){1,3}.+\/.+`
Required: No

 ** Credentials **   <a name="ssmsap-Type-Database-Credentials"></a>
The credentials of the database.
Type: Array of [ApplicationCredential](API_ApplicationCredential.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** DatabaseId **   <a name="ssmsap-Type-Database-DatabaseId"></a>
The ID of the SAP HANA database.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `.*[\w\d]+`
Required: No

 ** DatabaseName **   <a name="ssmsap-Type-Database-DatabaseName"></a>
The name of the database.
Type: String
Required: No

 ** DatabaseType **   <a name="ssmsap-Type-Database-DatabaseType"></a>
The type of the database.
Type: String
Valid Values: `SYSTEM | TENANT`
Required: No

 ** LastUpdated **   <a name="ssmsap-Type-Database-LastUpdated"></a>
The time at which the database was last updated.
Type: Timestamp
Required: No

 ** PrimaryHost **   <a name="ssmsap-Type-Database-PrimaryHost"></a>
The primary host of the database.
Type: String
Required: No

 ** SQLPort **   <a name="ssmsap-Type-Database-SQLPort"></a>
The SQL port of the database.
Type: Integer
Required: No

 ** Status **   <a name="ssmsap-Type-Database-Status"></a>
The status of the database.
Type: String
Valid Values: `RUNNING | STARTING | STOPPED | WARNING | UNKNOWN | ERROR`
Required: No

## See Also
<a name="API_Database_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/Database)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/Database)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/Database)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager for SAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ssmsap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
