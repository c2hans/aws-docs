---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/API_MetadataTransferJobStatus.html
---

# MetadataTransferJobStatus
<a name="API_MetadataTransferJobStatus"></a>

The metadata transfer job status.

## Contents
<a name="API_MetadataTransferJobStatus_Contents"></a>

 ** error **   <a name="tm-Type-MetadataTransferJobStatus-error"></a>
The metadata transfer job error.
Type: [ErrorDetails](API_ErrorDetails.md) object
Required: No

 ** queuedPosition **   <a name="tm-Type-MetadataTransferJobStatus-queuedPosition"></a>
The queued position.
Type: Integer
Required: No

 ** state **   <a name="tm-Type-MetadataTransferJobStatus-state"></a>
The metadata transfer job state.
Type: String
Valid Values: `VALIDATING | PENDING | RUNNING | CANCELLING | ERROR | COMPLETED | CANCELLED`
Required: No

## See Also
<a name="API_MetadataTransferJobStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iottwinmaker-2021-11-29/MetadataTransferJobStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iottwinmaker-2021-11-29/MetadataTransferJobStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iottwinmaker-2021-11-29/MetadataTransferJobStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IoT TwinMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-twinmaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
