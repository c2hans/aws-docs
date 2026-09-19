---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_AssociateConnectionsToResiliencyGroup.html
---

# AssociateConnectionsToResiliencyGroup
<a name="API_AssociateConnectionsToResiliencyGroup"></a>

Associates one or more connections with the specified resiliency group. This operation is atomic: either all of the specified connections are associated, or the operation fails and no changes are made.

## Request Syntax
<a name="API_AssociateConnectionsToResiliencyGroup_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "connectionIdentifiers": [ "{{string}}" ],
   "resiliencyGroupId": "{{string}}"
}
```

## Request Parameters
<a name="API_AssociateConnectionsToResiliencyGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_AssociateConnectionsToResiliencyGroup_RequestSyntax) **   <a name="DX-AssociateConnectionsToResiliencyGroup-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [connectionIdentifiers](#API_AssociateConnectionsToResiliencyGroup_RequestSyntax) **   <a name="DX-AssociateConnectionsToResiliencyGroup-request-connectionIdentifiers"></a>
The IDs or ARNs of the connections to associate with the resiliency group.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** [resiliencyGroupId](#API_AssociateConnectionsToResiliencyGroup_RequestSyntax) **   <a name="DX-AssociateConnectionsToResiliencyGroup-request-resiliencyGroupId"></a>
The ID of the resiliency group.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `^(dxrg|DXRG)-[0-9a-zA-Z]{17}$`
Required: Yes

## Response Syntax
<a name="API_AssociateConnectionsToResiliencyGroup_ResponseSyntax"></a>

```
{
   "resiliencyGroupAssociations": [
      {
         "connectionArn": "string",
         "resiliencyGroupId": "string",
         "state": "string"
      }
   ]
}
```

## Response Elements
<a name="API_AssociateConnectionsToResiliencyGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [resiliencyGroupAssociations](#API_AssociateConnectionsToResiliencyGroup_ResponseSyntax) **   <a name="DX-AssociateConnectionsToResiliencyGroup-response-resiliencyGroupAssociations"></a>
The connection associations for the resiliency group.
Type: Array of [ResiliencyGroupAssociation](API_ResiliencyGroupAssociation.md) objects

## Errors
<a name="API_AssociateConnectionsToResiliencyGroup_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectConnectClientException **
One or more parameters are not valid.
HTTP Status Code: 400

 ** DirectConnectServerException **
A server-side error occurred.
HTTP Status Code: 400

 ** LimitExceededException **
The rate limiter limit has been exceeded for the connection. You cannot add more rate limiters to virtual interfaces on this connection.
HTTP Status Code: 400

## See Also
<a name="API_AssociateConnectionsToResiliencyGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/directconnect-2012-10-25/AssociateConnectionsToResiliencyGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/directconnect-2012-10-25/AssociateConnectionsToResiliencyGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/AssociateConnectionsToResiliencyGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/directconnect-2012-10-25/AssociateConnectionsToResiliencyGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/AssociateConnectionsToResiliencyGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/directconnect-2012-10-25/AssociateConnectionsToResiliencyGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/directconnect-2012-10-25/AssociateConnectionsToResiliencyGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/directconnect-2012-10-25/AssociateConnectionsToResiliencyGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/directconnect-2012-10-25/AssociateConnectionsToResiliencyGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/AssociateConnectionsToResiliencyGroup)
