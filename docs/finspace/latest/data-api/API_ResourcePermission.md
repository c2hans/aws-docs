---
source_url: https://docs.aws.amazon.com/finspace/latest/data-api/API_ResourcePermission.html
---

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/data-api/amazon-finspace-end-of-support.html).

# ResourcePermission
<a name="API_ResourcePermission"></a>

Resource permission for a dataset. When you create a dataset, all the other members of the same user group inherit access to the dataset. You can only create a dataset if your user group has application permission for Create Datasets.

The following is a list of valid dataset permissions that you can apply:
+  `ViewDatasetDetails`
+  `ReadDatasetDetails`
+  `AddDatasetData`
+  `CreateDataView`
+  `EditDatasetMetadata`
+  `DeleteDataset`

For more information on the dataset permissions, see [Supported Dataset Permissions](https://docs.aws.amazon.com/finspace/latest/userguide/managing-user-permissions.html#supported-dataset-permissions) in the FinSpace User Guide.

## Contents
<a name="API_ResourcePermission_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** permission **   <a name="finspace-Type-ResourcePermission-permission"></a>
Permission for a resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Pattern: `[\s\S]*\S[\s\S]*`
Required: No

## See Also
<a name="API_ResourcePermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2020-07-13/ResourcePermission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2020-07-13/ResourcePermission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2020-07-13/ResourcePermission)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FinSpace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query finspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
