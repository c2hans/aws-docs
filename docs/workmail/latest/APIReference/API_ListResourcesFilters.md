---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListResourcesFilters.html
---

# ListResourcesFilters
<a name="API_ListResourcesFilters"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

Filtering options for *ListResources* operation. This is only used as input to Operation.

## Contents
<a name="API_ListResourcesFilters_Contents"></a>

 ** NamePrefix **   <a name="workmail-Type-ListResourcesFilters-NamePrefix"></a>
Filters only resource that start with the entered name prefix .
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** PrimaryEmailPrefix **   <a name="workmail-Type-ListResourcesFilters-PrimaryEmailPrefix"></a>
Filters only resource with the provided primary email prefix.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** State **   <a name="workmail-Type-ListResourcesFilters-State"></a>
Filters only resource with the provided state.
Type: String
Valid Values: `ENABLED | DISABLED | DELETED`
Required: No

## See Also
<a name="API_ListResourcesFilters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/ListResourcesFilters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/ListResourcesFilters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/ListResourcesFilters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkMail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workmail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
