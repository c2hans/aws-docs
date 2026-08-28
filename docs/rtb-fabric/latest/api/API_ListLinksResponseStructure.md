---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_ListLinksResponseStructure.html
---

# ListLinksResponseStructure
<a name="API_ListLinksResponseStructure"></a>

Describes a link.

## Contents
<a name="API_ListLinksResponseStructure_Contents"></a>

 ** createdAt **   <a name="rtbfabric-Type-ListLinksResponseStructure-createdAt"></a>
The timestamp of when the link was created.
Type: Timestamp
Required: Yes

 ** gatewayId **   <a name="rtbfabric-Type-ListLinksResponseStructure-gatewayId"></a>
The unique identifier of the gateway.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 32.
Pattern: `rtb-gw-[a-z0-9-]{1,25}`
Required: Yes

 ** linkId **   <a name="rtbfabric-Type-ListLinksResponseStructure-linkId"></a>
The unique identifier of the link.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 30.
Pattern: `link-[a-z0-9-]{1,25}`
Required: Yes

 ** peerGatewayId **   <a name="rtbfabric-Type-ListLinksResponseStructure-peerGatewayId"></a>
The unique identifier of the peer gateway.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 32.
Pattern: `rtb-gw-[a-z0-9-]{1,25}`
Required: Yes

 ** status **   <a name="rtbfabric-Type-ListLinksResponseStructure-status"></a>
The status of the link.
Type: String
Valid Values: `PENDING_CREATION | PENDING_REQUEST | REQUESTED | ACCEPTED | ACTIVE | REJECTED | FAILED | PENDING_DELETION | DELETED | PENDING_UPDATE | PENDING_ISOLATION | ISOLATED | PENDING_RESTORATION`
Required: Yes

 ** updatedAt **   <a name="rtbfabric-Type-ListLinksResponseStructure-updatedAt"></a>
The timestamp of when the link was updated.
Type: Timestamp
Required: Yes

 ** attributes **   <a name="rtbfabric-Type-ListLinksResponseStructure-attributes"></a>
Describes attributes of a link.
Type: [LinkAttributes](API_LinkAttributes.md) object
Required: No

 ** connectivityType **   <a name="rtbfabric-Type-ListLinksResponseStructure-connectivityType"></a>
The connectivity type of the link.
Type: String
Valid Values: `DEFAULT | PUBLIC_INGRESS | PUBLIC_EGRESS | EXTERNAL_INBOUND`
Required: No

 ** direction **   <a name="rtbfabric-Type-ListLinksResponseStructure-direction"></a>
The direction of the link.
Type: String
Valid Values: `RESPONSE | REQUEST`
Required: No

 ** flowModules **   <a name="rtbfabric-Type-ListLinksResponseStructure-flowModules"></a>
Describes the configuration of flow modules.
Type: Array of [ModuleConfiguration](API_ModuleConfiguration.md) objects
Required: No

 ** logSettings **   <a name="rtbfabric-Type-ListLinksResponseStructure-logSettings"></a>
Describes the settings for a link log.
Type: [LinkLogSettings](API_LinkLogSettings.md) object
Required: No

 ** pendingFlowModules **   <a name="rtbfabric-Type-ListLinksResponseStructure-pendingFlowModules"></a>
Describes the configuration of pending flow modules.
Type: Array of [ModuleConfiguration](API_ModuleConfiguration.md) objects
Required: No

 ** publicEndpoint **   <a name="rtbfabric-Type-ListLinksResponseStructure-publicEndpoint"></a>
The public endpoint of the outbound link.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `(https|http)://.+`
Required: No

 ** tags **   <a name="rtbfabric-Type-ListLinksResponseStructure-tags"></a>
A map of the key-value pairs of the tag or tags to assign to the resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(resourceArn|internalId|[a-zA-Z0-9+\-=._:/@]+)`
Value Length Constraints: Minimum length of 0. Maximum length of 1600.
Required: No

## See Also
<a name="API_ListLinksResponseStructure_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/ListLinksResponseStructure)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/ListLinksResponseStructure)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/ListLinksResponseStructure)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS RTB Fabric. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rtb-fabric` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
