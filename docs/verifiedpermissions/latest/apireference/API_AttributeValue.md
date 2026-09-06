---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_AttributeValue.html
---

# AttributeValue
<a name="API_AttributeValue"></a>

The value of an attribute.

Contains information about the runtime context for a request for which an authorization decision is made.

This data type is used as a member of the [ContextDefinition](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ContextDefinition.html) structure which is used as a request parameter for the [IsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html), [BatchIsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorized.html), and [IsAuthorizedWithToken](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html) operations.

## Contents
<a name="API_AttributeValue_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** boolean **   <a name="verifiedpermissions-Type-AttributeValue-boolean"></a>
An attribute value of [Boolean](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-bool) type.
Example: `{"boolean": true}`
Type: Boolean
Required: No

 ** datetime **   <a name="verifiedpermissions-Type-AttributeValue-datetime"></a>
An attribute value of [datetime](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-datetime) type.
Example: `{"datetime": "2024-10-15T11:35:00Z"}`
Type: String
Length Constraints: Minimum length of 10. Maximum length of 28.
Pattern: `\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}:\d{2}(\.\d{3})?(Z|[+-]\d{4}))?`
Required: No

 ** decimal **   <a name="verifiedpermissions-Type-AttributeValue-decimal"></a>
An attribute value of [decimal](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-decimal) type.
Example: `{"decimal": "1.1"}`
Type: String
Length Constraints: Minimum length of 3. Maximum length of 23.
Pattern: `-?\d{1,15}\.\d{1,4}`
Required: No

 ** duration **   <a name="verifiedpermissions-Type-AttributeValue-duration"></a>
An attribute value of [duration](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-duration) type.
Example: `{"duration": "1h30m"}`
Type: String
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `-?(\d+d)?(\d+h)?(\d+m)?(\d+s)?(\d+ms)?`
Required: No

 ** entityIdentifier **   <a name="verifiedpermissions-Type-AttributeValue-entityIdentifier"></a>
An attribute value of type [EntityIdentifier](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EntityIdentifier.html).
Example: `{"entityIdentifier": { "entityId": "alice", "entityType": "User"} }`
Type: [EntityIdentifier](API_EntityIdentifier.md) object
Required: No

 ** ipaddr **   <a name="verifiedpermissions-Type-AttributeValue-ipaddr"></a>
An attribute value of [ipaddr](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-ipaddr) type.
Example: `{"ip": "192.168.1.100"}`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 44.
Pattern: `[0-9a-fA-F\.:\/]*`
Required: No

 ** long **   <a name="verifiedpermissions-Type-AttributeValue-long"></a>
An attribute value of [Long](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-long) type.
Example: `{"long": 0}`
Type: Long
Required: No

 ** record **   <a name="verifiedpermissions-Type-AttributeValue-record"></a>
An attribute value of [Record](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-record) type.
Example: `{"record": { "keyName": {} } }`
Type: String to [AttributeValue](#API_AttributeValue) object map
Required: No

 ** set **   <a name="verifiedpermissions-Type-AttributeValue-set"></a>
An attribute value of [Set](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-set) type.
Example: `{"set": [ {} ] }`
Type: Array of [AttributeValue](#API_AttributeValue) objects
Required: No

 ** string **   <a name="verifiedpermissions-Type-AttributeValue-string"></a>
An attribute value of [String](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-string) type.
Example: `{"string": "abc"}`
Type: String
Required: No

## See Also
<a name="API_AttributeValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/AttributeValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/AttributeValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/AttributeValue)
