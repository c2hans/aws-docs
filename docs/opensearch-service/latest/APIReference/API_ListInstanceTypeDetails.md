---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListInstanceTypeDetails.html
---

# ListInstanceTypeDetails
<a name="API_ListInstanceTypeDetails"></a>

Lists all instance types and available features for a given OpenSearch or Elasticsearch version.

## Request Syntax
<a name="API_ListInstanceTypeDetails_RequestSyntax"></a>

```
GET /2021-01-01/opensearch/instanceTypeDetails/{{EngineVersion}}?domainName={{DomainName}}&instanceType={{InstanceType}}&maxResults={{MaxResults}}&nextToken={{NextToken}}&retrieveAZs={{RetrieveAZs}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListInstanceTypeDetails_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_ListInstanceTypeDetails_RequestSyntax) **   <a name="opensearchservice-ListInstanceTypeDetails-request-uri-DomainName"></a>
The name of the domain.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`

 ** [EngineVersion](#API_ListInstanceTypeDetails_RequestSyntax) **   <a name="opensearchservice-ListInstanceTypeDetails-request-uri-EngineVersion"></a>
The version of OpenSearch or Elasticsearch, in the format Elasticsearch\_X.Y or OpenSearch\_X.Y. Defaults to the latest version of OpenSearch.
Length Constraints: Minimum length of 14. Maximum length of 18.
Pattern: `^Elasticsearch_[0-9]{1}\.[0-9]{1,2}$|^OpenSearch_[0-9]{1,2}\.[0-9]{1,2}$`
Required: Yes

 ** [InstanceType](#API_ListInstanceTypeDetails_RequestSyntax) **   <a name="opensearchservice-ListInstanceTypeDetails-request-uri-InstanceType"></a>
An optional parameter that lists information for a given instance type.
Length Constraints: Minimum length of 10. Maximum length of 40.
Pattern: `^.*\..*\.search$`

 ** [MaxResults](#API_ListInstanceTypeDetails_RequestSyntax) **   <a name="opensearchservice-ListInstanceTypeDetails-request-uri-MaxResults"></a>
An optional parameter that specifies the maximum number of results to return. You can use `nextToken` to get the next page of results.
Valid Range: Maximum value of 100.

 ** [NextToken](#API_ListInstanceTypeDetails_RequestSyntax) **   <a name="opensearchservice-ListInstanceTypeDetails-request-uri-NextToken"></a>
If your initial `ListInstanceTypeDetails` operation returns a `nextToken`, you can include the returned `nextToken` in subsequent `ListInstanceTypeDetails` operations, which returns results in the next page.

 ** [RetrieveAZs](#API_ListInstanceTypeDetails_RequestSyntax) **   <a name="opensearchservice-ListInstanceTypeDetails-request-uri-RetrieveAZs"></a>
An optional parameter that specifies the Availability Zones for the domain.

## Request Body
<a name="API_ListInstanceTypeDetails_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListInstanceTypeDetails_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "InstanceTypeDetails": [
      {
         "AdvancedSecurityEnabled": boolean,
         "AppLogsEnabled": boolean,
         "AvailabilityZones": [ "string" ],
         "CognitoEnabled": boolean,
         "EncryptionEnabled": boolean,
         "InstanceRole": [ "string" ],
         "InstanceType": "string",
         "WarmEnabled": boolean
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListInstanceTypeDetails_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InstanceTypeDetails](#API_ListInstanceTypeDetails_ResponseSyntax) **   <a name="opensearchservice-ListInstanceTypeDetails-response-InstanceTypeDetails"></a>
Lists all supported instance types and features for the given OpenSearch or Elasticsearch version.
Type: Array of [InstanceTypeDetails](API_InstanceTypeDetails.md) objects

 ** [NextToken](#API_ListInstanceTypeDetails_ResponseSyntax) **   <a name="opensearchservice-ListInstanceTypeDetails-response-NextToken"></a>
When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.
Type: String

## Errors
<a name="API_ListInstanceTypeDetails_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## Examples
<a name="API_ListInstanceTypeDetails_Examples"></a>

### Example
<a name="API_ListInstanceTypeDetails_Example_1"></a>

This example illustrates one usage of ListInstanceTypeDetails.

#### Sample Request
<a name="API_ListInstanceTypeDetails_Example_1_Request"></a>

```
GET /2021-01-01/opensearch/instanceTypeDetails/OpenSearch_2.7 HTTP/1.1
Host: es.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.15.13 Python/3.11.6 Windows/10 exe/AMD64 prompt/off command/opensearch.list-instance-type-details
X-Amz-Date: 20240205T214608Z
X-Amz-Security-Token: IQoJb3JpZ2luX2VjEIwEaCXVz==
Authorization: AWS4-HMAC-SHA256 Credential=ASIAU/20240205/us-east-1/es/aws4_request, SignedHeaders=host;x-amz-date;x-amz-security-token, Signature=ba339a65cce237509bf48253a8073a034173a5b198f693f9f29665d8bc6d4e48
```

#### Sample Response
<a name="API_ListInstanceTypeDetails_Example_1_Response"></a>

```
{
   "InstanceTypeDetails":[
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"r5.large.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"r4.2xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"c4.2xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"m5.large.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"c5.large.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"r6g.8xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"m5.12xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"i3.4xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"im4gn.2xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"c4.8xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"r4.xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"r6gd.16xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"r5.2xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"i2.2xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"r6g.2xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"m6g.2xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"r5.12xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"r4.large.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"r6g.xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":false,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"m3.2xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"m5.xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"c6g.12xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":false,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"r3.8xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"c6g.xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"r5.4xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"im4gn.8xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"i3.16xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"c5.4xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"c5.9xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"c4.xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"m4.2xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"r4.8xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":false,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"m3.medium.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"t3.medium.search",
         "WarmEnabled":false
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"t3.small.search",
         "WarmEnabled":false
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"i3.xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"im4gn.xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"r6g.12xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"m5.2xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":false,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"r3.xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "ultra_warm"
         ],
         "InstanceType":"ultrawarm1.large.search",
         "WarmEnabled":false
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"c4.4xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":false,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"r3.2xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"i3.large.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":false,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"r3.4xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":false,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"t2.medium.search",
         "WarmEnabled":false
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"r6g.large.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "ultra_warm"
         ],
         "InstanceType":"ultrawarm1.medium.search",
         "WarmEnabled":false
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"c5.xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"r6gd.4xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":false,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"t2.small.search",
         "WarmEnabled":false
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"m4.xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"r6gd.xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":false,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"m3.large.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"c6g.4xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"c6g.8xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"c5.18xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"r4.4xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"m6g.4xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"i2.xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"m4.10xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"i3.2xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"r6gd.8xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"im4gn.4xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"r6gd.large.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"c4.large.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"r4.16xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"c6g.large.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"c6g.2xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"r6g.4xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"im4gn.large.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"m6g.12xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"m4.large.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"r6gd.12xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"r5.xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":false,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"r3.large.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"i3.8xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"m5.4xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":false,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"m3.xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"m6g.xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"r6gd.2xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"im4gn.16xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"m4.4xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"c5.2xlarge.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"m6g.large.search",
         "WarmEnabled":true
      },
      {
         "AdvancedSecurityEnabled":true,
         "AppLogsEnabled":true,
         "AvailabilityZones":null,
         "CognitoEnabled":true,
         "EncryptionEnabled":true,
         "InstanceRole":[
            "data",
            "master"
         ],
         "InstanceType":"m6g.8xlarge.search",
         "WarmEnabled":true
      }
   ],
   "NextToken":null
}
```

## See Also
<a name="API_ListInstanceTypeDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/ListInstanceTypeDetails)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/ListInstanceTypeDetails)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/ListInstanceTypeDetails)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/ListInstanceTypeDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/ListInstanceTypeDetails)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/ListInstanceTypeDetails)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/ListInstanceTypeDetails)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/ListInstanceTypeDetails)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/ListInstanceTypeDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/ListInstanceTypeDetails)
