---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_MetadataTransferJobSummary.html
---

# MetadataTransferJobSummary
<a name="API_MetadataTransferJobSummary"></a>

The metadata transfer job summary.

## Contents
<a name="API_MetadataTransferJobSummary_Contents"></a>

 ** arn **   <a name="tm-Type-MetadataTransferJobSummary-arn"></a>
The metadata transfer job summary ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:((aws)|(aws-cn)|(aws-us-gov)):iottwinmaker:[a-z0-9-]+:[0-9]{12}:[\/a-zA-Z0-9_\-\.:]+`
Required: Yes

 ** creationDateTime **   <a name="tm-Type-MetadataTransferJobSummary-creationDateTime"></a>
The metadata transfer job summary creation DateTime object.
Type: Timestamp
Required: Yes

 ** metadataTransferJobId **   <a name="tm-Type-MetadataTransferJobSummary-metadataTransferJobId"></a>
The metadata transfer job summary Id.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+`
Required: Yes

 ** status **   <a name="tm-Type-MetadataTransferJobSummary-status"></a>
The metadata transfer job summary status.
Type: [MetadataTransferJobStatus](API_MetadataTransferJobStatus.md) object
Required: Yes

 ** updateDateTime **   <a name="tm-Type-MetadataTransferJobSummary-updateDateTime"></a>
The metadata transfer job summary update DateTime object
Type: Timestamp
Required: Yes

 ** progress **   <a name="tm-Type-MetadataTransferJobSummary-progress"></a>
The metadata transfer job summary progress.
Type: [MetadataTransferJobProgress](API_MetadataTransferJobProgress.md) object
Required: No

## See Also
<a name="API_MetadataTransferJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/MetadataTransferJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/MetadataTransferJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/MetadataTransferJobSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IoT TwinMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-twinmaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
