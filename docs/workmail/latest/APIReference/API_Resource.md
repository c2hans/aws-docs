---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_Resource.html
---

# Resource
<a name="API_Resource"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

The representation of a resource.

## Contents
<a name="API_Resource_Contents"></a>

 ** Description **   <a name="workmail-Type-Resource-Description"></a>
Resource description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** DisabledDate **   <a name="workmail-Type-Resource-DisabledDate"></a>
The date indicating when the resource was disabled from WorkMail use.
Type: Timestamp
Required: No

 ** Email **   <a name="workmail-Type-Resource-Email"></a>
The email of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 254.
Pattern: `[a-zA-Z0-9._%+-]{1,64}@[a-zA-Z0-9.-]+\.[a-zA-Z-]{2,}`
Required: No

 ** EnabledDate **   <a name="workmail-Type-Resource-EnabledDate"></a>
The date indicating when the resource was enabled for WorkMail use.
Type: Timestamp
Required: No

 ** Id **   <a name="workmail-Type-Resource-Id"></a>
The identifier of the resource.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 256.
Required: No

 ** Name **   <a name="workmail-Type-Resource-Name"></a>
The name of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `[\w\-.]+(@[a-zA-Z0-9.\-]+\.[a-zA-Z0-9-]{2,})?`
Required: No

 ** State **   <a name="workmail-Type-Resource-State"></a>
The state of the resource, which can be ENABLED, DISABLED, or DELETED.
Type: String
Valid Values: `ENABLED | DISABLED | DELETED`
Required: No

 ** Type **   <a name="workmail-Type-Resource-Type"></a>
The type of the resource: equipment or room.
Type: String
Valid Values: `ROOM | EQUIPMENT`
Required: No

## See Also
<a name="API_Resource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/Resource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/Resource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/Resource)
