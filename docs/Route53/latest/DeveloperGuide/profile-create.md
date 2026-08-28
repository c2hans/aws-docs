---
source_url: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/profile-create.html
---

# Creating Route 53 Profiles
<a name="profile-create"></a>

To create Route 53 Profiles, follow the guidance in this topic. Choose a tab to create a Route 53 Profile by using the Route 53 console, or AWS CLI.
+ [Console](#profile_create_console)
+ [CLI](#profile_create_CLI)

------
#### [ Console ]<a name="profile-create-procedure"></a>

**To create a Route 53 Profile**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the navigation pane, choose **Profiles**.

1. On the navigation bar, choose the Region where you want to create the Profile.

1. Enter a name for the Profile, optionally add tags, and choose **Create Profile**.

   This creates an empty Profile with default configurations to which you can associate resources. After you associate resources to the Profile, you can associate it to a number of VPCs and edit the how some of the Resolver configurations apply to the VPCs.

------
#### [ CLI ]

You can create a Profile by running a AWS CLI command like the following and using your own value for `name`.

`aws route53profiles create-profile --name test`

The following is an example output after you run the command:

```
{
    "Profile": {
        "Arn": "arn:aws:route53profiles:us-east-1:123456789012:profile/rp-6ffe47d5example",
        "ClientToken": "2ca1a304-32b3-4f5f-bc4c-EXAMPLE11111",
        "CreationTime": 1710850903.578,
        "Id": "rp-6ffe47d5example",
        "ModificationTime": 1710850903.578,
        "Name": "test",
        "OwnerId": "123456789012",
        "ShareStatus": "NOT_SHARED",
        "Status": "COMPLETE",
        "StatusMessage": "Created Profile"
    }
}
```

------

To associate your Profiles with different resources and edit the VPC configurations for the Profile, see the following procedures:

**Topics**
+ [Associate DNS Firewall rule groups to a Route 53 Profile](profile-associate-dns-firewall.md)
+ [Associate private hosted zones to a Route 53 Profile](profile-associate-private-hz.md)
+ [Associate Resolver rules to a Route 53 Profile](profile-associate-resolver-rules.md)
+ [Associate interface VPC endpoints to a Route 53 Profile](profile-associate-vpc-endpoints.md)
+ [Associate VPC Resolver query logging configurations to a Route 53 Profile](profile-associate-query-logging.md)
+ [Edit Route 53 Profile configurations](profile-edit-configurations.md)
+ [Associate a Route 53 Profile to VPCs](profile-associate-vpcs.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
