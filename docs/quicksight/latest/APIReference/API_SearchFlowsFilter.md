---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SearchFlowsFilter.html
---

# SearchFlowsFilter
<a name="API_SearchFlowsFilter"></a>

A structure that contains the filter information when searching flows.

## Contents
<a name="API_SearchFlowsFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Name **   <a name="QS-Type-SearchFlowsFilter-Name"></a>
The name of the value that you want to use as a filter, for example `"Name": "DIRECT_QUICKSIGHT_SOLE_OWNER"`.
Valid values are defined as follows:
+  `assetName`: Any flows whose names have a substring match to this value will be returned.
+  `assetDescription`: Any flows whose descriptions have a substring match to this value will be returned.
+  `DIRECT_QUICKSIGHT_SOLE_OWNER`: Provide an ARN of a user or group, and any analyses with that ARN listed as the only owner of the analysis are returned. Implicit permissions from folders or groups are not considered.
+  `DIRECT_QUICKSIGHT_OWNER`: Provide an ARN of a user or group, and any analyses with that ARN listed as one of the owners of the analyses are returned. Implicit permissions from folders or groups are not considered.
+  `DIRECT_QUICKSIGHT_VIEWER_OR_OWNER`: Provide an ARN of a user or group, and any analyses with that ARN listed as one of the owners or viewers of the analyses are returned. Implicit permissions from folders or groups are not considered.
Type: String
Valid Values: `assetName | assetDescription | DIRECT_QUICKSIGHT_OWNER | DIRECT_QUICKSIGHT_VIEWER_OR_OWNER | DIRECT_QUICKSIGHT_SOLE_OWNER`
Required: Yes

 ** Operator **   <a name="QS-Type-SearchFlowsFilter-Operator"></a>
The comparison operator that you want to use as a filter, for example `"Operator": "StringEquals"`. Valid values are `"StringEquals"` and `"StringLike"`.
Type: String
Valid Values: `StringEquals | StringLike`
Required: Yes

 ** Value **   <a name="QS-Type-SearchFlowsFilter-Value"></a>
The value of the named item, in this case `DIRECT_QUICKSIGHT_SOLE_OWNER`, that you want to use as a filter, for example `"Value"`. An example is `"arn:aws:quicksight:us-east-1:1:user/default/UserName1"`.
Type: String
Required: Yes

## See Also
<a name="API_SearchFlowsFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SearchFlowsFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SearchFlowsFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SearchFlowsFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
