---
source_url: https://docs.aws.amazon.com/redshift/latest/APIReference/API_ServiceIntegrationsUnion.html
---

# ServiceIntegrationsUnion
<a name="API_ServiceIntegrationsUnion"></a>

A list of service integrations.

## Contents
<a name="API_ServiceIntegrationsUnion_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** LakeFormation.member.N **
A list of scopes set up for Lake Formation integration.
Type: Array of [LakeFormationScopeUnion](API_LakeFormationScopeUnion.md) objects
Required: No

 ** Redshift.member.N **
A list of scopes set up for Amazon Redshift integration.
Type: Array of [RedshiftScopeUnion](API_RedshiftScopeUnion.md) objects
Required: No

 ** S3AccessGrants.member.N **
A list of scopes set up for S3 Access Grants integration.
Type: Array of [S3AccessGrantsScopeUnion](API_S3AccessGrantsScopeUnion.md) objects
Required: No

## See Also
<a name="API_ServiceIntegrationsUnion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ServiceIntegrationsUnion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ServiceIntegrationsUnion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ServiceIntegrationsUnion)
