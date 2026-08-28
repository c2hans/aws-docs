---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_ImagePermission.html
---

# ImagePermission
<a name="API_ImagePermission"></a>

Describes the AWS accounts that have been granted permission to use a shared image. For more information about sharing images, see [ Share or Unshare a Custom WorkSpaces Image](https://docs.aws.amazon.com/workspaces/latest/adminguide/share-custom-image.html).

## Contents
<a name="API_ImagePermission_Contents"></a>

 ** SharedAccountId **   <a name="WorkSpaces-Type-ImagePermission-SharedAccountId"></a>
The identifier of the AWS account that an image has been shared with.
Type: String
Pattern: `^\d{12}$`
Required: No

## See Also
<a name="API_ImagePermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/ImagePermission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/ImagePermission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/ImagePermission)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
