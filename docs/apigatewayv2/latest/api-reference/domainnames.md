---
source_url: https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/domainnames.html
---

# DomainNames
<a name="domainnames"></a>

Represents a collection of domain names. See [Set up Custom Domain Name for an API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html).

## URI
<a name="domainnames-url"></a>

`/v2/domainnames`

## HTTP methods
<a name="domainnames-http-methods"></a>

### GET
<a name="domainnamesget"></a>

**Operation ID:** `GetDomainNames`

Gets the domain names for an AWS account.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The next page of elements from this collection. Not valid for the last element of the collection. |
| maxResults | String | False | The maximum number of elements to be returned for this resource. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | DomainNames | Success |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

### POST
<a name="domainnamespost"></a>

**Operation ID:** `CreateDomainName`

Creates a domain name.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 201 | DomainName | The request has succeeded and has resulted in the creation of a resource. |
| 400 | BadRequestException | One of the parameters in the request is invalid. |
| 403 | AccessDeniedException | 403 response |
| 404 | NotFoundException | The resource specified in the request was not found. |
| 409 | ConflictException | The resource already exists. |
| 429 | LimitExceededException | The client is sending more than the allowed number of requests per unit of time. |

## Schemas
<a name="domainnames-schemas"></a>

### Request bodies
<a name="domainnames-request-examples"></a>

#### POST schema
<a name="domainnames-request-body-post-example"></a>

```
{
  "domainName": "string",
  "tags": {
  },
  "domainNameConfigurations": [
    {
      "endpointType": enum,
      "ipAddressType": enum,
      "certificateName": "string",
      "certificateArn": "string",
      "ownershipVerificationCertificateArn": "string",
      "apiGatewayDomainName": "string",
      "hostedZoneId": "string",
      "certificateUploadDate": "string",
      "securityPolicy": enum,
      "domainNameStatus": enum,
      "domainNameStatusMessage": "string"
    }
  ],
  "mutualTlsAuthentication": {
    "truststoreUri": "string",
    "truststoreVersion": "string"
  },
  "routingMode": enum
}
```

### Response bodies
<a name="domainnames-response-examples"></a>

#### DomainNames schema
<a name="domainnames-response-body-domainnames-example"></a>

```
{
  "items": [
    {
      "domainName": "string",
      "domainNameArn": "string",
      "domainNameConfigurations": [
        {
          "endpointType": enum,
          "ipAddressType": enum,
          "certificateName": "string",
          "certificateArn": "string",
          "ownershipVerificationCertificateArn": "string",
          "apiGatewayDomainName": "string",
          "hostedZoneId": "string",
          "certificateUploadDate": "string",
          "securityPolicy": enum,
          "domainNameStatus": enum,
          "domainNameStatusMessage": "string"
        }
      ],
      "apiMappingSelectionExpression": "string",
      "tags": {
      },
      "mutualTlsAuthentication": {
        "truststoreUri": "string",
        "truststoreVersion": "string",
        "truststoreWarnings": [
          "string"
        ]
      },
      "routingMode": enum
    }
  ],
  "nextToken": "string"
}
```

#### DomainName schema
<a name="domainnames-response-body-domainname-example"></a>

```
{
  "domainName": "string",
  "domainNameArn": "string",
  "domainNameConfigurations": [
    {
      "endpointType": enum,
      "ipAddressType": enum,
      "certificateName": "string",
      "certificateArn": "string",
      "ownershipVerificationCertificateArn": "string",
      "apiGatewayDomainName": "string",
      "hostedZoneId": "string",
      "certificateUploadDate": "string",
      "securityPolicy": enum,
      "domainNameStatus": enum,
      "domainNameStatusMessage": "string"
    }
  ],
  "apiMappingSelectionExpression": "string",
  "tags": {
  },
  "mutualTlsAuthentication": {
    "truststoreUri": "string",
    "truststoreVersion": "string",
    "truststoreWarnings": [
      "string"
    ]
  },
  "routingMode": enum
}
```

#### BadRequestException schema
<a name="domainnames-response-body-badrequestexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="domainnames-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### NotFoundException schema
<a name="domainnames-response-body-notfoundexception-example"></a>

```
{
  "message": "string",
  "resourceType": "string"
}
```

#### ConflictException schema
<a name="domainnames-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### LimitExceededException schema
<a name="domainnames-response-body-limitexceededexception-example"></a>

```
{
  "message": "string",
  "limitType": "string"
}
```

## Properties
<a name="domainnames-properties"></a>

### AccessDeniedException
<a name="domainnames-model-accessdeniedexception"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False |  |

