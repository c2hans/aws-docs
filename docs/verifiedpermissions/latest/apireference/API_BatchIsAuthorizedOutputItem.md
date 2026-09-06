---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorizedOutputItem.html
---

# BatchIsAuthorizedOutputItem
<a name="API_BatchIsAuthorizedOutputItem"></a>

The decision, based on policy evaluation, from an individual authorization request in a `BatchIsAuthorized` API request.

## Contents
<a name="API_BatchIsAuthorizedOutputItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** decision **   <a name="verifiedpermissions-Type-BatchIsAuthorizedOutputItem-decision"></a>
An authorization decision that indicates if the authorization request should be allowed or denied.
Type: String
Valid Values: `ALLOW | DENY`
Required: Yes

 ** determiningPolicies **   <a name="verifiedpermissions-Type-BatchIsAuthorizedOutputItem-determiningPolicies"></a>
The list of determining policies used to make the authorization decision. For example, if there are two matching policies, where one is a forbid and the other is a permit, then the forbid policy will be the determining policy. In the case of multiple matching permit policies then there would be multiple determining policies. In the case that no policies match, and hence the response is DENY, there would be no determining policies.
Type: Array of [DeterminingPolicyItem](API_DeterminingPolicyItem.md) objects
Required: Yes

 ** errors **   <a name="verifiedpermissions-Type-BatchIsAuthorizedOutputItem-errors"></a>
Errors that occurred while making an authorization decision. For example, a policy might reference an entity or attribute that doesn't exist in the request.
Type: Array of [EvaluationErrorItem](API_EvaluationErrorItem.md) objects
Required: Yes

 ** request **   <a name="verifiedpermissions-Type-BatchIsAuthorizedOutputItem-request"></a>
The authorization request that initiated the decision.
Type: [BatchIsAuthorizedInputItem](API_BatchIsAuthorizedInputItem.md) object
Required: Yes

## See Also
<a name="API_BatchIsAuthorizedOutputItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/BatchIsAuthorizedOutputItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/BatchIsAuthorizedOutputItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/BatchIsAuthorizedOutputItem)
