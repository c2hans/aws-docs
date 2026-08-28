---
source_url: https://docs.aws.amazon.com/rolesanywhere/latest/userguide/attribute-mapping.html
---

# Certificate attribute mapping
<a name="attribute-mapping"></a>

 IAM Roles Anywhere provides you with the capability to define a custom set of mapping rules, enabling you to specify which data are extracted from authenticating certificates as session tags for authorization policies. These customized attribute mappings are associated with a [profile](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-profile.html).

 Attributes are data elements that come from specific fields in the certificate. You can use specifiers to represent one or more attributes.

**Note**
 For information about session tag quotas, see [Session tagging operations](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html#id_session-tags_operations).

**Topics**
+ [Default mapping behavior](#attribute-mapping-default)
+ [Put attribute mappings](put-attribute-mapping.md)
+ [Delete attribute mappings](delete-attribute-mappings.md)
+ [Attribute mapping and trust policy](attribute-mapping-and-trust-policy.md)

## Default mapping behavior
<a name="attribute-mapping-default"></a>

The following attributes are mapped by default when you create a profile. The default mapping rules are as follows:
+ `x509Subject`: maps all supported Relative Distinguished Names (RDNs) from an authenticating certificate's Subject into distinct `PrincipalTag` elements in the session.
+ `x509Issuer`: maps all supported Relative Distinguished Names (RDNs) from an authenticating certificate's Issuer into distinct `PrincipalTag` elements in the session.
+ `x509SAN (Subject Alternative Name)`: maps the ** first** value of the following types: `DNS Names`, `Directory Name (DN)`, and `URI Names`

 To view your current mappings associated with a profile, using the following command:

```
$ aws rolesanywhere get-profile --profile-id {{PROFILE_ID}}
```

 Default mapping rules in a JSON format:

```
"attributeMappings": [
  {
    "mappingRules": [
        {
            "specifier": "*"
        }
    ],
    "certificateField": "x509Issuer"
  },
  {
    "mappingRules": [
        {
            "specifier": "DNS"
        },
        {
            "specifier": "URI"
        },
        {
            "specifier": "Name/*"
        }
    ],
    "certificateField": "x509SAN"
  },
  {
    "mappingRules": [
        {
            "specifier": "*"
        }
    ],
    "certificateField": "x509Subject"
  }
]
```

**Note**
If you see `*` as a specifier, it signifies the default behavior, which maps all recognizable RDNs for `x509Subject`, `x509Issuer` and `x509SAN/Name`. However, `*` does not have a defined behavior in the context of `x509SAN/URI`, `x509SAN/DNS`, or `x509SAN/`. The specifier `Name/` represents the first recognizable attribute of the `Directory Name`. Both `Name` and `Name/` are equivalent to `Name/*` and will be displayed as `Name/*`in the mapping rule.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for IAM Roles Anywhere. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rolesanywhere` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
