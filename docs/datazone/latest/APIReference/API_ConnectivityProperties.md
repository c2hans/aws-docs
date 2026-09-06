---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ConnectivityProperties.html
---

# ConnectivityProperties
<a name="API_ConnectivityProperties"></a>

Contains the network and authentication settings for a connection, including connection credentials, physical network requirements, and compute-environment validation options.

## Contents
<a name="API_ConnectivityProperties_Contents"></a>

 ** athenaProperties **   <a name="datazone-Type-ConnectivityProperties-athenaProperties"></a>
The Athena properties for this configuration.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** authenticationConfiguration **   <a name="datazone-Type-ConnectivityProperties-authenticationConfiguration"></a>
The authentication settings for this configuration.
Type: [AuthenticationConfigurationInput](API_AuthenticationConfigurationInput.md) object
Required: No

 ** connectionProperties **   <a name="datazone-Type-ConnectivityProperties-connectionProperties"></a>
The connection properties for this configuration.
Type: String to string map
Value Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** description **   <a name="datazone-Type-ConnectivityProperties-description"></a>
The description of the connectivity configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFF\r\n\t]*`
Required: No

 ** name **   <a name="datazone-Type-ConnectivityProperties-name"></a>
The name of the connectivity configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 41.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFF\t]*`
Required: No

 ** physicalConnectionRequirements **   <a name="datazone-Type-ConnectivityProperties-physicalConnectionRequirements"></a>
The physical network requirements for the connection, such as the subnet, security group, and VPC settings needed to reach the data source.
Type: [PhysicalConnectionRequirements](API_PhysicalConnectionRequirements.md) object
Required: No

 ** pythonProperties **   <a name="datazone-Type-ConnectivityProperties-pythonProperties"></a>
The Python properties for this configuration.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** sparkProperties **   <a name="datazone-Type-ConnectivityProperties-sparkProperties"></a>
The Spark properties for this configuration.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** validateCredentials **   <a name="datazone-Type-ConnectivityProperties-validateCredentials"></a>
Specifies whether to validate credentials for the connectivity configuration. Defaults to true if not specified.
Type: Boolean
Required: No

 ** validateForComputeEnvironments **   <a name="datazone-Type-ConnectivityProperties-validateForComputeEnvironments"></a>
The compute environments to use when validating connectivity. The service validates that the connection is reachable from each specified environment.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Valid Values: `SPARK | ATHENA | PYTHON`
Required: No

## See Also
<a name="API_ConnectivityProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ConnectivityProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ConnectivityProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ConnectivityProperties)
