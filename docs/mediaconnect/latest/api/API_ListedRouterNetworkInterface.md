---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_ListedRouterNetworkInterface.html
---

# ListedRouterNetworkInterface
<a name="API_ListedRouterNetworkInterface"></a>

A summary of a router network interface, including its name, type, ARN, ID, associated input/output counts, state, and other key details. This structure is used in the response of the ListRouterNetworkInterfaces operation.

## Contents
<a name="API_ListedRouterNetworkInterface_Contents"></a>

 ** arn **   <a name="mediaconnect-Type-ListedRouterNetworkInterface-arn"></a>
The Amazon Resource Name (ARN) of the router network interface.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:routerNetworkInterface:[a-z0-9]{12}`
Required: Yes

 ** associatedInputCount **   <a name="mediaconnect-Type-ListedRouterNetworkInterface-associatedInputCount"></a>
The number of router inputs associated with the network interface.
Type: Integer
Required: Yes

 ** associatedOutputCount **   <a name="mediaconnect-Type-ListedRouterNetworkInterface-associatedOutputCount"></a>
The number of router outputs associated with the network interface.
Type: Integer
Required: Yes

 ** createdAt **   <a name="mediaconnect-Type-ListedRouterNetworkInterface-createdAt"></a>
The timestamp when the network interface was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="mediaconnect-Type-ListedRouterNetworkInterface-id"></a>
The unique identifier of the router network interface.
Type: String
Required: Yes

 ** name **   <a name="mediaconnect-Type-ListedRouterNetworkInterface-name"></a>
The name of the router network interface.
Type: String
Required: Yes

 ** networkInterfaceType **   <a name="mediaconnect-Type-ListedRouterNetworkInterface-networkInterfaceType"></a>
The type of the router network interface.
Type: String
Valid Values: `PUBLIC | VPC`
Required: Yes

 ** regionName **   <a name="mediaconnect-Type-ListedRouterNetworkInterface-regionName"></a>
The AWS Region where the router network interface is located.
Type: String
Required: Yes

 ** state **   <a name="mediaconnect-Type-ListedRouterNetworkInterface-state"></a>
The current state of the router network interface.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | ERROR | RECOVERING`
Required: Yes

 ** updatedAt **   <a name="mediaconnect-Type-ListedRouterNetworkInterface-updatedAt"></a>
The timestamp when the router network interface was last updated.
Type: Timestamp
Required: Yes

## See Also
<a name="API_ListedRouterNetworkInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/ListedRouterNetworkInterface)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/ListedRouterNetworkInterface)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/ListedRouterNetworkInterface)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
