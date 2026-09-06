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
