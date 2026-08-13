---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_GetCaseRuleResponse.html
---

# GetCaseRuleResponse
<a name="API_connect-cases_GetCaseRuleResponse"></a>

Detailed case rule information. In the Connect Customer admin website, case rules are known as *case field conditions*. For more information about case field conditions, see [Add case field conditions to a case template](https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html).

## Contents
<a name="API_connect-cases_GetCaseRuleResponse_Contents"></a>

 ** caseRuleArn **   <a name="connect-Type-connect-cases_GetCaseRuleResponse-caseRuleArn"></a>
The Amazon Resource Name (ARN) of the case rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** caseRuleId **   <a name="connect-Type-connect-cases_GetCaseRuleResponse-caseRuleId"></a>
Unique identifier of a case rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** name **   <a name="connect-Type-connect-cases_GetCaseRuleResponse-name"></a>
Name of the case rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `.*[\S]`
Required: Yes

 ** rule **   <a name="connect-Type-connect-cases_GetCaseRuleResponse-rule"></a>
Represents what rule type should take place, under what conditions.
Type: [CaseRuleDetails](API_connect-cases_CaseRuleDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** createdTime **   <a name="connect-Type-connect-cases_GetCaseRuleResponse-createdTime"></a>
Timestamp when the resource was created.
Type: Timestamp
Required: No

 ** deleted **   <a name="connect-Type-connect-cases_GetCaseRuleResponse-deleted"></a>
Indicates whether the resource has been deleted.
Type: Boolean
Required: No

 ** description **   <a name="connect-Type-connect-cases_GetCaseRuleResponse-description"></a>
Description of a case rule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** lastModifiedTime **   <a name="connect-Type-connect-cases_GetCaseRuleResponse-lastModifiedTime"></a>
Timestamp when the resource was created or last modified.
Type: Timestamp
Required: No

 ** tags **   <a name="connect-Type-connect-cases_GetCaseRuleResponse-tags"></a>
A map of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.
Type: String to string map
Required: No

## See Also
<a name="API_connect-cases_GetCaseRuleResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/GetCaseRuleResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/GetCaseRuleResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/GetCaseRuleResponse)
