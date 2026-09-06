---
source_url: https://docs.aws.amazon.com/evs/latest/APIReference/API_ListEnvironmentVlans.html
---

# ListEnvironmentVlans
<a name="API_ListEnvironmentVlans"></a>

Lists environment VLANs that are associated with the specified environment.

## Request Syntax
<a name="API_ListEnvironmentVlans_RequestSyntax"></a>

```
{
   "environmentId": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListEnvironmentVlans_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [environmentId](#API_ListEnvironmentVlans_RequestSyntax) **   <a name="evs-ListEnvironmentVlans-request-environmentId"></a>
A unique ID for the environment.
Type: String
Pattern: `(env-[a-zA-Z0-9]{10})`
Required: Yes

 ** [maxResults](#API_ListEnvironmentVlans_RequestSyntax) **   <a name="evs-ListEnvironmentVlans-request-maxResults"></a>
The maximum number of results to return. If you specify `MaxResults` in the request, the response includes information up to the limit specified.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListEnvironmentVlans_RequestSyntax) **   <a name="evs-ListEnvironmentVlans-request-nextToken"></a>
A unique pagination token for each page. If `nextToken` is returned, there are more results available. Make the call again using the returned token with all other arguments unchanged to retrieve the next page. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken* error.
Type: String
Required: No

## Response Syntax
<a name="API_ListEnvironmentVlans_ResponseSyntax"></a>

```
{
   "environmentVlans": [
      {
         "availabilityZone": "string",
         "cidr": "string",
         "createdAt": number,
         "eipAssociations": [
            {
               "allocationId": "string",
               "associationId": "string",
               "ipAddress": "string"
            }
         ],
         "functionName": "string",
         "isPublic": boolean,
         "modifiedAt": number,
         "networkAclId": "string",
         "stateDetails": "string",
         "subnetId": "string",
         "vlanId": number,
         "vlanState": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListEnvironmentVlans_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [environmentVlans](#API_ListEnvironmentVlans_ResponseSyntax) **   <a name="evs-ListEnvironmentVlans-response-environmentVlans"></a>
A list of VLANs that are associated with the specified environment.
Type: Array of [Vlan](API_Vlan.md) objects

 ** [nextToken](#API_ListEnvironmentVlans_ResponseSyntax) **   <a name="evs-ListEnvironmentVlans-response-nextToken"></a>
A unique pagination token for next page results. Make the call again using this token to retrieve the next page.
Type: String

## Errors
<a name="API_ListEnvironmentVlans_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [ResourceNotFoundException](API_ResourceNotFoundException.md)
A service resource associated with the request could not be found. The resource might not be specified correctly, or it may have a `state` of `DELETED`.
 ** message **
Describes the error encountered.
 ** resourceId **
The ID of the resource that could not be found.
 ** resourceType **
The type of the resource that is associated with the error.
HTTP Status Code: 400

 [ValidationException](API_ValidationException.md)
The input fails to satisfy the specified constraints. You will see this exception if invalid inputs are provided for any of the Amazon EVS environment operations, or if a list operation is performed on an environment resource that is still initializing.
 ** fieldList **
A list of fields that didn't validate.
 ** message **
Describes the error encountered.
 ** reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListEnvironmentVlans_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/evs-2023-07-27/ListEnvironmentVlans)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/evs-2023-07-27/ListEnvironmentVlans)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/evs-2023-07-27/ListEnvironmentVlans)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/evs-2023-07-27/ListEnvironmentVlans)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/evs-2023-07-27/ListEnvironmentVlans)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/evs-2023-07-27/ListEnvironmentVlans)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/evs-2023-07-27/ListEnvironmentVlans)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/evs-2023-07-27/ListEnvironmentVlans)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/evs-2023-07-27/ListEnvironmentVlans)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/evs-2023-07-27/ListEnvironmentVlans)
