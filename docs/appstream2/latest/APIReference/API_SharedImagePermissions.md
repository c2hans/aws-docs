---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_SharedImagePermissions.html
---

# SharedImagePermissions
<a name="API_SharedImagePermissions"></a>

Describes the permissions that are available to the specified AWS account for a shared image.

## Contents
<a name="API_SharedImagePermissions_Contents"></a>

 ** imagePermissions **   <a name="WorkSpacesApplications-Type-SharedImagePermissions-imagePermissions"></a>
Describes the permissions for a shared image.
Type: [ImagePermissions](API_ImagePermissions.md) object
Required: Yes

 ** sharedAccountId **   <a name="WorkSpacesApplications-Type-SharedImagePermissions-sharedAccountId"></a>
The 12-digit identifier of the AWS account with which the image is shared.
Type: String
Pattern: `^\d+$`
Required: Yes

## See Also
<a name="API_SharedImagePermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/SharedImagePermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/SharedImagePermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/SharedImagePermissions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
