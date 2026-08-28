---
source_url: https://docs.aws.amazon.com/aws-supply-chain/latest/APIReference/API_BillOfMaterialsImportJob.html
---

# BillOfMaterialsImportJob
<a name="API_BillOfMaterialsImportJob"></a>

The BillOfMaterialsImportJob details.

## Contents
<a name="API_BillOfMaterialsImportJob_Contents"></a>

 ** instanceId **   <a name="supplychain-Type-BillOfMaterialsImportJob-instanceId"></a>
The BillOfMaterialsImportJob instanceId.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** jobId **   <a name="supplychain-Type-BillOfMaterialsImportJob-jobId"></a>
The BillOfMaterialsImportJob jobId.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** s3uri **   <a name="supplychain-Type-BillOfMaterialsImportJob-s3uri"></a>
The S3 URI from which the CSV is read.
Type: String
Length Constraints: Minimum length of 10.
Pattern: `[sS]3://[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]/.+`
Required: Yes

 ** status **   <a name="supplychain-Type-BillOfMaterialsImportJob-status"></a>
The BillOfMaterialsImportJob ConfigurationJobStatus.
Type: String
Valid Values: `NEW | FAILED | IN_PROGRESS | QUEUED | SUCCESS`
Required: Yes

 ** message **   <a name="supplychain-Type-BillOfMaterialsImportJob-message"></a>
When the BillOfMaterialsImportJob has reached a terminal state, there will be a message.
Type: String
Required: No

## See Also
<a name="API_BillOfMaterialsImportJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/supplychain-2024-01-01/BillOfMaterialsImportJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/supplychain-2024-01-01/BillOfMaterialsImportJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/supplychain-2024-01-01/BillOfMaterialsImportJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Supply Chain. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-supply-chain` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
