---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EntitiesDefinition.html
---

# EntitiesDefinition
<a name="API_EntitiesDefinition"></a>

Contains the list of entities to be considered during an authorization request. This includes all principals, resources, and actions required to successfully evaluate the request.

This data type is used as a field in the response parameter for the [IsAuthorized](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorized.html) and [IsAuthorizedWithToken](https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html) operations.

## Contents
<a name="API_EntitiesDefinition_Contents"></a>

**Note**
In the following list, the required parameters are described first.

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** cedarJson **   <a name="verifiedpermissions-Type-EntitiesDefinition-cedarJson"></a>
A Cedar JSON string representation of the entities needed to successfully evaluate an authorization request.
Example: `{"cedarJson": "[{\"uid\":{\"type\":\"Photo\",\"id\":\"VacationPhoto94.jpg\"},\"attrs\":{\"accessLevel\":\"public\"},\"parents\":[]}]"}`
Type: String
Required: No

 ** entityList **   <a name="verifiedpermissions-Type-EntitiesDefinition-entityList"></a>
An array of entities that are needed to successfully evaluate an authorization request. Each entity in this array must include an identifier for the entity, the attributes of the entity, and a list of any parent entities.
If you include multiple entities with the same `identifier`, only the last one is processed in the request.
Type: Array of [EntityItem](API_EntityItem.md) objects
Required: No

## See Also
<a name="API_EntitiesDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/EntitiesDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/EntitiesDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/EntitiesDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Verified Permissions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verifiedpermissions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
