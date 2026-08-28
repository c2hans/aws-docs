---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DatabaseInput.html
---

# DatabaseInput
<a name="API_DatabaseInput"></a>

The structure used to create or update a database.

## Contents
<a name="API_DatabaseInput_Contents"></a>

 ** Name **   <a name="Glue-Type-DatabaseInput-Name"></a>
The name of the database. For Hive compatibility, this is folded to lowercase when it is stored.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** CreateTableDefaultPermissions **   <a name="Glue-Type-DatabaseInput-CreateTableDefaultPermissions"></a>
Creates a set of default permissions on the table for principals. Used by AWS Lake Formation. Not used in the normal course of AWS Glue operations.
Type: Array of [PrincipalPermissions](API_PrincipalPermissions.md) objects
Required: No

 ** Description **   <a name="Glue-Type-DatabaseInput-Description"></a>
A description of the database.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** FederatedDatabase **   <a name="Glue-Type-DatabaseInput-FederatedDatabase"></a>
A `FederatedDatabase` structure that references an entity outside the AWS Glue Data Catalog.
Type: [FederatedDatabase](API_FederatedDatabase.md) object
Required: No

 ** LocationUri **   <a name="Glue-Type-DatabaseInput-LocationUri"></a>
The location of the database (for example, an HDFS path).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** Parameters **   <a name="Glue-Type-DatabaseInput-Parameters"></a>
These key-value pairs define parameters and properties of the database.
These key-value pairs define parameters and properties of the database.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Key Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Value Length Constraints: Maximum length of 512000.
Required: No

 ** TargetDatabase **   <a name="Glue-Type-DatabaseInput-TargetDatabase"></a>
A `DatabaseIdentifier` structure that describes a target database for resource linking.
Type: [DatabaseIdentifier](API_DatabaseIdentifier.md) object
Required: No

## See Also
<a name="API_DatabaseInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DatabaseInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DatabaseInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DatabaseInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
