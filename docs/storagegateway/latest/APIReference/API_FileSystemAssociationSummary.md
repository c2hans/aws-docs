---
source_url: https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_FileSystemAssociationSummary.html
---

# FileSystemAssociationSummary
<a name="API_FileSystemAssociationSummary"></a>

Gets the summary returned by `ListFileSystemAssociation`, which is a summary of a created file system association.

## Contents
<a name="API_FileSystemAssociationSummary_Contents"></a>

 ** FileSystemAssociationARN **   <a name="StorageGateway-Type-FileSystemAssociationSummary-FileSystemAssociationARN"></a>
The Amazon Resource Name (ARN) of the file system association.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 500.
Required: No

 ** FileSystemAssociationId **   <a name="StorageGateway-Type-FileSystemAssociationSummary-FileSystemAssociationId"></a>
The ID of the file system association.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 30.
Required: No

 ** FileSystemAssociationStatus **   <a name="StorageGateway-Type-FileSystemAssociationSummary-FileSystemAssociationStatus"></a>
The status of the file share. Valid Values: `AVAILABLE` \| `CREATING` \| `DELETING` \| `FORCE_DELETING` \| `UPDATING` \| `ERROR`
Type: String
Length Constraints: Minimum length of 3. Maximum length of 50.
Required: No

 ** GatewayARN **   <a name="StorageGateway-Type-FileSystemAssociationSummary-GatewayARN"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [ListGateways](API_ListGateways.md) operation to return a list of gateways for your account and AWS Region.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 500.
Required: No

## See Also
<a name="API_FileSystemAssociationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/storagegateway-2013-06-30/FileSystemAssociationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/storagegateway-2013-06-30/FileSystemAssociationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/storagegateway-2013-06-30/FileSystemAssociationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Storage Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query storagegateway` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
