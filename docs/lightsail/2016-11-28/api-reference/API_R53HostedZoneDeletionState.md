---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_R53HostedZoneDeletionState.html
---

# R53HostedZoneDeletionState
<a name="API_R53HostedZoneDeletionState"></a>

Describes the deletion state of an Amazon Route 53 hosted zone for a domain that is being automatically delegated to an Amazon Lightsail DNS zone.

## Contents
<a name="API_R53HostedZoneDeletionState_Contents"></a>

 ** code **   <a name="Lightsail-Type-R53HostedZoneDeletionState-code"></a>
The status code for the deletion state.
Following are the possible values:
+  `SUCCEEDED` - The hosted zone was successfully deleted.
+  `PENDING` - The hosted zone deletion is in progress.
+  `FAILED` - The hosted zone deletion failed.
+  `STARTED` - The hosted zone deletion started.
Type: String
Valid Values: `SUCCEEDED | PENDING | FAILED | STARTED`
Required: No

 ** message **   <a name="Lightsail-Type-R53HostedZoneDeletionState-message"></a>
The message that describes the reason for the status code.
Type: String
Required: No

## See Also
<a name="API_R53HostedZoneDeletionState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/R53HostedZoneDeletionState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/R53HostedZoneDeletionState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/R53HostedZoneDeletionState)
