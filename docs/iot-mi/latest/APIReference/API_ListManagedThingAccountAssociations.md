---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_ListManagedThingAccountAssociations.html
---

# ListManagedThingAccountAssociations
<a name="API_ListManagedThingAccountAssociations"></a>

Lists all account associations for a specific managed thing.

## Request Syntax
<a name="API_ListManagedThingAccountAssociations_RequestSyntax"></a>

```
GET /managed-thing-associations?AccountAssociationId={{AccountAssociationId}}&ManagedThingId={{ManagedThingId}}&MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListManagedThingAccountAssociations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AccountAssociationId](#API_ListManagedThingAccountAssociations_RequestSyntax) **   <a name="managedintegrations-ListManagedThingAccountAssociations-request-uri-AccountAssociationId"></a>
The identifier of the account association to filter results by. When specified, only associations with this account association ID will be returned.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z]+`

 ** [ManagedThingId](#API_ListManagedThingAccountAssociations_RequestSyntax) **   <a name="managedintegrations-ListManagedThingAccountAssociations-request-uri-ManagedThingId"></a>
The identifier of the managed thing to list account associations for.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9:_-]*`

 ** [MaxResults](#API_ListManagedThingAccountAssociations_RequestSyntax) **   <a name="managedintegrations-ListManagedThingAccountAssociations-request-uri-MaxResults"></a>
The maximum number of account associations to return in a single response.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListManagedThingAccountAssociations_RequestSyntax) **   <a name="managedintegrations-ListManagedThingAccountAssociations-request-uri-NextToken"></a>
A token used for pagination of results.
Length Constraints: Minimum length of 1. Maximum length of 65535.
Pattern: `[a-zA-Z0-9=_-]+`

## Request Body
<a name="API_ListManagedThingAccountAssociations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListManagedThingAccountAssociations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "AccountAssociationId": "string",
         "ManagedThingAssociationStatus": "string",
         "ManagedThingId": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListManagedThingAccountAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListManagedThingAccountAssociations_ResponseSyntax) **   <a name="managedintegrations-ListManagedThingAccountAssociations-response-Items"></a>
The list of managed thing associations that match the specified criteria, including the managed thing ID and account association ID for each association.
Type: Array of [ManagedThingAssociation](API_ManagedThingAssociation.md) objects

 ** [NextToken](#API_ListManagedThingAccountAssociations_ResponseSyntax) **   <a name="managedintegrations-ListManagedThingAccountAssociations-response-NextToken"></a>
A token used for pagination of results when there are more account associations than can be returned in a single response.
Type: String

## Errors
<a name="API_ListManagedThingAccountAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User is not authorized.
HTTP Status Code: 403

 ** InternalServerException **
Internal error from the service that indicates an unexpected error or that the service is unavailable.
HTTP Status Code: 500

 ** ThrottlingException **
The rate exceeds the limit.
HTTP Status Code: 429

 ** ValidationException **
A validation error occurred when performing the API request.
HTTP Status Code: 400

## See Also
<a name="API_ListManagedThingAccountAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-managed-integrations-2025-03-03/ListManagedThingAccountAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-managed-integrations-2025-03-03/ListManagedThingAccountAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/ListManagedThingAccountAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-managed-integrations-2025-03-03/ListManagedThingAccountAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/ListManagedThingAccountAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-managed-integrations-2025-03-03/ListManagedThingAccountAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-managed-integrations-2025-03-03/ListManagedThingAccountAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-managed-integrations-2025-03-03/ListManagedThingAccountAssociations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-managed-integrations-2025-03-03/ListManagedThingAccountAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/ListManagedThingAccountAssociations)
