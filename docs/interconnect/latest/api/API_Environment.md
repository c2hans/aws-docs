---
source_url: https://docs.aws.amazon.com/interconnect/latest/api/API_Environment.html
---

# Environment
<a name="API_Environment"></a>

Defines the logical topology that an AWS Interconnect [Connection](API_Connection.md) is created upon.

Specifically, an Environment defines the partner The remote Cloud Service Provider of this resource. or The remote Last Mile Provider of this resource. and the region or location specification to which an AWS Interconnect Connection can be made.

## Contents
<a name="API_Environment_Contents"></a>

 ** bandwidths **   <a name="interconnect-Type-Environment-bandwidths"></a>
The sets of bandwidths that are available and supported on this environment.
Type: [Bandwidths](API_Bandwidths.md) object
Required: Yes

 ** environmentId **   <a name="interconnect-Type-Environment-environmentId"></a>
The identifier of this [Environment](#API_Environment)
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** location **   <a name="interconnect-Type-Environment-location"></a>
The provider specific location on the remote side of this [Connection](API_Connection.md).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: Yes

 ** provider **   <a name="interconnect-Type-Environment-provider"></a>
The provider on the remote side of this [Connection](API_Connection.md).
Type: [Provider](API_Provider.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** state **   <a name="interconnect-Type-Environment-state"></a>
The state of the [Environment](#API_Environment). Possible values:
+  `available`: The environment is available and new [Connection](API_Connection.md) objects can be requested.
+  `limited`: The environment is available, but overall capacity is limited. The set of available bandwidths
+  `unavailable`: The environment is currently unavailable.
Type: String
Valid Values: `available | limited | unavailable`
Required: Yes

 ** type **   <a name="interconnect-Type-Environment-type"></a>
The specific product type of [Connection](API_Connection.md) objects provided by this [Environment](#API_Environment).
Type: String
Length Constraints: Minimum length of 5. Maximum length of 32.
Required: Yes

 ** activationPageUrl **   <a name="interconnect-Type-Environment-activationPageUrl"></a>
An HTTPS URL on the remote partner portal where the Activation Key should be brought to complete the creation process.
Type: String
Required: No

 ** remoteIdentifierType **   <a name="interconnect-Type-Environment-remoteIdentifierType"></a>
The type of identifying information that should be supplied to the `remoteAccount` parameter of a [CreateConnection](API_CreateConnection.md) call for this specific Environment.
Type: String
Valid Values: `account | email`
Required: No

## See Also
<a name="API_Environment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/interconnect-2022-07-26/Environment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/interconnect-2022-07-26/Environment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/interconnect-2022-07-26/Environment)
