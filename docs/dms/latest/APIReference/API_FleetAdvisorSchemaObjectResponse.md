---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_FleetAdvisorSchemaObjectResponse.html
---

# FleetAdvisorSchemaObjectResponse
<a name="API_FleetAdvisorSchemaObjectResponse"></a>

Describes a schema object in a Fleet Advisor collector inventory.

## Contents
<a name="API_FleetAdvisorSchemaObjectResponse_Contents"></a>

 ** CodeLineCount **   <a name="DMS-Type-FleetAdvisorSchemaObjectResponse-CodeLineCount"></a>
The number of lines of code in a schema object in a Fleet Advisor collector inventory.
Type: Long
Required: No

 ** CodeSize **   <a name="DMS-Type-FleetAdvisorSchemaObjectResponse-CodeSize"></a>
The size level of the code in a schema object in a Fleet Advisor collector inventory.
Type: Long
Required: No

 ** NumberOfObjects **   <a name="DMS-Type-FleetAdvisorSchemaObjectResponse-NumberOfObjects"></a>
The number of objects in a schema object in a Fleet Advisor collector inventory.
Type: Long
Required: No

 ** ObjectType **   <a name="DMS-Type-FleetAdvisorSchemaObjectResponse-ObjectType"></a>
The type of the schema object, as reported by the database engine. Examples include the following:
+  `function`
+  `trigger`
+  `SYSTEM_TABLE`
+  `QUEUE`
Type: String
Required: No

 ** SchemaId **   <a name="DMS-Type-FleetAdvisorSchemaObjectResponse-SchemaId"></a>
The ID of a schema object in a Fleet Advisor collector inventory.
Type: String
Required: No

## See Also
<a name="API_FleetAdvisorSchemaObjectResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/FleetAdvisorSchemaObjectResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/FleetAdvisorSchemaObjectResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/FleetAdvisorSchemaObjectResponse)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
