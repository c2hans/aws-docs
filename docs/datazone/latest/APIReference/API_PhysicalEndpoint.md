---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_PhysicalEndpoint.html
---

# PhysicalEndpoint
<a name="API_PhysicalEndpoint"></a>

The physical endpoints of a connection.

## Contents
<a name="API_PhysicalEndpoint_Contents"></a>

 ** awsLocation **   <a name="datazone-Type-PhysicalEndpoint-awsLocation"></a>
The location of a connection.
Type: [AwsLocation](API_AwsLocation.md) object
Required: No

 ** enableTrustedIdentityPropagation **   <a name="datazone-Type-PhysicalEndpoint-enableTrustedIdentityPropagation"></a>
Specified whether trusted identity propagation for the connection is enabled.
Type: Boolean
Required: No

 ** glueConnection **   <a name="datazone-Type-PhysicalEndpoint-glueConnection"></a>
The AWS Glue connection.
Type: [GlueConnection](API_GlueConnection.md) object
Required: No

 ** glueConnectionName **   <a name="datazone-Type-PhysicalEndpoint-glueConnectionName"></a>
The AWS Glue connection name.
Type: String
Required: No

 ** glueConnectionNames **   <a name="datazone-Type-PhysicalEndpoint-glueConnectionNames"></a>
The AWS Glue connection names in the physical endpoint.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 16 items.
Length Constraints: Minimum length of 0. Maximum length of 64.
Required: No

 ** host **   <a name="datazone-Type-PhysicalEndpoint-host"></a>
The host in the physical endpoints of a connection.
Type: String
Required: No

 ** port **   <a name="datazone-Type-PhysicalEndpoint-port"></a>
The port in the physical endpoints of a connection.
Type: Integer
Required: No

 ** protocol **   <a name="datazone-Type-PhysicalEndpoint-protocol"></a>
The protocol in the physical endpoints of a connection.
Type: String
Valid Values: `ATHENA | GLUE_INTERACTIVE_SESSION | HTTPS | JDBC | LIVY | ODBC | PRISM`
Required: No

 ** stage **   <a name="datazone-Type-PhysicalEndpoint-stage"></a>
The stage in the physical endpoints of a connection.
Type: String
Required: No

## See Also
<a name="API_PhysicalEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/PhysicalEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/PhysicalEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/PhysicalEndpoint)
