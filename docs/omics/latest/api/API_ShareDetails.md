---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ShareDetails.html
---

# ShareDetails
<a name="API_ShareDetails"></a>

The details of a resource share.

## Contents
<a name="API_ShareDetails_Contents"></a>

 ** creationTime **   <a name="omics-Type-ShareDetails-creationTime"></a>
The timestamp of when the resource share was created.
Type: Timestamp
Required: No

 ** ownerId **   <a name="omics-Type-ShareDetails-ownerId"></a>
The account ID for the data owner. The owner creates the resource share.
Type: String
Required: No

 ** principalSubscriber **   <a name="omics-Type-ShareDetails-principalSubscriber"></a>
The principal subscriber is the account that is sharing the resource.
Type: String
Required: No

 ** resourceArn **   <a name="omics-Type-ShareDetails-resourceArn"></a>
The Arn of the shared resource.
Type: String
Required: No

 ** resourceId **   <a name="omics-Type-ShareDetails-resourceId"></a>
The ID of the shared resource.
Type: String
Required: No

 ** shareId **   <a name="omics-Type-ShareDetails-shareId"></a>
The ID of the resource share.
Type: String
Required: No

 ** shareName **   <a name="omics-Type-ShareDetails-shareName"></a>
The name of the resource share.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

 ** status **   <a name="omics-Type-ShareDetails-status"></a>
The status of the share.
Type: String
Valid Values: `PENDING | ACTIVATING | ACTIVE | DELETING | DELETED | FAILED`
Required: No

 ** statusMessage **   <a name="omics-Type-ShareDetails-statusMessage"></a>
The status message for a resource share. It provides additional details about the share status.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** updateTime **   <a name="omics-Type-ShareDetails-updateTime"></a>
The timestamp of the resource share update.
Type: Timestamp
Required: No

## See Also
<a name="API_ShareDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ShareDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ShareDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ShareDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
