---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_ProvisionData.html
---

# ProvisionData
<a name="API_ProvisionData"></a>

Information about provisioning resources for an AWS DMS serverless replication.

## Contents
<a name="API_ProvisionData_Contents"></a>

 ** DateNewProvisioningDataAvailable **   <a name="DMS-Type-ProvisionData-DateNewProvisioningDataAvailable"></a>
The timestamp when provisioning became available.
Type: Timestamp
Required: No

 ** DateProvisioned **   <a name="DMS-Type-ProvisionData-DateProvisioned"></a>
The timestamp when AWS DMS provisioned replication resources.
Type: Timestamp
Required: No

 ** IsNewProvisioningAvailable **   <a name="DMS-Type-ProvisionData-IsNewProvisioningAvailable"></a>
Whether the new provisioning is available to the replication.
Type: Boolean
Required: No

 ** ProvisionedCapacityUnits **   <a name="DMS-Type-ProvisionData-ProvisionedCapacityUnits"></a>
The number of capacity units the replication is using.
Type: Integer
Required: No

 ** ProvisionState **   <a name="DMS-Type-ProvisionData-ProvisionState"></a>
The current provisioning state
Type: String
Required: No

 ** ReasonForNewProvisioningData **   <a name="DMS-Type-ProvisionData-ReasonForNewProvisioningData"></a>
A message describing the reason that AWS DMS provisioned new resources for the serverless replication.
Type: String
Required: No

## See Also
<a name="API_ProvisionData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/ProvisionData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/ProvisionData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/ProvisionData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
