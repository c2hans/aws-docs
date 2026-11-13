---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CountermeasureAction.html
---

# CountermeasureAction
<a name="API_CountermeasureAction"></a>

Contains an action that you can take to respond to a threat.

## Contents
<a name="API_CountermeasureAction_Contents"></a>

 ** affectedResources **   <a name="guardduty-Type-CountermeasureAction-affectedResources"></a>
The resources that the action applies to.
Type: Array of [AffectedResource](API_AffectedResource.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** cliCommands **   <a name="guardduty-Type-CountermeasureAction-cliCommands"></a>
 AWS CLI commands that you can run to carry out the action.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** defenseTechnique **   <a name="guardduty-Type-CountermeasureAction-defenseTechnique"></a>
The defensive technique that the action applies.
Type: String
Required: No

 ** description **   <a name="guardduty-Type-CountermeasureAction-description"></a>
A description of the action.
Type: String
Required: No

 ** disposition **   <a name="guardduty-Type-CountermeasureAction-disposition"></a>
The outcome of the action. Possible values are `Isolated`, `Blocked`, `Deleted`, `Access Revoked`, and `Logged`.
Type: String
Valid Values: `Isolated | Blocked | Deleted | Access Revoked | Logged`
Required: No

 ** dispositionId **   <a name="guardduty-Type-CountermeasureAction-dispositionId"></a>
The numeric identifier of the action's disposition.
Type: Integer
Required: No

 ** mitigates **   <a name="guardduty-Type-CountermeasureAction-mitigates"></a>
The MITRE ATT&CK technique IDs that the action mitigates, such as `T1059.004`.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Pattern: `(TA|T)\d{4}(\.\d{3})?`
Required: No

 ** priority **   <a name="guardduty-Type-CountermeasureAction-priority"></a>
The priority of the action. Possible values are `IMMEDIATE`, `SHORT_TERM`, and `STRATEGIC`.
Type: String
Valid Values: `IMMEDIATE | SHORT_TERM | STRATEGIC`
Required: No

 ** title **   <a name="guardduty-Type-CountermeasureAction-title"></a>
A short title for the action.
Type: String
Required: No

## See Also
<a name="API_CountermeasureAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/CountermeasureAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/CountermeasureAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/CountermeasureAction)
