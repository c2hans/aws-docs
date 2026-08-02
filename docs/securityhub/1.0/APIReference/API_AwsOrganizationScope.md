---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsOrganizationScope.html
---

# AwsOrganizationScope
<a name="API_AwsOrganizationScope"></a>

Specifies an AWS Organizations scope. Data from the specified organization or organizational unit is included in the response.

To scope to a specific organizational unit, provide `OrganizationalUnitId`. You can optionally include `OrganizationId`. If you omit `OrganizationId`, Security Hub uses the caller's organization ID. To scope to the delegated administrator's entire organization, provide only `OrganizationId`.

The organization ID and organizational unit must belong to the delegated administrator's own organization. Each request must use one scoping approach: either scope to the entire organization by providing an `AwsOrganizationScope` entry with only `OrganizationId`, or scope to specific organizational units by providing `AwsOrganizationScope` entries with `OrganizationalUnitId`. You can't combine both approaches in the same request.

## Contents
<a name="API_AwsOrganizationScope_Contents"></a>

 ** OrganizationalUnitId **   <a name="securityhub-Type-AwsOrganizationScope-OrganizationalUnitId"></a>
The unique identifier (ID) of the organizational unit (OU) (for example, `ou-ab12-cd345678`). The OU must exist within the delegated administrator's own organization. When specified, the results include only data from accounts in this OU.
Type: String
Pattern: `.*\S.*`
Required: No

 ** OrganizationId **   <a name="securityhub-Type-AwsOrganizationScope-OrganizationId"></a>
The unique identifier (ID) of the organization (for example, `o-abcd1234567890`). The organization must be the delegated administrator's own organization. If you omit this value and provide `OrganizationalUnitId`, Security Hub uses the caller's organization ID.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsOrganizationScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsOrganizationScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsOrganizationScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsOrganizationScope)
