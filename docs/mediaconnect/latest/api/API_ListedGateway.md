---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_ListedGateway.html
---

# ListedGateway
<a name="API_ListedGateway"></a>

 A summary of a gateway, including its name, ARN, and status.

## Contents
<a name="API_ListedGateway_Contents"></a>

 ** gatewayArn **   <a name="mediaconnect-Type-ListedGateway-gatewayArn"></a>
 The Amazon Resource Name (ARN) of the gateway.
Type: String
Required: Yes

 ** gatewayState **   <a name="mediaconnect-Type-ListedGateway-gatewayState"></a>
 The status of the gateway.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | ERROR | DELETING | DELETED`
Required: Yes

 ** name **   <a name="mediaconnect-Type-ListedGateway-name"></a>
 The name of the gateway.
Type: String
Required: Yes

## See Also
<a name="API_ListedGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/ListedGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/ListedGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/ListedGateway)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
