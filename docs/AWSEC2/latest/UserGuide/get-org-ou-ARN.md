---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/get-org-ou-ARN.html
---

# Get the ARN of an organization or organizational unit
<a name="get-org-ou-ARN"></a>

The organization and the organizational unit ARNs contain the 12-digit management account number. If you don't know the management account number, you can describe the organization and the organizational unit to get the ARN for each. In the following examples, `123456789012` is the account ID of the management account.

**Required permissions**
Before you can get the ARNs, you must have the permission to describe organizations and organizational units. The following policy provides the necessary permission.

------
#### [ JSON ]

****

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "organizations:Describe*"
            ],
            "Resource": "*"
        }
    ]
}
```

------

------
#### [ AWS CLI ]

**To get the ARN of an organization**
Use the [describe-organization](https://docs.aws.amazon.com/cli/latest/reference/organizations/describe-organization.html) command. Add the `--query` option to return only the organization ARN.

```
aws organizations describe-organization --query 'Organization.Arn'
```

The following is example output.

```
"arn:aws:organizations::123456789012:organization/o-1234567abc"
```

**To get the ARN of an organizational unit**
Use the [describe-organizational-unit](https://docs.aws.amazon.com/cli/latest/reference/organizations/describe-organizational-unit.html) command. Use the `--query` parameter to return only the organizational unit ARN.

```
aws organizations describe-organizational-unit \
    --organizational-unit-id {{ou-a123-b4567890}} \
    --query 'OrganizationalUnit.Arn'
```

The following is example output.

```
"arn:aws:organizations::123456789012:ou/o-1234567abc/ou-a123-b4567890"
```

------
#### [ PowerShell ]

**To get the ARN of an organization**
Use the [Get-ORGOrganization](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-ORGOrganization.html) cmdlet.

```
(Get-ORGOrganization).Arn
```

The following is example output.

```
arn:aws:organizations::123456789012:organization/o-1234567abc
```

**To get the ARN of an organizational unit**
Use the [Get-ORGOrganizationalUnit](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-ORGOrganizationalUnit.html) cmdlet.

```
(Get-ORGOrganizationalUnit -OrganizationalUnitId "ou-a123-b4567890").Arn
```

The following is example output.

```
arn:aws:organizations::123456789012:ou/o-1234567abc/ou-a123-b4567890
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
