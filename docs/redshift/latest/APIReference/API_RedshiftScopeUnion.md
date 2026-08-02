---
source_url: https://docs.aws.amazon.com/redshift/latest/APIReference/API_RedshiftScopeUnion.html
---

# RedshiftScopeUnion
<a name="API_RedshiftScopeUnion"></a>

A union structure that defines the scope of Amazon Redshift service integrations. Contains configuration for different integration types such as Amazon Redshift.

## Contents
<a name="API_RedshiftScopeUnion_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Connect **
The Amazon Redshift connect integration scope configuration. Defines authorization settings for Amazon Redshift connect service integration.
Type: [Connect](API_Connect.md) object
Required: No

## See Also
<a name="API_RedshiftScopeUnion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/RedshiftScopeUnion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/RedshiftScopeUnion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/RedshiftScopeUnion)
