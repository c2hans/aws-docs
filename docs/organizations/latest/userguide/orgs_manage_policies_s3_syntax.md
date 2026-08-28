---
source_url: https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_s3_syntax.html
---

# Amazon S3 policy syntax and examples
<a name="orgs_manage_policies_s3_syntax"></a>

An Amazon S3 policy is a plaintext file that is structured according to the rules of [JSON](http://json.org). The syntax for Amazon S3 policies follows the syntax for all declarative policy types. For more information, see [Understanding declarative policy inheritance](orgs_manage_policies_inheritance_mgmt.md). This topic focuses on applying that general syntax to the specific requirements of the Amazon S3 policies and the Block Public Access settings they help manage.

The following Amazon S3 policy example shows the basic policy syntax:

```
{
    "s3_attributes": {
        "public_access_block_configuration": {
            "@@assign": "all"
        }
    }
}
```

## The Amazon S3 policy syntax includes the following elements
<a name="s3-policy-syntax-elements"></a>

`s3_attributes`
The top-level key for Amazon S3 policy configuration.

`public_access_block_configuration`
Defines the Block Public Access behavior for the organization.

`@@assign`
The assignment operator that accepts one of two values:
+ `"all"` - Enables all four Amazon S3 Block Public Access settings at the organization level
+ `"none"` - Disables all four Amazon S3 Block Public Access settings at the organization level
Amazon S3 Block Public Access has four settings that control public access:

1. **BlockPublicAcls** - Amazon S3 will block public access permissions applied to newly added buckets or objects, and prevent the creation of new public access control lists (ACLs) for existing buckets and objects. This setting doesn't change any existing permissions that allow public access to Amazon S3 resources using ACLs.

1. **BlockPublicPolicy** - Amazon S3 will block new bucket and access point policies that grant public access to buckets and objects. This setting doesn't change any existing policies that allow public access to Amazon S3 resources.

1. **IgnorePublicAcls** - Amazon S3 will ignore all ACLs that grant public access to buckets and objects.

1. **RestrictPublicBuckets** - Amazon S3 will ignore public and cross-account access for buckets or access points with policies that grant public access to buckets and objects.
When you set `@@assign` to `"all"`, all four settings are consolidated and enabled at the organization level, providing comprehensive protection against public access across all accounts in your organization. If you want to manage Amazon S3 Block Public Access at an account level, you should disable S3 Policy type at the organization level

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Organizations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query organizations` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
