---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_SsmDocument.html
---

# SsmDocument
<a name="API_SsmDocument"></a>

AWS Systems Manager Document.

## Contents
<a name="API_SsmDocument_Contents"></a>

 ** actionName **   <a name="mgn-Type-SsmDocument-actionName"></a>
User-friendly name for the AWS Systems Manager Document.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

 ** ssmDocumentName **   <a name="mgn-Type-SsmDocument-ssmDocumentName"></a>
AWS Systems Manager Document name or full ARN.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 172.
Pattern: `([A-Za-z0-9/:_\.-])+`
Required: Yes

 ** externalParameters **   <a name="mgn-Type-SsmDocument-externalParameters"></a>
AWS Systems Manager Document external parameters.
Type: String to [SsmExternalParameter](API_SsmExternalParameter.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 1011.
Key Pattern: `([A-Za-z0-9])+`
Required: No

 ** mustSucceedForCutover **   <a name="mgn-Type-SsmDocument-mustSucceedForCutover"></a>
If true, Cutover will not be enabled if the document has failed.
Type: Boolean
Required: No

 ** parameters **   <a name="mgn-Type-SsmDocument-parameters"></a>
AWS Systems Manager Document parameters.
Type: String to array of [SsmParameterStoreParameter](API_SsmParameterStoreParameter.md) objects map
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 1011.
Key Pattern: `([A-Za-z0-9])+`
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** timeoutSeconds **   <a name="mgn-Type-SsmDocument-timeoutSeconds"></a>
AWS Systems Manager Document timeout seconds.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_SsmDocument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/SsmDocument)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/SsmDocument)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/SsmDocument)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
