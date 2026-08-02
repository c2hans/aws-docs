---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_SyncResourceFilter.html
---

# SyncResourceFilter
<a name="API_SyncResourceFilter"></a>

The sync resource filter.

## Contents
<a name="API_SyncResourceFilter_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** externalId **   <a name="tm-Type-SyncResourceFilter-externalId"></a>
The external ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
Required: No

 ** resourceId **   <a name="tm-Type-SyncResourceFilter-resourceId"></a>
The sync resource filter resource ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
Required: No

 ** resourceType **   <a name="tm-Type-SyncResourceFilter-resourceType"></a>
The sync resource filter resource type
Type: String
Valid Values: `ENTITY | COMPONENT_TYPE`
Required: No

 ** state **   <a name="tm-Type-SyncResourceFilter-state"></a>
The sync resource filter's state.
Type: String
Valid Values: `INITIALIZING | PROCESSING | DELETED | IN_SYNC | ERROR`
Required: No

## See Also
<a name="API_SyncResourceFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/SyncResourceFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/SyncResourceFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/SyncResourceFilter)
