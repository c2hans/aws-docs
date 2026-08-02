---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ResourceScopes.html
---

# ResourceScopes
<a name="API_ResourceScopes"></a>

Defines the data boundary for a resources query. Scopes determine which organizational units or organizations to retrieve data from.

## Contents
<a name="API_ResourceScopes_Contents"></a>

 ** AwsOrganizations **   <a name="securityhub-Type-ResourceScopes-AwsOrganizations"></a>
A list of AWS Organizations scopes to include in the query results. Each entry in the list specifies an organization or organizational unit to include for the delegated administrator's account. If the list specifies multiple entries, the entries are combined using OR logic.
Type: Array of [AwsOrganizationScope](API_AwsOrganizationScope.md) objects
Required: No

## See Also
<a name="API_ResourceScopes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ResourceScopes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ResourceScopes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ResourceScopes)
