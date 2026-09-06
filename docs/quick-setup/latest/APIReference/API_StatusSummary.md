---
source_url: https://docs.aws.amazon.com/quick-setup/latest/APIReference/API_StatusSummary.html
---

# StatusSummary
<a name="API_StatusSummary"></a>

A summarized description of the status.

## Contents
<a name="API_StatusSummary_Contents"></a>

 ** LastUpdatedAt **   <a name="quicksetup-Type-StatusSummary-LastUpdatedAt"></a>
The datetime stamp when the status was last updated.
Type: Timestamp
Required: Yes

 ** StatusType **   <a name="quicksetup-Type-StatusSummary-StatusType"></a>
The type of a status summary.
Type: String
Valid Values: `Deployment | AsyncExecutions`
Required: Yes

 ** Status **   <a name="quicksetup-Type-StatusSummary-Status"></a>
The current status.
Type: String
Valid Values: `INITIALIZING | DEPLOYING | SUCCEEDED | DELETING | STOPPING | FAILED | STOPPED | DELETE_FAILED | STOP_FAILED | NONE`
Required: No

 ** StatusDetails **   <a name="quicksetup-Type-StatusSummary-StatusDetails"></a>
Details about the status.
Type: String to string map
Required: No

 ** StatusMessage **   <a name="quicksetup-Type-StatusSummary-StatusMessage"></a>
When applicable, returns an informational message relevant to the current status and status type of the status summary object. We don't recommend implementing parsing logic around this value since the messages returned can vary in format.
Type: String
Required: No

## See Also
<a name="API_StatusSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-quicksetup-2018-05-10/StatusSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-quicksetup-2018-05-10/StatusSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-quicksetup-2018-05-10/StatusSummary)
