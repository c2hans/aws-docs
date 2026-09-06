---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ResourceSetSummary.html
---

# ResourceSetSummary
<a name="API_ResourceSetSummary"></a>

Summarizes the resource sets used in a policy.

## Contents
<a name="API_ResourceSetSummary_Contents"></a>

 ** Description **   <a name="fms-Type-ResourceSetSummary-Description"></a>
A description of the resource set.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** Id **   <a name="fms-Type-ResourceSetSummary-Id"></a>
A unique identifier for the resource set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `^[a-z0-9A-Z]{22}$`
Required: No

 ** LastUpdateTime **   <a name="fms-Type-ResourceSetSummary-LastUpdateTime"></a>
The last time that the resource set was changed.
Type: Timestamp
Required: No

 ** Name **   <a name="fms-Type-ResourceSetSummary-Name"></a>
The descriptive name of the resource set. You can't change the name of a resource set after you create it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** ResourceSetStatus **   <a name="fms-Type-ResourceSetSummary-ResourceSetStatus"></a>
Indicates whether the resource set is in or out of an admin's Region scope.
+  `ACTIVE` - The administrator can manage and delete the resource set.
+  `OUT_OF_ADMIN_SCOPE` - The administrator can view the resource set, but they can't edit or delete the resource set. Existing protections stay in place. Any new resource that come into scope of the resource set won't be protected.
Type: String
Valid Values: `ACTIVE | OUT_OF_ADMIN_SCOPE`
Required: No

## See Also
<a name="API_ResourceSetSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/ResourceSetSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/ResourceSetSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/ResourceSetSummary)
