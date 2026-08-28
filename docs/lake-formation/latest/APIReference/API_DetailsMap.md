---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_DetailsMap.html
---

# DetailsMap
<a name="API_DetailsMap"></a>

A structure containing the additional details to be returned in the `AdditionalDetails` attribute of `PrincipalResourcePermissions`.

If a catalog resource is shared through AWS Resource Access Manager (AWS RAM), then there will exist a corresponding AWS RAM resource share ARN.

## Contents
<a name="API_DetailsMap_Contents"></a>

 ** ResourceShare **   <a name="lakeformation-Type-DetailsMap-ResourceShare"></a>
A resource share ARN for a catalog resource shared through AWS RAM.
Type: Array of strings
Required: No

## See Also
<a name="API_DetailsMap_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/DetailsMap)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/DetailsMap)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/DetailsMap)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
