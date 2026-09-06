---
source_url: https://docs.aws.amazon.com/managedservices/latest/ApiReference-cm/API_ChangeTypeVersionSummary.html
---

# ChangeTypeVersionSummary
<a name="API_ChangeTypeVersionSummary"></a>

Summary information about a change type version.

## Contents
<a name="API_ChangeTypeVersionSummary_Contents"></a>

 ** AccessLevel **   <a name="amscm-Type-ChangeTypeVersionSummary-AccessLevel"></a>
The access level of the change type.
Type: [ChangeTypeAccessLevel](API_ChangeTypeAccessLevel.md) object
Required: No

 ** AutomationStatus **   <a name="amscm-Type-ChangeTypeVersionSummary-AutomationStatus"></a>
The automation status of a change type (`Automated` or `Manual`).
Type: [ChangeTypeAutomationStatus](API_ChangeTypeAutomationStatus.md) object
Required: No

 ** ChangeTypeId **   <a name="amscm-Type-ChangeTypeVersionSummary-ChangeTypeId"></a>
The unique ID of the change type, in the form ct-2ty5seo8rxfsc.
Type: String
Required: No

 ** CreatedTime **   <a name="amscm-Type-ChangeTypeVersionSummary-CreatedTime"></a>
The date and time that the change type version was created.
Type: String
Required: No

 ** DeprecationTime **   <a name="amscm-Type-ChangeTypeVersionSummary-DeprecationTime"></a>
The date and time that the change type version was deprecated.
Type: String
Required: No

 ** Description **   <a name="amscm-Type-ChangeTypeVersionSummary-Description"></a>
Description of the change type version.
Type: String
Required: No

 ** Name **   <a name="amscm-Type-ChangeTypeVersionSummary-Name"></a>
The title of the JSON Schema `ExecutionInputSchema` of the change type version.
Type: String
Required: No

 ** Version **   <a name="amscm-Type-ChangeTypeVersionSummary-Version"></a>
The version number for this change type version.
Type: String
Required: No

## See Also
<a name="API_ChangeTypeVersionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amscm-2020-05-21/ChangeTypeVersionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amscm-2020-05-21/ChangeTypeVersionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amscm-2020-05-21/ChangeTypeVersionSummary)
