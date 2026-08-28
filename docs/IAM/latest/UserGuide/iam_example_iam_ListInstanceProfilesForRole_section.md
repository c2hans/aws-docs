---
source_url: https://docs.aws.amazon.com/IAM/latest/UserGuide/iam_example_iam_ListInstanceProfilesForRole_section.html
---

# Use `ListInstanceProfilesForRole` with a CLI
<a name="iam_example_iam_ListInstanceProfilesForRole_section"></a>

The following code examples show how to use `ListInstanceProfilesForRole`.

------
#### [ CLI ]

**AWS CLI**
**To list the instance profiles for an IAM role**
The following `list-instance-profiles-for-role` command lists the instance profiles that are associated with the role `Test-Role`.

```
aws iam list-instance-profiles-for-role \
    --role-name {{Test-Role}}
```
Output:

```
{
    "InstanceProfiles": [
        {
            "InstanceProfileId": "AIDGPMS9RO4H3FEXAMPLE",
            "Roles": [
                {
                    "AssumeRolePolicyDocument": "<URL-encoded-JSON>",
                    "RoleId": "AIDACKCEVSQ6C2EXAMPLE",
                    "CreateDate": "2013-06-07T20:42:15Z",
                    "RoleName": "Test-Role",
                    "Path": "/",
                    "Arn": "arn:aws:iam::123456789012:role/Test-Role"
                }
            ],
            "CreateDate": "2013-06-07T21:05:24Z",
            "InstanceProfileName": "ExampleInstanceProfile",
            "Path": "/",
            "Arn": "arn:aws:iam::123456789012:instance-profile/ExampleInstanceProfile"
        }
    ]
}
```
For more information, see [Using instance profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html) in the *AWS IAM User Guide*.
+  For API details, see [ListInstanceProfilesForRole](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/list-instance-profiles-for-role.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example returns details of the instance profile associated with the role `ec2instancerole`.**

```
Get-IAMInstanceProfileForRole -RoleName ec2instancerole
```
**Output:**

```
      Arn                 : arn:aws:iam::123456789012:instance-profile/ec2instancerole
      CreateDate          : 2/17/2015 2:49:04 PM
      InstanceProfileId   : HH36PTZQJUR32EXAMPLE1
      InstanceProfileName : ec2instancerole
      Path                : /
      Roles               : {ec2instancerole}
```
+  For API details, see [ListInstanceProfilesForRole](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example returns details of the instance profile associated with the role `ec2instancerole`.**

```
Get-IAMInstanceProfileForRole -RoleName ec2instancerole
```
**Output:**

```
      Arn                 : arn:aws:iam::123456789012:instance-profile/ec2instancerole
      CreateDate          : 2/17/2015 2:49:04 PM
      InstanceProfileId   : HH36PTZQJUR32EXAMPLE1
      InstanceProfileName : ec2instancerole
      Path                : /
      Roles               : {ec2instancerole}
```
+  For API details, see [ListInstanceProfilesForRole](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Identity and Access Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IAM` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
