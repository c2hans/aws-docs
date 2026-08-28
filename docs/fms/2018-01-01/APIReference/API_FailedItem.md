---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_FailedItem.html
---

# FailedItem
<a name="API_FailedItem"></a>

Details of a resource that failed when trying to update it's association to a resource set.

## Contents
<a name="API_FailedItem_Contents"></a>

 ** Reason **   <a name="fms-Type-FailedItem-Reason"></a>
The reason the resource's association could not be updated.
Type: String
Valid Values: `NOT_VALID_ARN | NOT_VALID_PARTITION | NOT_VALID_REGION | NOT_VALID_SERVICE | NOT_VALID_RESOURCE_TYPE | NOT_VALID_ACCOUNT_ID`
Required: No

 ** URI **   <a name="fms-Type-FailedItem-URI"></a>
The univeral resource indicator (URI) of the resource that failed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_FailedItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/FailedItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/FailedItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/FailedItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for 1.0. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
