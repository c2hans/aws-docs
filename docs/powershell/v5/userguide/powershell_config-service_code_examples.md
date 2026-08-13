---
source_url: https://docs.aws.amazon.com/powershell/v5/userguide/powershell_config-service_code_examples.html
---

Version 5 (V5) of the AWS Tools for PowerShell has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html).

 [![Orange button with text "Click here for details".](http://docs.aws.amazon.com/powershell/v5/userguide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html)

# AWS Config examples using Tools for PowerShell V5
<a name="powershell_config-service_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V5 with AWS Config.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Add-CFGResourceTag`
<a name="config-service_TagResource_powershell_topic"></a>

The following code example shows how to use `Add-CFGResourceTag`.

**Tools for PowerShell V5**
**Example 1: This example associates specified tag to the resource ARN, which is config-rule/config-rule-16iyn0 in this case. **

```
Add-CFGResourceTag -ResourceArn arn:aws:config:eu-west-1:123456789012:config-rule/config-rule-16iyn0 -Tag @{Key="Release";Value="Beta"}
```
+  For API details, see [TagResource](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CFGAggregateComplianceByConfigRuleList`
<a name="config-service_DescribeAggregateComplianceByConfigRules_powershell_topic"></a>

The following code example shows how to use `Get-CFGAggregateComplianceByConfigRuleList`.

**Tools for PowerShell V5**
**Example 1: This example fetches the details from ConfigurationAggregator 'kaju' filtering for the given config rule and expands/returns the 'Compliance' of the rule.**

```
Get-CFGAggregateComplianceByConfigRuleList -ConfigurationAggregatorName kaju -Filters_ConfigRuleName ALB_HTTP_TO_HTTPS_REDIRECTION_CHECK | Select-Object -ExpandProperty Compliance
```
**Output:**

```
ComplianceContributorCount                            ComplianceType
--------------------------                            --------------
Amazon.ConfigService.Model.ComplianceContributorCount NON_COMPLIANT
```
**Example 2: This example fetches details from the given ConfigurationAggregator, filters it for the given account for all regions covered in the aggregator and further retuns the compliance for all the rules.**

```
Get-CFGAggregateComplianceByConfigRuleList -ConfigurationAggregatorName kaju -Filters_AccountId 123456789012 | Select-Object ConfigRuleName, @{N="Compliance";E={$_.Compliance.ComplianceType}}
```
**Output:**

```
ConfigRuleName                      Compliance
--------------                      ----------
ALB_HTTP_TO_HTTPS_REDIRECTION_CHECK NON_COMPLIANT
ec2-instance-no-public-ip           NON_COMPLIANT
desired-instance-type               NON_COMPLIANT
```
+  For API details, see [DescribeAggregateComplianceByConfigRules](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CFGAggregateComplianceDetailsByConfigRule`
<a name="config-service_GetAggregateComplianceDetailsByConfigRule_powershell_topic"></a>

The following code example shows how to use `Get-CFGAggregateComplianceDetailsByConfigRule`.

**Tools for PowerShell V5**
**Example 1: This example returns the evaluation results selecting the output with resource-id and resource-type for the AWS Config rule 'desired-instance-type' which are in 'COMPLIANT' state for the given account, aggregator, region and config rule**

```
Get-CFGAggregateComplianceDetailsByConfigRule -AccountId 123456789012 -AwsRegion eu-west-1 -ComplianceType COMPLIANT -ConfigRuleName desired-instance-type -ConfigurationAggregatorName raju | Select-Object -ExpandProperty EvaluationResultIdentifier | Select-Object -ExpandProperty EvaluationResultQualifier
```
**Output:**

```
ConfigRuleName        ResourceId          ResourceType
--------------        ----------          ------------
desired-instance-type i-0f1bf2f34c5678d12 AWS::EC2::Instance
desired-instance-type i-0fd12dd3456789123 AWS::EC2::Instance
```
+  For API details, see [GetAggregateComplianceDetailsByConfigRule](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CFGAggregateConfigRuleComplianceSummary`
<a name="config-service_GetAggregateConfigRuleComplianceSummary_powershell_topic"></a>

The following code example shows how to use `Get-CFGAggregateConfigRuleComplianceSummary`.

**Tools for PowerShell V5**
**Example 1: This example returns the number of noncompliant rules for the given aggregator.**

```
(Get-CFGAggregateConfigRuleComplianceSummary -ConfigurationAggregatorName raju).AggregateComplianceCounts.ComplianceSummary.NonCompliantResourceCount
```
**Output:**

```
CapExceeded CappedCount
----------- -----------
False       5
```
+  For API details, see [GetAggregateConfigRuleComplianceSummary](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CFGAggregateDiscoveredResourceCount`
<a name="config-service_GetAggregateDiscoveredResourceCounts_powershell_topic"></a>

The following code example shows how to use `Get-CFGAggregateDiscoveredResourceCount`.

**Tools for PowerShell V5**
**Example 1: This example returns the resource count for the given aggregator filtered for region us-east-1.**

```
Get-CFGAggregateDiscoveredResourceCount -ConfigurationAggregatorName Master -Filters_Region us-east-1
```
**Output:**

```
GroupByKey GroupedResourceCounts NextToken TotalDiscoveredResources
---------- --------------------- --------- ------------------------
           {}                              455
```
**Example 2: This example returns the resource count grouped by RESOURCE\_TYPE for the filtered region for the given aggregator.**

```
Get-CFGAggregateDiscoveredResourceCount -ConfigurationAggregatorName Master -Filters_Region us-east-1 -GroupByKey RESOURCE_TYPE |
			Select-Object -ExpandProperty GroupedResourceCounts
```
**Output:**

```
GroupName                          ResourceCount
---------                          -------------
AWS::CloudFormation::Stack         12
AWS::CloudFront::Distribution      1
AWS::CloudTrail::Trail             1
AWS::DynamoDB::Table               1
AWS::EC2::EIP                      2
AWS::EC2::FlowLog                  2
AWS::EC2::InternetGateway          4
AWS::EC2::NatGateway               2
AWS::EC2::NetworkAcl               4
AWS::EC2::NetworkInterface         12
AWS::EC2::RouteTable               13
AWS::EC2::SecurityGroup            18
AWS::EC2::Subnet                   16
AWS::EC2::VPC                      4
AWS::EC2::VPCEndpoint              2
AWS::EC2::VPCPeeringConnection     1
AWS::IAM::Group                    2
AWS::IAM::Policy                   51
AWS::IAM::Role                     78
AWS::IAM::User                     7
AWS::Lambda::Function              3
AWS::RDS::DBSecurityGroup          1
AWS::S3::Bucket                    3
AWS::SSM::AssociationCompliance    107
AWS::SSM::ManagedInstanceInventory 108
```
+  For API details, see [GetAggregateDiscoveredResourceCounts](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CFGAggregateDiscoveredResourceList`
<a name="config-service_ListAggregateDiscoveredResources_powershell_topic"></a>

The following code example shows how to use `Get-CFGAggregateDiscoveredResourceList`.

**Tools for PowerShell V5**
**Example 1: This example returns the resource identifiers for the given resource type aggregated in 'Ireland' aggregator. For the list of resource types, please check https://docs.aws.amazon.com/sdkfornet/v4/apidocs/index.html?page=ConfigService/TConfigServiceResourceType.html&tocid=Amazon\_ConfigService\_ResourceType.**

```
Get-CFGAggregateDiscoveredResourceList -ConfigurationAggregatorName Ireland -ResourceType ([Amazon.ConfigService.ResourceType]::AWSAutoScalingAutoScalingGroup)
```
**Output:**

```
ResourceId      : arn:aws:autoscaling:eu-west-1:123456789012:autoScalingGroup:12e3b4fc-1234-1234-a123-1d2ba3c45678:autoScalingGroupName/asg-1
ResourceName    : asg-1
ResourceType    : AWS::AutoScaling::AutoScalingGroup
SourceAccountId : 123456789012
SourceRegion    : eu-west-1
```
**Example 2: This example returns the resource type `AwsEC2SecurityGroup` named 'default' for the given aggregator filtered with region us-east-1.**

```
Get-CFGAggregateDiscoveredResourceList -ConfigurationAggregatorName raju -ResourceType ([Amazon.ConfigService.ResourceType]::AWSEC2SecurityGroup) -Filters_Region us-east-1 -Filters_ResourceName default
```
**Output:**

```
ResourceId      : sg-01234bd5dbfa67c89
ResourceName    : default
ResourceType    : AWS::EC2::SecurityGroup
SourceAccountId : 123456789102
SourceRegion    : us-east-1

ResourceId      : sg-0123a4ebbf56789be
ResourceName    : default
ResourceType    : AWS::EC2::SecurityGroup
SourceAccountId : 123456789102
SourceRegion    : us-east-1

ResourceId      : sg-4fc1d234
ResourceName    : default
ResourceType    : AWS::EC2::SecurityGroup
SourceAccountId : 123456789102
SourceRegion    : us-east-1
```
+  For API details, see [ListAggregateDiscoveredResources](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CFGAggregateResourceConfig`
<a name="config-service_GetAggregateResourceconfig-service_powershell_topic"></a>

The following code example shows how to use `Get-CFGAggregateResourceConfig`.

**Tools for PowerShell V5**
**Example 1: This example returns the Configuration Item for the given resource aggregated and expands Configuration.**

```
(Get-CFGAggregateResourceConfig -ResourceIdentifier_SourceRegion us-east-1 -ResourceIdentifier_SourceAccountId 123456789012 -ResourceIdentifier_ResourceId sg-4fc1d234 -ResourceIdentifier_ResourceType ([Amazon.ConfigService.ResourceType]::AWSEC2SecurityGroup) -ConfigurationAggregatorName raju).Configuration | ConvertFrom-Json
```
**Output:**

```
{"description":"default VPC security group","groupName":"default","ipPermissions":[{"ipProtocol":"-1","ipv6Ranges":[],"prefixListIds":[],"userIdGroupPairs":[{"groupId":"sg-4fc1d234","userId":"123456789012"}],"ipv4Ranges":[],"ipRanges":[]},{"fromPort":3389,"ipProtocol":"tcp","ipv6Ranges":[],"prefixListIds":[],"toPort":3389,"userIdGroupPairs":[],"ipv4Ranges":[{"cidrIp":"54.240.197.224/29","description":"office subnet"},{"cidrIp":"72.21.198.65/32","description":"home pc"}],"ipRanges":["54.240.197.224/29","72.21.198.65/32"]}],"ownerId":"123456789012","groupId":"sg-4fc1d234","ipPermissionsEgress":[{"ipProtocol":"-1","ipv6Ranges":[],"prefixListIds":[],"userIdGroupPairs":[],"ipv4Ranges":[{"cidrIp":"0.0.0.0/0"}],"ipRanges":["0.0.0.0/0"]}],"tags":[],"vpcId":"vpc-2d1c2e34"}
```
+  For API details, see [GetAggregateResourceconfig-service](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CFGAggregateResourceConfigBatch`
<a name="config-service_BatchGetAggregateResourceconfig-service_powershell_topic"></a>

The following code example shows how to use `Get-CFGAggregateResourceConfigBatch`.

**Tools for PowerShell V5**
**Example 1: This example fetches current configuration item for resource (identified) present in the given aggregator.**

```
$resIdentifier=[Amazon.ConfigService.Model.AggregateResourceIdentifier]@{
		ResourceId= "i-012e3cb4df567e8aa"
		ResourceName = "arn:aws:ec2:eu-west-1:123456789012:instance/i-012e3cb4df567e8aa"
		ResourceType = [Amazon.ConfigService.ResourceType]::AWSEC2Instance
		SourceAccountId = "123456789012"
		SourceRegion = "eu-west-1"
	}

	Get-CFGAggregateResourceConfigBatch -ResourceIdentifier $resIdentifier -ConfigurationAggregatorName raju
```
**Output:**

```
BaseConfigurationItems UnprocessedResourceIdentifiers
---------------------- ------------------------------
{}                     {arn:aws:ec2:eu-west-1:123456789012:instance/i-012e3cb4df567e8aa}
```
+  For API details, see [BatchGetAggregateResourceconfig-service](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CFGAggregationAuthorizationList`
<a name="config-service_DescribeAggregationAuthorizations_powershell_topic"></a>

The following code example shows how to use `Get-CFGAggregationAuthorizationList`.

**Tools for PowerShell V5**
**Example 1: This example retrieves authorizations granted to aggregators.**

```
Get-CFGAggregationAuthorizationList
```
**Output:**

```
AggregationAuthorizationArn                                                            AuthorizedAccountId AuthorizedAwsRegion CreationTime
---------------------------                                                            ------------------- ------------------- ------------
arn:aws:config-service:eu-west-1:123456789012:aggregation-authorization/123456789012/eu-west-1 123456789012        eu-west-1           8/26/2019 12:55:27 AM
```
+  For API details, see [DescribeAggregationAuthorizations](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CFGComplianceByConfigRule`
<a name="config-service_DescribeComplianceByConfigRule_powershell_topic"></a>

The following code example shows how to use `Get-CFGComplianceByConfigRule`.

**Tools for PowerShell V5**
**Example 1: This example retrieves compliances details for the rule ebs-optimized-instance, for which there is no current evaluation results for the rule, hence it returns INSUFFICIENT\_DATA**

```
(Get-CFGComplianceByConfigRule -ConfigRuleName ebs-optimized-instance).Compliance
```
**Output:**

```
ComplianceContributorCount ComplianceType
-------------------------- --------------
                           INSUFFICIENT_DATA
```
**Example 2: This example returns the number of non-compliant resources for the rule ALB\_HTTP\_TO\_HTTPS\_REDIRECTION\_CHECK.**

```
(Get-CFGComplianceByConfigRule -ConfigRuleName ALB_HTTP_TO_HTTPS_REDIRECTION_CHECK -ComplianceType NON_COMPLIANT).Compliance.ComplianceContributorCount
```
**Output:**

```
CapExceeded CappedCount
----------- -----------
False       2
```
+  For API details, see [DescribeComplianceByConfigRule](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CFGComplianceByResource`
<a name="config-service_DescribeComplianceByResource_powershell_topic"></a>

The following code example shows how to use `Get-CFGComplianceByResource`.

**Tools for PowerShell V5**
**Example 1: This example checks the `AWS::SSM::ManagedInstanceInventory` resource type for 'COMPLIANT' compliance type.**

```
Get-CFGComplianceByResource -ComplianceType COMPLIANT -ResourceType AWS::SSM::ManagedInstanceInventory
```
**Output:**

```
Compliance                            ResourceId          ResourceType
----------                            ----------          ------------
Amazon.ConfigService.Model.Compliance i-0123bcf4b567890e3 AWS::SSM::ManagedInstanceInventory
Amazon.ConfigService.Model.Compliance i-0a1234f6f5d6b78f7 AWS::SSM::ManagedInstanceInventory
```
+  For API details, see [DescribeComplianceByResource](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CFGComplianceDetailsByConfigRule`
<a name="config-service_GetComplianceDetailsByConfigRule_powershell_topic"></a>

The following code example shows how to use `Get-CFGComplianceDetailsByConfigRule`.

**Tools for PowerShell V5**
**Example 1: This example obtains the evaluation results for the rule access-keys-rotated and returns the output grouped by compliance-type**

```
Get-CFGComplianceDetailsByConfigRule -ConfigRuleName access-keys-rotated | Group-Object ComplianceType
```
**Output:**

```
Count Name                      Group
----- ----                      -----
    2 COMPLIANT                 {Amazon.ConfigService.Model.EvaluationResult, Amazon.ConfigService.Model.EvaluationResult}
    5 NON_COMPLIANT             {Amazon.ConfigService.Model.EvaluationResult, Amazon.ConfigService.Model.EvaluationResult, Amazon.ConfigService.Model.EvaluationRes...
```
**Example 2: This example queries compliance details for the rule access-keys-rotated for COMPLIANT resources.**

```
Get-CFGComplianceDetailsByConfigRule -ConfigRuleName access-keys-rotated -ComplianceType COMPLIANT | ForEach-Object {$_.EvaluationResultIdentifier.EvaluationResultQualifier}
```
**Output:**

```
ConfigRuleName      ResourceId            ResourceType
--------------      ----------            ------------
access-keys-rotated BCAB1CDJ2LITAPVEW3JAH AWS::IAM::User
access-keys-rotated BCAB1CDJ2LITL3EHREM4Q AWS::IAM::User
```
+  For API details, see [GetComplianceDetailsByConfigRule](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CFGComplianceDetailsByResource`
<a name="config-service_GetComplianceDetailsByResource_powershell_topic"></a>

The following code example shows how to use `Get-CFGComplianceDetailsByResource`.

**Tools for PowerShell V5**
**Example 1: This example evaulation results for the given resource.**

```
Get-CFGComplianceDetailsByResource -ResourceId ABCD5STJ4EFGHIVEW6JAH -ResourceType 'AWS::IAM::User'
```
**Output:**

```
Annotation                 :
ComplianceType             : COMPLIANT
ConfigRuleInvokedTime      : 8/25/2019 11:34:56 PM
EvaluationResultIdentifier : Amazon.ConfigService.Model.EvaluationResultIdentifier
ResultRecordedTime         : 8/25/2019 11:34:56 PM
ResultToken                :
```
+  For API details, see [GetComplianceDetailsByResource](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CFGComplianceSummaryByConfigRule`
<a name="config-service_GetComplianceSummaryByConfigRule_powershell_topic"></a>

The following code example shows how to use `Get-CFGComplianceSummaryByConfigRule`.

**Tools for PowerShell V5**
**Example 1: This sample returns the number of Config rules that are non-compliant.**

```
Get-CFGComplianceSummaryByConfigRule -Select ComplianceSummary.NonCompliantResourceCount
```
**Output:**

```
CapExceeded CappedCount
----------- -----------
False       9
```
+  For API details, see [GetComplianceSummaryByConfigRule](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CFGComplianceSummaryByResourceType`
<a name="config-service_GetComplianceSummaryByResourceType_powershell_topic"></a>

The following code example shows how to use `Get-CFGComplianceSummaryByResourceType`.

**Tools for PowerShell V5**
**Example 1: This sample returns the number of resources that are compliant or noncompliant and converts the output to json.**

```
Get-CFGComplianceSummaryByResourceType -Select ComplianceSummariesByResourceType.ComplianceSummary | ConvertTo-Json
{
  "ComplianceSummaryTimestamp": "2019-12-14T06:14:49.778Z",
  "CompliantResourceCount": {
    "CapExceeded": false,
    "CappedCount": 2
  },
  "NonCompliantResourceCount": {
    "CapExceeded": true,
    "CappedCount": 100
  }
}
```
+  For API details, see [GetComplianceSummaryByResourceType](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CFGConfigRule`
<a name="config-service_DescribeConfigRules_powershell_topic"></a>

The following code example shows how to use `Get-CFGConfigRule`.

**Tools for PowerShell V5**
**Example 1: This sample lists config rules for the account, with selected properties.**

```
Get-CFGConfigRule | Select-Object ConfigRuleName, ConfigRuleId, ConfigRuleArn, ConfigRuleState
```
**Output:**

```
ConfigRuleName                                    ConfigRuleId       ConfigRuleArn                                                        ConfigRuleState
--------------                                    ------------       -------------                                                        ---------------
ALB_REDIRECTION_CHECK                             config-rule-12iyn3 arn:aws:config-service:eu-west-1:123456789012:config-rule/config-rule-12iyn3 ACTIVE
access-keys-rotated                               config-rule-aospfr arn:aws:config-service:eu-west-1:123456789012:config-rule/config-rule-aospfr ACTIVE
autoscaling-group-elb-healthcheck-required        config-rule-cn1f2x arn:aws:config-service:eu-west-1:123456789012:config-rule/config-rule-cn1f2x ACTIVE
```
+  For API details, see [DescribeConfigRules](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CFGConfigRuleEvaluationStatus`
<a name="config-service_DescribeConfigRuleEvaluationStatus_powershell_topic"></a>

The following code example shows how to use `Get-CFGConfigRuleEvaluationStatus`.

**Tools for PowerShell V5**
**Example 1: This sample returns the status information for the given config rules. **

```
Get-CFGConfigRuleEvaluationStatus -ConfigRuleName root-account-mfa-enabled, vpc-flow-logs-enabled
```
**Output:**

```
ConfigRuleArn                : arn:aws:config:eu-west-1:123456789012:config-rule/config-rule-kvq1wk
ConfigRuleId                 : config-rule-kvq1wk
ConfigRuleName               : root-account-mfa-enabled
FirstActivatedTime           : 8/27/2019 8:05:17 AM
FirstEvaluationStarted       : True
LastErrorCode                :
LastErrorMessage             :
LastFailedEvaluationTime     : 1/1/0001 12:00:00 AM
LastFailedInvocationTime     : 1/1/0001 12:00:00 AM
LastSuccessfulEvaluationTime : 12/13/2019 8:12:03 AM
LastSuccessfulInvocationTime : 12/13/2019 8:12:03 AM

ConfigRuleArn                : arn:aws:config:eu-west-1:123456789012:config-rule/config-rule-z1s23b
ConfigRuleId                 : config-rule-z1s23b
ConfigRuleName               : vpc-flow-logs-enabled
FirstActivatedTime           : 8/14/2019 6:23:44 AM
FirstEvaluationStarted       : True
LastErrorCode                :
LastErrorMessage             :
LastFailedEvaluationTime     : 1/1/0001 12:00:00 AM
LastFailedInvocationTime     : 1/1/0001 12:00:00 AM
LastSuccessfulEvaluationTime : 12/13/2019 7:12:01 AM
LastSuccessfulInvocationTime : 12/13/2019 7:12:01 AM
```
+  For API details, see [DescribeConfigRuleEvaluationStatus](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CFGConfigurationAggregatorList`
<a name="config-service_DescribeConfigurationAggregators_powershell_topic"></a>

The following code example shows how to use `Get-CFGConfigurationAggregatorList`.

**Tools for PowerShell V5**
**Example 1: This sample returns all the aggregators for the region/account.**

```
Get-CFGConfigurationAggregatorList
```
**Output:**

```
AccountAggregationSources     : {Amazon.ConfigService.Model.AccountAggregationSource}
ConfigurationAggregatorArn    : arn:aws:config-service:eu-west-1:123456789012:config-aggregator/config-aggregator-xabca1me
ConfigurationAggregatorName   : IrelandMaster
CreationTime                  : 8/25/2019 11:42:39 PM
LastUpdatedTime               : 8/25/2019 11:42:39 PM
OrganizationAggregationSource :

AccountAggregationSources     : {}
ConfigurationAggregatorArn    : arn:aws:config-service:eu-west-1:123456789012:config-aggregator/config-aggregator-qubqabcd
ConfigurationAggregatorName   : raju
CreationTime                  : 8/11/2019 8:39:25 AM
LastUpdatedTime               : 8/11/2019 8:39:25 AM
OrganizationAggregationSource : Amazon.ConfigService.Model.OrganizationAggregationSource
```
+  For API details, see [DescribeConfigurationAggregators](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CFGConfigurationAggregatorSourcesStatus`
<a name="config-service_DescribeConfigurationAggregatorSourcesStatus_powershell_topic"></a>

The following code example shows how to use `Get-CFGConfigurationAggregatorSourcesStatus`.

**Tools for PowerShell V5**
**Example 1: This sample displays requested fields for the sources in the given aggregator.**

```
Get-CFGConfigurationAggregatorSourcesStatus -ConfigurationAggregatorName raju | select SourceType, LastUpdateStatus, LastUpdateTime, SourceId
```
**Output:**

```
SourceType   LastUpdateStatus LastUpdateTime        SourceId
----------   ---------------- --------------        --------
ORGANIZATION SUCCEEDED        12/31/2019 7:45:06 AM Organization
ACCOUNT      SUCCEEDED        12/31/2019 7:09:38 AM 612641234567
ACCOUNT      SUCCEEDED        12/31/2019 7:12:53 AM 933301234567
ACCOUNT      SUCCEEDED        12/31/2019 7:18:10 AM 933301234567
ACCOUNT      SUCCEEDED        12/31/2019 7:25:17 AM 933301234567
ACCOUNT      SUCCEEDED        12/31/2019 7:25:49 AM 612641234567
ACCOUNT      SUCCEEDED        12/31/2019 7:26:11 AM 612641234567
```
+  For API details, see [DescribeConfigurationAggregatorSourcesStatus](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CFGConfigurationRecorder`
<a name="config-service_DescribeConfigurationRecorders_powershell_topic"></a>

The following code example shows how to use `Get-CFGConfigurationRecorder`.

**Tools for PowerShell V5**
**Example 1: This example returns the details of configuration recorders.**

```
Get-CFGConfigurationRecorder | Format-List
```
**Output:**

```
Name           : default
RecordingGroup : Amazon.ConfigService.Model.RecordingGroup
RoleARN        : arn:aws:iam::123456789012:role/aws-service-role/config.amazonaws.com/AWSServiceRoleForConfig
```
+  For API details, see [DescribeConfigurationRecorders](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CFGConfigurationRecorderStatus`
<a name="config-service_DescribeConfigurationRecorderStatus_powershell_topic"></a>

The following code example shows how to use `Get-CFGConfigurationRecorderStatus`.

**Tools for PowerShell V5**
**Example 1: This sample returns status of the configuration recorders. **

```
Get-CFGConfigurationRecorderStatus
```
**Output:**

```
LastErrorCode        :
LastErrorMessage     :
LastStartTime        : 10/11/2019 10:13:51 AM
LastStatus           : Success
LastStatusChangeTime : 12/31/2019 6:14:12 AM
LastStopTime         : 10/11/2019 10:13:46 AM
Name                 : default
Recording            : True
```
+  For API details, see [DescribeConfigurationRecorderStatus](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CFGConformancePack`
<a name="config-service_DescribeConformancePacks_powershell_topic"></a>

The following code example shows how to use `Get-CFGConformancePack`.

**Tools for PowerShell V5**
**Example 1: This sample lists all conformance packs.**

```
Get-CFGConformancePack
```
**Output:**

```
ConformancePackArn             : arn:aws:config:eu-west-1:123456789012:conformance-pack/dono/conformance-pack-p0acq8bpz
ConformancePackId              : conformance-pack-p0acabcde
ConformancePackInputParameters : {}
ConformancePackName            : dono
CreatedBy                      :
DeliveryS3Bucket               : kt-ps-examples
DeliveryS3KeyPrefix            :
LastUpdateRequestedTime        : 12/31/2019 8:45:31 AM
```
+  For API details, see [DescribeConformancePacks](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CFGDeliveryChannel`
<a name="config-service_DescribeDeliveryChannels_powershell_topic"></a>

The following code example shows how to use `Get-CFGDeliveryChannel`.

**Tools for PowerShell V5**
**Example 1: This example retrieves the delivery channel for the region and displays details.**

```
Get-CFGDeliveryChannel -Region eu-west-1 | Select-Object Name, S3BucketName, S3KeyPrefix, @{N="DeliveryFrequency";E={$_.ConfigSnapshotDeliveryProperties.DeliveryFrequency}}
```
**Output:**

```
Name    S3BucketName               S3KeyPrefix DeliveryFrequency
----    ------------               ----------- -----------------
default config-bucket-NA my          TwentyFour_Hours
```
+  For API details, see [DescribeDeliveryChannels](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CFGResourceTag`
<a name="config-service_ListTagsForResource_powershell_topic"></a>

The following code example shows how to use `Get-CFGResourceTag`.

**Tools for PowerShell V5**
**Example 1: This example lists associated tags for the given resource**

```
Get-CFGResourceTag -ResourceArn $rules[0].ConfigRuleArn
```
**Output:**

```
Key     Value
---     -----
Version 1.3
```
+  For API details, see [ListTagsForResource](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-CFGConformancePack`
<a name="config-service_DeleteConformancePack_powershell_topic"></a>

The following code example shows how to use `Remove-CFGConformancePack`.

**Tools for PowerShell V5**
**Example 1: This sample removes the given conformance pack, along with all the rules, remediation actions and evaluation results for the pack.**

```
Remove-CFGConformancePack -ConformancePackName dono
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-CFGConformancePack (DeleteConformancePack)" on target "dono".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"): Y
```
+  For API details, see [DeleteConformancePack](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Write-CFGConformancePack`
<a name="config-service_PutConformancePack_powershell_topic"></a>

The following code example shows how to use `Write-CFGConformancePack`.

**Tools for PowerShell V5**
**Example 1: This sample creates conformance pack, fetching template from the given yaml file. **

```
Write-CFGConformancePack -ConformancePackName dono -DeliveryS3Bucket amzn-s3-demo-bucket -TemplateBody (Get-Content C:\windows\temp\template.yaml -Raw)
```
+  For API details, see [PutConformancePack](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Write-CFGDeliveryChannel`
<a name="config-service_PutDeliveryChannel_powershell_topic"></a>

The following code example shows how to use `Write-CFGDeliveryChannel`.

**Tools for PowerShell V5**
**Example 1: This example changes the deliveryFrequency property of an existing delivery channel.**

```
Write-CFGDeliveryChannel -ConfigSnapshotDeliveryProperties_DeliveryFrequency TwentyFour_Hours -DeliveryChannelName default -DeliveryChannel_S3BucketName amzn-s3-demo-bucket -DeliveryChannel_S3KeyPrefix my
```
+  For API details, see [PutDeliveryChannel](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.
