---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ActionIdentifier.html
---

# ActionIdentifier
<a name="API_ActionIdentifier"></a>

Contains information about an action for a request for which an authorization decision is made.

This data type is used as a request parameter to the [IsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html), [BatchIsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorized.html), and [IsAuthorizedWithToken](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html) operations.

Example: `{ "actionId": "<action name>", "actionType": "Action" }`

## Contents
<a name="API_ActionIdentifier_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** actionId **   <a name="verifiedpermissions-Type-ActionIdentifier-actionId"></a>
The ID of an action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `.*`
Required: Yes

 ** actionType **   <a name="verifiedpermissions-Type-ActionIdentifier-actionType"></a>
The type of an action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `Action$|^.+::Action`
Required: Yes

## See Also
<a name="API_ActionIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/ActionIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/ActionIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/ActionIdentifier)
