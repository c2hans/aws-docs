---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_ModifyDBClusterEndpoint.html
---

# ModifyDBClusterEndpoint
<a name="API_ModifyDBClusterEndpoint"></a>

Modifies the properties of an endpoint in an Amazon Neptune DB cluster.

## Request Parameters
<a name="API_ModifyDBClusterEndpoint_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBClusterEndpointIdentifier **
The identifier of the endpoint to modify. This parameter is stored as a lowercase string.
Type: String
Required: Yes

 ** EndpointType **
The type of the endpoint. One of: `READER`, `WRITER`, `ANY`.
Type: String
Required: No

 **ExcludedMembers.member.N**
List of DB instance identifiers that aren't part of the custom endpoint group. All other eligible instances are reachable through the custom endpoint. Only relevant if the list of static members is empty.
Type: Array of strings
Required: No

 **StaticMembers.member.N**
List of DB instance identifiers that are part of the custom endpoint group.
Type: Array of strings
Required: No

## Response Elements
<a name="API_ModifyDBClusterEndpoint_ResponseElements"></a>

The following elements are returned by the service.

 ** CustomEndpointType **
The type associated with a custom endpoint. One of: `READER`, `WRITER`, `ANY`.
Type: String

 ** DBClusterEndpointArn **
The Amazon Resource Name (ARN) for the endpoint.
Type: String

 ** DBClusterEndpointIdentifier **
The identifier associated with the endpoint. This parameter is stored as a lowercase string.
Type: String

 ** DBClusterEndpointResourceIdentifier **
A unique system-generated identifier for an endpoint. It remains the same for the whole life of the endpoint.
Type: String

 ** DBClusterIdentifier **
The DB cluster identifier of the DB cluster associated with the endpoint. This parameter is stored as a lowercase string.
Type: String

 ** Endpoint **
The DNS address of the endpoint.
Type: String

 ** EndpointType **
The type of the endpoint. One of: `READER`, `WRITER`, `CUSTOM`.
Type: String

 **ExcludedMembers.member.N**
List of DB instance identifiers that aren't part of the custom endpoint group. All other eligible instances are reachable through the custom endpoint. Only relevant if the list of static members is empty.
Type: Array of strings

 **StaticMembers.member.N**
List of DB instance identifiers that are part of the custom endpoint group.
Type: Array of strings

 ** Status **
The current status of the endpoint. One of: `creating`, `available`, `deleting`, `inactive`, `modifying`. The `inactive` state applies to an endpoint that cannot be used for a certain kind of cluster, such as a `writer` endpoint for a read-only secondary cluster in a global database.
Type: String

## Errors
<a name="API_ModifyDBClusterEndpoint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBClusterEndpointNotFoundFault **
The specified custom endpoint doesn't exist.
HTTP Status Code: 400

 ** DBInstanceNotFound **
 *DBInstanceIdentifier* does not refer to an existing DB instance.
HTTP Status Code: 404

 ** InvalidDBClusterEndpointStateFault **
The requested operation cannot be performed on the endpoint while the endpoint is in this state.
HTTP Status Code: 400

 ** InvalidDBClusterStateFault **
The DB cluster is not in a valid state.
HTTP Status Code: 400

 ** InvalidDBInstanceState **
The specified DB instance is not in the *available* state.
HTTP Status Code: 400

## See Also
<a name="API_ModifyDBClusterEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/ModifyDBClusterEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/ModifyDBClusterEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/ModifyDBClusterEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/ModifyDBClusterEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/ModifyDBClusterEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/ModifyDBClusterEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/ModifyDBClusterEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/ModifyDBClusterEndpoint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/ModifyDBClusterEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/ModifyDBClusterEndpoint)
