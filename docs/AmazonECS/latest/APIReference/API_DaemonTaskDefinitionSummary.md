---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DaemonTaskDefinitionSummary.html
---

# DaemonTaskDefinitionSummary
<a name="API_DaemonTaskDefinitionSummary"></a>

A summary of a daemon task definition.

## Contents
<a name="API_DaemonTaskDefinitionSummary_Contents"></a>

 ** arn **   <a name="ECS-Type-DaemonTaskDefinitionSummary-arn"></a>
The Amazon Resource Name (ARN) of the daemon task definition.
Type: String
Required: No

 ** deleteRequestedAt **   <a name="ECS-Type-DaemonTaskDefinitionSummary-deleteRequestedAt"></a>
The Unix timestamp for the time when the daemon task definition delete was requested.
Type: Timestamp
Required: No

 ** registeredAt **   <a name="ECS-Type-DaemonTaskDefinitionSummary-registeredAt"></a>
The Unix timestamp for the time when the daemon task definition was registered.
Type: Timestamp
Required: No

 ** registeredBy **   <a name="ECS-Type-DaemonTaskDefinitionSummary-registeredBy"></a>
The principal that registered the daemon task definition.
Type: String
Required: No

 ** status **   <a name="ECS-Type-DaemonTaskDefinitionSummary-status"></a>
The status of the daemon task definition.
Type: String
Valid Values: `ACTIVE | DELETE_IN_PROGRESS | DELETED`
Required: No

## See Also
<a name="API_DaemonTaskDefinitionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DaemonTaskDefinitionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DaemonTaskDefinitionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DaemonTaskDefinitionSummary)
