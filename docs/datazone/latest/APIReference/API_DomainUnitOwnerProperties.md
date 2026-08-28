---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_DomainUnitOwnerProperties.html
---

# DomainUnitOwnerProperties
<a name="API_DomainUnitOwnerProperties"></a>

The properties of the domain unit owner.

## Contents
<a name="API_DomainUnitOwnerProperties_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** group **   <a name="datazone-Type-DomainUnitOwnerProperties-group"></a>
Indicates that the domain unit owner is a group.
Type: [DomainUnitGroupProperties](API_DomainUnitGroupProperties.md) object
Required: No

 ** user **   <a name="datazone-Type-DomainUnitOwnerProperties-user"></a>
Indicates that the domain unit owner is a user.
Type: [DomainUnitUserProperties](API_DomainUnitUserProperties.md) object
Required: No

## See Also
<a name="API_DomainUnitOwnerProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/DomainUnitOwnerProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/DomainUnitOwnerProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/DomainUnitOwnerProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
