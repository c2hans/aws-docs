---
source_url: https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_FieldDefinition.html
---

# FieldDefinition
<a name="API_FieldDefinition"></a>

 A field definition consists out of a name and a type.

## Contents
<a name="API_FieldDefinition_Contents"></a>

 ** name **   <a name="keyspaces-Type-FieldDefinition-name"></a>
 The identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** type **   <a name="keyspaces-Type-FieldDefinition-type"></a>
 Any supported Cassandra data type, including collections and other user-defined types that are contained in the same keyspace.
For more information, see [Cassandra data type support](https://docs.aws.amazon.com/keyspaces/latest/devguide/cassandra-apis.html#cassandra-data-type) in the *Amazon Keyspaces Developer Guide*.
Type: String
Required: Yes

## See Also
<a name="API_FieldDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspaces-2022-02-10/FieldDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspaces-2022-02-10/FieldDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspaces-2022-02-10/FieldDefinition)
