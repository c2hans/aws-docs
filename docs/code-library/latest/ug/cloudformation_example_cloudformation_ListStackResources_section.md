---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cloudformation_example_cloudformation_ListStackResources_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListStackResources` with a CLI
<a name="cloudformation_example_cloudformation_ListStackResources_section"></a>

The following code examples show how to use `ListStackResources`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Creating your first infrastructure stack](cloudformation_example_cloudformation_GettingStarted_021_section.md)

------
#### [ CLI ]

**AWS CLI**
**To list resources in a stack**
The following command displays the list of resources in the specified stack.

```
aws cloudformation list-stack-resources \
    --stack-name {{my-stack}}
```
Output:

```
{
    "StackResourceSummaries": [
        {
            "LogicalResourceId": "bucket",
            "PhysicalResourceId": "my-stack-bucket-1vc62xmplgguf",
            "ResourceType": "AWS::S3::Bucket",
            "LastUpdatedTimestamp": "2019-10-02T04:34:11.345Z",
            "ResourceStatus": "CREATE_COMPLETE",
            "DriftInformation": {
                "StackResourceDriftStatus": "IN_SYNC"
            }
        },
        {
            "LogicalResourceId": "function",
            "PhysicalResourceId": "my-function-SEZV4XMPL4S5",
            "ResourceType": "AWS::Lambda::Function",
            "LastUpdatedTimestamp": "2019-10-02T05:34:27.989Z",
            "ResourceStatus": "UPDATE_COMPLETE",
            "DriftInformation": {
                "StackResourceDriftStatus": "IN_SYNC"
            }
        },
        {
            "LogicalResourceId": "functionRole",
            "PhysicalResourceId": "my-functionRole-HIZXMPLEOM9E",
            "ResourceType": "AWS::IAM::Role",
            "LastUpdatedTimestamp": "2019-10-02T04:34:06.350Z",
            "ResourceStatus": "CREATE_COMPLETE",
            "DriftInformation": {
                "StackResourceDriftStatus": "IN_SYNC"
            }
        }
    ]
}
```
+  For API details, see [ListStackResources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-stack-resources.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Returns descriptions of all the resources associated with the specified stack.**

```
Get-CFNStackResourceSummary -StackName "myStack"
```
+  For API details, see [ListStackResources](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Returns descriptions of all the resources associated with the specified stack.**

```
Get-CFNStackResourceSummary -StackName "myStack"
```
+  For API details, see [ListStackResources](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
