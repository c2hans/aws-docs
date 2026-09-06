---
source_url: https://docs.aws.amazon.com/security-ir/latest/APIReference/API_IncidentResponder.html
---

# IncidentResponder
<a name="API_IncidentResponder"></a>

## Contents
<a name="API_IncidentResponder_Contents"></a>

 ** email **   <a name="securityir-Type-IncidentResponder-email"></a>

Type: String
Length Constraints: Minimum length of 6. Maximum length of 254.
Pattern: `[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*`
Required: Yes

 ** jobTitle **   <a name="securityir-Type-IncidentResponder-jobTitle"></a>

Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: Yes

 ** name **   <a name="securityir-Type-IncidentResponder-name"></a>

Type: String
Length Constraints: Minimum length of 3. Maximum length of 50.
Required: Yes

 ** communicationPreferences **   <a name="securityir-Type-IncidentResponder-communicationPreferences"></a>

Type: Array of strings
Valid Values: `Case Created | Case Updated | Case Acknowledged | Case Closed | Case Updated To Service Managed | Case Status Updated | Case Pending Customer Action Reminder | Case Attachment Url Uploaded | Case Comment Added | Case Comment Updated | Membership Created | Membership Updated | Membership Cancelled | Register Delegated Administrator | Deregister Delegated Administrator | Disable AWS Service Access`
Required: No

## See Also
<a name="API_IncidentResponder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/security-ir-2018-05-10/IncidentResponder)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/security-ir-2018-05-10/IncidentResponder)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/security-ir-2018-05-10/IncidentResponder)
