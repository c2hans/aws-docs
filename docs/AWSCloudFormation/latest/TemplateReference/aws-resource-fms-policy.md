---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-fms-policy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FMS::Policy
<a name="aws-resource-fms-policy"></a>

An AWS Firewall Manager policy.

A Firewall Manager policy is specific to the individual policy type. If you want to enforce multiple policy types across accounts, you can create multiple policies. You can create more than one policy for each type.

If you add a new account to an organization that you created with AWS Organizations, Firewall Manager automatically applies the policy to the resources in that account that are within scope of the policy.

Policies require some setup to use. For more information, see the sections on prerequisites and getting started under [Firewall Manager prerequisites](https://docs.aws.amazon.com/waf/latest/developerguide/fms-prereq.html).

Firewall Manager provides the following types of policies:
+ **AWS WAF policy** - This policy applies AWS WAF web ACL protections to specified accounts and resources.
+ **Shield Advanced policy** - This policy applies Shield Advanced protection to specified accounts and resources.
+ **Security Groups policy** - This type of policy gives you control over security groups that are in use throughout your organization in AWS Organizations and lets you enforce a baseline set of rules across your organization.
+ **Network ACL policy** - This type of policy gives you control over the network ACLs that are in use throughout your organization in AWS Organizations and lets you enforce a baseline set of first and last network ACL rules across your organization.
+ **Network Firewall policy** - This policy applies Network Firewall protection to your organization's VPCs.
+ **DNS Firewall policy** - This policy applies Amazon Route 53 Resolver DNS Firewall protections to your organization's VPCs.
+ **Third-party firewall policy** - This policy applies third-party firewall protections. Third-party firewalls are available by subscription through the AWS Marketplace console at [AWS Marketplace](https://aws.amazon.com/marketplace).
  + **Palo Alto Networks Cloud NGFW policy** - This policy applies Palo Alto Networks Cloud Next Generation Firewall (NGFW) protections and Palo Alto Networks Cloud NGFW rulestacks to your organization's VPCs.
  + **Fortigate CNF policy** - This policy applies Fortigate Cloud Native Firewall (CNF) protections. Fortigate CNF is a cloud-centered solution that blocks Zero-Day threats and secures cloud infrastructures with industry-leading advanced threat prevention, smart web application firewalls (WAF), and API protection.

## Syntax
<a name="aws-resource-fms-policy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-fms-policy-syntax.json"></a>

```
{
  "Type" : "AWS::FMS::Policy",
  "Properties" : {
      "[DeleteAllPolicyResources](#cfn-fms-policy-deleteallpolicyresources)" : {{Boolean}},
      "[ExcludeMap](#cfn-fms-policy-excludemap)" : {{IEMap}},
      "[ExcludeResourceTags](#cfn-fms-policy-excluderesourcetags)" : {{Boolean}},
      "[IncludeMap](#cfn-fms-policy-includemap)" : {{IEMap}},
      "[PolicyDescription](#cfn-fms-policy-policydescription)" : {{String}},
      "[PolicyName](#cfn-fms-policy-policyname)" : {{String}},
      "[RemediationEnabled](#cfn-fms-policy-remediationenabled)" : {{Boolean}},
      "[ResourcesCleanUp](#cfn-fms-policy-resourcescleanup)" : {{Boolean}},
      "[ResourceSetIds](#cfn-fms-policy-resourcesetids)" : {{[ String, ... ]}},
      "[ResourceTagLogicalOperator](#cfn-fms-policy-resourcetaglogicaloperator)" : {{String}},
      "[ResourceTags](#cfn-fms-policy-resourcetags)" : {{[ ResourceTag, ... ]}},
      "[ResourceType](#cfn-fms-policy-resourcetype)" : {{String}},
      "[ResourceTypeList](#cfn-fms-policy-resourcetypelist)" : {{[ String, ... ]}},
      "[SecurityServicePolicyData](#cfn-fms-policy-securityservicepolicydata)" : {{SecurityServicePolicyData}},
      "[Tags](#cfn-fms-policy-tags)" : {{[ PolicyTag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-fms-policy-syntax.yaml"></a>

```
Type: AWS::FMS::Policy
Properties:
  [DeleteAllPolicyResources](#cfn-fms-policy-deleteallpolicyresources): {{Boolean}}
  [ExcludeMap](#cfn-fms-policy-excludemap): {{
    IEMap}}
  [ExcludeResourceTags](#cfn-fms-policy-excluderesourcetags): {{Boolean}}
  [IncludeMap](#cfn-fms-policy-includemap): {{
    IEMap}}
  [PolicyDescription](#cfn-fms-policy-policydescription): {{String}}
  [PolicyName](#cfn-fms-policy-policyname): {{String}}
  [RemediationEnabled](#cfn-fms-policy-remediationenabled): {{Boolean}}
  [ResourcesCleanUp](#cfn-fms-policy-resourcescleanup): {{Boolean}}
  [ResourceSetIds](#cfn-fms-policy-resourcesetids): {{
    - String}}
  [ResourceTagLogicalOperator](#cfn-fms-policy-resourcetaglogicaloperator): {{String}}
  [ResourceTags](#cfn-fms-policy-resourcetags): {{
    - ResourceTag}}
  [ResourceType](#cfn-fms-policy-resourcetype): {{String}}
  [ResourceTypeList](#cfn-fms-policy-resourcetypelist): {{
    - String}}
  [SecurityServicePolicyData](#cfn-fms-policy-securityservicepolicydata): {{
    SecurityServicePolicyData}}
  [Tags](#cfn-fms-policy-tags): {{
    - PolicyTag}}
```

## Properties
<a name="aws-resource-fms-policy-properties"></a>

`DeleteAllPolicyResources`  <a name="cfn-fms-policy-deleteallpolicyresources"></a>
Used when deleting a policy. If `true`, Firewall Manager performs cleanup according to the policy type.
For AWS WAF and Shield Advanced policies, Firewall Manager does the following:
+ Deletes rule groups created by Firewall Manager
+ Removes web ACLs from in-scope resources
+ Deletes web ACLs that contain no rules or rule groups
For security group policies, Firewall Manager does the following for each security group in the policy:
+ Disassociates the security group from in-scope resources
+ Deletes the security group if it was created through Firewall Manager and if it's no longer associated with any resources through another policy
After the cleanup, in-scope resources are no longer protected by web ACLs in this policy. Protection of out-of-scope resources remains unchanged. Scope is determined by tags that you create and accounts that you associate with the policy. When creating the policy, if you specify that only resources in specific accounts or with specific tags are in scope of the policy, those accounts and resources are handled by the policy. All others are out of scope. If you don't specify tags or accounts, all resources are in scope.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExcludeMap`  <a name="cfn-fms-policy-excludemap"></a>
Specifies the AWS account IDs and AWS Organizations organizational units (OUs) to exclude from the policy. Specifying an OU is the equivalent of specifying all accounts in the OU and in any of its child OUs, including any child OUs and accounts that are added at a later time.
You can specify inclusions or exclusions, but not both. If you specify an `IncludeMap`, AWS Firewall Manager applies the policy to all accounts specified by the `IncludeMap`, and does not evaluate any `ExcludeMap` specifications. If you do not specify an `IncludeMap`, then Firewall Manager applies the policy to all accounts except for those specified by the `ExcludeMap`.
You can specify account IDs, OUs, or a combination:
+ Specify account IDs by setting the key to `ACCOUNT`. For example, the following is a valid map: `{“ACCOUNT” : [“accountID1”, “accountID2”]}`.
+ Specify OUs by setting the key to `ORGUNIT`. For example, the following is a valid map: `{“ORGUNIT” : [“ouid111”, “ouid112”]}`.
+ Specify accounts and OUs together in a single map, separated with a comma. For example, the following is a valid map: `{“ACCOUNT” : [“accountID1”, “accountID2”], “ORGUNIT” : [“ouid111”, “ouid112”]}`.
*Required*: No
*Type*: [IEMap](aws-properties-fms-policy-iemap.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExcludeResourceTags`  <a name="cfn-fms-policy-excluderesourcetags"></a>
Used only when tags are specified in the `ResourceTags` property. If this property is `True`, resources with the specified tags are not in scope of the policy. If it's `False`, only resources with the specified tags are in scope of the policy.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IncludeMap`  <a name="cfn-fms-policy-includemap"></a>
Specifies the AWS account IDs and AWS Organizations organizational units (OUs) to include in the policy. Specifying an OU is the equivalent of specifying all accounts in the OU and in any of its child OUs, including any child OUs and accounts that are added at a later time.
You can specify inclusions or exclusions, but not both. If you specify an `IncludeMap`, AWS Firewall Manager applies the policy to all accounts specified by the `IncludeMap`, and does not evaluate any `ExcludeMap` specifications. If you do not specify an `IncludeMap`, then Firewall Manager applies the policy to all accounts except for those specified by the `ExcludeMap`.
You can specify account IDs, OUs, or a combination:
+ Specify account IDs by setting the key to `ACCOUNT`. For example, the following is a valid map: `{“ACCOUNT” : [“accountID1”, “accountID2”]}`.
+ Specify OUs by setting the key to `ORGUNIT`. For example, the following is a valid map: `{“ORGUNIT” : [“ouid111”, “ouid112”]}`.
+ Specify accounts and OUs together in a single map, separated with a comma. For example, the following is a valid map: `{“ACCOUNT” : [“accountID1”, “accountID2”], “ORGUNIT” : [“ouid111”, “ouid112”]}`.
*Required*: No
*Type*: [IEMap](aws-properties-fms-policy-iemap.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyDescription`  <a name="cfn-fms-policy-policydescription"></a>
Your description of the AWS Firewall Manager policy.
*Required*: No
*Type*: String
*Pattern*: `^([a-zA-Z0-9_.:/=+\-@\s]+)$`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PolicyName`  <a name="cfn-fms-policy-policyname"></a>
The name of the AWS Firewall Manager policy.
*Required*: Yes
*Type*: String
*Pattern*: `^([a-zA-Z0-9_.:/=+\-@\s]+)$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RemediationEnabled`  <a name="cfn-fms-policy-remediationenabled"></a>
Indicates if the policy should be automatically applied to new resources.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourcesCleanUp`  <a name="cfn-fms-policy-resourcescleanup"></a>
Indicates whether AWS Firewall Manager should automatically remove protections from resources that leave the policy scope and clean up resources that Firewall Manager is managing for accounts when those accounts leave policy scope. For example, Firewall Manager will disassociate a Firewall Manager managed web ACL from a protected customer resource when the customer resource leaves policy scope.
By default, Firewall Manager doesn't remove protections or delete Firewall Manager managed resources.
This option is not available for Shield Advanced or AWS WAF Classic policies.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceSetIds`  <a name="cfn-fms-policy-resourcesetids"></a>
The unique identifiers of the resource sets used by the policy.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceTagLogicalOperator`  <a name="cfn-fms-policy-resourcetaglogicaloperator"></a>
Specifies whether to combine multiple resource tags with AND, so that a resource must have all tags to be included or excluded, or OR, so that a resource must have at least one tag.
Default: `AND`
*Required*: No
*Type*: String
*Allowed values*: `AND | OR`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceTags`  <a name="cfn-fms-policy-resourcetags"></a>
An array of `ResourceTag` objects, used to explicitly include resources in the policy scope or explicitly exclude them. If this isn't set, then tags aren't used to modify policy scope. See also `ExcludeResourceTags`.
*Required*: No
*Type*: Array of [ResourceTag](aws-properties-fms-policy-resourcetag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceType`  <a name="cfn-fms-policy-resourcetype"></a>
The type of resource protected by or in scope of the policy. This is in the format shown in the [AWS Resource Types Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html). To apply this policy to multiple resource types, specify a resource type of `ResourceTypeList` and then specify the resource types in a `ResourceTypeList`.
The following are valid resource types for each Firewall Manager policy type:
+ AWS WAF Classic - `AWS::ApiGateway::Stage`, `AWS::CloudFront::Distribution`, and `AWS::ElasticLoadBalancingV2::LoadBalancer`.
+ AWS WAF - `AWS::ApiGateway::Stage`, `AWS::ElasticLoadBalancingV2::LoadBalancer`, and `AWS::CloudFront::Distribution`.
+ Shield Advanced - `AWS::ElasticLoadBalancingV2::LoadBalancer`, `AWS::ElasticLoadBalancing::LoadBalancer`, `AWS::EC2::EIP`, and `AWS::CloudFront::Distribution`.
+ Network ACL - `AWS::EC2::Subnet`.
+ Security group usage audit - `AWS::EC2::SecurityGroup`.
+ Security group content audit - `AWS::EC2::SecurityGroup`, `AWS::EC2::NetworkInterface`, and `AWS::EC2::Instance`.
+ DNS Firewall, AWS Network Firewall, and third-party firewall - `AWS::EC2::VPC`.
*Required*: No
*Type*: String
*Pattern*: `^([^\s]*)$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceTypeList`  <a name="cfn-fms-policy-resourcetypelist"></a>
An array of `ResourceType` objects. Use this only to specify multiple resource types. To specify a single resource type, use `ResourceType`.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityServicePolicyData`  <a name="cfn-fms-policy-securityservicepolicydata"></a>
Details about the security service that is being used to protect the resources.
This contains the following settings:
+ Type - Indicates the service type that the policy uses to protect the resource. For security group policies, Firewall Manager supports one security group for each common policy and for each content audit policy. This is an adjustable limit that you can increase by contacting AWS Support.

  Valid values: `DNS_FIREWALL` \| `NETWORK_FIREWALL` \| `SECURITY_GROUPS_COMMON` \| `SECURITY_GROUPS_CONTENT_AUDIT` \| `SECURITY_GROUPS_USAGE_AUDIT` \| `SHIELD_ADVANCED` \| `THIRD_PARTY_FIREWALL` \| `WAFV2` \| `WAF`
+ ManagedServiceData - Details about the service that are specific to the service type, in JSON format.
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
*Required*: Yes
*Type*: [SecurityServicePolicyData](aws-properties-fms-policy-securityservicepolicydata.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-fms-policy-tags"></a>
A collection of key:value pairs associated with an AWS resource. The key:value pair can be anything you define. Typically, the tag key represents a category (such as "environment") and the tag value represents a specific value within that category (such as "test," "development," or "production"). You can add up to 50 tags to each AWS resource.
*Required*: No
*Type*: Array of [PolicyTag](aws-properties-fms-policy-policytag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-fms-policy-return-values"></a>

### Ref
<a name="aws-resource-fms-policy-return-values-ref"></a>

The `Ref` for this resource returns the `PolicyId`.

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource physical ID, such as 1234a1a-a1b1-12a1-abcd-a123b123456.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-fms-policy-return-values-fn--getatt"></a>

####
<a name="aws-resource-fms-policy-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the policy.

`Id`  <a name="Id-fn::getatt"></a>
The ID of the policy.

## Examples
<a name="aws-resource-fms-policy--examples"></a>

**Topics**
+ [Create a Firewall ManagerAWS WAF policy](#aws-resource-fms-policy--examples--Create_a_policy)
+ [Create a Firewall ManagerAWS WAF Classic policy](#aws-resource-fms-policy--examples--Create_a_Classic_policy)
+ [Create a Firewall Manager Shield Advanced policy](#aws-resource-fms-policy--examples--Create_a_Firewall_Manager_Shield_Advanced_policy)
+ [Create a Firewall Manager common security group policy](#aws-resource-fms-policy--examples--Create_a_Firewall_Manager_common_security_group_policy)
+ [Create a Firewall Manager content audit security group policy](#aws-resource-fms-policy--examples--Create_a_Firewall_Manager_content_audit_security_group_policy)
+ [Create a Firewall Manager usage audit security group policy](#aws-resource-fms-policy--examples--Create_a_Firewall_Manager_usage_audit_security_group_policy)
+ [Create a Firewall Manager network ACL policy](#aws-resource-fms-policy--examples--Create_a_network_ACL_policy)
+ [Create a Firewall Manager Network Firewall policy](#aws-resource-fms-policy--examples--Create_a_Firewall_Manager_Network_Firewall_policy)
+ [Create a Firewall Manager DNS Firewall policy](#aws-resource-fms-policy--examples--Create_a_Firewall_Manager_DNS_Firewall_policy)

### Create a Firewall ManagerAWS WAF policy
<a name="aws-resource-fms-policy--examples--Create_a_policy"></a>

The following shows an example Firewall Manager WAF policy for the latest version of AWS WAF.

#### YAML
<a name="aws-resource-fms-policy--examples--Create_a_policy--yaml"></a>

```
PolicyWAFv2:
    Type: AWS::FMS::Policy
    Properties:
      ExcludeResourceTags: false
      PolicyName: Policy
      RemediationEnabled: false
      ResourceType: AWS::ElasticLoadBalancingV2::LoadBalancer
      SecurityServicePolicyData:
        Type: WAFV2
        ManagedServiceData: !Sub '{"type":"WAFV2",
                                  "preProcessRuleGroups":[{
                                  "ruleGroupType":"RuleGroup",
                                  "ruleGroupArn":"${RuleGroup.Arn}",
                                  "overrideAction":{"type":"NONE"}}],
                                  "postProcessRuleGroups":[],
                                  "defaultAction":{"type":"BLOCK"}}'
```

#### JSON
<a name="aws-resource-fms-policy--examples--Create_a_policy--json"></a>

```
"PolicyWAFv2": {
    "Type": "AWS::FMS::Policy",
    "Properties": {
        "ExcludeResourceTags": false,
        "PolicyName": "Policy",
        "RemediationEnabled": false,
        "ResourceType": "AWS::ElasticLoadBalancingV2::LoadBalancer",
        "SecurityServicePolicyData": {
            "Type": "WAFV2",
            "ManagedServiceData": {
                "Fn::Sub": "{\"type\":\"WAFV2\",\"preProcessRuleGroups\":[{\"ruleGroupType\":\"RuleGroup,\"ruleGroupArn\":\"${RuleGroup.Arn}\",\"overrideAction\":{\"type\":\"NONE\"}}],\"postProcessRuleGroups\":[],\"defaultAction\":{\"type\":\"BLOCK\"}}"
            }
        }
    }
}
```

### Create a Firewall ManagerAWS WAF Classic policy
<a name="aws-resource-fms-policy--examples--Create_a_Classic_policy"></a>

The following shows an example Firewall ManagerAWS WAF Classic policy.

#### YAML
<a name="aws-resource-fms-policy--examples--Create_a_Classic_policy--yaml"></a>

```
PolicyWAF:
    Type: AWS::FMS::Policy
    Properties:
      ExcludeResourceTags: false
      PolicyName: Policy
      RemediationEnabled: false
      ResourceType: AWS::ElasticLoadBalancingV2::LoadBalancer
      SecurityServicePolicyData:
        Type: WAF
        ManagedServiceData: !Sub '{"type":"WAF",
                                  "defaultAction":{"type":"BLOCK"},
                                  "overrideCustomerWebACLAssociation":false,
                                  "ruleGroups":[
                                    {
                                      "id":"${RuleGroupId}",
                                      "overrideAction":{"type":"NONE"}
                                    }
                                  ]}'
```

#### JSON
<a name="aws-resource-fms-policy--examples--Create_a_Classic_policy--json"></a>

```
"PolicyWAF": {
    "Type": "AWS::FMS::Policy",
    "Properties": {
        "ExcludeResourceTags": false,
        "PolicyName": "Policy",
        "RemediationEnabled": false,
        "ResourceType": "AWS::ElasticLoadBalancingV2::LoadBalancer",
        "SecurityServicePolicyData": {
            "Type": "WAF",
            "ManagedServiceData": {
                "Fn::Sub": "{\"type\":\"WAF\",\"defaultAction\":{\"type\":\"BLOCK\"},\"overrideCustomerWebACLAssociation\":false,\"ruleGroups\":[{\"id\":\"${RuleGroupId}\",\"overrideAction\":{\"type\":\"NONE\"}}]}"
            }
        }
    }
}
```

### Create a Firewall Manager Shield Advanced policy
<a name="aws-resource-fms-policy--examples--Create_a_Firewall_Manager_Shield_Advanced_policy"></a>

The following shows an example Firewall Manager Shield Advanced policy. This example uses account and resource tag specifications to limit the scope of the policy.

#### YAML
<a name="aws-resource-fms-policy--examples--Create_a_Firewall_Manager_Shield_Advanced_policy--yaml"></a>

```
Policy:
    Type: AWS::FMS::Policy
    Properties:
      ExcludeResourceTags: true
      ResourceTags:
        - Key: resourceTag1
          Value: value
        - Key: resourceTag2
          Value: value
      IncludeMap:
        ACCOUNT:
          - !Ref AWS::AccountId
      PolicyName: TaggedPolicy
      RemediationEnabled: false
      ResourceType: ResourceTypeList
      ResourceTypeList:
        - AWS::ElasticLoadBalancingV2::LoadBalancer
        - AWS::EC2::EIP
      SecurityServicePolicyData:
        Type: SHIELD_ADVANCED
      DeleteAllPolicyResources: false
      Tags:
        - Key: tag1
          Value: value
        - Key: tag2
          Value: value
```

#### JSON
<a name="aws-resource-fms-policy--examples--Create_a_Firewall_Manager_Shield_Advanced_policy--json"></a>

```
"Policy": {
    "Type": "AWS::FMS::Policy",
    "Properties": {
        "ExcludeResourceTags": true,
        "ResourceTags": [
            {
                "Key": "resourceTag1",
                "Value": "value"
            },
            {
                "Key": "resourceTag2",
                "Value": "value"
            }
          ],
          "IncludeMap": {
              "ACCOUNT": [
                {
                  "Ref": "AWS::AccountId"
                }
              ]
          },
          "PolicyName": "TaggedPolicy",
          "RemediationEnabled": false,
          "ResourceType": "ResourceTypeList",
          "ResourceTypeList": [
              "AWS::ElasticLoadBalancingV2::LoadBalancer",
              "AWS::EC2::EIP"
          ],
          "SecurityServicePolicyData": {
              "Type": "SHIELD_ADVANCED"
          },
          "Tags": [
              {
                "Key": "tag1",
                "Value": "value"
              },
              {
              "Key": "tag2",
              "Value": "value"
            }
        ]
    }
}
```

### Create a Firewall Manager common security group policy
<a name="aws-resource-fms-policy--examples--Create_a_Firewall_Manager_common_security_group_policy"></a>

The following shows an example Firewall Manager common security group policy.

#### YAML
<a name="aws-resource-fms-policy--examples--Create_a_Firewall_Manager_common_security_group_policy--yaml"></a>

```
Policy:
    Type: AWS::FMS::Policy
    Properties:
      ExcludeResourceTags: false
      PolicyName: SecurityGroupsCommonsPolicy
      RemediationEnabled: false
      ResourceType: AWS::EC2::Instance
      SecurityServicePolicyData:
        Type: SECURITY_GROUPS_COMMON
        ManagedServiceData: !Sub '{"type":"SECURITY_GROUPS_COMMON",
                                  "revertManualSecurityGroupChanges":true,
                                  "securityGroups":[{"id":"${SecurityGroup.GroupId}"}]}'
```

#### JSON
<a name="aws-resource-fms-policy--examples--Create_a_Firewall_Manager_common_security_group_policy--json"></a>

```
"Policy": {
    "Type": "AWS::FMS::Policy",
    "Properties": {
        "ExcludeResourceTags": false,
        "PolicyName": "SecurityGroupsCommonsPolicy",
        "RemediationEnabled": false,
        "ResourceType": "AWS::EC2::Instance",
        "SecurityServicePolicyData": {
            "Type": "SECURITY_GROUPS_COMMON",
            "ManagedServiceData": {
                "Fn::Sub": "{\"type\":\"SECURITY_GROUPS_COMMON\",\"revertManualSecurityGroupChanges\":true,\"securityGroups\":[{\"id\":\"${SecurityGroup.GroupId}\"}]}"
            }
        }
    }
}
```

### Create a Firewall Manager content audit security group policy
<a name="aws-resource-fms-policy--examples--Create_a_Firewall_Manager_content_audit_security_group_policy"></a>

The following shows an example Firewall Manager usage audit security group policy.

#### YAML
<a name="aws-resource-fms-policy--examples--Create_a_Firewall_Manager_content_audit_security_group_policy--yaml"></a>

```
PolicySGContentAudit:
    Type: AWS::FMS::Policy
    Properties:
      ExcludeResourceTags: false
      PolicyName: Policy
      RemediationEnabled: false
      ResourceType: AWS::EC2::Instance
      SecurityServicePolicyData:
        Type: SECURITY_GROUPS_CONTENT_AUDIT
        ManagedServiceData: !Sub '{"type":"SECURITY_GROUPS_CONTENT_AUDIT",
                                  "securityGroupAction":{"type":"ALLOW"},
                                  "securityGroups":[
                                    {"id":"${SecurityGroup.GroupId}"}
                                  ]}'
```

#### JSON
<a name="aws-resource-fms-policy--examples--Create_a_Firewall_Manager_content_audit_security_group_policy--json"></a>

```
"PolicySGContentAudit": {
    "Type": "AWS::FMS::Policy",
    "Properties": {
            "ExcludeResourceTags": false,
            "PolicyName": "Policy",
            "RemediationEnabled": false,
            "ResourceType": "AWS::EC2::Instance",
            "SecurityServicePolicyData": {
                "Type": "SECURITY_GROUPS_CONTENT_AUDIT",
                "ManagedServiceData": {
                    "Fn::Sub": "{\"type\":\"SECURITY_GROUPS_CONTENT_AUDIT\",\"securityGroupAction\":{\"type\":\"ALLOW\"},\"securityGroups\":[{\"id\":\"${SecurityGroup.GroupId}\"}]}"
                }
            }
        }
    }
```

### Create a Firewall Manager usage audit security group policy
<a name="aws-resource-fms-policy--examples--Create_a_Firewall_Manager_usage_audit_security_group_policy"></a>

The following shows an example Firewall Manager usage audit security group policy.

#### YAML
<a name="aws-resource-fms-policy--examples--Create_a_Firewall_Manager_usage_audit_security_group_policy--yaml"></a>

```
PolicySGUsageAudit:
    Type: AWS::FMS::Policy
    Properties:
      ExcludeResourceTags: false
      PolicyName: Policy
      RemediationEnabled: false
      ResourceType: AWS::EC2::SecurityGroup
      SecurityServicePolicyData:
        Type: SECURITY_GROUPS_USAGE_AUDIT
        ManagedServiceData: !Sub '{"type":"SECURITY_GROUPS_USAGE_AUDIT",
                                  "deleteUnusedSecurityGroups":false,
                                  "coalesceRedundantSecurityGroups":false,
                                  "optionalDelayForUnusedInMinutes":null}'
```

#### JSON
<a name="aws-resource-fms-policy--examples--Create_a_Firewall_Manager_usage_audit_security_group_policy--json"></a>

```
"PolicySGUsageAudit": {
    "Type": "AWS::FMS::Policy",
    "Properties": {
        "ExcludeResourceTags": false,
        "PolicyName": "PolicySGUsageAudit",
        "RemediationEnabled": false,
        "ResourceType": "AWS::EC2::SecurityGroup",
        "SecurityServicePolicyData": {
            "Type": "SECURITY_GROUPS_USAGE_AUDIT",
            "ManagedServiceData": {
                "Fn::Sub": "{\"type\":\"SECURITY_GROUPS_USAGE_AUDIT\",\"deleteUnusedSecurityGroups\":false,\"coalesceRedundantSecurityGroups\":false,\"optionalDelayForUnusedInMinutes\":null}"
            }
        }
    }
}
```

### Create a Firewall Manager network ACL policy
<a name="aws-resource-fms-policy--examples--Create_a_network_ACL_policy"></a>

The following shows an example Firewall Manager network ACL policy.

#### YAML
<a name="aws-resource-fms-policy--examples--Create_a_network_ACL_policy--yaml"></a>

```
PolicyNetworkAcl:
  Type: AWS::FMS::Policy
  Properties:
    PolicyName: FMSNetworkAclPolicy
    DeleteAllPolicyResources: true
    ResourcesCleanUp: true
    RemediationEnabled: true
    ExcludeResourceTags: false
    ResourceType: AWS::EC2::Subnet
    SecurityServicePolicyData:
      Type: NETWORK_ACL_COMMON
      ManagedServiceData: '{"type":"NETWORK_ACL_COMMON"}'
      PolicyOption:
        NetworkAclCommonPolicy:
          NetworkAclEntrySet:
            FirstEntries:
              - Protocol: '6'
                PortRange:
                  From: 2048
                  To: 2048
                CidrBlock: 10.16.0.0/16
                RuleAction: allow
                Egress: false
              - Protocol: '6'
                PortRange:
                  From: 2048
                  To: 2048
                CidrBlock: 10.16.0.0/16
                RuleAction: allow
                Egress: true
            LastEntries:
              - Protocol: '6'
                PortRange:
                  From: 4096
                  To: 4096
                CidrBlock: 10.16.0.0/16
                RuleAction: allow
                Egress: true
              - Protocol: '6'
                PortRange:
                  From: 4096
                  To: 4096
                CidrBlock: 10.16.0.0/16
                RuleAction: allow
                Egress: false
            ForceRemediateForFirstEntries: true
            ForceRemediateForLastEntries: true
```

#### JSON
<a name="aws-resource-fms-policy--examples--Create_a_network_ACL_policy--json"></a>

```
"PolicyNetworkAcl": {
    "Type": "AWS::FMS::Policy",
    "Properties": {
        "PolicyName": "FMSNetworkAclPolicy",
        "DeleteAllPolicyResources": true,
        "ResourcesCleanUp": true,
        "RemediationEnabled": true,
        "ExcludeResourceTags": false,
        "ResourceType": "AWS::EC2::Subnet",
        "SecurityServicePolicyData": {
            "Type": "NETWORK_ACL_COMMON",
            "ManagedServiceData": "{\"type\":\"NETWORK_ACL_COMMON\"}",
            "PolicyOption": {
                "NetworkAclCommonPolicy": {
                    "NetworkAclEntrySet": {
                        "FirstEntries": [
                            {
                                "Protocol": "6",
                                "PortRange": {
                                    "From": 2048,
                                    "To": 2048
                                },
                                "CidrBlock": "10.16.0.0/16",
                                "RuleAction": "allow",
                                "Egress": false
                            },
                            {
                                "Protocol": "6",
                                "PortRange": {
                                    "From": 2048,
                                    "To": 2048
                                },
                                "CidrBlock": "10.16.0.0/16",
                                "RuleAction": "allow",
                                "Egress": true
                            }
                        ],
                        "LastEntries": [
                            {
                                "Protocol": "6",
                                "PortRange": {
                                    "From": 4096,
                                    "To": 4096
                                },
                                "CidrBlock": "10.16.0.0/16",
                                "RuleAction": "allow",
                                "Egress": true
                            },
                            {
                                "Protocol": "6",
                                "PortRange": {
                                    "From": 4096,
                                    "To": 4096
                                },
                                "CidrBlock": "10.16.0.0/16",
                                "RuleAction": "allow",
                                "Egress": false
                            }
                        ],
                        "ForceRemediateForFirstEntries": true,
                        "ForceRemediateForLastEntries": true
                    }
                }
            }
        }
    }
}
```

### Create a Firewall Manager Network Firewall policy
<a name="aws-resource-fms-policy--examples--Create_a_Firewall_Manager_Network_Firewall_policy"></a>

The following shows an example Firewall Manager Network Firewall policy.

#### YAML
<a name="aws-resource-fms-policy--examples--Create_a_Firewall_Manager_Network_Firewall_policy--yaml"></a>

```
PolicyNetworkFirewall:
    Type: AWS::FMS::Policy
    Properties:
      ExcludeResourceTags: false
      PolicyName: PolicyNetworkFirewall
      RemediationEnabled: true
      ResourceType: AWS::EC2::VPC
      DeleteAllPolicyResources: true
      SecurityServicePolicyData:
        Type: NETWORK_FIREWALL
        ManagedServiceData: '
          {
            "type": "NETWORK_FIREWALL",
            "networkFirewallStatelessRuleGroupReferences": [
              {
                "resourceARN": "arn:aws:network-firewall:us-east-1:000000000000:stateless-rulegroup/example",
                "priority": 1
              }
            ],
            "networkFirewallStatelessDefaultActions": [
              "aws:drop",
              "example"
            ],
            "networkFirewallStatelessFragmentDefaultActions": [
              "aws:drop",
              "example"
            ],
            "networkFirewallStatelessCustomActions": [
              {
                "actionName": "example",
                "actionDefinition": {
                  "publishMetricAction": {
                    "dimensions": [
                      {
                        "value": "example"
                      }
                    ]
                  }
                }
              }
            ],
            "networkFirewallStatefulRuleGroupReferences": [
              {
                "resourceARN": "arn:aws:network-firewall:us-east-1:000000000000:stateful-rulegroup/example"
              }
            ],
            "networkFirewallOrchestrationConfig": {
              "singleFirewallEndpointPerVPC": false,
              "allowedIPV4CidrList": []
            }
          }'
```

#### JSON
<a name="aws-resource-fms-policy--examples--Create_a_Firewall_Manager_Network_Firewall_policy--json"></a>

```
"PolicyNetworkFirewall": {
    "Type": "AWS::FMS::Policy",
    "Properties": {
        "ExcludeResourceTags": false,
        "PolicyName": "PolicyNetworkFirewall",
        "RemediationEnabled": true,
        "ResourceType": "AWS::EC2::VPC",
        "DeleteAllPolicyResources": true,
        "SecurityServicePolicyData": {
            "Type": "NETWORK_FIREWALL",
            "ManagedServiceData": "{\"type\":\"NETWORK_FIREWALL\",\"networkFirewallStatelessRuleGroupReferences\":[{\"resourceARN\":\"arn:aws:network-firewall:us-east-1:000000000000:stateless-rulegroup\/example\",\"priority\":1}],\"networkFirewallStatelessDefaultActions\":[\"aws:drop\",\"example\"],\"networkFirewallStatelessFragmentDefaultActions\":[\"aws:drop\",\"example\"],\"networkFirewallStatelessCustomActions\":[{\"actionName\":\"example\",\"actionDefinition\":{\"publishMetricAction\":{\"dimensions\":[{\"value\":\"example\"}]}}}],\"networkFirewallStatefulRuleGroupReferences\":[{\"resourceARN\":\"arn:aws:network-firewall:us-east-1:000000000000:stateful-rulegroup\/example\"}],\"networkFirewallOrchestrationConfig\":{\"singleFirewallEndpointPerVPC\":false,\"allowedIPV4CidrList\":[]}}"
        }
    }
}
```

### Create a Firewall Manager DNS Firewall policy
<a name="aws-resource-fms-policy--examples--Create_a_Firewall_Manager_DNS_Firewall_policy"></a>

The following shows an example Firewall Manager DNS Firewall policy.

#### YAML
<a name="aws-resource-fms-policy--examples--Create_a_Firewall_Manager_DNS_Firewall_policy--yaml"></a>

```
Policy:
    Type: AWS::FMS::Policy
    Properties:
      ExcludeResourceTags: false
      PolicyName: DnsFirewallPolicy
      RemediationEnabled: false
      ResourceType: AWS::EC2::VPC
      SecurityServicePolicyData:
        Type: DNS_FIREWALL
        ManagedServiceData: !Sub '{"type":"DNS_FIREWALL",
                                  "preProcessRuleGroups":[{"ruleGroupId": "${PreRuleGroupId}", "priority": 11}],
                                  "postProcessRuleGroups":[{"ruleGroupId": "${PostRuleGroupId}", "priority": 9902}]}'
```

#### JSON
<a name="aws-resource-fms-policy--examples--Create_a_Firewall_Manager_DNS_Firewall_policy--json"></a>

```
"Policy": {
    "Type": "AWS::FMS::Policy",
    "Properties": {
        "ExcludeResourceTags": false,
        "PolicyName": "DnsFirewallPolicy",
        "RemediationEnabled": false,
        "ResourceType": "AWS::EC2::VPC",
        "SecurityServicePolicyData": {
            "Type": "DNS_FIREWALL",
            "ManagedServiceData": {
                "Fn::Sub": "{\"type\":\"DNS_FIREWALL\",\"preProcessRuleGroups\":[{\"ruleGroupId\": \"${PreRuleGroupId}\", \"priority\": 11}],\"postProcessRuleGroups\":[{\"ruleGroupId\": \"${PostRuleGroupId}\", \"priority\": 9902}]}"
            }
        }
    }
}
```
