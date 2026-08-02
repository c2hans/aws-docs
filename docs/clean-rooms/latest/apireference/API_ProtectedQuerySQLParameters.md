---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ProtectedQuerySQLParameters.html
---

# ProtectedQuerySQLParameters
<a name="API_ProtectedQuerySQLParameters"></a>

The parameters for the SQL type Protected Query.

## Contents
<a name="API_ProtectedQuerySQLParameters_Contents"></a>

 ** analysisTemplateArn **   <a name="API-Type-ProtectedQuerySQLParameters-analysisTemplateArn"></a>
The Amazon Resource Name (ARN) associated with the analysis template within a collaboration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `arn:aws[-a-z]*:cleanrooms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:membership/[\d\w-]+/analysistemplate/[\d\w-]+`
Required: No

 ** parameters **   <a name="API-Type-ProtectedQuerySQLParameters-parameters"></a>
The protected query SQL parameters.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 100.
Key Pattern: `[0-9a-zA-Z_]+`
Value Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** queryString **   <a name="API-Type-ProtectedQuerySQLParameters-queryString"></a>
The query string to be submitted.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500000.
Required: No

## See Also
<a name="API_ProtectedQuerySQLParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ProtectedQuerySQLParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ProtectedQuerySQLParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ProtectedQuerySQLParameters)
