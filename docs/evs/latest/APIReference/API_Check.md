---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_Check.html
---

# Check
<a name="API_Check"></a>

A check on the environment to identify environment health and validate VMware VCF licensing compliance.

## Contents
<a name="API_Check_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** id **   <a name="evs-Type-Check-id"></a>
A unique ID for the check.
Type: String
Required: No

 ** impairedSince **   <a name="evs-Type-Check-impairedSince"></a>
The time when environment health began to be impaired.
Type: Timestamp
Required: No

 ** result **   <a name="evs-Type-Check-result"></a>
 The check result.
Type: String
Valid Values: `PASSED | FAILED | UNKNOWN`
Required: No

 ** type **   <a name="evs-Type-Check-type"></a>
The check type. Amazon EVS performs the following checks:
+  `KEY_REUSE`: Verifies that the VCF license key is not used by another Amazon EVS environment.
+  `KEY_COVERAGE`: Verifies that the VCF license key allocates sufficient vCPU cores for all deployed hosts.
+  `REACHABILITY`: Verifies that the Amazon EVS control plane has a persistent connection to SDDC Manager.
+  `HOST_COUNT`: Verifies that the environment meets the minimum host count.
+  `VCENTER_REACHABILITY`: Verifies vCenter Server reachability through the vCenter connector.
+  `VCENTER_VM_SYNC`: Verifies that the vCenter connector can synchronize VM inventory from vCenter Server.
+  `VCENTER_VM_EVENT`: Verifies that the vCenter connector can receive VM lifecycle events from vCenter Server.
+  `OPERATIONS_MANAGER_REACHABILITY`: Verifies Operations Manager reachability through the Operations Manager connector.
+  `SDDC_MANAGER_REACHABILITY`: Verifies SDDC Manager reachability through the SDDC Manager connector.
+  `SDDC_MANAGER_HOST_COUNT`: Verifies that the host count reported by SDDC Manager meets Amazon EVS minimum requirements.
+  `SDDC_MANAGER_KEY_COVERAGE`: Verifies that the VCF license key configured in SDDC Manager covers all deployed hosts.
+  `SDDC_MANAGER_KEY_REUSE`: Verifies that the VCF license key configured in SDDC Manager is not used by another Amazon EVS environment.
+  `CONNECTOR_HEALTH`: Aggregate health across all connectors in the environment.
Type: String
Valid Values: `KEY_REUSE | KEY_COVERAGE | REACHABILITY | HOST_COUNT | VCENTER_REACHABILITY | VCENTER_VM_SYNC | VCENTER_VM_EVENT | OPERATIONS_MANAGER_REACHABILITY | SDDC_MANAGER_REACHABILITY | SDDC_MANAGER_HOST_COUNT | SDDC_MANAGER_KEY_COVERAGE | SDDC_MANAGER_KEY_REUSE | CONNECTOR_HEALTH`
Required: No

## See Also
<a name="API_Check_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/evs-2023-07-27/Check)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/evs-2023-07-27/Check)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/Check)
