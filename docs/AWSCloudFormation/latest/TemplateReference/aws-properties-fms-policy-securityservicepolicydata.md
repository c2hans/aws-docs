---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-fms-policy-securityservicepolicydata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FMS::Policy SecurityServicePolicyData
<a name="aws-properties-fms-policy-securityservicepolicydata"></a>

Details about the security service that is being used to protect the resources.

## Syntax
<a name="aws-properties-fms-policy-securityservicepolicydata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-fms-policy-securityservicepolicydata-syntax.json"></a>

```
{
  "[ManagedServiceData](#cfn-fms-policy-securityservicepolicydata-managedservicedata)" : {{String}},
  "[PolicyOption](#cfn-fms-policy-securityservicepolicydata-policyoption)" : {{PolicyOption}},
  "[Type](#cfn-fms-policy-securityservicepolicydata-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-fms-policy-securityservicepolicydata-syntax.yaml"></a>

```
  [ManagedServiceData](#cfn-fms-policy-securityservicepolicydata-managedservicedata): {{String}}
  [PolicyOption](#cfn-fms-policy-securityservicepolicydata-policyoption): {{
    PolicyOption}}
  [Type](#cfn-fms-policy-securityservicepolicydata-type): {{String}}
```

## Properties
<a name="aws-properties-fms-policy-securityservicepolicydata-properties"></a>

`ManagedServiceData`  <a name="cfn-fms-policy-securityservicepolicydata-managedservicedata"></a>
Details about the service that are specific to the service type, in JSON format.
+ Example: `DNS_FIREWALL`

   `"{\"type\":\"DNS_FIREWALL\",\"preProcessRuleGroups\":[{\"ruleGroupId\":\"rslvr-frg-1\",\"priority\":10}],\"postProcessRuleGroups\":[{\"ruleGroupId\":\"rslvr-frg-2\",\"priority\":9911}]}"`
**Note**
Valid values for `preProcessRuleGroups` are between 1 and 99. Valid values for `postProcessRuleGroups` are between 9901 and 10000.
+ Example: `NETWORK_FIREWALL` - Centralized deployment model

   `"{\"type\":\"NETWORK_FIREWALL\",\"awsNetworkFirewallConfig\":{\"networkFirewallStatelessRuleGroupReferences\":[{\"resourceARN\":\"arn:aws:network-firewall:us-east-1:123456789011:stateless-rulegroup/test\",\"priority\":1}],\"networkFirewallStatelessDefaultActions\":[\"aws:forward_to_sfe\",\"customActionName\"],\"networkFirewallStatelessFragmentDefaultActions\":[\"aws:forward_to_sfe\",\"customActionName\"],\"networkFirewallStatelessCustomActions\":[{\"actionName\":\"customActionName\",\"actionDefinition\":{\"publishMetricAction\":{\"dimensions\":[{\"value\":\"metricdimensionvalue\"}]}}}],\"networkFirewallStatefulRuleGroupReferences\":[{\"resourceARN\":\"arn:aws:network-firewall:us-east-1:123456789011:stateful-rulegroup/test\"}],\"networkFirewallLoggingConfiguration\":{\"logDestinationConfigs\":[{\"logDestinationType\":\"S3\",\"logType\":\"ALERT\",\"logDestination\":{\"bucketName\":\"s3-bucket-name\"}},{\"logDestinationType\":\"S3\",\"logType\":\"FLOW\",\"logDestination\":{\"bucketName\":\"s3-bucket-name\"}}],\"overrideExistingConfig\":true}},\"firewallDeploymentModel\":{\"centralizedFirewallDeploymentModel\":{\"centralizedFirewallOrchestrationConfig\":{\"inspectionVpcIds\":[{\"resourceId\":\"vpc-1234\",\"accountId\":\"123456789011\"}],\"firewallCreationConfig\":{\"endpointLocation\":{\"availabilityZoneConfigList\":[{\"availabilityZoneId\":null,\"availabilityZoneName\":\"us-east-1a\",\"allowedIPV4CidrList\":[\"10.0.0.0/28\"]}]}},\"allowedIPV4CidrList\":[]}}}}"`

  To use the distributed deployment model, you must set [FirewallDeploymentModel](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html) to `DISTRIBUTED`.
+ Example: `NETWORK_FIREWALL` - Distributed deployment model with automatic Availability Zone configuration

   ` "{\"type\":\"NETWORK_FIREWALL\",\"networkFirewallStatelessRuleGroupReferences\":[{\"resourceARN\":\"arn:aws:network-firewall:us-east-1:123456789011:stateless-rulegroup/test\",\"priority\":1}],\"networkFirewallStatelessDefaultActions\":[\"aws:forward_to_sfe\",\"customActionName\"],\"networkFirewallStatelessFragmentDefaultActions\":[\"aws:forward_to_sfe\",\"customActionName\"],\"networkFirewallStatelessCustomActions\":[{\"actionName\":\"customActionName\",\"actionDefinition\":{\"publishMetricAction\":{\"dimensions\":[{\"value\":\"metricdimensionvalue\"}]}}}],\"networkFirewallStatefulRuleGroupReferences\":[{\"resourceARN\":\"arn:aws:network-firewall:us-east-1:123456789011:stateful-rulegroup/test\"}],\"networkFirewallOrchestrationConfig\":{\"singleFirewallEndpointPerVPC\":false,\"allowedIPV4CidrList\":[\"10.0.0.0/28\",\"192.168.0.0/28\"],\"routeManagementAction\":\"OFF\"},\"networkFirewallLoggingConfiguration\":{\"logDestinationConfigs\":[{\"logDestinationType\":\"S3\",\"logType\":\"ALERT\",\"logDestination\":{\"bucketName\":\"s3-bucket-name\"}},{\"logDestinationType\":\"S3\",\"logType\":\"FLOW\",\"logDestination\":{\"bucketName\":\"s3-bucket-name\"}}],\"overrideExistingConfig\":true}}" `

   With automatic Availbility Zone configuration, Firewall Manager chooses which Availability Zones to create the endpoints in. To use the distributed deployment model, you must set [FirewallDeploymentModel](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html) to `DISTRIBUTED`.
+ Example: `NETWORK_FIREWALL` - Distributed deployment model with automatic Availability Zone configuration and route management

   ` "{\"type\":\"NETWORK_FIREWALL\",\"networkFirewallStatelessRuleGroupReferences\":[{\"resourceARN\":\"arn:aws:network-firewall:us-east-1:123456789011:stateless-rulegroup/test\",\"priority\":1}],\"networkFirewallStatelessDefaultActions\":[\"aws:forward_to_sfe\",\"customActionName\"],\"networkFirewallStatelessFragmentDefaultActions\":[\"aws:forward_to_sfe\",\"customActionName\"],\"networkFirewallStatelessCustomActions\":[{\"actionName\":\"customActionName\",\"actionDefinition\":{\"publishMetricAction\":{\"dimensions\":[{\"value\":\"metricdimensionvalue\"}]}}}],\"networkFirewallStatefulRuleGroupReferences\":[{\"resourceARN\":\"arn:aws:network-firewall:us-east-1:123456789011:stateful-rulegroup/test\"}],\"networkFirewallOrchestrationConfig\":{\"singleFirewallEndpointPerVPC\":false,\"allowedIPV4CidrList\":[\"10.0.0.0/28\",\"192.168.0.0/28\"],\"routeManagementAction\":\"MONITOR\",\"routeManagementTargetTypes\":[\"InternetGateway\"]},\"networkFirewallLoggingConfiguration\":{\"logDestinationConfigs\":[{\"logDestinationType\":\"S3\",\"logType\":\"ALERT\",\"logDestination\":{\"bucketName\":\"s3-bucket-name\"}},{\"logDestinationType\":\"S3\",\"logType\": \"FLOW\",\"logDestination\":{\"bucketName\":\"s3-bucket-name\"}}],\"overrideExistingConfig\":true}}" `

  To use the distributed deployment model, you must set [FirewallDeploymentModel](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html) to `DISTRIBUTED`.
+ Example: `NETWORK_FIREWALL` - Distributed deployment model with custom Availability Zone configuration

   `"{\"type\":\"NETWORK_FIREWALL\",\"networkFirewallStatelessRuleGroupReferences\":[{\"resourceARN\":\"arn:aws:network-firewall:us-east-1:123456789011:stateless-rulegroup/test\",\"priority\":1}],\"networkFirewallStatelessDefaultActions\":[\"aws:forward_to_sfe\",\"customActionName\"],\"networkFirewallStatelessFragmentDefaultActions\":[\"aws:forward_to_sfe\",\"fragmentcustomactionname\"],\"networkFirewallStatelessCustomActions\":[{\"actionName\":\"customActionName\", \"actionDefinition\":{\"publishMetricAction\":{\"dimensions\":[{\"value\":\"metricdimensionvalue\"}]}}},{\"actionName\":\"fragmentcustomactionname\",\"actionDefinition\":{\"publishMetricAction\":{\"dimensions\":[{\"value\":\"fragmentmetricdimensionvalue\"}]}}}],\"networkFirewallStatefulRuleGroupReferences\":[{\"resourceARN\":\"arn:aws:network-firewall:us-east-1:123456789011:stateful-rulegroup/test\"}],\"networkFirewallOrchestrationConfig\":{\"firewallCreationConfig\":{ \"endpointLocation\":{\"availabilityZoneConfigList\":[{\"availabilityZoneName\":\"us-east-1a\",\"allowedIPV4CidrList\":[\"10.0.0.0/28\"]},{\"availabilityZoneName\":\"us-east-1b\",\"allowedIPV4CidrList\":[ \"10.0.0.0/28\"]}]} },\"singleFirewallEndpointPerVPC\":false,\"allowedIPV4CidrList\":null,\"routeManagementAction\":\"OFF\",\"networkFirewallLoggingConfiguration\":{\"logDestinationConfigs\":[{\"logDestinationType\":\"S3\",\"logType\":\"ALERT\",\"logDestination\":{\"bucketName\":\"s3-bucket-name\"}},{\"logDestinationType\":\"S3\",\"logType\":\"FLOW\",\"logDestination\":{\"bucketName\":\"s3-bucket-name\"}}],\"overrideExistingConfig\":boolean}}" `

   With custom Availability Zone configuration, you define which specific Availability Zones to create endpoints in by configuring `firewallCreationConfig`. To configure the Availability Zones in `firewallCreationConfig`, specify either the `availabilityZoneName` or `availabilityZoneId` parameter, not both parameters.

  To use the distributed deployment model, you must set [FirewallDeploymentModel](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html) to `DISTRIBUTED`.
+ Example: `NETWORK_FIREWALL` - Distributed deployment model with custom Availability Zone configuration and route management

   `"{\"type\":\"NETWORK_FIREWALL\",\"networkFirewallStatelessRuleGroupReferences\":[{\"resourceARN\":\"arn:aws:network-firewall:us-east-1:123456789011:stateless-rulegroup/test\",\"priority\":1}],\"networkFirewallStatelessDefaultActions\":[\"aws:forward_to_sfe\",\"customActionName\"],\"networkFirewallStatelessFragmentDefaultActions\":[\"aws:forward_to_sfe\",\"fragmentcustomactionname\"],\"networkFirewallStatelessCustomActions\":[{\"actionName\":\"customActionName\",\"actionDefinition\":{\"publishMetricAction\":{\"dimensions\":[{\"value\":\"metricdimensionvalue\"}]}}},{\"actionName\":\"fragmentcustomactionname\",\"actionDefinition\":{\"publishMetricAction\":{\"dimensions\":[{\"value\":\"fragmentmetricdimensionvalue\"}]}}}],\"networkFirewallStatefulRuleGroupReferences\":[{\"resourceARN\":\"arn:aws:network-firewall:us-east-1:123456789011:stateful-rulegroup/test\"}],\"networkFirewallOrchestrationConfig\":{\"firewallCreationConfig\":{\"endpointLocation\":{\"availabilityZoneConfigList\":[{\"availabilityZoneName\":\"us-east-1a\",\"allowedIPV4CidrList\":[\"10.0.0.0/28\"]},{\"availabilityZoneName\":\"us-east-1b\",\"allowedIPV4CidrList\":[\"10.0.0.0/28\"]}]}},\"singleFirewallEndpointPerVPC\":false,\"allowedIPV4CidrList\":null,\"routeManagementAction\":\"MONITOR\",\"routeManagementTargetTypes\":[\"InternetGateway\"],\"routeManagementConfig\":{\"allowCrossAZTrafficIfNoEndpoint\":true}},\"networkFirewallLoggingConfiguration\":{\"logDestinationConfigs\":[{\"logDestinationType\":\"S3\",\"logType\":\"ALERT\",\"logDestination\":{\"bucketName\":\"s3-bucket-name\"}},{\"logDestinationType\":\"S3\",\"logType\":\"FLOW\",\"logDestination\":{\"bucketName\":\"s3-bucket-name\"}}],\"overrideExistingConfig\":boolean}}" `

  To use the distributed deployment model, you must set [FirewallDeploymentModel](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-networkfirewallpolicy.html) to `DISTRIBUTED`.
+ Example: `THIRD_PARTY_FIREWALL` - Palo Alto Networks Cloud Next-Generation Firewall centralized deployment model

   `"{ \"type\":\"THIRD_PARTY_FIREWALL\", \"thirdPartyFirewall\":\"PALO_ALTO_NETWORKS_CLOUD_NGFW\", \"thirdPartyFirewallConfig\":{ \"thirdPartyFirewallPolicyList\":[\"global-1\"] },\"firewallDeploymentModel\":{\"centralizedFirewallDeploymentModel\":{\"centralizedFirewallOrchestrationConfig\":{\"inspectionVpcIds\":[{\"resourceId\":\"vpc-1234\",\"accountId\":\"123456789011\"}],\"firewallCreationConfig\":{\"endpointLocation\":{\"availabilityZoneConfigList\":[{\"availabilityZoneId\":null,\"availabilityZoneName\":\"us-east-1a\",\"allowedIPV4CidrList\":[\"10.0.0.0/28\"]}]}},\"allowedIPV4CidrList\":[]}}}}"`

  To use the distributed deployment model, you must set [FirewallDeploymentModel](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-thirdpartyfirewallpolicy.html) to `CENTRALIZED`.
+ Example: `THIRD_PARTY_FIREWALL` - Palo Alto Networks Cloud Next-Generation Firewall distributed deployment model

   `"{\"type\":\"THIRD_PARTY_FIREWALL\",\"thirdPartyFirewall\":\"PALO_ALTO_NETWORKS_CLOUD_NGFW\",\"thirdPartyFirewallConfig\":{\"thirdPartyFirewallPolicyList\":[\"global-1\"] },\"firewallDeploymentModel\":{ \"distributedFirewallDeploymentModel\":{ \"distributedFirewallOrchestrationConfig\":{\"firewallCreationConfig\":{\"endpointLocation\":{ \"availabilityZoneConfigList\":[ {\"availabilityZoneName\":\"${AvailabilityZone}\" } ] } }, \"allowedIPV4CidrList\":[ ] } } } }"`

  To use the distributed deployment model, you must set [FirewallDeploymentModel](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-fms-policy-thirdpartyfirewallpolicy.html) to `DISTRIBUTED`.
+ Specification for `SHIELD_ADVANCED` for Amazon CloudFront distributions

   `"{\"type\":\"SHIELD_ADVANCED\",\"automaticResponseConfiguration\": {\"automaticResponseStatus\":\"ENABLED|IGNORED|DISABLED\", \"automaticResponseAction\":\"BLOCK|COUNT\"}, \"overrideCustomerWebaclClassic\":true|false}"`

  For example: `"{\"type\":\"SHIELD_ADVANCED\",\"automaticResponseConfiguration\": {\"automaticResponseStatus\":\"ENABLED\", \"automaticResponseAction\":\"COUNT\"}}"`

  The default value for `automaticResponseStatus` is `IGNORED`. The value for `automaticResponseAction` is only required when `automaticResponseStatus` is set to `ENABLED`. The default value for `overrideCustomerWebaclClassic` is `false`.

  For other resource types that you can protect with a Shield Advanced policy, this `ManagedServiceData` configuration is an empty string.
+ Example: `WAFV2`

   `"{\"type\":\"WAFV2\",\"preProcessRuleGroups\":[{\"ruleGroupArn\":null,\"overrideAction\":{\"type\":\"NONE\"},\"managedRuleGroupIdentifier\":{\"version\":null,\"vendorName\":\"AWS\",\"managedRuleGroupName\":\"AWSManagedRulesAmazonIpReputationList\"},\"ruleGroupType\":\"ManagedRuleGroup\",\"excludeRules\":[{\"name\":\"NoUserAgent_HEADER\"}]}],\"postProcessRuleGroups\":[],\"defaultAction\":{\"type\":\"ALLOW\"},\"overrideCustomerWebACLAssociation\":false,\"loggingConfiguration\":{\"logDestinationConfigs\":[\"arn:aws:firehose:us-west-2:12345678912:deliverystream/aws-waf-logs-fms-admin-destination\"],\"redactedFields\":[{\"redactedFieldType\":\"SingleHeader\",\"redactedFieldValue\":\"Cookies\"},{\"redactedFieldType\":\"Method\"}]}}"`

  In the `loggingConfiguration`, you can specify one `logDestinationConfigs`, you can optionally provide up to 20 `redactedFields`, and the `RedactedFieldType` must be one of `URI`, `QUERY_STRING`, `HEADER`, or `METHOD`.
+ Example: `AWS WAF Classic`

   `"{\"type\": \"WAF\", \"ruleGroups\": [{\"id\":\"12345678-1bcd-9012-efga-0987654321ab\", \"overrideAction\" : {\"type\": \"COUNT\"}}], \"defaultAction\": {\"type\": \"BLOCK\"}}"`
+ Example: `WAFV2` - AWS Firewall Manager support for AWS WAF managed rule group versioning

   `"{\"type\":\"WAFV2\",\"preProcessRuleGroups\":[{\"ruleGroupArn\":null,\"overrideAction\":{\"type\":\"NONE\"},\"managedRuleGroupIdentifier\":{\"versionEnabled\":true,\"version\":\"Version_2.0\",\"vendorName\":\"AWS\",\"managedRuleGroupName\":\"AWSManagedRulesCommonRuleSet\"},\"ruleGroupType\":\"ManagedRuleGroup\",\"excludeRules\":[{\"name\":\"NoUserAgent_HEADER\"}]}],\"postProcessRuleGroups\":[],\"defaultAction\":{\"type\":\"ALLOW\"},\"overrideCustomerWebACLAssociation\":false,\"loggingConfiguration\":{\"logDestinationConfigs\":[\"arn:aws:firehose:us-west-2:12345678912:deliverystream/aws-waf-logs-fms-admin-destination\"],\"redactedFields\":[{\"redactedFieldType\":\"SingleHeader\",\"redactedFieldValue\":\"Cookies\"},{\"redactedFieldType\":\"Method\"}]}}"`

   To use a specific version of a AWS WAF managed rule group in your Firewall Manager policy, you must set `versionEnabled` to `true`, and set `version` to the version you'd like to use. If you don't set `versionEnabled` to `true`, or if you omit `versionEnabled`, then Firewall Manager uses the default version of the AWS WAF managed rule group.
+ Example: `SECURITY_GROUPS_COMMON`

   `"{\"type\":\"SECURITY_GROUPS_COMMON\",\"revertManualSecurityGroupChanges\":false,\"exclusiveResourceSecurityGroupManagement\":false, \"applyToAllEC2InstanceENIs\":false,\"securityGroups\":[{\"id\":\" sg-000e55995d61a06bd\"}]}"`
+ Example: Shared VPCs. Apply the preceding policy to resources in shared VPCs as well as to those in VPCs that the account owns

   `"{\"type\":\"SECURITY_GROUPS_COMMON\",\"revertManualSecurityGroupChanges\":false,\"exclusiveResourceSecurityGroupManagement\":false, \"applyToAllEC2InstanceENIs\":false,\"includeSharedVPC\":true,\"securityGroups\":[{\"id\":\" sg-000e55995d61a06bd\"}]}"`
+ Example: `SECURITY_GROUPS_CONTENT_AUDIT`

   `"{\"type\":\"SECURITY_GROUPS_CONTENT_AUDIT\",\"securityGroups\":[{\"id\":\"sg-000e55995d61a06bd\"}],\"securityGroupAction\":{\"type\":\"ALLOW\"}}"`

  The security group action for content audit can be `ALLOW` or `DENY`. For `ALLOW`, all in-scope security group rules must be within the allowed range of the policy's security group rules. For `DENY`, all in-scope security group rules must not contain a value or a range that matches a rule value or range in the policy security group.
+ Example: `SECURITY_GROUPS_USAGE_AUDIT`

   `"{\"type\":\"SECURITY_GROUPS_USAGE_AUDIT\",\"deleteUnusedSecurityGroups\":true,\"coalesceRedundantSecurityGroups\":true}"`
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `30000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyOption`  <a name="cfn-fms-policy-securityservicepolicydata-policyoption"></a>
Contains the settings to configure a network ACL policy, a AWS Network Firewall firewall policy deployment model, or a third-party firewall policy.
*Required*: No
*Type*: [PolicyOption](aws-properties-fms-policy-policyoption.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-fms-policy-securityservicepolicydata-type"></a>
The service that the policy is using to protect the resources. This specifies the type of policy that is created, either an AWS WAF policy, a Shield Advanced policy, or a security group policy. For security group policies, Firewall Manager supports one security group for each common policy and for each content audit policy. This is an adjustable limit that you can increase by contacting AWS Support.
*Required*: Yes
*Type*: String
*Allowed values*: `WAF | WAFV2 | SHIELD_ADVANCED | SECURITY_GROUPS_COMMON | SECURITY_GROUPS_CONTENT_AUDIT | SECURITY_GROUPS_USAGE_AUDIT | NETWORK_FIREWALL | THIRD_PARTY_FIREWALL | DNS_FIREWALL | IMPORT_NETWORK_FIREWALL | NETWORK_ACL_COMMON`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-fms-policy-securityservicepolicydata--examples"></a>

**Topics**
+ [Define the SecurityServicePolicyData for AWS WAF](#aws-properties-fms-policy-securityservicepolicydata--examples--Define_the_SecurityServicePolicyData_for)
+ [Define the SecurityServicePolicyData for AWS WAF Classic](#aws-properties-fms-policy-securityservicepolicydata--examples--Define_the_SecurityServicePolicyData_for_Classic)
+ [Define the SecurityServicePolicyData for SECURITY\_GROUPS\_COMMON](#aws-properties-fms-policy-securityservicepolicydata--examples--Define_the_SecurityServicePolicyData_for_SECURITY_GROUPS_COMMON)
+ [Define the SecurityServicePolicyData for SECURITY\_GROUPS\_CONTENT\_AUDIT](#aws-properties-fms-policy-securityservicepolicydata--examples--Define_the_SecurityServicePolicyData_for_SECURITY_GROUPS_CONTENT_AUDIT)
+ [Define the SecurityServicePolicyData for SECURITY\_GROUPS\_USAGE\_AUDIT](#aws-properties-fms-policy-securityservicepolicydata--examples--Define_the_SecurityServicePolicyData_for_SECURITY_GROUPS_USAGE_AUDIT)

### Define the SecurityServicePolicyData for AWS WAF
<a name="aws-properties-fms-policy-securityservicepolicydata--examples--Define_the_SecurityServicePolicyData_for"></a>

The following shows an example SecurityServicePolicyData specification in an WAF policy for the latest version of AWS WAF.

#### JSON
<a name="aws-properties-fms-policy-securityservicepolicydata--examples--Define_the_SecurityServicePolicyData_for--json"></a>

```
"ManagedServiceData": {
    "Fn::Sub": "{\"type\":\"WAFV2\",\"preProcessRuleGroups\":[{\"ruleGroupType\":\"RuleGroup,\"ruleGroupArn\":\"${RuleGroup.Arn}\", \"overrideAction\":{\"type\":\"NONE\"}}],\"postProcessRuleGroups\":[],\"defaultAction\":{\"type\":\"BLOCK\"}}" }
```

#### YAML
<a name="aws-properties-fms-policy-securityservicepolicydata--examples--Define_the_SecurityServicePolicyData_for--yaml"></a>

```
ManagedServiceData: !Sub '{"type":"WAFV2",
                 "preProcessRuleGroups":[{
                 "ruleGroupType":"RuleGroup",
                 "ruleGroupArn":"${RuleGroup.Arn}",
                 "overrideAction":{"type":"NONE"}}],
                 "postProcessRuleGroups":[],
                 "defaultAction":{"type":"BLOCK"}}'
