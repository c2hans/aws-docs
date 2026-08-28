---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_RelationalDatabaseSnapshot.html
---

# RelationalDatabaseSnapshot
<a name="API_RelationalDatabaseSnapshot"></a>

Describes a database snapshot.

## Contents
<a name="API_RelationalDatabaseSnapshot_Contents"></a>

 ** arn **   <a name="Lightsail-Type-RelationalDatabaseSnapshot-arn"></a>
The Amazon Resource Name (ARN) of the database snapshot.
Type: String
Pattern: `.*\S.*`
Required: No

 ** createdAt **   <a name="Lightsail-Type-RelationalDatabaseSnapshot-createdAt"></a>
The timestamp when the database snapshot was created.
Type: Timestamp
Required: No

 ** engine **   <a name="Lightsail-Type-RelationalDatabaseSnapshot-engine"></a>
The software of the database snapshot (for example, `MySQL`)
Type: String
Pattern: `.*\S.*`
Required: No

 ** engineVersion **   <a name="Lightsail-Type-RelationalDatabaseSnapshot-engineVersion"></a>
The database engine version for the database snapshot (for example, `5.7.23`).
Type: String
Pattern: `.*\S.*`
Required: No

 ** fromRelationalDatabaseArn **   <a name="Lightsail-Type-RelationalDatabaseSnapshot-fromRelationalDatabaseArn"></a>
The Amazon Resource Name (ARN) of the database from which the database snapshot was created.
Type: String
Pattern: `.*\S.*`
Required: No

 ** fromRelationalDatabaseBlueprintId **   <a name="Lightsail-Type-RelationalDatabaseSnapshot-fromRelationalDatabaseBlueprintId"></a>
The blueprint ID of the database from which the database snapshot was created. A blueprint describes the major engine version of a database.
Type: String
Required: No

 ** fromRelationalDatabaseBundleId **   <a name="Lightsail-Type-RelationalDatabaseSnapshot-fromRelationalDatabaseBundleId"></a>
The bundle ID of the database from which the database snapshot was created.
Type: String
Required: No

 ** fromRelationalDatabaseName **   <a name="Lightsail-Type-RelationalDatabaseSnapshot-fromRelationalDatabaseName"></a>
The name of the source database from which the database snapshot was created.
Type: String
Pattern: `.*\S.*`
Required: No

 ** location **   <a name="Lightsail-Type-RelationalDatabaseSnapshot-location"></a>
The Region name and Availability Zone where the database snapshot is located.
Type: [ResourceLocation](API_ResourceLocation.md) object
Required: No

 ** name **   <a name="Lightsail-Type-RelationalDatabaseSnapshot-name"></a>
The name of the database snapshot.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

 ** resourceType **   <a name="Lightsail-Type-RelationalDatabaseSnapshot-resourceType"></a>
The Lightsail resource type.
Type: String
Valid Values: `ContainerService | Instance | StaticIp | KeyPair | InstanceSnapshot | Domain | PeeredVpc | LoadBalancer | LoadBalancerTlsCertificate | Disk | DiskSnapshot | RelationalDatabase | RelationalDatabaseSnapshot | ExportSnapshotRecord | CloudFormationStackRecord | Alarm | ContactMethod | Distribution | Certificate | Bucket`
Required: No

 ** sizeInGb **   <a name="Lightsail-Type-RelationalDatabaseSnapshot-sizeInGb"></a>
The size of the disk in GB (for example, `32`) for the database snapshot.
Type: Integer
Required: No

 ** state **   <a name="Lightsail-Type-RelationalDatabaseSnapshot-state"></a>
The state of the database snapshot.
Type: String
Pattern: `.*\S.*`
Required: No

 ** supportCode **   <a name="Lightsail-Type-RelationalDatabaseSnapshot-supportCode"></a>
The support code for the database snapshot. Include this code in your email to support when you have questions about a database snapshot in Lightsail. This code enables our support team to look up your Lightsail information more easily.
Type: String
Required: No

 ** tags **   <a name="Lightsail-Type-RelationalDatabaseSnapshot-tags"></a>
The tag keys and optional values for the resource. For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags).
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_RelationalDatabaseSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/RelationalDatabaseSnapshot)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/RelationalDatabaseSnapshot)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/RelationalDatabaseSnapshot)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
