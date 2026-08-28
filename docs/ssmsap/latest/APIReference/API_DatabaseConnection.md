---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_DatabaseConnection.html
---

# DatabaseConnection
<a name="API_DatabaseConnection"></a>

The connection specifications for the database.

## Contents
<a name="API_DatabaseConnection_Contents"></a>

 ** ConnectionIp **   <a name="ssmsap-Type-DatabaseConnection-ConnectionIp"></a>
The IP address for connection.
Type: String
Required: No

 ** DatabaseArn **   <a name="ssmsap-Type-DatabaseConnection-DatabaseArn"></a>
The Amazon Resource Name of the connected SAP HANA database.
Type: String
Pattern: `arn:(.+:){2,4}.+$|^arn:(.+:){1,3}.+\/.+`
Required: No

 ** DatabaseConnectionMethod **   <a name="ssmsap-Type-DatabaseConnection-DatabaseConnectionMethod"></a>
The method of connection.
Type: String
Valid Values: `DIRECT | OVERLAY`
Required: No

## See Also
<a name="API_DatabaseConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/DatabaseConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/DatabaseConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/DatabaseConnection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager for SAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ssmsap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
