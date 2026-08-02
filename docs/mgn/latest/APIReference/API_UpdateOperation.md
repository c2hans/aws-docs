---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_UpdateOperation.html
---

# UpdateOperation
<a name="API_UpdateOperation"></a>

An operation that updates the properties of a construct.

## Contents
<a name="API_UpdateOperation_Contents"></a>

 ** excluded **   <a name="mgn-Type-UpdateOperation-excluded"></a>
Whether to exclude this construct from the migration.
Type: Boolean
Required: No

 ** name **   <a name="mgn-Type-UpdateOperation-name"></a>
The updated name for the construct.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[^\s\x00]( *[^\s\x00])*`
Required: No

 ** properties **   <a name="mgn-Type-UpdateOperation-properties"></a>
The properties to update on the construct.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Key Length Constraints: Minimum length of 0. Maximum length of 24.
Value Length Constraints: Minimum length of 0. Maximum length of 65536.
Required: No

## See Also
<a name="API_UpdateOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/UpdateOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/UpdateOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/UpdateOperation)
