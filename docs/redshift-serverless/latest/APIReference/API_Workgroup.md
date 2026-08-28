---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_Workgroup.html
---

# Workgroup
<a name="API_Workgroup"></a>

The collection of computing resources from which an endpoint is created.

## Contents
<a name="API_Workgroup_Contents"></a>

 ** baseCapacity **   <a name="redshiftserverless-Type-Workgroup-baseCapacity"></a>
The base data warehouse capacity of the workgroup in Redshift Processing Units (RPUs).
Type: Integer
Required: No

 ** configParameters **   <a name="redshiftserverless-Type-Workgroup-configParameters"></a>
An array of parameters to set for advanced control over a database. The options are `auto_mv`, `datestyle`, `enable_case_sensitive_identifier`, `enable_user_activity_logging`, `query_group`, `search_path`, `require_ssl`, `use_fips_ssl`, and either `wlm_json_configuration` or query monitoring metrics that let you define performance boundaries. You can either specify individual query monitoring metrics (such as `max_scan_row_count`, `max_query_execution_time`) or use `wlm_json_configuration` to define query queues with rules, but not both. If you're using `wlm_json_configuration`, the maximum size of `parameterValue` is 8000 characters. For more information about query monitoring rules and available metrics, see [ Query monitoring metrics for Amazon Redshift Serverless](https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html#cm-c-wlm-query-monitoring-metrics-serverless).
Type: Array of [ConfigParameter](API_ConfigParameter.md) objects
Required: No

 ** creationDate **   <a name="redshiftserverless-Type-Workgroup-creationDate"></a>
The creation date of the workgroup.
Type: Timestamp
Required: No

 ** crossAccountVpcs **   <a name="redshiftserverless-Type-Workgroup-crossAccountVpcs"></a>
A list of VPCs. Each entry is the unique identifier of a virtual private cloud with access to Amazon Redshift Serverless. If all of the VPCs for the grantee are allowed, it shows an asterisk.
Type: Array of strings
Required: No

 ** customDomainCertificateArn **   <a name="redshiftserverless-Type-Workgroup-customDomainCertificateArn"></a>
The custom domain name’s certificate Amazon resource name (ARN).
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*arn:[\w+=/,.@-]+:acm:[\w+=/,.@-]*:[0-9]+:[\w+=,.@-]+(/[\w+=,.@-]+)*.*`
Required: No

 ** customDomainCertificateExpiryTime **   <a name="redshiftserverless-Type-Workgroup-customDomainCertificateExpiryTime"></a>
The expiration time for the certificate.
Type: Timestamp
Required: No

 ** customDomainName **   <a name="redshiftserverless-Type-Workgroup-customDomainName"></a>
The custom domain name associated with the workgroup.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 253.
Pattern: `(((?!-)[A-Za-z0-9-]{0,62}[A-Za-z0-9])\.)+((?!-)[A-Za-z0-9-]{1,62}[A-Za-z0-9])`
Required: No

 ** endpoint **   <a name="redshiftserverless-Type-Workgroup-endpoint"></a>
The endpoint that is created from the workgroup.
Type: [Endpoint](API_Endpoint.md) object
Required: No

 ** enhancedVpcRouting **   <a name="redshiftserverless-Type-Workgroup-enhancedVpcRouting"></a>
The value that specifies whether to enable enhanced virtual private cloud (VPC) routing, which forces Amazon Redshift Serverless to route traffic through your VPC.
Type: Boolean
Required: No

 ** extraComputeForAutomaticOptimization **   <a name="redshiftserverless-Type-Workgroup-extraComputeForAutomaticOptimization"></a>
A boolean value that, if `true`, indicates that the workgroup allocates additional compute resources to run automatic optimization operations.
Default: false
Type: Boolean
Required: No

 ** ipAddressType **   <a name="redshiftserverless-Type-Workgroup-ipAddressType"></a>
The IP address type that the workgroup supports. Possible values are `ipv4` and `dualstack`.
Type: String
Pattern: `(ipv4|dualstack)`
Required: No

 ** maxCapacity **   <a name="redshiftserverless-Type-Workgroup-maxCapacity"></a>
The maximum data-warehouse capacity Amazon Redshift Serverless uses to serve queries. The max capacity is specified in RPUs.
Type: Integer
Required: No

 ** namespaceName **   <a name="redshiftserverless-Type-Workgroup-namespaceName"></a>
The namespace the workgroup is associated with.
Type: String
Required: No

 ** patchVersion **   <a name="redshiftserverless-Type-Workgroup-patchVersion"></a>
The patch version of your Amazon Redshift Serverless workgroup. For more information about patch versions, see [Cluster versions for Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/cluster-versions.html).
Type: String
Required: No

 ** pendingTrackName **   <a name="redshiftserverless-Type-Workgroup-pendingTrackName"></a>
The name for the track that you want to assign to the workgroup. When the track changes, the workgroup is switched to the latest workgroup release available for the track. At this point, the track name is applied.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_]+`
Required: No

 ** port **   <a name="redshiftserverless-Type-Workgroup-port"></a>
The custom port to use when connecting to a workgroup. Valid port ranges are 5431-5455 and 8191-8215. The default is 5439.
Type: Integer
Required: No

 ** pricePerformanceTarget **   <a name="redshiftserverless-Type-Workgroup-pricePerformanceTarget"></a>
An object that represents the price performance target settings for the workgroup.
Type: [PerformanceTarget](API_PerformanceTarget.md) object
Required: No

 ** publiclyAccessible **   <a name="redshiftserverless-Type-Workgroup-publiclyAccessible"></a>
A value that specifies whether the workgroup can be accessible from a public network.
Type: Boolean
Required: No

 ** securityGroupIds **   <a name="redshiftserverless-Type-Workgroup-securityGroupIds"></a>
An array of security group IDs to associate with the workgroup.
Type: Array of strings
Required: No

 ** status **   <a name="redshiftserverless-Type-Workgroup-status"></a>
The status of the workgroup.
Type: String
Valid Values: `CREATING | AVAILABLE | MODIFYING | DELETING`
Required: No

 ** subnetIds **   <a name="redshiftserverless-Type-Workgroup-subnetIds"></a>
An array of subnet IDs the workgroup is associated with.
Type: Array of strings
Required: No

 ** trackName **   <a name="redshiftserverless-Type-Workgroup-trackName"></a>
The name of the track for the workgroup.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9_]+`
Required: No

 ** workgroupArn **   <a name="redshiftserverless-Type-Workgroup-workgroupArn"></a>
The Amazon Resource Name (ARN) that links to the workgroup.
Type: String
Required: No

 ** workgroupId **   <a name="redshiftserverless-Type-Workgroup-workgroupId"></a>
The unique identifier of the workgroup.
Type: String
Required: No

 ** workgroupName **   <a name="redshiftserverless-Type-Workgroup-workgroupName"></a>
The name of the workgroup.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z0-9-]+`
Required: No

 ** workgroupVersion **   <a name="redshiftserverless-Type-Workgroup-workgroupVersion"></a>
The Amazon Redshift Serverless version of your workgroup. For more information about Amazon Redshift Serverless versions, see[Cluster versions for Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/cluster-versions.html).
Type: String
Required: No

## See Also
<a name="API_Workgroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/Workgroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/Workgroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/Workgroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
