---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CedarTagValue.html
---

# CedarTagValue
<a name="API_CedarTagValue"></a>

The value of an entity's Cedar tag.

This data type is used as a member of the [EntityItem](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EntityItem.html) structure that forms the body of the `Entities` request parameter for the [IsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html), [BatchIsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorized.html), [IsAuthorizedWithToken](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html), and [BatchIsAuthorizedWithToken](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorizedWithToken.html) operations.

## Contents
<a name="API_CedarTagValue_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** boolean **   <a name="verifiedpermissions-Type-CedarTagValue-boolean"></a>
A Cedar tag value of [Boolean](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-bool) type.
Example: `{"boolean": false}`
Type: Boolean
Required: No

 ** datetime **   <a name="verifiedpermissions-Type-CedarTagValue-datetime"></a>
A Cedar tag value of [datetime](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-datetime) type.
Example: `{"datetime": "2025-11-04T11:35:00.000+0100"}`
Type: String
Length Constraints: Minimum length of 10. Maximum length of 28.
Pattern: `\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}:\d{2}(\.\d{3})?(Z|[+-]\d{4}))?`
Required: No

 ** decimal **   <a name="verifiedpermissions-Type-CedarTagValue-decimal"></a>
A Cedar tag value of [decimal](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-decimal) type.
Example: `{"decimal": "-2.0"}`
Type: String
Length Constraints: Minimum length of 3. Maximum length of 23.
Pattern: `-?\d{1,15}\.\d{1,4}`
Required: No

 ** duration **   <a name="verifiedpermissions-Type-CedarTagValue-duration"></a>
A Cedar tag value of [duration](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-duration) type.
Example: `{"duration": "-1d12h"}`
Type: String
Length Constraints: Minimum length of 2. Maximum length of 100.
Pattern: `-?(\d+d)?(\d+h)?(\d+m)?(\d+s)?(\d+ms)?`
Required: No

 ** entityIdentifier **   <a name="verifiedpermissions-Type-CedarTagValue-entityIdentifier"></a>
A Cedar tag value of type [EntityIdentifier](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EntityIdentifier.html).
Example: `{"entityIdentifier": { "entityId": "alice", "entityType": "User"} }`
Type: [EntityIdentifier](API_EntityIdentifier.md) object
Required: No

 ** ipaddr **   <a name="verifiedpermissions-Type-CedarTagValue-ipaddr"></a>
A Cedar tag value of [ipaddr](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-ipaddr) type.
Example: `{"ip": "10.50.0.0/24"}`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 44.
Pattern: `[0-9a-fA-F\.:\/]*`
Required: No

 ** long **   <a name="verifiedpermissions-Type-CedarTagValue-long"></a>
A Cedar tag value of [Long](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-long) type.
Example: `{"long": 0}`
Type: Long
Required: No

 ** record **   <a name="verifiedpermissions-Type-CedarTagValue-record"></a>
A Cedar tag value of [Record](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-record) type.
Example: `{"record": { "keyName": {} } }`
Type: String to [CedarTagValue](#API_CedarTagValue) object map
Required: No

 ** set **   <a name="verifiedpermissions-Type-CedarTagValue-set"></a>
A Cedar tag value of [Set](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-set) type.
Example: `{"set": [ { "string": "abc" } ] }`
Type: Array of [CedarTagValue](#API_CedarTagValue) objects
Required: No

 ** string **   <a name="verifiedpermissions-Type-CedarTagValue-string"></a>
A Cedar tag value of [String](https://docs.cedarpolicy.com/policies/syntax-datatypes.html#datatype-string) type.
Example: `{"string": "abc"}`
Type: String
Required: No

## See Also
<a name="API_CedarTagValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/CedarTagValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/CedarTagValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/CedarTagValue)
