---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_Target.html
---

# Target
<a name="API_Target"></a>

An array of search criteria that targets managed nodes using a key-value pair that you specify.

**Note**
 One or more targets must be specified for maintenance window Run Command-type tasks. Depending on the task, targets are optional for other maintenance window task types (Automation, AWS Lambda, and AWS Step Functions). For more information about running tasks that don't specify targets, see [Registering maintenance window tasks without targets](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html) in the * AWS Systems Manager User Guide*.

Supported formats include the following.

 **For all Systems Manager tools:**
+  `Key=tag-key,Values=tag-value-1,tag-value-2`

 **For Automation and Change Manager:**
+  `Key=tag:tag-key,Values=tag-value`
+  `Key=ResourceGroup,Values=resource-group-name`
+  `Key=ParameterValues,Values=value-1,value-2,value-3`
+ To target all instances in the AWS Region:
  +  `Key=AWS::EC2::Instance,Values=*`
  +  `Key=InstanceIds,Values=*`

 **For Run Command and Maintenance Windows:**
+  `Key=InstanceIds,Values=instance-id-1,instance-id-2,instance-id-3`
+  `Key=tag:tag-key,Values=tag-value-1,tag-value-2`
+  `Key=resource-groups:Name,Values=resource-group-name`
+ Additionally, Maintenance Windows support targeting resource types:
  +  `Key=resource-groups:ResourceTypeFilters,Values=resource-type-1,resource-type-2`

 **For State Manager:**
+  `Key=InstanceIds,Values=instance-id-1,instance-id-2,instance-id-3`
+  `Key=tag:tag-key,Values=tag-value-1,tag-value-2`
+ To target all instances in the AWS Region:
  +  `Key=InstanceIds,Values=*`

For more information about how to send commands that target managed nodes using `Key,Value` parameters, see [Targeting multiple managed nodes](https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-targeting) in the * AWS Systems Manager User Guide*.

## Contents
<a name="API_Target_Contents"></a>

 ** Key **   <a name="systemsmanager-Type-Target-Key"></a>
User-defined criteria for sending commands that target managed nodes that meet the criteria.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 163.
Pattern: `^[\p{L}\p{Z}\p{N}_.:/=\-@]*$|resource-groups:ResourceTypeFilters|resource-groups:Name`
Required: No

 ** Values **   <a name="systemsmanager-Type-Target-Values"></a>
User-defined criteria that maps to `Key`. For example, if you specified `tag:ServerRole`, you could specify `value:WebServer` to run a command on instances that include EC2 tags of `ServerRole,WebServer`.
Depending on the type of target, the maximum number of values for a key might be lower than the global maximum of 50.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## See Also
<a name="API_Target_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/Target)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/Target)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/Target)
