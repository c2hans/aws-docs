---
source_url: https://docs.aws.amazon.com/cloudwatchinvestigations/latest/APIReference/API_ListInvestigationGroupsModel.html
---

# ListInvestigationGroupsModel
<a name="API_ListInvestigationGroupsModel"></a>

This structure contains information about one investigation group in the account.

## Contents
<a name="API_ListInvestigationGroupsModel_Contents"></a>

 ** arn **   <a name="cloudwatchinvestigations-Type-ListInvestigationGroupsModel-arn"></a>
The Amazon Resource Name (ARN) of the investigation group.
Type: String
Pattern: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):aiops:[a-zA-Z0-9-]*:[0-9]{12}:investigation-group\/[A-Za-z0-9]{16}`
Required: No

 ** name **   <a name="cloudwatchinvestigations-Type-ListInvestigationGroupsModel-name"></a>
The name of the investigation group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\-_A-Za-z0-9\[\]\(\)\{\}\.: ]+`
Required: No

## See Also
<a name="API_ListInvestigationGroupsModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/aiops-2018-05-10/ListInvestigationGroupsModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/aiops-2018-05-10/ListInvestigationGroupsModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/aiops-2018-05-10/ListInvestigationGroupsModel)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CloudWatch investigations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatchinvestigations` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
