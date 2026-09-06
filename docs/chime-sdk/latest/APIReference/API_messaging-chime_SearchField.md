---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_messaging-chime_SearchField.html
---

# SearchField
<a name="API_messaging-chime_SearchField"></a>

A `Field` of the channel that you want to search.

**Note**
This operation isn't supported for `AppInstanceUsers` with a large number of memberships.

## Contents
<a name="API_messaging-chime_SearchField_Contents"></a>

 ** Key **   <a name="chimesdk-Type-messaging-chime_SearchField-Key"></a>
An `enum` value that indicates the key to search the channel on. `MEMBERS` allows you to search channels based on memberships. You can use it with the `EQUALS` operator to get channels whose memberships are equal to the specified values, and with the `INCLUDES` operator to get channels whose memberships include the specified values.
Type: String
Valid Values: `MEMBERS`
Required: Yes

 ** Operator **   <a name="chimesdk-Type-messaging-chime_SearchField-Operator"></a>
The operator used to compare field values, currently `EQUALS` or `INCLUDES`. Use the `EQUALS` operator to find channels whose memberships equal the specified values. Use the `INCLUDES` operator to find channels whose memberships include the specified values.
Type: String
Valid Values: `EQUALS | INCLUDES`
Required: Yes

 ** Values **   <a name="chimesdk-Type-messaging-chime_SearchField-Values"></a>
The values that you want to search for, a list of strings. The values must be `AppInstanceUserArns` specified as a list of strings.
This operation isn't supported for `AppInstanceUsers` with a large number of memberships.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\s\S]*`
Required: Yes

## See Also
<a name="API_messaging-chime_SearchField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-sdk-messaging-2021-05-15/SearchField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-sdk-messaging-2021-05-15/SearchField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-sdk-messaging-2021-05-15/SearchField)