```

### Define the SecurityServicePolicyData for AWS WAF Classic
<a name="aws-properties-fms-policy-securityservicepolicydata--examples--Define_the_SecurityServicePolicyData_for_Classic"></a>

The following shows an example SecurityServicePolicyData specification for an AWS WAF Classic policy.

#### JSON
<a name="aws-properties-fms-policy-securityservicepolicydata--examples--Define_the_SecurityServicePolicyData_for_Classic--json"></a>

```
"ManagedServiceData": "{\"type\": \"WAF\", \"ruleGroups\": [{\"id\":
              \"12345678-1bcd-9012-efga-0987654321ab\", \"overrideAction\" : {\"type\": \"COUNT\"}}],
              \"defaultAction\": {\"type\": \"BLOCK\"}}
```

### Define the SecurityServicePolicyData for SECURITY\_GROUPS\_COMMON
<a name="aws-properties-fms-policy-securityservicepolicydata--examples--Define_the_SecurityServicePolicyData_for_SECURITY_GROUPS_COMMON"></a>

The following shows an example SecurityServicePolicyData specification for a common security group policy.

#### JSON
<a name="aws-properties-fms-policy-securityservicepolicydata--examples--Define_the_SecurityServicePolicyData_for_SECURITY_GROUPS_COMMON--json"></a>

```
"SecurityServicePolicyData":{"Type":"SECURITY_GROUPS_COMMON","ManagedServiceData":"{\"type\":\"SECURITY_GROUPS_COMMON\",\"revertManualSecurityGroupChanges\":false,
  \"exclusiveResourceSecurityGroupManagement\":false,\"securityGroups\":[{\"id\":\"
              sg-000e55995d61a06bd\"}]}"},"RemediationEnabled":false,"ResourceType":"AWS::EC2::NetworkInterface"}
