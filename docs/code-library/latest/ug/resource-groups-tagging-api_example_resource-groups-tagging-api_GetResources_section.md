---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/resource-groups-tagging-api_example_resource-groups-tagging-api_GetResources_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `GetResources` with a CLI
<a name="resource-groups-tagging-api_example_resource-groups-tagging-api_GetResources_section"></a>

The following code examples show how to use `GetResources`.

------
#### [ CLI ]

**AWS CLI**
**To get a list of tagged resources**
The following `get-resources` example displays a list of resources in the account that are tagged with the specified key name and value.

```
aws resourcegroupstaggingapi get-resources \
    --tag-filters {{Key=Environment,Values=Production}} \
    --tags-per-page {{100}}
```
Output:

```
{
    "ResourceTagMappingList": [
        {
            "ResourceARN": " arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-7sbz2Kz0",
            "Tags": [
                {
                    "Key": "Environment",
                    "Value": "Production"
                }
            ]
        }
    ]
}
```
For more information, see [GetResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html) in the *Resource Groups Tagging API Reference*.
+  For API details, see [GetResources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resourcegroupstaggingapi/get-resources.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Returns all the tagged resources in a region and the tag keys associated with the resource. If no -Region parameter is supplied to the cmdlet it will attempt to infer region from the shell or EC2 instance metadata.**

```
Get-RGTResource
```
**Output:**

```
ResourceARN                                                      Tags
-----------                                                      ----
arn:aws:dynamodb:us-west-2:123456789012:table/mytable            {stage, version}
arn:aws:s3:::amzn-s3-demo-bucket                                            {stage, version, othertag}
```
**Example 2: Returns all the tagged resources of the specified type in a region. The string for each service name and resource type is the same as that embedded in a resource's Amazon Resource Name (ARN).**

```
Get-RGTResource -ResourceType "s3"
```
**Output:**

```
ResourceARN                                                      Tags
-----------                                                      ----
arn:aws:s3:::amzn-s3-demo-bucket                                            {stage, version, othertag}
```
**Example 3: Returns all the tagged resources of the specified type in a region. Note that when the resource types are piped into the cmdlet, one call to the service is made for each supplied resource type.**

```
"dynamodb","s3" | Get-RGTResource
```
**Output:**

```
ResourceARN                                                      Tags
-----------                                                      ----
arn:aws:dynamodb:us-west-2:123456789012:table/mytable            {stage, version}
arn:aws:s3:::amzn-s3-demo-bucket                                            {stage, version, othertag}
```
**Example 4: Returns all the tagged resources that match the specified filter.**

```
Get-RGTResource -TagFilter @{ Key="stage" }
```
**Output:**

```
ResourceARN                                                      Tags
-----------                                                      ----
arn:aws:s3:::amzn-s3-demo-bucket                                            {stage, version, othertag}
```
**Example 5: Returns all the tagged resources that match the specified filter and resource type.**

```
Get-RGTResource -TagFilter @{ Key="stage" } -ResourceType "dynamodb"
```
**Output:**

```
ResourceARN                                                      Tags
-----------                                                      ----
arn:aws:dynamodb:us-west-2:123456789012:table/mytable            {stage, version}
```
**Example 6: Returns all the tagged resources that match the specified filter.**

```
Get-RGTResource -TagFilter @{ Key="stage"; Values=@("beta","gamma") }
```
**Output:**

```
ResourceARN                                                      Tags
-----------                                                      ----
arn:aws:dynamodb:us-west-2:123456789012:table/mytable            {stage, version}
```
+  For API details, see [GetResources](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Returns all the tagged resources in a region and the tag keys associated with the resource. If no -Region parameter is supplied to the cmdlet it will attempt to infer region from the shell or EC2 instance metadata.**

```
Get-RGTResource
```
**Output:**

```
ResourceARN                                                      Tags
-----------                                                      ----
arn:aws:dynamodb:us-west-2:123456789012:table/mytable            {stage, version}
arn:aws:s3:::amzn-s3-demo-bucket                                            {stage, version, othertag}
```
**Example 2: Returns all the tagged resources of the specified type in a region. The string for each service name and resource type is the same as that embedded in a resource's Amazon Resource Name (ARN).**

```
Get-RGTResource -ResourceType "s3"
```
**Output:**

```
ResourceARN                                                      Tags
-----------                                                      ----
arn:aws:s3:::amzn-s3-demo-bucket                                            {stage, version, othertag}
```
**Example 3: Returns all the tagged resources of the specified type in a region. Note that when the resource types are piped into the cmdlet, one call to the service is made for each supplied resource type.**

```
"dynamodb","s3" | Get-RGTResource
```
**Output:**

```
ResourceARN                                                      Tags
-----------                                                      ----
arn:aws:dynamodb:us-west-2:123456789012:table/mytable            {stage, version}
arn:aws:s3:::amzn-s3-demo-bucket                                            {stage, version, othertag}
```
**Example 4: Returns all the tagged resources that match the specified filter.**

```
Get-RGTResource -TagFilter @{ Key="stage" }
```
**Output:**

```
ResourceARN                                                      Tags
-----------                                                      ----
arn:aws:s3:::amzn-s3-demo-bucket                                            {stage, version, othertag}
```
**Example 5: Returns all the tagged resources that match the specified filter and resource type.**

```
Get-RGTResource -TagFilter @{ Key="stage" } -ResourceType "dynamodb"
```
**Output:**

```
ResourceARN                                                      Tags
-----------                                                      ----
arn:aws:dynamodb:us-west-2:123456789012:table/mytable            {stage, version}
```
**Example 6: Returns all the tagged resources that match the specified filter.**

```
Get-RGTResource -TagFilter @{ Key="stage"; Values=@("beta","gamma") }
```
**Output:**

```
ResourceARN                                                      Tags
-----------                                                      ----
arn:aws:dynamodb:us-west-2:123456789012:table/mytable            {stage, version}
```
+  For API details, see [GetResources](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
