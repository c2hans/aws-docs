---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_ListedBridge.html
---

# ListedBridge
<a name="API_ListedBridge"></a>

 Displays details of the selected bridge.

## Contents
<a name="API_ListedBridge_Contents"></a>

 ** bridgeArn **   <a name="mediaconnect-Type-ListedBridge-bridgeArn"></a>
 The ARN of the bridge.
Type: String
Required: Yes

 ** bridgeState **   <a name="mediaconnect-Type-ListedBridge-bridgeState"></a>
The state of the bridge.
Type: String
Valid Values: `CREATING | STANDBY | STARTING | DEPLOYING | ACTIVE | STOPPING | DELETING | DELETED | START_FAILED | START_PENDING | STOP_FAILED | UPDATING`
Required: Yes

 ** bridgeType **   <a name="mediaconnect-Type-ListedBridge-bridgeType"></a>
 The type of the bridge.
Type: String
Required: Yes

 ** name **   <a name="mediaconnect-Type-ListedBridge-name"></a>
 The name of the bridge.
Type: String
Required: Yes

 ** placementArn **   <a name="mediaconnect-Type-ListedBridge-placementArn"></a>
 The ARN of the gateway associated with the bridge.
Type: String
Required: Yes

## See Also
<a name="API_ListedBridge_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/ListedBridge)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/ListedBridge)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/ListedBridge)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
