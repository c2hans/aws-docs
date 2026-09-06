---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_ConnectorCheck.html
---

# ConnectorCheck
<a name="API_ConnectorCheck"></a>

A check on a connector to identify connectivity health.

## Contents
<a name="API_ConnectorCheck_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** impairedSince **   <a name="evs-Type-ConnectorCheck-impairedSince"></a>
The time when connector health began to be impaired.
Type: Timestamp
Required: No

 ** lastCheckAttempt **   <a name="evs-Type-ConnectorCheck-lastCheckAttempt"></a>
The date and time of the last check attempt.
Type: Timestamp
Required: No

 ** result **   <a name="evs-Type-ConnectorCheck-result"></a>
The check result.
Type: String
Valid Values: `PASSED | FAILED | UNKNOWN`
Required: No

 ** type **   <a name="evs-Type-ConnectorCheck-type"></a>
The check type.
Type: String
Valid Values: `KEY_REUSE | KEY_COVERAGE | REACHABILITY | HOST_COUNT | VCENTER_REACHABILITY | VCENTER_VM_SYNC | VCENTER_VM_EVENT | OPERATIONS_MANAGER_REACHABILITY | SDDC_MANAGER_REACHABILITY | SDDC_MANAGER_HOST_COUNT | SDDC_MANAGER_KEY_COVERAGE | SDDC_MANAGER_KEY_REUSE | CONNECTOR_HEALTH`
Required: No

## See Also
<a name="API_ConnectorCheck_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/evs-2023-07-27/ConnectorCheck)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/evs-2023-07-27/ConnectorCheck)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/ConnectorCheck)
