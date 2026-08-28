---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/userguide/troubleshooting-portal.html
---

# Troubleshoot an AWS IoT SiteWise portal
<a name="troubleshooting-portal"></a>

Troubleshoot common issues with your AWS IoT SiteWise portals.

## Users and administrators can't access AWS IoT SiteWise portal
<a name="acessing-SiteWise-portals"></a>

If users or administrators cannot access your AWS IoT SiteWise portal, you may have restricted permissions in attached AWS Identity and Access Management (IAM) policies that prevent successful logins.

See the following examples of IAM policies that will result in login failure:

**Note**
Any attached IAM policies that include a `"Condition"` element will cause a login failure.

**Example 1**: The condition here is a limited IP, and this will cause a login failure.

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
                "iotsitewise:DescribePortal"
            ],
            "Resource": "*",
            "Condition": {
                "IpAddress": {
                    "aws:SourceIp": [
                        "{{203.0.113.0/24}}"
                    ]
                }
            }
        }
    ]
}
```

------

**Example 2**: The condition here is an included tag, and this will cause a login failure.

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
                "iotsitewise:DescribePortal"
            ],
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "aws:ResourceTag/project": "*"
                }
            }
        }
    ]
}
```

------

When adding users or administrators to the portal, avoid creating IAM policies that restrict user permissions, such as limited IP. Any attached policies with restricted permissions will not be able to connect to the AWS IoT SiteWise portal.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
