---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_SchemaResponse.html
---

# SchemaResponse
<a name="API_SchemaResponse"></a>

Describes a schema in a Fleet Advisor collector inventory.

## Contents
<a name="API_SchemaResponse_Contents"></a>

 ** CodeLineCount **   <a name="DMS-Type-SchemaResponse-CodeLineCount"></a>
The number of lines of code in a schema in a Fleet Advisor collector inventory.
Type: Long
Required: No

 ** CodeSize **   <a name="DMS-Type-SchemaResponse-CodeSize"></a>
The size level of the code in a schema in a Fleet Advisor collector inventory.
Type: Long
Required: No

 ** Complexity **   <a name="DMS-Type-SchemaResponse-Complexity"></a>
The complexity level of the code in a schema in a Fleet Advisor collector inventory.
Type: String
Required: No

 ** DatabaseInstance **   <a name="DMS-Type-SchemaResponse-DatabaseInstance"></a>
The database for a schema in a Fleet Advisor collector inventory.
Type: [DatabaseShortInfoResponse](API_DatabaseShortInfoResponse.md) object
Required: No

 ** OriginalSchema **   <a name="DMS-Type-SchemaResponse-OriginalSchema"></a>
Describes a schema in a Fleet Advisor collector inventory.
Type: [SchemaShortInfoResponse](API_SchemaShortInfoResponse.md) object
Required: No

 ** SchemaId **   <a name="DMS-Type-SchemaResponse-SchemaId"></a>
The ID of a schema in a Fleet Advisor collector inventory.
Type: String
Required: No

 ** SchemaName **   <a name="DMS-Type-SchemaResponse-SchemaName"></a>
The name of a schema in a Fleet Advisor collector inventory.
Type: String
Required: No

 ** Server **   <a name="DMS-Type-SchemaResponse-Server"></a>
The database server for a schema in a Fleet Advisor collector inventory.
Type: [ServerShortInfoResponse](API_ServerShortInfoResponse.md) object
Required: No

 ** Similarity **   <a name="DMS-Type-SchemaResponse-Similarity"></a>
The similarity value for a schema in a Fleet Advisor collector inventory. A higher similarity value indicates that a schema is likely to be a duplicate.
Type: Double
Required: No

## See Also
<a name="API_SchemaResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/SchemaResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/SchemaResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/SchemaResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
