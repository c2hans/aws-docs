---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_PrivateConnectionProvisioningState.html
---

# PrivateConnectionProvisioningState
<a name="API_PrivateConnectionProvisioningState"></a>

 Specifies the private connection provisioning state.

## Contents
<a name="API_PrivateConnectionProvisioningState_Contents"></a>

 ** failureCause **   <a name="appflow-Type-PrivateConnectionProvisioningState-failureCause"></a>
 Specifies the private connection provisioning failure cause.
Type: String
Valid Values: `CONNECTOR_AUTHENTICATION | CONNECTOR_SERVER | INTERNAL_SERVER | ACCESS_DENIED | VALIDATION`
Required: No

 ** failureMessage **   <a name="appflow-Type-PrivateConnectionProvisioningState-failureMessage"></a>
 Specifies the private connection provisioning failure reason.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `[\s\w/!@#+=.-]*`
Required: No

 ** status **   <a name="appflow-Type-PrivateConnectionProvisioningState-status"></a>
 Specifies the private connection provisioning status.
Type: String
Valid Values: `FAILED | PENDING | CREATED`
Required: No

## See Also
<a name="API_PrivateConnectionProvisioningState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/PrivateConnectionProvisioningState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/PrivateConnectionProvisioningState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/PrivateConnectionProvisioningState)
