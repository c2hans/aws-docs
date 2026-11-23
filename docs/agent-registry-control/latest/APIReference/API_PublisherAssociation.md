---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_PublisherAssociation.html
---

# PublisherAssociation

An association between a registry record and a publisher, including the public identifier assigned to the registry record.

## Contents
<a name="API_PublisherAssociation_Contents"></a>

 ** publicIdentifier **   <a name="agentregistrycontrol-Type-PublisherAssociation-publicIdentifier"></a>
The public identifier assigned to the registry record. It has the form `urn:air:authority[:category...]:name[;kind]`:
+  `authority` - The publisher's domain, prefixed by the subdomain if you specified one.
+  `category` - The categories that you specified, if any.
+  `name` - The registry record's name.
+  `kind` - A suffix derived from the record type: `mcp`, `agent`, `skill`, or `webbot`. Gateway records have no suffix.
For example, `urn:air:agents.example.com:finance:weather;mcp`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[uU][rR][nN]:[aA][iI][rR]:([a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,63}:([a-zA-Z0-9._~!$&'()*+,;=:@/-]|%[0-9a-fA-F]{2})+(\?\+([a-zA-Z0-9._~!$&'()*+,;=:@-]|%[0-9a-fA-F]{2})([a-zA-Z0-9._~!$&'()*+,;=:@/?-]|%[0-9a-fA-F]{2})*)?(\?=([a-zA-Z0-9._~!$&'()*+,;=:@-]|%[0-9a-fA-F]{2})([a-zA-Z0-9._~!$&'()*+,;=:@/?-]|%[0-9a-fA-F]{2})*)?(#([a-zA-Z0-9._~!$&'()*+,;=:@/?-]|%[0-9a-fA-F]{2})*)?`
Required: Yes

 ** publisher **   <a name="agentregistrycontrol-Type-PublisherAssociation-publisher"></a>
The Amazon Resource Name (ARN) of the publisher that the registry record is associated with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):[a-z0-9-]+::[0-9]{12}:[a-zA-Z0-9._/-]+`
Required: Yes

 ** recordArn **   <a name="agentregistrycontrol-Type-PublisherAssociation-recordArn"></a>
The Amazon Resource Name (ARN) of the associated registry record.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws(-[^:]+)?:agent-registry:[a-z0-9-]+:[0-9]{12}:registry/[a-zA-Z0-9]{12,16}/record/[a-zA-Z0-9]{12}`
Required: Yes

 ** status **   <a name="agentregistrycontrol-Type-PublisherAssociation-status"></a>
The status of the association is one of the following:
+  `PENDING_APPROVAL` - The association is waiting for a curator to approve or reject it.
+  `APPROVED` - A curator approved the association.
+  `REJECTED` - A curator rejected the association.
+  `SUSPENDED` - The association was approved but is suspended, for example because the publisher's domain could no longer be verified. `statusReason`, when present, describes why.
Type: String
Valid Values: `PENDING_APPROVAL | APPROVED | REJECTED | SUSPENDED`
Required: Yes

 ** statusReason **   <a name="agentregistrycontrol-Type-PublisherAssociation-statusReason"></a>
The reason for the association's current status, such as why it is suspended. Present only when a reason is available.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\P{C}\t\r\n]*`
Required: No

## See Also
<a name="API_PublisherAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/PublisherAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/PublisherAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/PublisherAssociation)
