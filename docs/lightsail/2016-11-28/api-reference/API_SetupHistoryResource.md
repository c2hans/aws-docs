---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_SetupHistoryResource.html
---

# SetupHistoryResource
<a name="API_SetupHistoryResource"></a>

The Lightsail resource that `SetupHistory` was ran on.

## Contents
<a name="API_SetupHistoryResource_Contents"></a>

 ** arn **   <a name="Lightsail-Type-SetupHistoryResource-arn"></a>
The Amazon Resource Name (ARN) of the Lightsail resource.
Type: String
Pattern: `.*\S.*`
Required: No

 ** createdAt **   <a name="Lightsail-Type-SetupHistoryResource-createdAt"></a>
The timestamp for when the resource was created.
Type: Timestamp
Required: No

 ** location **   <a name="Lightsail-Type-SetupHistoryResource-location"></a>
Describes the resource location.
Type: [ResourceLocation](API_ResourceLocation.md) object
Required: No

 ** name **   <a name="Lightsail-Type-SetupHistoryResource-name"></a>
The name of the Lightsail resource.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** resourceType **   <a name="Lightsail-Type-SetupHistoryResource-resourceType"></a>
The Lightsail resource type. For example, `Instance`.
Type: String
Valid Values: `ContainerService | Instance | StaticIp | KeyPair | InstanceSnapshot | Domain | PeeredVpc | LoadBalancer | LoadBalancerTlsCertificate | Disk | DiskSnapshot | RelationalDatabase | RelationalDatabaseSnapshot | ExportSnapshotRecord | CloudFormationStackRecord | Alarm | ContactMethod | Distribution | Certificate | Bucket`
Required: No

## See Also
<a name="API_SetupHistoryResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/SetupHistoryResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/SetupHistoryResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/SetupHistoryResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
