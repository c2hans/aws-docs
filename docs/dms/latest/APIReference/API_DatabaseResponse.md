---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DatabaseResponse.html
---

# DatabaseResponse
<a name="API_DatabaseResponse"></a>

Describes a database in a Fleet Advisor collector inventory.

## Contents
<a name="API_DatabaseResponse_Contents"></a>

 ** Collectors **   <a name="DMS-Type-DatabaseResponse-Collectors"></a>
A list of collectors associated with the database.
Type: Array of [CollectorShortInfoResponse](API_CollectorShortInfoResponse.md) objects
Required: No

 ** DatabaseId **   <a name="DMS-Type-DatabaseResponse-DatabaseId"></a>
The ID of a database in a Fleet Advisor collector inventory.
Type: String
Required: No

 ** DatabaseName **   <a name="DMS-Type-DatabaseResponse-DatabaseName"></a>
The name of a database in a Fleet Advisor collector inventory.
Type: String
Required: No

 ** IpAddress **   <a name="DMS-Type-DatabaseResponse-IpAddress"></a>
The IP address of a database in a Fleet Advisor collector inventory.
Type: String
Required: No

 ** NumberOfSchemas **   <a name="DMS-Type-DatabaseResponse-NumberOfSchemas"></a>
The number of schemas in a Fleet Advisor collector inventory database.
Type: Long
Required: No

 ** Server **   <a name="DMS-Type-DatabaseResponse-Server"></a>
The server name of a database in a Fleet Advisor collector inventory.
Type: [ServerShortInfoResponse](API_ServerShortInfoResponse.md) object
Required: No

 ** SoftwareDetails **   <a name="DMS-Type-DatabaseResponse-SoftwareDetails"></a>
The software details of a database in a Fleet Advisor collector inventory, such as database engine and version.
Type: [DatabaseInstanceSoftwareDetailsResponse](API_DatabaseInstanceSoftwareDetailsResponse.md) object
Required: No

## See Also
<a name="API_DatabaseResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DatabaseResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DatabaseResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DatabaseResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
