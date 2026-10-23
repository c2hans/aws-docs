---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ReplicationFinding.html
---

# ReplicationFinding
<a name="API_ReplicationFinding"></a>

Contains information about a resource that could not be replicated across the Regions of a Global Resiliency deployment, including the reason and any action required to resolve it.

## Contents
<a name="API_ReplicationFinding_Contents"></a>

 ** Arn **   <a name="connect-Type-ReplicationFinding-Arn"></a>
The Amazon Resource Name (ARN) of the resource that the finding is for.
Type: String
Required: Yes

 ** Id **   <a name="connect-Type-ReplicationFinding-Id"></a>
The identifier of the resource that the finding is for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** ResourceType **   <a name="connect-Type-ReplicationFinding-ResourceType"></a>
The type of resource that the finding is for, such as `QUEUE` or `ROUTING_PROFILE`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** Message **   <a name="connect-Type-ReplicationFinding-Message"></a>
A human-readable description of the finding and the action, if any, required to resolve it.
Type: String
Length Constraints: Maximum length of 4096.
Required: No

 ** Name **   <a name="connect-Type-ReplicationFinding-Name"></a>
The name of the resource that the finding is for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** Operation **   <a name="connect-Type-ReplicationFinding-Operation"></a>
The replication operation that produced the finding, such as a create, update, or delete of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** ReferenceCode **   <a name="connect-Type-ReplicationFinding-ReferenceCode"></a>
A stable code that identifies the class of the finding. Use this code to look up the recommended steps to resolve the finding.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** Region **   <a name="connect-Type-ReplicationFinding-Region"></a>
The AWS Region that the finding was detected in.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 31.
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

## See Also
<a name="API_ReplicationFinding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ReplicationFinding)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ReplicationFinding)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ReplicationFinding)