### BadRequestException
<a name="domainnames-model-badrequestexception"></a>

The request is not valid, for example, the input is incomplete or incorrect. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### ConflictException
<a name="domainnames-model-conflictexception"></a>

The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |

### CreateDomainNameInput
<a name="domainnames-model-createdomainnameinput"></a>

Represents the input parameters for a `CreateDomainName` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| domainName | string | True | The domain name. |
| domainNameConfigurations | Array of type [DomainNameConfiguration](#domainnames-model-domainnameconfiguration) | False | The domain name configurations. |
| mutualTlsAuthentication | [MutualTlsAuthenticationInput](#domainnames-model-mutualtlsauthenticationinput) | False | The mutual TLS authentication configuration for a custom domain name. |
| routingMode | [RoutingMode](#domainnames-model-routingmode) | False | The routing mode API Gateway uses to route traffic to your APIs. |
| tags | [Tags](#domainnames-model-tags) | False | The collection of tags associated with a domain name. |

### DomainName
<a name="domainnames-model-domainname"></a>

Represents a domain name.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| apiMappingSelectionExpression | string | False | The API mapping selection expression. |
| domainName | string | True | The name of the DomainName resource. |
| domainNameArn | string | False | The ARN of the DomainName resource. |
| domainNameConfigurations | Array of type [DomainNameConfiguration](#domainnames-model-domainnameconfiguration) | False | The domain name configurations. |
| mutualTlsAuthentication | [MutualTlsAuthentication](#domainnames-model-mutualtlsauthentication) | False | The mutual TLS authentication configuration for a custom domain name. |
| routingMode | [RoutingMode](#domainnames-model-routingmode) | False | The routing mode API Gateway uses to route traffic to your APIs. |
| tags | [Tags](#domainnames-model-tags) | False | The collection of tags associated with a domain name. |

### DomainNameConfiguration
<a name="domainnames-model-domainnameconfiguration"></a>

The domain name configuration.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| apiGatewayDomainName | string | False | A domain name for the API. |
| certificateArn | string | False | An AWS-managed certificate that will be used by the edge-optimized endpoint for this domain name. AWS Certificate Manager is the only supported source. |
| certificateName | string | False | The user-friendly name of the certificate that will be used by the edge-optimized endpoint for this domain name. |
| certificateUploadDate | string<br />Format: date-time | False | The timestamp when the certificate that was used by edge-optimized endpoint for this domain name was uploaded. |
| domainNameStatus | [DomainNameStatus](#domainnames-model-domainnamestatus) | False | Identifies the status of a domain name migration. Statuses can have a value of AVAILABLE, UPDATING, PENDING\_CERTIFICATE\_REIMPORT, or PENDING\_OWNERSHIP VERIFICATION. A domain can be modified if its status is AVAILABLE. If the domain's status is UPDATING, you must wait until the current operation is complete.  |
| domainNameStatusMessage | string | False | An optional text message containing detailed information about status of the domain name migration. |
| endpointType | [EndpointType](#domainnames-model-endpointtype) | False | The endpoint type. |
| hostedZoneId | string | False | The Amazon Route 53 Hosted Zone ID of the endpoint. |
| ipAddressType | [IpAddressType](#domainnames-model-ipaddresstype) | False | The IP address types that can invoke the domain name. Use `ipv4` to allow only IPv4 addresses to invoke your domain name, or use `dualstack` to allow both IPv4 and IPv6 addresses to invoke your domain name. |
| ownershipVerificationCertificateArn | string | False | The Amazon resource name (ARN) for the public certificate issued by AWS Certificate Manager. This ARN is used to validate custom domain ownership. It's required only if you configure mutual TLS and use either an ACM-imported or a private CA certificate ARN as the regionalCertificateArn. |
| securityPolicy | [SecurityPolicy](#domainnames-model-securitypolicy) | False | The Transport Layer Security (TLS) version of the security policy for this domain name. The valid values are `TLS_1_0` and `TLS_1_2`. |

### DomainNameStatus
<a name="domainnames-model-domainnamestatus"></a>

Identifies the status of a domain name migration. Statuses can have a value of AVAILABLE, UPDATING, PENDING\_CERTIFICATE\_REIMPORT, or PENDING\_OWNERSHIP VERIFICATION. A domain can be modified if its status is AVAILABLE. If the domain's status is UPDATING, you must wait until the current operation is complete.
+ `AVAILABLE`
+ `UPDATING`
+ `PENDING_CERTIFICATE_REIMPORT`
+ `PENDING_OWNERSHIP_VERIFICATION`

### DomainNames
<a name="domainnames-model-domainnames"></a>

Represents a collection of domain names.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| items | Array of type [DomainName](#domainnames-model-domainname) | False | The elements from this collection. |
| nextToken | string | False | The next page of elements from this collection. Not valid for the last element of the collection. |

### EndpointType
<a name="domainnames-model-endpointtype"></a>

Represents an endpoint type.
+ `REGIONAL`
+ `EDGE`

### IpAddressType
<a name="domainnames-model-ipaddresstype"></a>

The IP address types that can invoke your API or domain name.
+ `ipv4`
+ `dualstack`

### LimitExceededException
<a name="domainnames-model-limitexceededexception"></a>

A limit has been exceeded. See the accompanying error message for details.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| limitType | string | False | The limit type. |
| message | string | False | Describes the error encountered. |

### MutualTlsAuthentication
<a name="domainnames-model-mutualtlsauthentication"></a>

If specified, API Gateway performs two-way authentication between the client and the server. Clients must present a trusted certificate to access your API.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| truststoreUri | string | False | An Amazon S3 URL that specifies the truststore for mutual TLS authentication, for example, `s3://{{bucket-name}}/{{key-name}} `. The truststore can contain certificates from public or private certificate authorities. To update the truststore, upload a new version to S3, and then update your custom domain name to use the new version. To update the truststore, you must have permissions to access the S3 object. |
| truststoreVersion | string | False | The version of the S3 object that contains your truststore. To specify a version, you must have versioning enabled for the S3 bucket. |
| truststoreWarnings | Array of type string | False | A list of warnings that API Gateway returns while processing your truststore. Invalid certificates produce warnings. Mutual TLS is still enabled, but some clients might not be able to access your API. To resolve warnings, upload a new truststore to S3, and then update you domain name to use the new version. |

### MutualTlsAuthenticationInput
<a name="domainnames-model-mutualtlsauthenticationinput"></a>

If specified, API Gateway performs two-way authentication between the client and the server. Clients must present a trusted certificate to access your API.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| truststoreUri | string | False | An Amazon S3 URL that specifies the truststore for mutual TLS authentication, for example, `s3://{{bucket-name}}/{{key-name}} `. The truststore can contain certificates from public or private certificate authorities. To update the truststore, upload a new version to S3, and then update your custom domain name to use the new version. To update the truststore, you must have permissions to access the S3 object. |
| truststoreVersion | string | False | The version of the S3 object that contains your truststore. To specify a version, you must have versioning enabled for the S3 bucket. |

### NotFoundException
<a name="domainnames-model-notfoundexception"></a>

The resource specified in the request was not found. See the `message` field for more information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | False | Describes the error encountered. |
| resourceType | string | False | The resource type. |

### RoutingMode
<a name="domainnames-model-routingmode"></a>

The routing mode API Gateway uses to route traffic to your APIs.
+ `API_MAPPING_ONLY`
+ `ROUTING_RULE_ONLY`
+ `ROUTING_RULE_THEN_API_MAPPING`

### SecurityPolicy
<a name="domainnames-model-securitypolicy"></a>

The Transport Layer Security (TLS) version of the security policy for this domain name. The valid values are `TLS_1_0` and `TLS_1_2`.
+ `TLS_1_0`
+ `TLS_1_2`

### Tags
<a name="domainnames-model-tags"></a>

Represents a collection of tags associated with the resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

## See also
<a name="domainnames-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetDomainNames
<a name="GetDomainNames-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/GetDomainNames)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/GetDomainNames)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/GetDomainNames)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/GetDomainNames)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/GetDomainNames)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/GetDomainNames)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/GetDomainNames)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/GetDomainNames)
+ [AWS SDK for Python](/goto/boto3/apigatewayv2-2018-11-29/GetDomainNames)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/GetDomainNames)

### CreateDomainName
<a name="CreateDomainName-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/apigatewayv2-2018-11-29/CreateDomainName)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/apigatewayv2-2018-11-29/CreateDomainName)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/apigatewayv2-2018-11-29/CreateDomainName)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/apigatewayv2-2018-11-29/CreateDomainName)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/apigatewayv2-2018-11-29/CreateDomainName)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/apigatewayv2-2018-11-29/CreateDomainName)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/apigatewayv2-2018-11-29/CreateDomainName)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/apigatewayv2-2018-11-29/CreateDomainName)
+ [AWS SDK for Python](/goto/boto3/apigatewayv2-2018-11-29/CreateDomainName)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/apigatewayv2-2018-11-29/CreateDomainName)