```

### Define the SecurityServicePolicyData for SECURITY\_GROUPS\_CONTENT\_AUDIT
<a name="aws-properties-fms-policy-securityservicepolicydata--examples--Define_the_SecurityServicePolicyData_for_SECURITY_GROUPS_CONTENT_AUDIT"></a>

The following shows an example SecurityServicePolicyData specification for a content audit security group policy. The security group action for content audit can be `ALLOW` or `DENY`. For `ALLOW`, all in-scope security group rules must be within the allowed range of the policy's security group rules. For `DENY`, all in-scope security group rules must not contain a value or a range that matches a rule value or range in the policy security group.

#### JSON
<a name="aws-properties-fms-policy-securityservicepolicydata--examples--Define_the_SecurityServicePolicyData_for_SECURITY_GROUPS_CONTENT_AUDIT--json"></a>

```
"SecurityServicePolicyData":{"Type":"SECURITY_GROUPS_CONTENT_AUDIT","ManagedServiceData":"{\"type\":\"SECURITY_GROUPS_CONTENT_AUDIT\",\"securityGroups\":[{\"id\":\"
              sg-000e55995d61a06bd
              \"}],\"securityGroupAction\":{\"type\":\"ALLOW\"}}"},"RemediationEnabled":false,"ResourceType":"AWS::EC2::NetworkInterface"}
```

### Define the SecurityServicePolicyData for SECURITY\_GROUPS\_USAGE\_AUDIT
<a name="aws-properties-fms-policy-securityservicepolicydata--examples--Define_the_SecurityServicePolicyData_for_SECURITY_GROUPS_USAGE_AUDIT"></a>

The following shows an example SecurityServicePolicyData specification for a usage audit security group policy.

#### JSON
<a name="aws-properties-fms-policy-securityservicepolicydata--examples--Define_the_SecurityServicePolicyData_for_SECURITY_GROUPS_USAGE_AUDIT--json"></a>

```
"SecurityServicePolicyData":{"Type":"SECURITY_GROUPS_USAGE_AUDIT","ManagedServiceData":"{\"type\":\"SECURITY_GROUPS_USAGE_AUDIT\",\"deleteUnusedSecurityGroups\":true,
  \"coalesceRedundantSecurityGroups\":true}"},"RemediationEnabled":false,"Resou
              rceType":"AWS::EC2::SecurityGroup"}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
