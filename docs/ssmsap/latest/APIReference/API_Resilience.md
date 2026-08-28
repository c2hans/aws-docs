---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_Resilience.html
---

# Resilience
<a name="API_Resilience"></a>

Details of the SAP HANA system replication for the instance.

## Contents
<a name="API_Resilience_Contents"></a>

 ** ClusterStatus **   <a name="ssmsap-Type-Resilience-ClusterStatus"></a>
The cluster status of the component.
Type: String
Valid Values: `ONLINE | STANDBY | MAINTENANCE | OFFLINE | NONE`
Required: No

 ** EnqueueReplication **   <a name="ssmsap-Type-Resilience-EnqueueReplication"></a>
Indicates if or not enqueue replication is enabled for the ASCS component.
Type: Boolean
Required: No

 ** HsrOperationMode **   <a name="ssmsap-Type-Resilience-HsrOperationMode"></a>
The operation mode of the component.
Type: String
Valid Values: `PRIMARY | LOGREPLAY | DELTA_DATASHIPPING | LOGREPLAY_READACCESS | NONE`
Required: No

 ** HsrReplicationMode **   <a name="ssmsap-Type-Resilience-HsrReplicationMode"></a>
The replication mode of the component.
Type: String
Valid Values: `PRIMARY | NONE | SYNC | SYNCMEM | ASYNC`
Required: No

 ** HsrTier **   <a name="ssmsap-Type-Resilience-HsrTier"></a>
The tier of the component.
Type: String
Required: No

## See Also
<a name="API_Resilience_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/Resilience)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/Resilience)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/Resilience)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager for SAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ssmsap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
