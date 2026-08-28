---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DatabaseInstanceSoftwareDetailsResponse.html
---

# DatabaseInstanceSoftwareDetailsResponse
<a name="API_DatabaseInstanceSoftwareDetailsResponse"></a>

Describes an inventory database instance for a Fleet Advisor collector.

## Contents
<a name="API_DatabaseInstanceSoftwareDetailsResponse_Contents"></a>

 ** Engine **   <a name="DMS-Type-DatabaseInstanceSoftwareDetailsResponse-Engine"></a>
The database engine of a database in a Fleet Advisor collector inventory, for example `Microsoft SQL Server`.
Type: String
Required: No

 ** EngineEdition **   <a name="DMS-Type-DatabaseInstanceSoftwareDetailsResponse-EngineEdition"></a>
The database engine edition of a database in a Fleet Advisor collector inventory, for example `Express`.
Type: String
Required: No

 ** EngineVersion **   <a name="DMS-Type-DatabaseInstanceSoftwareDetailsResponse-EngineVersion"></a>
The database engine version of a database in a Fleet Advisor collector inventory, for example `2019`.
Type: String
Required: No

 ** OsArchitecture **   <a name="DMS-Type-DatabaseInstanceSoftwareDetailsResponse-OsArchitecture"></a>
The operating system architecture of the database.
Type: Integer
Required: No

 ** ServicePack **   <a name="DMS-Type-DatabaseInstanceSoftwareDetailsResponse-ServicePack"></a>
The service pack level of the database.
Type: String
Required: No

 ** SupportLevel **   <a name="DMS-Type-DatabaseInstanceSoftwareDetailsResponse-SupportLevel"></a>
The support level of the database, for example `Mainstream support`.
Type: String
Required: No

 ** Tooltip **   <a name="DMS-Type-DatabaseInstanceSoftwareDetailsResponse-Tooltip"></a>
Information about the database engine software, for example `Mainstream support ends on November 14th, 2024`.
Type: String
Required: No

## See Also
<a name="API_DatabaseInstanceSoftwareDetailsResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DatabaseInstanceSoftwareDetailsResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DatabaseInstanceSoftwareDetailsResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DatabaseInstanceSoftwareDetailsResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
