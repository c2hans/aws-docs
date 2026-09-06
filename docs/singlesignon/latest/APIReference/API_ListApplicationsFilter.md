---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_ListApplicationsFilter.html
---

# ListApplicationsFilter
<a name="API_ListApplicationsFilter"></a>

A structure that describes a filter for applications.

## Contents
<a name="API_ListApplicationsFilter_Contents"></a>

 ** ApplicationAccount **   <a name="singlesignon-Type-ListApplicationsFilter-ApplicationAccount"></a>
An AWS account ID number that filters the results in the response.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** ApplicationProvider **   <a name="singlesignon-Type-ListApplicationsFilter-ApplicationProvider"></a>
The ARN of an application provider that can filter the results in the response.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso::aws:applicationProvider/[a-zA-Z0-9-/]+`
Required: No

## See Also
<a name="API_ListApplicationsFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/ListApplicationsFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/ListApplicationsFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/ListApplicationsFilter)
