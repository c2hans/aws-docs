---
source_url: https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_SqlParameter.html
---

# SqlParameter
<a name="API_SqlParameter"></a>

A parameter used in a SQL statement.

## Contents
<a name="API_SqlParameter_Contents"></a>

 ** name **   <a name="rdsdtataservice-Type-SqlParameter-name"></a>
The name of the parameter.
Type: String
Required: No

 ** typeHint **   <a name="rdsdtataservice-Type-SqlParameter-typeHint"></a>
A hint that specifies the correct object type for data type mapping. Possible values are as follows:
+  `DATE` - The corresponding `String` parameter value is sent as an object of `DATE` type to the database. The accepted format is `YYYY-MM-DD`.
+  `DECIMAL` - The corresponding `String` parameter value is sent as an object of `DECIMAL` type to the database.
+  `JSON` - The corresponding `String` parameter value is sent as an object of `JSON` type to the database.
+  `TIME` - The corresponding `String` parameter value is sent as an object of `TIME` type to the database. The accepted format is `HH:MM:SS[.FFF]`.
+  `TIMESTAMP` - The corresponding `String` parameter value is sent as an object of `TIMESTAMP` type to the database. The accepted format is `YYYY-MM-DD HH:MM:SS[.FFF]`.
+  `UUID` - The corresponding `String` parameter value is sent as an object of `UUID` type to the database.
Type: String
Valid Values: `JSON | UUID | TIMESTAMP | DATE | TIME | DECIMAL`
Required: No

 ** value **   <a name="rdsdtataservice-Type-SqlParameter-value"></a>
The value of the parameter.
Type: [Field](API_Field.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_SqlParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-data-2018-08-01/SqlParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-data-2018-08-01/SqlParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-data-2018-08-01/SqlParameter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS Data Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rdsdataservice` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
