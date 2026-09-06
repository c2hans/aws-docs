---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_SetupHistory.html
---

# SetupHistory
<a name="API_SetupHistory"></a>

Returns a list of the commands that were ran on the target resource.

The status of each command is also returned.

## Contents
<a name="API_SetupHistory_Contents"></a>

 ** executionDetails **   <a name="Lightsail-Type-SetupHistory-executionDetails"></a>
Describes the full details of the request.
Type: Array of [SetupExecutionDetails](API_SetupExecutionDetails.md) objects
Required: No

 ** operationId **   <a name="Lightsail-Type-SetupHistory-operationId"></a>
A GUID that's used to identify the operation.
Type: String
Pattern: `.*\S.*`
Required: No

 ** request **   <a name="Lightsail-Type-SetupHistory-request"></a>
Information about the specified request.
Type: [SetupRequest](API_SetupRequest.md) object
Required: No

 ** resource **   <a name="Lightsail-Type-SetupHistory-resource"></a>
The target resource name for the request.
Type: [SetupHistoryResource](API_SetupHistoryResource.md) object
Required: No

 ** status **   <a name="Lightsail-Type-SetupHistory-status"></a>
The status of the request.
Type: String
Valid Values: `succeeded | failed | inProgress`
Required: No

## See Also
<a name="API_SetupHistory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/SetupHistory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/SetupHistory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/SetupHistory)
