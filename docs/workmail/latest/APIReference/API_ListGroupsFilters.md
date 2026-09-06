---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListGroupsFilters.html
---

# ListGroupsFilters
<a name="API_ListGroupsFilters"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

 Filtering options for *ListGroups* operation. This is only used as input to Operation.

## Contents
<a name="API_ListGroupsFilters_Contents"></a>

 ** NamePrefix **   <a name="workmail-Type-ListGroupsFilters-NamePrefix"></a>
Filters only groups with the provided name prefix.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** PrimaryEmailPrefix **   <a name="workmail-Type-ListGroupsFilters-PrimaryEmailPrefix"></a>
Filters only groups with the provided primary email prefix.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** State **   <a name="workmail-Type-ListGroupsFilters-State"></a>
Filters only groups with the provided state.
Type: String
Valid Values: `ENABLED | DISABLED | DELETED`
Required: No

## See Also
<a name="API_ListGroupsFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/ListGroupsFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/ListGroupsFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/ListGroupsFilters)
