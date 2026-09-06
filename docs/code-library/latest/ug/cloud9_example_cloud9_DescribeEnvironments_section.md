---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cloud9_example_cloud9_DescribeEnvironments_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeEnvironments` with a CLI
<a name="cloud9_example_cloud9_DescribeEnvironments_section"></a>

The following code examples show how to use `DescribeEnvironments`.

------
#### [ CLI ]

**AWS CLI**
**To get information about AWS Cloud9 development environments**
This example gets information about the specified AWS Cloud9 development environments.
Command:

```
aws cloud9 describe-environments --environment-ids {{685f892f431b45c2b28cb69eadcdb0EX}} {{349c86d4579e4e7298d500ff57a6b2EX}}
```
Output:

```
{
  "environments": [
    {
      "id": "685f892f431b45c2b28cb69eadcdb0EX",
      "name": "my-demo-ec2-env",
      "description": "Created from CodeStar.",
      "type": "ec2",
      "arn": "arn:aws:cloud9:us-east-1:123456789012:environment:685f892f431b45c2b28cb69eadcdb0EX",
      "ownerArn": "arn:aws:iam::123456789012:user/MyDemoUser",
      "lifecycle": {
        "status": "CREATED"
      }
    },
    {
      "id": "349c86d4579e4e7298d500ff57a6b2EX",
      "name": my-demo-ssh-env",
      "description": "",
      "type": "ssh",
      "arn": "arn:aws:cloud9:us-east-1:123456789012:environment:349c86d4579e4e7298d500ff57a6b2EX",
      "ownerArn": "arn:aws:iam::123456789012:user/MyDemoUser",
      "lifecycle": {
        "status": "CREATED"
      }
    }
  ]
}
```
+  For API details, see [DescribeEnvironments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/describe-environments.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example gets information about the specified AWS Cloud9 development environments.**

```
Get-C9EnvironmentData -EnvironmentId 685f892f431b45c2b28cb69eadcdb0EX,1980b80e5f584920801c09086667f0EX
```
**Output:**

```
Arn         : arn:aws:cloud9:us-east-1:123456789012:environment:685f892f431b45c2b28cb69eadcdb0EX
Description : Created from CodeStar.
Id          : 685f892f431b45c2b28cb69eadcdb0EX
Lifecycle   : Amazon.Cloud9.Model.EnvironmentLifecycle
Name        : my-demo-ec2-env
OwnerArn    : arn:aws:iam::123456789012:user/MyDemoUser
Type        : ec2

Arn         : arn:aws:cloud9:us-east-1:123456789012:environment:1980b80e5f584920801c09086667f0EX
Description :
Id          : 1980b80e5f584920801c09086667f0EX
Lifecycle   : Amazon.Cloud9.Model.EnvironmentLifecycle
Name        : my-demo-ssh-env
OwnerArn    : arn:aws:iam::123456789012:user/MyDemoUser
Type        : ssh
```
**Example 2: This example gets information about the lifecycle status of the specified AWS Cloud9 development environment.**

```
(Get-C9EnvironmentData -EnvironmentId 685f892f431b45c2b28cb69eadcdb0EX).Lifecycle
```
**Output:**

```
FailureResource Reason Status
--------------- ------ ------
                       CREATED
```
+  For API details, see [DescribeEnvironments](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example gets information about the specified AWS Cloud9 development environments.**

```
Get-C9EnvironmentData -EnvironmentId 685f892f431b45c2b28cb69eadcdb0EX,1980b80e5f584920801c09086667f0EX
```
**Output:**

```
Arn         : arn:aws:cloud9:us-east-1:123456789012:environment:685f892f431b45c2b28cb69eadcdb0EX
Description : Created from CodeStar.
Id          : 685f892f431b45c2b28cb69eadcdb0EX
Lifecycle   : Amazon.Cloud9.Model.EnvironmentLifecycle
Name        : my-demo-ec2-env
OwnerArn    : arn:aws:iam::123456789012:user/MyDemoUser
Type        : ec2

Arn         : arn:aws:cloud9:us-east-1:123456789012:environment:1980b80e5f584920801c09086667f0EX
Description :
Id          : 1980b80e5f584920801c09086667f0EX
Lifecycle   : Amazon.Cloud9.Model.EnvironmentLifecycle
Name        : my-demo-ssh-env
OwnerArn    : arn:aws:iam::123456789012:user/MyDemoUser
Type        : ssh
```
**Example 2: This example gets information about the lifecycle status of the specified AWS Cloud9 development environment.**

```
(Get-C9EnvironmentData -EnvironmentId 685f892f431b45c2b28cb69eadcdb0EX).Lifecycle
```
**Output:**

```
FailureResource Reason Status
--------------- ------ ------
                       CREATED
```
+  For API details, see [DescribeEnvironments](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
