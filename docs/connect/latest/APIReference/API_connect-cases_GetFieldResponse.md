---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_GetFieldResponse.html
---

# GetFieldResponse
<a name="API_connect-cases_GetFieldResponse"></a>

Object to store detailed field information.

## Contents
<a name="API_connect-cases_GetFieldResponse_Contents"></a>

 ** fieldArn **   <a name="connect-Type-connect-cases_GetFieldResponse-fieldArn"></a>
The Amazon Resource Name (ARN) of the field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** fieldId **   <a name="connect-Type-connect-cases_GetFieldResponse-fieldId"></a>
Unique identifier of the field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** name **   <a name="connect-Type-connect-cases_GetFieldResponse-name"></a>
Name of the field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `.*[\S]`
Required: Yes

 ** namespace **   <a name="connect-Type-connect-cases_GetFieldResponse-namespace"></a>
Namespace of the field.
Type: String
Valid Values: `System | Custom`
Required: Yes

 ** type **   <a name="connect-Type-connect-cases_GetFieldResponse-type"></a>
Type of the field.
Type: String
Valid Values: `Text | Number | Boolean | DateTime | SingleSelect | Url | User`
Required: Yes

 ** attributes **   <a name="connect-Type-connect-cases_GetFieldResponse-attributes"></a>
Union of field attributes.
Type: [FieldAttributes](API_connect-cases_FieldAttributes.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** createdTime **   <a name="connect-Type-connect-cases_GetFieldResponse-createdTime"></a>
Timestamp at which the resource was created.
Type: Timestamp
Required: No

 ** deleted **   <a name="connect-Type-connect-cases_GetFieldResponse-deleted"></a>
Denotes whether or not the resource has been deleted.
Type: Boolean
Required: No

 ** description **   <a name="connect-Type-connect-cases_GetFieldResponse-description"></a>
Description of the field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** lastModifiedTime **   <a name="connect-Type-connect-cases_GetFieldResponse-lastModifiedTime"></a>
Timestamp at which the resource was created or last modified.
Type: Timestamp
Required: No

 ** tags **   <a name="connect-Type-connect-cases_GetFieldResponse-tags"></a>
A map of of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.
Type: String to string map
Required: No

## See Also
<a name="API_connect-cases_GetFieldResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/GetFieldResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/GetFieldResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/GetFieldResponse)
