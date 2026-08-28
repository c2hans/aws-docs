---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/implicit-profile-object-types.html
---

# Implicit profile object types in Connect Customer Customer Profiles
<a name="implicit-profile-object-types"></a>

You can use any object type that matches the name of a template ID (as returned by the [ListProfileObjectTypeTemplates](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListProfileObjectTypeTemplates.html) API) without explicitly defining it. The object type will exactly match the definition of the template definition of this object type. If an explicit object type is defined, it replaces the implicit one.

Implicit object types are included in the [ListProfileObjectTypes](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_ListProfileObjectTypes.html) API or returned by [GetProfileObjectType](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetProfileObjectType.html) operations, but they can still be deleted if you want to remove all data ingested from that object type.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
