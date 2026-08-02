---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_StandardsManagedBy.html
---

# StandardsManagedBy
<a name="API_StandardsManagedBy"></a>

Provides details about the management of a security standard.

## Contents
<a name="API_StandardsManagedBy_Contents"></a>

 ** Company **   <a name="securityhub-Type-StandardsManagedBy-Company"></a>
An identifier for the company that manages a specific security standard. For existing standards, the value is equal to ` AWS `.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Product **   <a name="securityhub-Type-StandardsManagedBy-Product"></a>
An identifier for the product that manages a specific security standard. For existing standards, the value is equal to the AWS service that manages the standard.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_StandardsManagedBy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/StandardsManagedBy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/StandardsManagedBy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/StandardsManagedBy)
