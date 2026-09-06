---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cloudformation_example_cloudformation_DescribeStackResource_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeStackResource` with a CLI
<a name="cloudformation_example_cloudformation_DescribeStackResource_section"></a>

The following code examples show how to use `DescribeStackResource`.

------
#### [ CLI ]

**AWS CLI**
**To get information about a stack resource**
The following `describe-stack-resource` example displays details for the resource named `MyFunction` in the specified stack.

```
aws cloudformation describe-stack-resource \
    --stack-name {{MyStack}} \
    --logical-resource-id {{MyFunction}}
```
Output:

```
{
    "StackResourceDetail": {
        "StackName": "MyStack",
        "StackId": "arn:aws:cloudformation:us-east-2:123456789012:stack/MyStack/d0a825a0-e4cd-xmpl-b9fb-061c69e99204",
        "LogicalResourceId": "MyFunction",
        "PhysicalResourceId": "my-function-SEZV4XMPL4S5",
        "ResourceType": "AWS::Lambda::Function",
        "LastUpdatedTimestamp": "2019-10-02T05:34:27.989Z",
        "ResourceStatus": "UPDATE_COMPLETE",
        "Metadata": "{}",
        "DriftInformation": {
            "StackResourceDriftStatus": "IN_SYNC"
        }
    }
}
```
+  For API details, see [DescribeStackResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stack-resource.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Returns the description of a resource identified in the template associated with the specified stack by the logical ID "MyDBInstance".**

```
Get-CFNStackResource -StackName "myStack" -LogicalResourceId "MyDBInstance"
```
+  For API details, see [DescribeStackResource](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Returns the description of a resource identified in the template associated with the specified stack by the logical ID "MyDBInstance".**

```
Get-CFNStackResource -StackName "myStack" -LogicalResourceId "MyDBInstance"
```
+  For API details, see [DescribeStackResource](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
