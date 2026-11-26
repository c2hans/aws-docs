---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/resources-retained.html
---

# Resources retained after deletion

The solution’s CloudFormation stacks retain the following resources after deletion. Review these resources and manually delete any that you no longer need. Retained resources can continue to incur charges.

 **Compute stack**
+ Customer Managed Key
  +  `AwsSolutions/InnovationSandbox/InnovationSandbox-Compute`
+ CloudWatch log groups
  +  `InnovationSandbox-Compute-ISBLogGroupXXXXX`
  +  `InnovationSandbox-Compute-ISBLogGroupCustomResourcesXXXXX`
+ S3 buckets
  + CloudFront distribution host (`innovationsandbox-compute-cloudfrontuiapiisbfronte-XXXXX`)
  + CloudFront distribution access log (`innovationsandbox-compute-cloudfrontuiapiisbfronte-XXXXX`)
  + Application logs archive (`innovationsandbox-compute-logarchivingisblogsarchi-XXXXX`)

 **Data stack**
+ Customer Managed Key
  +  `AwsSolutions/InnovationSandbox/InnovationSandbox-Data`
+ CloudWatch log group
  +  `InnovationSandbox-Data-ISBLogGroupCustomResourcesXXXXX`
+ DynamoDB tables
  +  `InnovationSandbox-Data-SandboxAccountTableXXXXX`
  +  `InnovationSandbox-Data-LeaseTemplateTableXXXXX`
  +  `InnovationSandbox-Data-LeaseTableXXXXX`
  +  `InnovationSandbox-Data-BlueprintTableXXXXX`
  +  `InnovationSandbox-Data-PrincipalTableXXXXX`
  +  `InnovationSandbox-Data-CleanupReportTableXXXXX`
  +  `InnovationSandbox-Data-ConfigTableXXXXX`
  +  `InnovationSandbox-Data-SandboxSpacesUsageTableXXXXX`
  +  `InnovationSandbox-Data-LeaseCostHistoryTableXXXXX`

 **IDC stack**
+ Customer Managed Key
  +  `AwsSolutions/InnovationSandbox/InnovationSandbox-IDC`
+ CloudWatch log group
  +  `InnovationSandbox-IDC-ISBLogGroupCustomResourcesXXXXX`
+ Innovation Sandbox groups
  + <NAMESPACE>\_IsbUsersGroup
  + <NAMESPACE>\_IsbManagersGroup
  + <NAMESPACE>\_IsbAdminsGroup

 **Account Pool stack**
+ Customer Managed Key
  +  `AwsSolutions/InnovationSandbox/InnovationSandbox-AccountPool`
+ CloudWatch log group
  +  `InnovationSandbox-AccountPool-ISBLogGroupCustomResourcesXXXXX`
