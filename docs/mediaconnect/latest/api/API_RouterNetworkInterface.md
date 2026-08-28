---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_RouterNetworkInterface.html
---

# RouterNetworkInterface
<a name="API_RouterNetworkInterface"></a>

A router network interface in AWS Elemental MediaConnect. A router network interface is a network interface that can be associated with one or more router inputs and outputs.

## Contents
<a name="API_RouterNetworkInterface_Contents"></a>

 ** arn **   <a name="mediaconnect-Type-RouterNetworkInterface-arn"></a>
The Amazon Resource Name (ARN) of the router network interface.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:routerNetworkInterface:[a-z0-9]{12}`
Required: Yes

 ** associatedInputCount **   <a name="mediaconnect-Type-RouterNetworkInterface-associatedInputCount"></a>
The number of router inputs associated with the network interface.
Type: Integer
Required: Yes

 ** associatedOutputCount **   <a name="mediaconnect-Type-RouterNetworkInterface-associatedOutputCount"></a>
The number of router outputs associated with the network interface.
Type: Integer
Required: Yes

 ** configuration **   <a name="mediaconnect-Type-RouterNetworkInterface-configuration"></a>
The configuration settings for a router network interface.
Type: [RouterNetworkInterfaceConfiguration](API_RouterNetworkInterfaceConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** createdAt **   <a name="mediaconnect-Type-RouterNetworkInterface-createdAt"></a>
The timestamp when the router network interface was created.
Type: Timestamp
Required: Yes

 ** id **   <a name="mediaconnect-Type-RouterNetworkInterface-id"></a>
The unique identifier of the router network interface.
Type: String
Required: Yes

 ** name **   <a name="mediaconnect-Type-RouterNetworkInterface-name"></a>
The name of the router network interface.
Type: String
Required: Yes

 ** networkInterfaceType **   <a name="mediaconnect-Type-RouterNetworkInterface-networkInterfaceType"></a>
The type of the router network interface.
Type: String
Valid Values: `PUBLIC | VPC`
Required: Yes

 ** regionName **   <a name="mediaconnect-Type-RouterNetworkInterface-regionName"></a>
The AWS Region where the router network interface is located.
Type: String
Required: Yes

 ** state **   <a name="mediaconnect-Type-RouterNetworkInterface-state"></a>
The current state of the router network interface.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | ERROR | RECOVERING`
Required: Yes

 ** tags **   <a name="mediaconnect-Type-RouterNetworkInterface-tags"></a>
Key-value pairs that can be used to tag and organize this router network interface.
Type: String to string map
Required: Yes

 ** updatedAt **   <a name="mediaconnect-Type-RouterNetworkInterface-updatedAt"></a>
The timestamp when the router network interface was last updated.
Type: Timestamp
Required: Yes

## See Also
<a name="API_RouterNetworkInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/RouterNetworkInterface)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/RouterNetworkInterface)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/RouterNetworkInterface)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
