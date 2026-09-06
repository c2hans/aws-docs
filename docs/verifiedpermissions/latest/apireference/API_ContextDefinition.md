---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ContextDefinition.html
---

# ContextDefinition
<a name="API_ContextDefinition"></a>

Contains additional details about the context of the request. Verified Permissions evaluates this information in an authorization request as part of the `when` and `unless` clauses in a policy.

This data type is used as a request parameter for the [IsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html), [BatchIsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_BatchIsAuthorized.html), and [IsAuthorizedWithToken](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html) operations.

If you're passing context as part of the request, exactly one instance of `context` must be passed. If you don't want to pass context, omit the `context` parameter from your request rather than sending `context {}`.

Example: `"context":{"contextMap":{"<KeyName1>":{"boolean":true},"<KeyName2>":{"long":1234}}}`

## Contents
<a name="API_ContextDefinition_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** cedarJson **   <a name="verifiedpermissions-Type-ContextDefinition-cedarJson"></a>
A Cedar JSON string representation of the context needed to successfully evaluate an authorization request.
Example: `{"cedarJson":"{\"<KeyName1>\": true, \"<KeyName2>\": 1234}" }`
Type: String
Required: No

 ** contextMap **   <a name="verifiedpermissions-Type-ContextDefinition-contextMap"></a>
An list of attributes that are needed to successfully evaluate an authorization request. Each attribute in this array must include a map of a data type and its value.
Example: `"contextMap":{"<KeyName1>":{"boolean":true},"<KeyName2>":{"long":1234}}`
Type: String to [AttributeValue](API_AttributeValue.md) object map
Required: No

## See Also
<a name="API_ContextDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/ContextDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/ContextDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/ContextDefinition)
