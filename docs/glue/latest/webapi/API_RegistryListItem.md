---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_RegistryListItem.html
---

# RegistryListItem
<a name="API_RegistryListItem"></a>

A structure containing the details for a registry.

## Contents
<a name="API_RegistryListItem_Contents"></a>

 ** CreatedTime **   <a name="Glue-Type-RegistryListItem-CreatedTime"></a>
The data the registry was created.
Type: String
Required: No

 ** Description **   <a name="Glue-Type-RegistryListItem-Description"></a>
A description of the registry.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** RegistryArn **   <a name="Glue-Type-RegistryListItem-RegistryArn"></a>
The Amazon Resource Name (ARN) of the registry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.
Pattern: `arn:aws(-(cn|us-gov|iso(-[bef])?))?:glue:.*`
Required: No

 ** RegistryName **   <a name="Glue-Type-RegistryListItem-RegistryName"></a>
The name of the registry.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9-_$#.]+`
Required: No

 ** Status **   <a name="Glue-Type-RegistryListItem-Status"></a>
The status of the registry.
Type: String
Valid Values: `AVAILABLE | DELETING`
Required: No

 ** UpdatedTime **   <a name="Glue-Type-RegistryListItem-UpdatedTime"></a>
The date the registry was updated.
Type: String
Required: No

## See Also
<a name="API_RegistryListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/RegistryListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/RegistryListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/RegistryListItem)
