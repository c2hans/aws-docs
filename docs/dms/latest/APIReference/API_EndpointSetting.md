---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_EndpointSetting.html
---

# EndpointSetting
<a name="API_EndpointSetting"></a>

Endpoint settings.

## Contents
<a name="API_EndpointSetting_Contents"></a>

 ** Applicability **   <a name="DMS-Type-EndpointSetting-Applicability"></a>
The relevance or validity of an endpoint setting for an engine name and its endpoint type.
Type: String
Required: No

 ** DefaultValue **   <a name="DMS-Type-EndpointSetting-DefaultValue"></a>
The default value of the endpoint setting if no value is specified using `CreateEndpoint` or `ModifyEndpoint`.
Type: String
Required: No

 ** EnumValues **   <a name="DMS-Type-EndpointSetting-EnumValues"></a>
Enumerated values to use for this endpoint.
Type: Array of strings
Required: No

 ** IntValueMax **   <a name="DMS-Type-EndpointSetting-IntValueMax"></a>
The maximum value of an endpoint setting that is of type `int`.
Type: Integer
Required: No

 ** IntValueMin **   <a name="DMS-Type-EndpointSetting-IntValueMin"></a>
The minimum value of an endpoint setting that is of type `int`.
Type: Integer
Required: No

 ** Name **   <a name="DMS-Type-EndpointSetting-Name"></a>
The name that you want to give the endpoint settings.
Type: String
Required: No

 ** Sensitive **   <a name="DMS-Type-EndpointSetting-Sensitive"></a>
A value that marks this endpoint setting as sensitive.
Type: Boolean
Required: No

 ** Type **   <a name="DMS-Type-EndpointSetting-Type"></a>
The type of endpoint. Valid values are `source` and `target`.
Type: String
Valid Values: `string | boolean | integer | enum`
Required: No

 ** Units **   <a name="DMS-Type-EndpointSetting-Units"></a>
The unit of measure for this endpoint setting.
Type: String
Required: No

## See Also
<a name="API_EndpointSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/EndpointSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/EndpointSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/EndpointSetting)
