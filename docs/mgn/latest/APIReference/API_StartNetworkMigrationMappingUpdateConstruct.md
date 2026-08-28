---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_StartNetworkMigrationMappingUpdateConstruct.html
---

# StartNetworkMigrationMappingUpdateConstruct
<a name="API_StartNetworkMigrationMappingUpdateConstruct"></a>

A construct update to apply during a mapping update operation.

## Contents
<a name="API_StartNetworkMigrationMappingUpdateConstruct_Contents"></a>

 ** constructID **   <a name="mgn-Type-StartNetworkMigrationMappingUpdateConstruct-constructID"></a>
The ID of the construct to update.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** constructType **   <a name="mgn-Type-StartNetworkMigrationMappingUpdateConstruct-constructType"></a>
The type of the construct.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 24.
Pattern: `AWS::([A-Z\d]){2,10}::[a-zA-Z\d]{2,30}`
Required: Yes

 ** segmentID **   <a name="mgn-Type-StartNetworkMigrationMappingUpdateConstruct-segmentID"></a>
The ID of the segment containing the construct.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** operation **   <a name="mgn-Type-StartNetworkMigrationMappingUpdateConstruct-operation"></a>
The operation to perform on the construct.
Type: [OperationUnion](API_OperationUnion.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_StartNetworkMigrationMappingUpdateConstruct_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/StartNetworkMigrationMappingUpdateConstruct)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/StartNetworkMigrationMappingUpdateConstruct)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/StartNetworkMigrationMappingUpdateConstruct)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
